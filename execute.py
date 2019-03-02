import sys
from Utils import Utils

def execute():
    utils = Utils(sys.argv[1], sys.argv[2])
    if sys.argv[3] == "base":
        utils.create_base_files()
        return
    if  '.txt' in sys.argv[3]:
        utils.update_action_files(sys.argv[3])
        return


execute()