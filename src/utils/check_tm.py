from database import load_database
tm_database = load_database("tm.yaml")
def check_tm(Telemtry):
    service = Telemtry[7]
    subservice = Telemtry[8]
    for tm in tm_database:
        tmserv=tm_database[tm]["service"]
        tmsubserv=tm_database[tm]["subservice"]
        if (tmserv,tmsubserv)==(service,subservice) : return tm

    return False