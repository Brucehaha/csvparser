import os
import sys

BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASEDIR)
from config.settings import INPUT_PATH
from src.scripts import run
from lib.log import Logger

if __name__ == '__main__':
    # list all the file to parse in files/output
    only_files = [f for f in os.listdir(INPUT_PATH) if os.path.isfile(os.path.join(INPUT_PATH, f))]
    if len(only_files) == 0:
        Logger().log('no input file')
    for file in only_files:
        run(file)

