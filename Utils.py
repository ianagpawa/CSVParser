import csv 
import sys

from FileObject import FileObject

def read(file_name):
    output_array = []
    with open(file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            row.pop(0)
            output_array.append(row)
    return output_array
    

def write_section(rows, output_file_name):
    with open(output_file_name, mode='w', newline='') as file:
        row_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in rows:
            row_writer.writerow(row)

        
def get_tups():
    pos = {
        'u': 6,
        's': 9,
        'r': 11,
        'e': 14,
        'm': 15,
        'c': 18,
        'l': 22
    }
    return [(0,pos['u']), (pos['u'], pos['s']), (pos['s'], pos['r']), (pos['r'], pos['e']), (pos['e'], pos['m']), (pos['m'], pos['l'])]


def read_write(file_name):
    output_arr = read(file_name)
    count = 1
    for tup in get_tups():
        rows = output_arr[tup[0]:tup[1]]
        write_section(rows, "%s.csv" % count)
        count += 1


# read_write(sys.argv[1])

def parse_text_file(file_name):
    """
    Parses text file into array of line items.
    
    @type file_name: str
    @param file_name: Name of text file.

    @rtype: array
    @return Array of line times.
    """
    file = open(file_name, "r")
    return file.read().splitlines()


print(parse_text_file(sys.argv[1]))