null = []
code = list(input())
pont = -1
out = ''
pte = ''

while pont < len(code):
    try:
        pont += 1
        out += code[pont]
        pont += 1
        out += code[pont]
        pont += 1
        out += code[pont]
    except IndexError:
        if pont != len(code):
            print('indexerror: code offset')
            break

    if out == 'nul':
        null.append(0)

    elif out == 'prt':
        if null:
            print(null[-1])
        else:
            print('argumentError: function (prt) expected 1 argument, got 0')
            break

    elif out == 'sif':
        if null:
            null.append(null.pop(0))  # currently a no-op
        else:
            print('argumentError: function (sif) expected 1 argument, got 0')
            break

    elif out == 'pta':
        if null:
            pte += str(null[-1])
        else:
            print('argumentError: function (pta) expected 1 argument, got 0')
            break

    elif out == 'pt8':
        try:
            print(chr(int(pte, 2)), end='')   # fixed to convert digits to char
        except:
            print('Unknown error has occurred')
            break

    elif out == 'flp':
        if null:
            if null[-1] == 0:
                null[-1] = 1  # fixed assignment
            else:
                null[-1] = 0
        else:
            print('argumentError: function (flp) expected 1 argument, got 0')
            break
    elif out == 'ptc': pte=''
    out = ''  # reset for next opcode
