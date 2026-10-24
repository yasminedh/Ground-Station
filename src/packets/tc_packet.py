from .field import field
from utils.crc import ecss_crc
class tc_packet:
    def __init__(self):
        self.tc_ccsds_header={
            "vNum" : "000",
            "Type" : "1",
            "dataFieldFlag" : "1",
            "APID" : "0",
            "groupingFlags" : "11",
            "seqCount" : "0",
            "pLength" : format(5,"016b")
        }
        self.pus_header={
            "sec_header_flag" : "0",
            "pus_vNum" : "001",
            "ack" : "1001",
            "service" : "0",
            "subservice" : "0",
            "sourceID": "00000001",
        }
        self.data = field(0)
        self.crc=field(16)
    def create_tc(self):
        data=False
        if self.data !=None : 
            self.tc_ccsds_header["pLength"]=format(len(self.data)+5,"016b")
            data=True
        tc_header = (
            self.tc_ccsds_header["vNum"]
            + self.tc_ccsds_header["Type"]
            + self.tc_ccsds_header["dataFieldFlag"]
            + self.tc_ccsds_header["APID"]
            + self.tc_ccsds_header["groupingFlags"]
            + self.tc_ccsds_header["seqCount"]
            + self.tc_ccsds_header["pLength"]
            + self.pus_header["sec_header_flag"]
            + self.pus_header["pus_vNum"]
            + self.pus_header["ack"]
            + self.pus_header["service"]
            + self.pus_header["subservice"]
            + self.pus_header["sourceID"]
        )
        tc_header=format(int(tc_header,2),"020x")
        if not data :
            tc=tc_header
        """else :
            tc=tc_header+self.data"""
        print(tc)
        crc=ecss_crc(bytes.fromhex(tc))
        tc=tc+crc
        print(tc_header)
        print(tc)
        return tc