from secondary_fn import split_by_student
from secondary_fn import insert_ID
from secondary_fn import generate_set
from secondary_fn import add_tupl
from secondary_fn import add_dic
from secondary_fn import add_student
from secondary_fn import remove_stud
from secondary_fn import create_avg_dic
from secondary_fn import order_avg_dic
from secondary_fn import create_ranking
try:
    with open("Prueba.txt", "r", encoding="utf-8") as file:
        archivo_txt = file.readlines()
    class_202R = add_tupl(insert_ID(split_by_student(archivo_txt)))
    class_set = generate_set(class_202R)
    class_202R = add_dic(class_202R, class_set)
    print(class_set)
    print(class_202R)
    add_student(class_202R, class_set)
    class_202R, class_set = remove_stud(class_202R, class_set)
    print(class_set)
    print(class_202R)
    print(order_avg_dic(create_avg_dic(class_202R)))
    create_ranking(class_202R, order_avg_dic(create_avg_dic(class_202R)))
except FileNotFoundError as e:
    print(f"File doesn't exist: {e}")
except Exception as error:
    print(f"Error: {error}")