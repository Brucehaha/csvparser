#!/usr/bin/env python
# -*- coding:utf-8 -*
import os
import json
import os
from config import settings
from lib.log import Logger
import threading


class ParseToCSV(object):
    __instance = None

    def __init__(self):
        self.spec_dict = self.load_spec()

    def __new__(cls, *args, **kwargs):
        """
        singleton
        :param args:
        :param kwargs:
        :return:
        """
        if not cls.__instance:
            cls.__instance = object.__new__(cls, *args, **kwargs)
        return cls.__instance

    @staticmethod
    def split_by_lens(lens, line, count, file_name):
        """
        split string in to array list by list of required length
        :param lens: strings contains length for each cell, e.g "3,12,3,2,13,1,10,13,3,13""
        :param line: line written to output file
        :return: string with ',' as delimiter
        """
        len_list = lens.split(',')
        line_list = list(line)
        index = 0
        # insert the delimiter to line_list
        for w in len_list:
            index += int(w)
            if index > len(line_list):
                Logger().log('%s in line %s has less length be separated in to %s cells'
                             % (file_name, count, len(len_list)))
                break
            line_list.insert(index, ",")
            index += 1
        return ''.join(line_list)

    def load_spec(self):
        """
        load specifications of the format of output date
        :return: dictionary data
        """
        try:
            with open(settings.SPEC_FILE, "r") as spec:
                data = json.load(spec)
        except OSError:
            Logger().log("Spec file does not exist in path:'/config/'", False)
            print("Please put spec.json to /config")

        return data

    def parse_to_csv(self, file_name, output_name = None):
        """
        :param file_name: input file name
        :param output_name: default is None for customi, get name base on input file name,
        :return:
        """
        input_path = os.path.join(settings.INPUT_PATH, file_name)
        output_path = os.path.join(settings.OUTPUT_PATH, file_name+'.csv')
        lines = None
        try:
            with open(input_path, "r", encoding=self.spec_dict['InputEncoding'], errors=settings.OPEN_ERROR) as file:
                lines = file.readlines()
        except UnicodeDecodeError:
            error = '%s is not %s' % (file_name, self.spec_dict['InputEncoding'])
            print(error)
            Logger().log(error, False)
        except Exception as e:
            Logger().log(e, False)

        count = 1
        if lines is not None:
            with open(output_path, "w",
                      encoding=self.spec_dict['OutputEncoding'],
                      errors=settings.OPEN_ERROR) as output:
                for line in lines:
                    if count == 1 and self.spec_dict["IncludeHeader"]:
                        header = self.spec_dict["ColumnNames"]
                        output.write(header)
                        output.write("\n")
                    count += 1
                    new_line = self.split_by_lens(self.spec_dict['Offsets'], line, count, file_name)
                    output.write(new_line)

    def process(self, path):
        self.parse_to_csv(path)


