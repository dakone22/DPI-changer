import configparser

DEFAULTS = {
    'WidthDPI': 300,
    'HeightDPI': 300,
    '': None,
    'InputDir': 'IMAGES',
    '# if SeparateOutput is False then output override input images!': None,
    'SeparateOutput': True,
    'SeparateOutputDir': 'OUTPUT',
}


def load_config(path: str) -> configparser.ConfigParser:
    configparser.ConfigParser.optionxform = str
    config = configparser.ConfigParser(
        defaults=DEFAULTS,
        allow_no_value=True,
    )

    config.read(path)
    return config
