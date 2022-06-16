import configparser

class _Config:
    def __init__(self, config_file) -> None:
        config = configparser.ConfigParser()
        config.read(config_file)
        self.width = config.getint("DISPLAY", "width")
        self.height = config.getint("DISPLAY", "height")

CONFIG = _Config("configuration.ini")
