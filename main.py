string = """case 0x0066BB:
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
            return 226""".replace(" ", "").replace("case", "").replace("return", "")
l = string.split("\n")
i = 0
n = ""
for j in range(int(len(l))):
    if l[j][-1] != ":":
        l[j] += ","
    n += l[j]
    if i % 2 == 1:
        n += "\n"
    i += 1
values = n.split("\n")
b = ""
for j in values:
    try:
        a = j.split(":")
        b += a[1] + a[0] + ":" + "\n"
    except:
        a = ""
print(b.replace(":", ".").replace(",", ":").replace(".", ","))