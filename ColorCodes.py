HEX_CODES = [26299, 187, 48059, 0, 47872, 47974, 6732544, 12255419, 12281344, 12255334, 12255232, 8947848, 8939008, 6684859, 12303291, 12303104, 35071, 255, 65535, 6710886, 65280, 65416, 8978176, 16711935, 16746496, 16711816, 16711680, 14540253, 14531328, 8913151, 16777215, 16776960]

def ConvertAnsiToHex(code: int):
        match code:
            case 25:
                return 0x0066BB
            case 19:
                return 0x0000BB
            case 37:
                return 0x00BBBB
            case 16:
                return 0x000000
            case 34:
                return 0x00BB00
            case 35:
                return 0x00BB66
            case 70:
                return 0x66BB00
            case 127:
                return 0xBB00BB
            case 130:
                return 0xBB6600
            case 125:
                return 0xBB0066
            case 124:
                return 0xBB0000
            case 102:
                return 0x888888
            case 94:
                return 0x886600
            case 55:
                return 0x6600BB
            case 145:
                return 0xBBBBBB
            case 142:
                return 0xBBBB00
            case 33:
                return 0x0088FF
            case 21:
                return 0x0000FF
            case 51:
                return 0x00FFFF
            case 59:
                return 0x666666
            case 46:
                return 0x00FF00
            case 48:
                return 0x00FF88
            case 118:
                return 0x88FF00
            case 201:
                return 0xFF00FF
            case 208:
                return 0xFF8800
            case 198:
                return 0xFF0088
            case 196:
                return 0xFF0000
            case 188:
                return 0xDDDDDD
            case 178:
                return 0xDDBB00
            case 93:
                return 0x8800FF
            case 231:
                return 0xFFFFFF
            case 226:
                return 0xFFFF00

def ConvertHexToAnsiCode(code: int):
    match code:
        case 0x0066BB:
            return 25
        case 0x0000BB:
            return 19
        case 0x00BBBB:
            return 37
        case 0x000000:
            return 16
        case 0x00BB00:
            return 34
        case 0x00BB66:
            return 35
        case 0x66BB00:
            return 70
        case 0xBB00BB:
            return 127
        case 0xBB6600:
            return 130
        case 0xBB0066:
            return 125
        case 0xBB0000:
            return 124
        case 0x888888:
            return 102
        case 0x886600:
            return 94
        case 0x6600BB:
            return 55
        case 0xBBBBBB:
            return 145
        case 0xBBBB00:
            return 142
        case 0x0088FF:
            return 33
        case 0x0000FF:
            return 21
        case 0x00FFFF:
            return 51
        case 0x666666:
            return 59
        case 0x00FF00:
            return 46
        case 0x00FF88:
            return 48
        case 0x88FF00:
            return 118
        case 0xFF00FF:
            return 201
        case 0xFF8800:
            return 208
        case 0xFF0088:
            return 198
        case 0xFF0000:
            return 196
        case 0xDDDDDD:
            return 188
        case 0xDDBB00:
            return 178
        case 0x8800FF:
            return 93
        case 0xFFFFFF:
            return 231
        case 0xFFFF00:
            return 226

def ConvertHexToRGB(code: int):
    return tuple(int(code[i:i + 2], 16) for i in (0, 2, 4))

def ConvertRGBToHex(code: tuple):
    return "{:02x}{:02x}{:02x}".format(code[0], code[1], code[2])

def ConvertHexToAnsi(code: int):
    smallestDifference = [0xFFFFFFF, 0]
    for i in HEX_CODES:
        if smallestDifference[0] > abs(code - i):
            smallestDifference[0] = abs(code - i)
            smallestDifference[1] = i
    return ConvertHexToAnsiCode(smallestDifference[1])