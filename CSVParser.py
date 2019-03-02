import csv

class CSVParser:
    """
    Creates CSV Parser
    """
    def __init__(self, csv_file):
        """
        Initializes CSV Parser constructor

        @type csv_file: str
        @param csv_file: Name of json file.
        """
        self.parsed_csv_file_arr = self.parse_csv(csv_file)
        self.rows = None


    def parse_csv(self, csv_file_name):
        """
        Sets file object property
        
        @type csv_file_name: str
        @param csv_file_name: Name of json file.

        @rtype array
        @returns output_array: Array of lines in csv file.
        """
        output_array = []
        with open(csv_file_name) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                row.pop(0)
                output_array.append(row)
        return output_array
    

    def get_parsed_csv_file(self):
        """
        Gets file object property
        
        @rtype: object

        @returns file object property
        """
        return self.parsed_csv_file_arr


    def write_csv_section(self, rows, output_file_name):
        with open(output_file_name, mode='w', newline='') as file:
            row_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for row in rows:
                row_writer.writerow(row)


    def set_rows(self, rows):
        self.rows = rows





    