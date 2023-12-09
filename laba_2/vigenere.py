def caesar_decode(line,rotation):
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
def decoding(line):
    code="столлман" #Клод Шеннон и 1945 год спасли!)
    code = code*(len(line)//4+1)
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    alphabet_square = [0]*33
    alphabet_square[0]=alphabet
    for i in range(1,33):
        alphabet_square[i] = alphabet[1:]+alphabet[0]
        alphabet = alphabet_square[i]
    alphabet=alphabet_square[0]
    solver_first = {}
    for i in range(33):
        solver_first[alphabet[i]]=i
    end = ""
    for i in range(len(line)):
        rotation = solver_first.get(code[i])
        end += caesar_decode(line[i],33-rotation)
    return end
print(decoding(input()))
