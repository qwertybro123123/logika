with open("virsik.txt", "r" , encoding="utf-8") as file:
    text = file.read()
    print(text)
avtor = input("хто автор? ")
with open("virsik.txt", "w" , encoding="utf-8") as file:
    print(file.write(text+avtor))
while 1:
    text2 = input("додати ше? 'ні' щоб вийти ")
    if text2 == "ні":
        break
    else:
        with open("virsik.txt", "w" , encoding="utf-8") as file:
            file.write(text+text2)

with open("virsik.txt", "r" , encoding="utf-8") as file:
    text = file.read()
    print(text)
