import sys
from Utils import Utils

def execute():
    """
    Parses csv file by section, creates individual csv for each section.
    """
    utils = Utils(sys.argv[1], sys.argv[2])
    utils.create_updated_action_files(sys.argv[3]) if len(sys.argv) > 3 else utils.create_base_files()


execute()