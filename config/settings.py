#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os

BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# log file location
ERROR_LOG_FILE = os.path.join(BASEDIR, "log", 'error.log')
# run log
RUN_LOG_FILE = os.path.join(BASEDIR, "log", 'run.log')

SPEC_FILE = os.path.join(BASEDIR, "fixed-width", 'spec.json')

OUTPUT_PATH = os.path.join(BASEDIR, "files", 'output')

INPUT_PATH = os.path.join(BASEDIR, "files", 'input')

OPEN_ERROR = 'strict'