# __main__.py
import serial
import serial.tools.list_ports


from database import loader
from packets import tc_packet
from utils.check_tm import check_tm
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
        tc.tc_ccsds_header["APID"]=format(tc_database[tc_name]["APID"],"011b")
        tc.tc_ccsds_header["seqCount"]=format(0,"014b")
        #tc.tc_ccsds_header["pLength"]=format(0,"016b")

        tc.pus_header["service"]=format(tc_database[tc_name]["service"],"08b")
        tc.pus_header["subservice"]=format(tc_database[tc_name]["subservice"],"08b")
        
        tc.data=None    
        tc.crc=format(0,"016b")
        print(type(tc.tc_ccsds_header["pLength"]))
        telecommand = tc.create_tc()
    else:
        print("TC doesnt exist in the Data Base. Please verify the name or add it to DBs")


    ######################################################
    """" Connection with the FT32 USB-to-UART converter"""
    ######################################################
    ports = serial.tools.list_ports.comports()
    ft232_port = None

    for port in ports:
        if port.vid == 0x0403 and port.pid == 0x6001:
            ft232_port = port.device
            print(f"Found FT232 on: {ft232_port}")
            break

    if ft232_port is None:
        raise RuntimeError("FT232 USB-to-UART converter not found!")
    ######################################################
    """" Connection with the FT32 USB-to-UART converter"""
    ######################################################

    # Step 2: Open the serial connection
    try:
        with serial.Serial(
            port=ft232_port,
            baudrate=115200,
            bytesize=serial.EIGHTBITS,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            timeout=1
        ) as ser:

            print(f"Successfully connected to {ser.name}")

            # Send your telecommand as bytes
            tc_bytes = bytes.fromhex(telecommand)
            ser.write(tc_bytes)
            ser.flush()

            print(f"Sent: {tc_bytes.hex(' ')}")

            # Read the response as raw bytes
            telemetry = ser.read(20)
            print(f"Received: {telemetry.hex(' ')}")
            tm=check_tm(telemetry)
            if tm : print("Telemtry : " ,tm)

    except serial.SerialException as e:
        print(f"Serial communication error: {e}")
if __name__ == "__main__":
    main()