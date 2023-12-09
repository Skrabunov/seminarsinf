def decoding(line):
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    notalphabet = alphabet[::-1]
    solver = {}
    for i in range (33):
        solver[notalphabet[i]]=alphabet[i]
        solver[notalphabet[i].upper()]=alphabet[i].upper()
    decode=""
    for x in line:
        decode+=solver.get(x,x)
    return decode
print(decoding(input()))