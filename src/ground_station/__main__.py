# __main__.py
from database import loader
from packets import tc_packet
#from utils import check_tc
tm_database = loader.load_database("tm.yaml")
tc_database = loader.load_database("tc.yaml")


def main():
    print("Ground station starting...")
    tc_name = input("Enter your tc_name : ")
    print(tc_name)
    print(tc_database)
    if tc_name in tc_database : 
        tc=tc_packet()
    else:
        print("TC doesnt exist in the Data Base. Please verify the name or add it to DBs")

if __name__ == "__main__":
    main()