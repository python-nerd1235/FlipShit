def char_to_ops(ch):
    ops = ""
    binary = f"{ord(ch):07b}"
    for bit in binary:
        if bit == "0":
            ops += "nulpta"
        else:
            ops += "nulflppta"
    ops += "pt8ptc"
    return ops

def text_to_ops(text):
    return "".join(char_to_ops(ch) for ch in text)

print(text_to_ops("Hello World"))
