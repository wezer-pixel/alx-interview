def validUTF8(data):
    if not data:
        return False

    num_bytes = 0

    for num in data:
        bin_num = format(num, '08b')

        if num_bytes == 0:
            if bin_num.startswith("0"):
                continue
            elif bin_num.startswith("110"):
                num_bytes = 1
            elif bin_num.startswith("1110"):
                num_bytes = 2
            elif bin_num.startswith("11110"):
                num_bytes = 3
            else:
                return False
        else:
            if not bin_num.startswith("10"):
                return False
            num_bytes -= 1

    return num_bytes == 0
