import unittest
from extension_task import CeleryTask


class TestExtensionTask(unittest.TestCase):

    def set_up(self):
        pass

    '''' 1. Test Case For CSV To CSV'''
    def test_csv_csv_task(self):
        input_file_path = '/home/msingh/Documents/PycharmProjects/FlaskAppTask/Data/input/'
        output_file_path = '/home/msingh/Documents/PycharmProjects/FlaskAppTask/Data/output/'
        columns_names = ["createdon","leadowner","campaignname","territory","productname","rating","teamname",
                         "leadname","processname","createdonyear"]
        file_name_input = 'crmnextleaddata'
        file_name_output = 'crmnextleaddata_csv_2_csv'
        input_extension = 'csv'
        output_extension = 'csv'

        task_obj = CeleryTask(input_file_path=input_file_path, file_name_input=file_name_input, file_name_output=file_name_output,
                              output_file_path=output_file_path, input_extension=input_extension, output_extension=output_extension,
                              columns_names=columns_names)
        job_status = task_obj.csv_task()
        self.assertEqual(job_status, "Job Completed")

    '''' 2. Test Case For CSV To TXT'''
    def test_csv_txt_task(self):
        input_file_path = '/home/msingh/Documents/PycharmProjects/FlaskAppTask/Data/input/'
        output_file_path = '/home/msingh/Documents/PycharmProjects/FlaskAppTask/Data/output/'
        columns_names = ["createdon","leadowner","campaignname","territory","productname","rating","teamname",
                         "leadname","processname","createdonyear"]
        file_name_input = 'crmnextleaddata'
        file_name_output = 'crmnextleaddata_csv_2_txt'
        input_extension = 'csv'
        output_extension = 'txt'

        task_obj = CeleryTask(input_file_path=input_file_path, file_name_input=file_name_input, file_name_output=file_name_output,
                              output_file_path=output_file_path, input_extension=input_extension, output_extension=output_extension,
                              columns_names=columns_names)
        job_status = task_obj.csv_task()
        self.assertEqual(job_status, "Job Completed")

    '''' 3. Test Case For CSV To JSON'''
    def test_csv_json_task(self):
        input_file_path = '/home/msingh/Documents/PycharmProjects/FlaskAppTask/Data/input/'
        output_file_path = '/home/msingh/Documents/PycharmProjects/FlaskAppTask/Data/output/'
        columns_names = ["createdon","leadowner","campaignname","territory","productname","rating","teamname",
                         "leadname","processname","createdonyear"]
        file_name_input = 'crmnextleaddata'
        file_name_output = 'crmnextleaddata_csv_2_json'
        input_extension = 'csv'
        output_extension = 'json'

        task_obj = CeleryTask(input_file_path=input_file_path, file_name_input=file_name_input, file_name_output=file_name_output,
                              output_file_path=output_file_path, input_extension=input_extension, output_extension=output_extension,
                              columns_names=columns_names)
        job_status = task_obj.csv_task()
        self.assertEqual(job_status, "Job Completed")

    '''' 4. Test Case For TXT To CSV'''
    def test_txt_csv_task(self):
        input_file_path = '/home/msingh/Documents/PycharmProjects/FlaskAppTask/Data/input/'
        output_file_path = '/home/msingh/Documents/PycharmProjects/FlaskAppTask/Data/output/'
        columns_names = ["createdon","leadowner","campaignname","territory","productname","rating","teamname",
                         "leadname","processname","createdonyear"]
        file_name_input = 'crmnextleaddata'
        file_name_output = 'crmnextleaddata_txt_2_csv'
        input_extension = 'csv'
        output_extension = 'csv'

        task_obj = CeleryTask(input_file_path=input_file_path, file_name_input=file_name_input, file_name_output=file_name_output,
                              output_file_path=output_file_path, input_extension=input_extension, output_extension=output_extension,
                              columns_names=columns_names)
        job_status = task_obj.csv_task()
        self.assertEqual(job_status, "Job Completed")

    '''' 5. Test Case For TXT To TXT'''
    def test_txt_txt_task(self):
        input_file_path = '/home/msingh/Documents/PycharmProjects/FlaskAppTask/Data/input/'
        output_file_path = '/home/msingh/Documents/PycharmProjects/FlaskAppTask/Data/output/'
        columns_names = ["createdon","leadowner","campaignname","territory","productname","rating","teamname",
                         "leadname","processname","createdonyear"]
        file_name_input = 'crmnextleaddata'
        file_name_output = 'crmnextleaddata_txt_2_txt'
        input_extension = 'csv'
        output_extension = 'txt'

        task_obj = CeleryTask(input_file_path=input_file_path, file_name_input=file_name_input, file_name_output=file_name_output,
                              output_file_path=output_file_path, input_extension=input_extension, output_extension=output_extension,
                              columns_names=columns_names)
        job_status = task_obj.csv_task()
        self.assertEqual(job_status, "Job Completed")

    '''' 6. Test Case For TXT To JSON'''
    def test_txt_json_task(self):
        input_file_path = '/home/msingh/Documents/PycharmProjects/FlaskAppTask/Data/input/'
        output_file_path = '/home/msingh/Documents/PycharmProjects/FlaskAppTask/Data/output/'
        columns_names = ["createdon","leadowner","campaignname","territory","productname","rating","teamname",
                         "leadname","processname","createdonyear"]
        file_name_input = 'crmnextleaddata'
        file_name_output = 'crmnextleaddata_txt_2_json'
        input_extension = 'csv'
        output_extension = 'json'

        task_obj = CeleryTask(input_file_path=input_file_path, file_name_input=file_name_input, file_name_output=file_name_output,
                              output_file_path=output_file_path, input_extension=input_extension, output_extension=output_extension,
                              columns_names=columns_names)
        job_status = task_obj.csv_task()
        self.assertEqual(job_status, "Job Completed")


if __name__ == "__main__":
    unittest.main()