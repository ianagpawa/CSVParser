import json

class FileObject:
    """
    Create File Object
    """


    def __init__(self, json_file_name):
        """
        Initializes File Object constructor
        
        @type json_file_name: str
        @param json_file_name: Name of json file.
        """
        self.file_object = self.set_file_object(json_file_name)


    def set_file_object(self, json_file_name):
        """
        Sets file object property
        
        @type json_file_name: str
        @param json_file_name: Name of json file.
        """
        data = None
        with open(json_file_name) as f:
            data = json.load(f)
        return data


    def get_file_object(self):
        """
        Gets file object property
        
        @rtype: object

        @returns file object property
        """
        return self.file_object


    def get_tuples(self):
        """
        Gets tuples for each section by lines.
        
        @rtype: array
        @return Array of tuples for each section.
        """
        sections = self.file_object["sections"]
        tuples = []
        for index in range(len(sections)):
            tuple_set = (0, sections[index]["position"]) if index == 0 else (sections[index-1]["position"], sections[index]["position"])
            tuples.append(tuple_set)
        return tuples


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

    def get_file_name(self, index):
        return self.file_object["sections"][index]["name"]