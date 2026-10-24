def ecss_crc(data: bytes) -> bytes:
    """Computes CRC on data using the ECSS PUS algorithm
    (CRC-16/CCITT-FALSE: poly=0x1021, init=0xFFFF, no input/output reflection)
    :param data: data on which to apply CRC
    :type data: bytes
    :return: the CRC
    :rtype: bytes
    """
    crc = 0xFFFF
    for byte in data:
        crc ^= byte << 8
        for _ in range(8):
            if crc & 0x8000:
                crc = ((crc << 1) ^ 0x1021) & 0xFFFF
            else:
                crc = (crc << 1) & 0xFFFF
    return crc.to_bytes(length=2, byteorder="big").hex()