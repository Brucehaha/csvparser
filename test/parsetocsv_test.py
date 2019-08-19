#!/usr/bin/env python
# -*- coding:utf-8 -*
import os
import sys

BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASEDIR)

import unittest
from unittest import TestCase
import json
import tempfile
from src.csvparser import ParseToCSV
from config import settings


class ParserTest(TestCase):
    def setUp(self):
        # Create a temporary directory
        self.test_dir = tempfile.mkdtemp()

    def test_spec_exist(self):
        self.assertEqual(os.path.exists(settings.SPEC_FILE), 1)

    def test_spec_json(self):
        with open(settings.SPEC_FILE, "r") as spec:
            data = json.load(spec)
        self.assertDictEqual(data, ParseToCSV.load_spec(self))

    def test_UnicodeDecodingError(self):
        """
        test if the file is encoding as required in the spec
        :return:
        """
        spec = {
            "ColumnNames": "f1, f2, f3, f4, f5, f6, f7, f8, f9, f10",
            "Offsets": "3,12,3,2,13,1,10,13,3,13",
            "InputEncoding": "windows-1252",
            "IncludeHeader": "True",
            "OutputEncoding": "utf-8"}
        parser = ParseToCSV
        parser.spec_dict = spec
        with open(os.path.join(self.test_dir, 'test.txt'), 'w', encoding='utf-8') as f:
            f.write('hello')
        self.assertRaises(UnicodeDecodeError)


if __name__ == '__main__':
        unittest.main()
