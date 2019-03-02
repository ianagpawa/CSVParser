from FileObject import FileObject
from CSVParser import CSVParser

class Utils:
    def __init__(self, csv_file_name, json_file_name):
        self.csv_parser = CSVParser(csv_file_name)
        self.file_object = FileObject(json_file_name)

    


    def write_file(self,index):
        tup = self.file_object.get_tuples()[index]
        rows = self.csv_parser.get_parsed_csv_file()[tup[0]:tup[1]]
        self.csv_parser.write_csv_section(rows, "./output/%s-%s.csv" % (index, self.file_object.get_file_name(index)))


    def create_base_files(self):
        for index in range(2):
            self.write_file(index)


    def create_action_files(self):
        for index in range(2,len(self.file_object.get_tuples())):
            self.write_file(index)