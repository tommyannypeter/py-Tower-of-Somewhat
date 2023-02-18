import configparser

class _Config:
    def __init__(self, config_file) -> None:
        parser = configparser.ConfigParser()
        parser.read(config_file)
        self.width = parser.getint("DISPLAY", "width")
        self.height = parser.getint("DISPLAY", "height")

CONFIG = _Config("docs/configuration.ini")
