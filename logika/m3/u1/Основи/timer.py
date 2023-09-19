from time import *
start_time = time()
with open("students_large.txt", "r" , encoding="utf-8") as file:
    text = file.read()
    print(text)
end_time = time()
print(round(end_time - start_time, 2))