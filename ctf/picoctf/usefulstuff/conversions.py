def b_to_string(bytes):
    return bytes.decode('utf-8')

def dec_to_string(number):
    m_hex = format(number, 'x')
    return bytes.fromhex(m_hex).decode("ASCII")
