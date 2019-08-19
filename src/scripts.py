#!/usr/bin/env python
# -*- coding:utf-8 -*-
from src.csvparser import ParseToCSV
from config import settings


def run(path):
    cli = ParseToCSV()
    cli.process(path)

