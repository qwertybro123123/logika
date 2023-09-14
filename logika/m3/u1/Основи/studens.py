class studentsdas():
    def __init__(self, surname, name, grade) -> None:
        self.surname = surname
        self.name = name
        self.grade = grade
studens = []
with open("stud.txt", "r" , encoding="utf-8") as file:
    for line in file:   
        data = line.split(' ')
        obj = studentsdas(data[0],data[1],int(data[2]))
        studens.append(obj)


for studen in studens:
    if studen.grade == 5:
        print(studen.name, studen.surname)