import pandas as pd


class CSVDataFrameFunction(object):

    def __init__(self, input_file, output_file, output_extension, file_delimiter, columns_names):
        self.input_file = input_file
        self.output_file = output_file
        self.output_extension = output_extension
        self.file_delimiter = file_delimiter
        self.columns_names = columns_names
        self.output_dataframe = pd.DataFrame(columns=self.columns_names)

    def data_transfer(self):

        if self.output_extension is 'csv':
            i = 0
            j = 1
            chunk_size = 10000
            file_ = self.output_file + "." + self.output_extension
            self.output_dataframe.to_csv(file_, mode="a", index=False)
            for df in pd.read_csv(self.input_file, chunksize=chunk_size, iterator=True, sep=self.file_delimiter):
                df.index += j
                i += 1
                j = df.index[-1] + 1
                df.to_csv(file_, mode="a", header=False, index=False)
            return "Job Completed"

        elif self.output_extension is 'txt':
            i = 0
            j = 1
            chunk_size = 10000
            file_ = self.output_file + "." + self.output_extension
            self.output_dataframe.to_csv(file_, mode="a", index=False)
            for df in pd.read_csv(self.input_file, chunksize=chunk_size, iterator=True, sep=self.file_delimiter):
                df.index += j
                i += 1
                j = df.index[-1] + 1
                df.to_csv(file_, mode="a", header=False, index=False)
            return "Job Completed"

        elif self.output_extension is 'json':
            i = 0
            j = 1
            chunk_size = 100000
            for df in pd.read_csv(self.input_file, chunksize=chunk_size, iterator=True, sep=self.file_delimiter):
                df.index += j
                i += 1
                j = df.index[-1] + 1
                file_ = self.output_file + str(i) + "." + self.output_extension
                df.to_json(file_, orient='records')
            return "Job Completed"

        else:
            return "Check your extension"

