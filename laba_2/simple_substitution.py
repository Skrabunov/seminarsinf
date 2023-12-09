def decoding(line):
    alphabet_turned = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    alphabet = "птхиёшцрыязэчджвфгмуъюьоксещйбанл"
    solver = {}
    for i in range(33):
        solver[alphabet_turned[i]]=alphabet[i]
        solver[alphabet_turned[i].upper()]=alphabet[i].upper()
    end = ""
    for x in line:
        end += solver.get(x,x)
    return end
print(decoding(input()))