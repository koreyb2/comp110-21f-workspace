__author__ = "730425339"


def decode_char(x: str) -> str:
    """Shift given string by one place in the alphabet."""
    ascii_code: int = ord(x)
    if ascii_code % 90 == 0:
        ascii_code = ascii_code - 25
    else:
        ascii_code = ascii_code - 1
    encoded_character: str = chr(ascii_code)
    return encoded_character


def decode_str(x: str) -> str:
    """Decode a given string."""
    decoded: str = ""
    i: int = 0
    while i < len(x):
        ascii_code: int = ord(x[0])
        if ascii_code % 90 == 0:
            ascii_code = ascii_code - 25
        else:
            ascii_code = ascii_code - 1
        encoded_character: str = chr(ascii_code)
        decoded = encoded_character
        encoded_character = ""
        i += 1
    return decoded


print(decode_str("BCDEF"))