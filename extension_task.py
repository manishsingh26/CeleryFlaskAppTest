
from celery import Celery

from utils.pandas_csv_function import CSVDataFrameFunction
from utils.pandas_txt_function import TXTDataFrameFunction


class CeleryTask(object):

    def __init__(self, input_file_path, file_name_input, file_name_output, output_file_path, input_extension, output_extension,
                 columns_names, delimiter=None, xml_attribute=None):
        self.app = Celery()
        self.file_name_input = str(file_name_input)
        self.file_name_output = str(file_name_output)
        self.input_file_path = str(input_file_path)
        self.output_file_path = str(output_file_path)
        self.input_extension = input_extension
        self.delimiter = delimiter
        self.columns_names = columns_names
        self.xml_attribute = xml_attribute
        self.output_extension = output_extension

    def csv_task(self):
        input_file = self.input_file_path + self.file_name_input + str('.') + self.input_extension
        output_file = self.output_file_path + self.file_name_output
        file_delimiter = ',' if self.delimiter is None else self.delimiter
        pandas_obj = CSVDataFrameFunction(input_file, output_file, self.output_extension,
                                          file_delimiter, self.columns_names)
        job_status = pandas_obj.data_transfer()
        return job_status

    def txt_task(self):
        input_file = self.input_file_path + self.file_name_input + str('.') + self.input_extension
        output_file = self.output_file_path + self.file_name_output
        file_delimiter = ',' if self.delimiter is None else self.delimiter
        pandas_obj = TXTDataFrameFunction(input_file, output_file, self.output_extension,
                                          file_delimiter, self.columns_names)
        job_status = pandas_obj.data_transfer()
        return job_status



