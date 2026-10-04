import Field
class tc_packet:
    def __init__(self):
        self.tc_ccsds_header={
            "vNum" : b'000',
            "Type" : b'1',
            "dataFieldFlag" : b'0',
            "APID" : Field(11),
            "groupingFlags" : b'11',
            "seqCount" : Field(14),
            "pLength" : Field(16)
        }
        self.pus_header={
            "sec_header_flag" : b'0',
            "pus_vNum" : b'001',
            "ack" : Field(4),
            "service" : Field(8),
            "subservice" : Field(8),
            "sourceID": b'00000001',
        }
        self.data = Field(0)
        self.crc=Field(16)