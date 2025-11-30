def is_cap_letter(let_):
    if type(let_) != type(""):
        raise Exception("is_cap_let received invalid type of argument")
    if "A" <= let_ <= "Z":
        return True
    else:
        return False
def is_valid_name(str_):
    if type(str_) != type(""):
        raise Exception("es_palabra received invalid type of argument")
    for i in str_:
        if not ("a" <= i <= "z" or "A" <= i <= "Z"):
            return False
    return True
def is_int(str_num):
    if type(str_num) != type(""):
        raise Exception("es_num received invalid type of argument")
    try:
        sol = int(str_num)
        return True
    except ValueError as e:
        return False
def ask_age():
    cond_age = False
    while cond_age == False:
        cond_age = True
        age_ = input("Student age: ")
        if not (is_int(age_)):
            cond_age = False
        if cond_age:
            if not (int(age_) > 0):
                cond_age = False
    return age_
def ask_grade():
    cond = False
    while cond == False:
        cond = True
        grade_ = input("Type studante grade: ")
        if not (is_int(grade_) or grade_ == "-"):
            cond = False
        if cond and grade_ != "-":
            if not (0 <= int(grade_) <= 10):
                cond = False
    return grade_
def add_student(dic_, set_):
    if type(dic_) != type({"a": 1}) or type(set_) != type({1, 2}):
        raise Exception("add_student received invalid type of argument")
    cond, cond_2 = False, True
    while cond == False and cond_2:
        cond = True
        print("Type enter in student name if you whish to cancel input")
        name_ = input("Student name: ")
        if name_ == "":
            cond_2 = False
        if cond and cond_2:
            if not (is_valid_name(name_)):
                cond = False
        if cond and cond_2:
            age = ask_age()
            grades_ = []
            grades_.append(ask_grade())
            grades_.append(ask_grade())
            grades_.append(ask_grade())
            grades_ = tuple(grades_)
    if len(name_) == 0:
        return dic_, set_
    else:
        from random import randint
        stud_info = []
        stud_info.append(name_)
        stud_info.append(age)
        stud_info.append(grades_)
        cond = False
        while cond == False:
            cond = True
            stud_id = randint(1000, 9999)
            if not (stud_id not in set_):
                cond = False
        dic_[stud_id] = stud_info
        set_.add(stud_id)
        return dic_, set_
def order_avg_dic(dic_):
    if type(dic_) != type({1: 2}):
        raise Exception("order_avg_dic received invalid type of argument")
    lst_avg_ord, lst_id_ord = [], []
    for i in dic_:
        if len(lst_avg_ord) == 0:
            lst_avg_ord.append(dic_[i])
            lst_id_ord.append(i)
        else:
            t = 0
            length = len(lst_avg_ord)
            cond = True
            while t < length and cond:
                if dic_[i] >= lst_avg_ord[t]:
                    lst_avg_ord.insert(t, dic_[i])
                    lst_id_ord.insert(t, i)
                    cond = False
                t += 1
            if cond:
                lst_avg_ord.append(dic_[i])
                lst_id_ord.append(i)
    return lst_avg_ord, lst_id_ord
def create_avg_dic(dic_):
    if type(dic_) != type({1: 2}):
        raise Exception("create_avg_dic received invalid type of argument")
    prom_dic = {}
    from statistics import mean
    for i in dic_:
        final_grades = []
        for grade in dic_[i][2]:
            try:
                if 0 <= int(grade) <= 10:
                    final_grades.append(int(grade))
            except ValueError:
                final_grades.append(0)
        prom_dic[i] = round(mean(final_grades), 2)
    return prom_dic
def create_ranking(dic_, tupl_):
    if type(dic_) != type({1: 2}) or type(tupl_) != type((1,2)):
        raise Exception("create_ranking received wrong type of argument")
    longest = 0
    for i in dic_:
        if len(dic_[i][0]) > longest:
            longest = len(dic_[i][0])
    with open("Ranking.txt", "w+", encoding="utf-8") as file:
        t = 1
        for i in tupl_[1]:
            name = dic_[i][0]
            while len(name) < longest:
                name = " " + name
            file.write(f"{t}. Student ID: {i}, Name: {name}, Course grade: {tupl_[0][t - 1]}\n")
            t += 1
