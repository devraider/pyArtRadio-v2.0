import datetime
from abc import ABC
from typing import Tuple

from commons.logger import logger
from commons.settings import settings
from driver.browser import WebDrivers
from model.radio import Radio
from model.song import Song
from vespucci.discover import DiscoverStrategy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class MyRadioOnlineStrategy(DiscoverStrategy, ABC):

    __url = settings.my_radio_online

    def __init__(self, _radio: Radio, browser: WebDrivers):
        """
        Initiate songs discoverer on MyRadioOnline.ro
        :param _radio: Radio instance from database
        """
        super().__init__()
        logger.debug(f"Initiated {self.__class__.__name__} for slug {_radio.slug}")
        self._radio = _radio
        self._browser = browser

    def discover(self) -> Song:
        logger.info("Starting song discovery")
        self.load_page()

        # Get raw song details from stream
        raw_song_playing, youtube_id = self.get_raw_song_from_stream()

        # singer and song name split
        singer, name = self._split_song_singer_name(raw_song_playing)
        logger.info(f"All details are read to build Song object {singer, name} -> {raw_song_playing, youtube_id}")
        return Song(
            radio_id=self._radio.id,
            singer=singer,
            name=name,
            raw_song=raw_song_playing,
            youtube_id=youtube_id,
        )

    def load_page(self) -> None:
        """
        Wait for song HTML elements to be loaded on the page
        :return: None
        """
        logger.info("Wait to load complete page")

        WebDriverWait(self._browser, 10).until(
            ec.presence_of_element_located((By.CLASS_NAME, "songCont"))
        )

    def get_raw_song_from_stream(self) -> Tuple[str, str]:
        """
        Extract raw name of the song from radio stream and YouTube id of the song
        :return: Tuple[str, str] (raw name,  YouTube id)
        """
        logger.debug("Start extraction of raw song details")
        song_element = self._browser.find_element(By.CLASS_NAME, "songCont")
        unwanted_text = song_element.find_element(By.CLASS_NAME, "txt2").text
        youtube_id = song_element.get_attribute("data-youtube")
        raw_song_playing = song_element.text.replace(unwanted_text, "").strip()
        logger.debug(f"Successfully extracted raw song details {raw_song_playing}, {youtube_id}")
        return raw_song_playing, youtube_id

    @staticmethod
    def _split_song_singer_name(song: str) -> Tuple[str, str]:
        """
        We need to process raw song name from radio into singer and song name
        :param str song: Raw song string from radio
        :return: Tuple[str, str] of singer and name of the song
        """
        song_list = song.split(" - ")
        logger.debug(f"Split song list {song_list}")
        return "".join(song_list[:1]), "".join(song_list[1:])

    def page_reload(self) -> None:
        """
        Refresh radio page
        :return: None
        """
        self._browser.refresh()
        logger.debug(f"Successfully reloaded page {self._browser.current_url}")
