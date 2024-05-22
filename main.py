import time
from typing import Iterable
from datetime import datetime, timedelta
from commons.logger import logger
from commons.settings import settings
from driver.browser import chrome_driver, WebDrivers
from model.radio import Radio
from model.song import Song
from vespucci.myradioonline_strategy import MyRadioOnlineStrategy
from commons.sql_conector import connector
from sqlmodel import select, text, Session
from selenium.common.exceptions import StaleElementReferenceException

def open_browser_tabs(browser: WebDrivers, results: Iterable[Radio]) -> None:
    """
    Open all browser tabs with radios url
    :param browser: Browser object
    :param results: List[Radio]
    :return: None
    """
    logger.info("Opening browser tabs")
    for index, _radio in enumerate(results):
        if index:
            logger.debug(f"Open new tab {index}")
            browser.switch_to.new_window()
        logger.debug(f"Opening url {_radio.url}")
        browser.get(_radio.url)
    # reset browser tab to 0
    logger.debug(f"f {browser.window_handles}f")
    browser.switch_to.window(browser.window_handles[0])


def merge_song(_session: Session, song: Song) -> Song:
    """
    Merge song into the database after we're checking by raw_song name
    :param _session: Database session
    :param song: Song Object
    :return: Song
    """
    logger.info(f"Inserting/update song {song}")
    song_query = _session.query(Song).filter_by(raw_song=song.raw_song, radio_id=song.radio_id).first()
    if song_query:
        song_query.date_stream_played = song.date_stream_played
    else:
        song_query = song

    _session.merge(song_query)
    _session.commit()
    # _session.refresh(song_query)

    logger.debug("Successfully added song into database")
    return song_query


def main() -> None:
    """
    Radio entrypoint
    :return: None
    """
    with connector() as session:
        result = session.exec(select(Radio)).all()
        with chrome_driver() as cd:
            open_browser_tabs(cd, result)
            search = True
            refresh_time = datetime.now()
            while search:
                for idx, tab in enumerate(cd.window_handles):
                    try:
                        cd.switch_to.window(cd.window_handles[idx])
                        radio = MyRadioOnlineStrategy(result[idx], cd)
                        s = radio.discover()
                        logger.debug(f"Song is {s}")
                        merge_song(session, s)
                    except StaleElementReferenceException as e:
                        logger.error(f"Exception: {e.msg} on screen {e.screen}")

                    if refresh_time < datetime.now():
                        logger.debug(f"Refresh time passed {refresh_time}, reloading radio page {result[idx].url}")
                        radio.page_reload()
                        logger.info(f"refresh_time is greater than datetime.now() ({refresh_time} < {datetime.now()})")
                if refresh_time < datetime.now():
                    refresh_time = datetime.now() + timedelta(hours=1)
                    logger.info(f"Refresh time changed to {refresh_time}")
                time.sleep(150)


if __name__ == '__main__':
    main()


