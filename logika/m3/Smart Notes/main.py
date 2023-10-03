from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, 
    QHBoxLayout, QVBoxLayout, QListWidget, QLineEdit, 
    QTextEdit, QInputDialog, QTableWidget,  QListWidgetItem,
    QFormLayout, QGroupBox, QButtonGroup, QRadioButton, QSpinBox)
import json
app = QApplication([])
window = QWidget()

field_text = QTextEdit()
lb_notes = QLabel("Замітки")
lst_notes = QListWidget()

btn_note_create = QPushButton("Зробити замітку")
btn_note_delete = QPushButton("Видалити замітку")
btn_note_save = QPushButton("Зберегти замітку")

tg_lb = QLabel("Теги")
tg_lst = QListWidget()
tg_edit = QLineEdit("Введіть тег...")

btn_tg_create = QPushButton("Зробити тег")
btn_tg_delete = QPushButton("Видалити тег")
btn_tg_find = QPushButton("Шукати за тегом")

layout_notes = QHBoxLayout()
col1 = QVBoxLayout()
col2 = QVBoxLayout()

layout_notes.addLayout(col1, stretch=2)
layout_notes.addLayout(col2, stretch=1)

col1.addWidget(field_text)
col2.addWidget(lb_notes)

row1 = QHBoxLayout()
row1.addWidget(btn_note_create)
row1.addWidget(btn_note_delete)

row2 = QHBoxLayout()
row2.addWidget(btn_note_save)

row3 = QHBoxLayout()
row3.addWidget(tg_lb)

row4 = QHBoxLayout()
row4.addWidget(tg_lst)

row5 = QHBoxLayout()
row5.addWidget(tg_edit)

row6 = QHBoxLayout()
row6.addWidget(btn_tg_create)
row6.addWidget(btn_tg_delete)

row7 = QHBoxLayout()
row7.addWidget(btn_tg_find)



col2.addWidget(lst_notes)
col2.addLayout(row1)
col2.addLayout(row2)
col2.addLayout(row3)
col2.addLayout(row4)
col2.addLayout(row5)
col2.addLayout(row6)
col2.addLayout(row7)








with open("txt.json", "r", encoding="utf-8") as file:
    notes = json.load(file)
lst_notes.addItems(notes)

window.setLayout(layout_notes)
window.show()
app.exec_()