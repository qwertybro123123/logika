from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, 
    QHBoxLayout, QVBoxLayout, QListWidget, QLineEdit, 
    QTextEdit, QInputDialog, QTableWidget,  QListWidgetItem,
    QFormLayout, QGroupBox, QButtonGroup, QRadioButton, QSpinBox)
import json

def save_file():
    with open("txt.json", "w", encoding="utf-8") as file:   
        json.dump(notes, file, ensure_ascii=False, sort_keys = True, indent=4)   





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
tg_edit = QLineEdit("")

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




def show_note():
    key = lst_notes.currentItem().text()
    field_text.setText(notes[key]["текст"])
    
    tg_lst.clear()
    tg_lst.addItems(notes[key]["теги"])
    
def save_note():
    key = lst_notes.currentItem().text()
    notes[key]["текст"] = field_text.toPlainText()

    save_file()



def add_note():
    note_name, ok = QInputDialog.getText(window, "Додавання замітки", "Назва замітки")
    if note_name and ok:
        notes[note_name] = {"текст": '', "теги": []}    
        lst_notes.addItem(note_name)

def del_note():
    key = lst_notes.currentItem().text()
    del notes[key]
    save_file()

    field_text.clear()
    lst_notes.clear()
    tg_lst.clear()
    lst_notes.addItems(notes)



def add_tag():
    key = lst_notes.currentItem().text()
    tag = tg_edit.text()

    notes[key]["теги"].append(tag)

    tg_lst.addItem(tag)
    tg_edit.clear()
    
    save_file()


def del_tag():
    key = lst_notes.currentItem().text()
    tag = tg_lst.currentItem().text()

    notes[key]["теги"].remove(tag)

    tg_lst.clear()
    tg_lst.addItems(notes[key]["теги"])

    save_file()


def find_tag():
    tag = tg_edit.text()

    if btn_tg_find.text() == "Шукати за тегом":
        filtered_notes = {}

        for key in notes:  
            if tag in notes[key]["теги"]:
                filtered_notes[key] = notes[key]
        btn_tg_find.setText("Скинути пошук")
        lst_notes.clear()
        lst_notes.addItems(filtered_notes)

        tg_lst.clear()

    elif btn_tg_find.text() == "Скинути пошук":
        btn_tg_find.setText("Шукати за тегом")

        lst_notes.clear()
        tg_lst.clear()
        tg_edit.clear()

        lst_notes.addItems(notes)


btn_tg_create.clicked.connect(add_tag)
btn_tg_delete.clicked.connect(del_tag)
btn_tg_find.clicked.connect(find_tag)

with open("txt.json", "r", encoding="utf-8") as file:
    notes = json.load(file)

btn_note_create.clicked.connect(add_note)
btn_note_delete.clicked.connect(del_note)


btn_note_save.clicked.connect(save_note)
lst_notes.itemClicked.connect(show_note)
lst_notes.addItems(notes)



window.setStyleSheet('''
                        background-color: rgb(25, 25, 112); 
                        color: white;
                        font-size: 20px;
                        border: 2px solid white; 
                        ''')
btn_note_create.setStyleSheet('''
                        background-color: green;
                        color: white;
                        font-size: 20px;
                        border: 2px solid white; 
                        ''')
btn_note_delete.setStyleSheet('''
                        background-color: red;
                        color: white;
                        font-size: 20px;
                        border: 2px solid white; 
                        ''')
btn_tg_create.setStyleSheet('''
                        background-color: green;
                        color: white;
                        font-size: 20px;
                        border: 2px solid white; 
                        ''')
btn_tg_delete.setStyleSheet('''
                        background-color: red;
                        color: white;
                        font-size: 20px;
                        border: 2px solid white; 
                        ''')
window.setLayout(layout_notes)
window.show()
app.exec_()