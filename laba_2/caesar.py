def decoding(line,rotation):
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    alphabet+=alphabet
    alphabet_upper=alphabet.upper()
    solver={}
    for i in range(33):
        solver[alphabet[i]] = alphabet[i+rotation%33]
        solver[alphabet_upper[i]] = alphabet_upper[i+rotation%33]
    decode = ""
    for x in line:
        decode += solver.get(x,x)
    return decode
#line=input() --- подбор ротации
#for i in range(33):
#    print(decoding(line,i),"rotation =",i)
print(decoding(input(),14))