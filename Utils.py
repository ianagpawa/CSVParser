from FileObject import FileObject
from CSVParser import CSVParser

def read_write(csv_file_name, json_file_name):
    csv_parser = CSVParser(csv_file_name)
    file_object = FileObject(json_file_name)
    for index in range(len(file_object.get_tuples())):
        tup = file_object.get_tuples()[index]
        rows = csv_parser.get_parsed_csv_file()[tup[0]:tup[1]]
        csv_parser.write_csv_section(rows, "./output/%s-%s.csv" % (index, file_object.get_file_name(index)))
