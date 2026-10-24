# __main__.py
from database import load_database
tc_database = load_database("database/tc.yaml")
def check_tc(name):
    return