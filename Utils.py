from FileObject import FileObject
from CSVParser import CSVParser

class Utils:
    """
    Create Utils Object for using FileObject and CSVParser
    """


    def __init__(self, csv_file_name, json_file_name):
        """
        Initializes Utils
        
        @type json_file_name: str
        @param json_file_name: Name of json file.

        @type csv_file: str
        @param csv_file: Name of json file.
        """
        self.csv_parser = CSVParser(csv_file_name)
        self.file_object = FileObject(json_file_name)


    def write_file(self,index):
        """
        Writes csv file by section using CSV parser object
        
        @type index: number
        @param index: Index
        """
        tup = self.file_object.get_tuples()[index]
        rows = self.csv_parser.get_parsed_csv_file()[tup[0]:tup[1]]
        self.csv_parser.write_csv_section(rows, "./output/%s-%s.csv" % (index, self.file_object.get_file_name(index)))


    def create_base_files(self):
        """
        Writes base csv files
        """
        for index in range(2):
            self.write_file(index)


    def create_action_files(self):
        """
        Writes action csv files
        """
        for index in range(2,len(self.file_object.get_tuples())):
            self.write_file(index)


    def update_action_files(self, file_name):
        self.csv_parser.insert_values(1, self.file_object.get_cutoff_index(), file_name)
        self.create_action_files()