def remove_stud(dic_, set_):
    if type(dic_) != type({"a": 1}) or type(set_) != type({1, 2}):
        raise Exception("add_student received invalid type of argument")
    cond = False
    while cond == False:
        cond = True
        print("If you whish to cancel student deletion, hit enter when asked to type student id")
        stud_id = input("Type student ID number for removal: ")
        try:
            if int(stud_id) not in set_:
                cond = False
        except ValueError:
            cond = False
        if stud_id == "":
            return dic_, set_
    new_dic = list(dic_)
    print(new_dic)
    pos = 0
    while pos < len(new_dic):
        if new_dic[pos] == int(stud_id):
            del new_dic[pos]
            set_.remove(int(stud_id))
        pos += 1
    new_dic = {key: dic_[key] for key in new_dic if key in dic_}
    return new_dic, set_
def return_format(str_):            # receives a string and returns it stripped from unnecessary information
    if type(str_) != type(""):
        raise Exception("return_format received invalid type of argument")
    info_ = ["Student", "Age", "Grade_1", "Grade_2", "Grade_3"]
    cond = False
    t, pos = 0, 0
    sol = ""
    while t < len(info_) and not cond:
        if info_[t] in str_:
            cond = True
            pos = t
        t += 1
    if pos == 0:
        w = 1                              # Student:\tJuan\n
        condi = True
        while w < len(str_) and condi:
            if is_cap_letter(str_[w]):
                sol = str_[w: len(str_) - 1]
                condi = False
            w += 1
    elif pos == 1:
        for i in str_:
            if "0" <= i <= "9":
                sol += i
    else:
        for i in str_[8:]:
            if "0" <= i <= "9" or i == "-":
                sol += i
    return sol
def split_by_student(lst_):         # takes the whole lst from the file and returns a new one with sublists for each student
    if type(lst_) != type([]):
        raise Exception("split_by_student received invalid type of argument")
    sub_lst, final_lst = [], []
    t = 0
    split = "---"
    while t < len(lst_):
        if split not in lst_[t]:
            sub_lst.append(return_format(lst_[t]))
        else:
            if len(sub_lst) != 0:
                final_lst.append(sub_lst)
                sub_lst = []
        t += 1
    return final_lst
def insert_ID(lst_):
    if type(lst_) != type([]):
        raise Exception("insert_ID received invalid type of argument")
    from random import randint
    lst_id = []
    while len(lst_) != len(lst_id):
        id_ = randint(1000, 9999)
        if id_ not in lst_id:
            lst_id.append(id_)
    t = 0
    while t < len(lst_):
        lst_[t].insert(0, lst_id[t])
        t += 1
    return lst_
def generate_set(lst_):
    if type(lst_) != type([]):
        raise Exception("generate_set received invalid type of argument")
    sol = []
    for i in lst_:
        sol.append(i[0])
    sol = set(sol)
    return sol
def add_tupl(lst_):
    if type(lst_) != type([]):
        raise Exception("return_tupl received invalid type of argument")
    t = 0
    while t < len(lst_):
        if len(lst_[t]) != 6:
            raise Exception("return_tupl received invalid argument")
        t += 1
    sol = []
    t = 0
    while t < len(lst_):
        grades_ = tuple(lst_[t][3:])
        lst_[t] = lst_[t][:3]
        lst_[t].append(grades_)
        t += 1
    return lst_
def add_dic(lst_, set_):
    if type(lst_) != type([]) or type(set_) != type({1, 2}):
        raise Exception("return_dic received invalid type of argument")
    if len(lst_) != len(set_):
        raise Exception("return_dic received invalid list")
    sol = {}
    for i in set_:
        t = 0
        while t < len(lst_):
            if lst_[t][0] == i:
                sol[i] = lst_[t][1:]
            t += 1
    return sol
def write_error(num_, name_file):
    if type(num_) != type(1) or type(name_file) != type(""):
        raise Exception("write_error received invalid type of argument")
    try:
        with open(f"{name_file}", "r", encoding="utf-8") as fd:
            file = fd.readlines()
            file.insert(num_, "ERROR FORMATO")
        with open(f"{name_file}", "w", encoding="utf-8") as fd:
            fd.writelines(file)
    except FileNotFoundError as e:
        print(f"File {name_file} doesn't exist")