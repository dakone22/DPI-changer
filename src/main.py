import os

from config import load_config
from process import change_DPI


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(BASE_DIR)
CONFIG_PATH = os.path.join(BASE_DIR, 'config.ini')


def main():
    config = load_config(CONFIG_PATH)

    with open(CONFIG_PATH, mode='w') as f:
        config.write(f)

    input_dir = os.path.abspath(config.get('DEFAULT', 'InputDir'))
    output_dir = input_dir

    if config.getboolean('DEFAULT', 'SeparateOutput'):
        output_dir = os.path.abspath(config.get('DEFAULT', 'SeparateOutputDir'))

    dpi = (config.getint('DEFAULT', 'WidthDPI'), config.getint('DEFAULT', 'HeightDPI'))

    change_DPI(input_dir, output_dir, dpi)

    input("Program finished. Press Enter to close...")


if __name__ == '__main__':
    main()
