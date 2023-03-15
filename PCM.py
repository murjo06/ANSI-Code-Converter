HEX_CODES = [26299, 187, 48059, 0, 47872, 47974, 6732544, 12255419, 12281344, 12255334, 12255232, 8947848, 8939008, 6684859, 12303291, 12303104, 35071, 255, 65535, 6710886, 65280, 65416, 8978176, 16711935, 16746496, 16711816, 16711680, 14540253, 14531328, 8913151, 16777215, 16776960]
HEX_TO_ANSI = {
    0x0066BB: 25,
    0x0000BB: 19,
    0x00BBBB: 37,
    0x000000: 16,
    0x00BB00: 34,
    0x00BB66: 35,
    0x66BB00: 70,
    0xBB00BB: 127,
    0xBB6600: 130,
    0xBB0066: 125,
    0xBB0000: 124,
    0x888888: 102,
    0x886600: 94,
    0x6600BB: 55,
    0xBBBBBB: 145,
    0xBBBB00: 142,
    0x0088FF: 33,
    0x0000FF: 21,
    0x00FFFF: 51,
    0x666666: 59,
    0x00FF00: 46,
    0x00FF88: 48,
    0x88FF00: 118,
    0xFF00FF: 201,
    0xFF8800: 208,
    0xFF0088: 198,
    0xFF0000: 196,
    0xDDDDDD: 188,
    0xDDBB00: 178,
    0x8800FF: 93,
    0xFFFFFF: 231,
    0xFFFF00: 226
}
ANSI_TO_HEX = {
    25: 0x0066BB,
    19: 0x0000BB,
    37: 0x00BBBB,
    16: 0x000000,
    34: 0x00BB00,
    35: 0x00BB66,
    70: 0x66BB00,
    127: 0xBB00BB,
    130: 0xBB6600,
    125: 0xBB0066,
    124: 0xBB0000,
    102: 0x888888,
    94: 0x886600,
    55: 0x6600BB,
    145: 0xBBBBBB,
    142: 0xBBBB00,
    33: 0x0088FF,
    21: 0x0000FF,
    51: 0x00FFFF,
    59: 0x666666,
    46: 0x00FF00,
    48: 0x00FF88,
    118: 0x88FF00,
    201: 0xFF00FF,
    208: 0xFF8800,
    198: 0xFF0088,
    196: 0xFF0000,
    188: 0xDDDDDD,
    178: 0xDDBB00,
    93: 0x8800FF,
    231: 0xFFFFFF,
    226: 0xFFFF00
}



def convertHexToRGB(code: int):
    return tuple(int(str(code)[i:i + 2], 16) for i in (0, 2, 4))

def convertRGBToHex(code: tuple):
    return "{:02x}{:02x}{:02x}".format(code[0], code[1], code[2])

def convertHexToAnsi(code: int):
    smallestDifference = [0xFFFFFFF, 0]
    for i in HEX_CODES:
        if smallestDifference[0] > abs(code - i):
            smallestDifference[0] = abs(code - i)
            smallestDifference[1] = i
    return convertHexToAnsiCode(smallestDifference[1])