from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
        Application settings model
    """
    path_chrome_driver: str
    artradio: str
    my_radio_online: str
    mysql_uri: str

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'
        case_sensitive = True


settings = Settings()

if __name__ == '__main__':
    print(settings.path_chrome_driver)