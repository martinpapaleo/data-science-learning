'''
student_dic = {"Name": "Pepe", "Age": 21, "Grade": 8}
print(student_dic)
new_ord = ["Age", "Name", "Grade"]
ordered_dict = {key: student_dic[key] for key in new_ord if key in student_dic}
print(ordered_dict)
'''

def es_bisiesto(num):
    if num % 400 == 0:
        return True
    elif not (num % 100 == 0) and num % 4 == 0:
        return True
    else:
        return False
def dias_mes(mes_, bisiesto):
    if mes_ == 2 and bisiesto:
        return 29
    elif mes_ == 2:
        return 28
    elif mes_ in [1,3,5,7,8,10,12]:
        return 31
    else:
        return 30
def es_int(s):
    try:
        x = int(s)
        return True
    except ValueError:
        return False

def es_letras_o_num(s):
    for i in s:
        if not ("0" <= i <= "9" or "a" <= i <= "z" or "A" <= i <= "Z"):
            return False
    return True

cond = False
while not cond:
    cond = True
    fecha = input("Ingrese fecha en formato 'dd/mm/yyyy': ")
    if not (len(fecha) == 10):
        cond = False
    if cond:
        if not (fecha[2] == "/" and fecha[5] == "/"):
            cond = False
    if cond:
        for i in fecha[:2]:
            if not es_int(i):
                cond = False
        for i in fecha[3:5]:
            if not es_int(i):
                cond = False
        for i in fecha[6:]:
            if not es_int(i):
                cond = False    # A partir de ahora es valido el formato
    if cond and not (1 <= int(fecha[:2]) <= 31 and 1 <= int(fecha[3:5]) <= 12 and 1 <= int(fecha[6:]) <= 9999):
        cond = False
    if cond:
        if es_bisiesto(int(fecha[6:])):
            if not (1 <= int(fecha[:2]) <= dias_mes(int(fecha[3:5]), True)):
                cond = False
        else:
            if not (1 <= int(fecha[:2]) <= dias_mes(int(fecha[3:5]), False)):
                cond = False
cond = False
while not cond:
    cond = True
    nombre_arch = input("Ingrese nombre archivo valido (solo letras y/o numeros): ")
    if not es_letras_o_num(nombre_arch):
        cond = False
nombre_arch += ".txt"

with open(f"{nombre_arch}", "w", encoding="utf-8") as file:
    file.write(fecha)

