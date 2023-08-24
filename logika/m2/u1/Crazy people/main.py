from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from random import randint

s = True

app = QApplication([])
main_window = QWidget()

buton = QPushButton("Скачати 1221 троянів")
text = QLabel("Натисни щоб скачати майнкрафт 2 без регистрації і смс")
winner = QLabel("?")


line = QVBoxLayout()
line.addWidget(text)
line.addWidget(winner)
line.addWidget(buton)

def win():
    global s
    if s == True:
        ran = randint(1, 1000) 
        winner.setText(str(ran))
        buton.hide()
        s=False

        
buton.clicked.connect(win)


main_window.setLayout(line)






main_window.show()
app.exec_()