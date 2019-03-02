import csv

class CSVParser:
    """
    Creates CSV Parser
    """
    def __init__(self, csv_file):
        """
        Initializes CSV Parser

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
        """
        Writes csv sections

        @type array
        @param rows:

        @type str
        @param output_file_name: Destination of output file.
        
        """
        with open(output_file_name, mode='w', newline='') as file:
            row_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for row in rows:
                row_writer.writerow(row)


    def parse_text_file(self, file_name):
        """
        Parses text file into array of line items.
        
        @type file_name: str
        @param file_name: Name of text file.

        @rtype: array
        @return Array of line times.
        """
        file = open(file_name, "r")
        return file.read().splitlines()


    def insert_value_into_row(self, row, value, column_index):
        row[column_index] = value
        return row


    def insert_values(self, column_index, cut_off_index, add_list_file):
        text_file_arr = self.parse_text_file(add_list_file)
        row_count = 0
        ind = 0
        for row in self.get_parsed_csv_file():
            if row_count >= cut_off_index:
                value = text_file_arr[ind % len(text_file_arr)]
                row = self.insert_value_into_row(row, value, column_index)
                self.parsed_csv_file_arr[row_count] = row
                ind += 1
            row_count += 1
