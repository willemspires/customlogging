from datetime import datetime
class colors:
    class font:
        reset = '\033[00m'
        bold = '\033[01m'
        disable = '\033[02m'
        underline = '\033[04m'
        reverse = '\033[07m'
        strikethrough = '\033[09m'
        invisible = '\033[08m'
    class color:
        black = '\033[30m'
        red = '\033[31m'
        green = '\033[32m'
        orange = '\033[33m'
        blue = '\033[34m'
        purple = '\033[35m'
        cyan = '\033[36m'
        lightgrey = '\033[37m'
        darkgrey = '\033[90m'
        lightred = '\033[91m'
        lightgreen = '\033[92m'
        yellow = '\033[93m'
        lightblue = '\033[94m'
        pink = '\033[95m'
        lightcyan = '\033[96m'


class Logging:
    class config:
        color_map = {
            "INFO": colors.color.blue,
            "ERROR": colors.color.red,
            "WARNING": colors.color.yellow,
            "DEBUG": colors.color.green,
            "CUSTOM": colors.color.blue
        }
        
        default_map = {
            "INFO": colors.color.blue,
            "ERROR": colors.color.red,
            "WARNING": colors.color.yellow,
            "DEBUG": colors.color.green,
            "CUSTOM": colors.color.blue         
        }
        
        @classmethod
        def color(cls, level, color):
            if color in vars(colors.color).values():
                cls.color_map[level.upper()] = color
            else:
                raise ValueError("Invalid color. Use a color defined in the colors.color class.")
    
    @staticmethod
    def _log(level, color, string):
        timestamp = datetime.now().strftime("%H:%M:%S|%d-%m-%Y")
        print(colors.font.reverse+f"{timestamp}{colors.font.reset} {colors.font.bold}[{color}{level}{colors.font.reset}{colors.font.bold}]"+colors.font.reset, string)

    @classmethod
    def info(cls, string=None):
        if string:
            cls._log("INFO", cls.config.color_map["INFO"], string)

    @classmethod
    def error(cls, string=None):
        if string:
            cls._log("ERROR", cls.config.color_map["ERROR"], string)
    
    @classmethod
    def warn(cls, string=None):
        if string:
            cls._log("WARNING", cls.config.color_map["WARNING"], string)
    
    @classmethod
    def debug(cls, string=None):
        if string:
            cls._log("DEBUG", cls.config.color_map["DEBUG"], string)
    
    @classmethod
    def custom(cls, custom: str, string=None):
        if string and custom:
            cls._log(custom.upper(), cls.config.color_map["CUSTOM"], string)

