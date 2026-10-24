from packets import field
class tm_packet:
    def __init__(self):
        self.tc_ccsds_header={
            "vNum" : b'000',
            "Type" : b'1',
            "dataFieldFlag" : b'0',
            "APID" : field(11),
            "groupingFlags" : b'11',
            "seqCount" : field(14),
            "pLength" : field(16)
        }
        self.pus_header={
            "spare" : b'0',
            "pus_vNum" : b'001',
            "spare" : b'0000',
            "service" : field(8),
            "subservice" : field(8),
            "destID": b'00000001',
            "time" : field(56)
        }
        self.data = None
        self.crc=None