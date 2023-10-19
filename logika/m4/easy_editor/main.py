from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap 

from PIL import Image, ImageFilter

import os


app = QApplication([])
window = QWidget()




btn_folder = QPushButton("folder")
btn_left = QPushButton("right")
btn_right = QPushButton("left")
btn_flip = QPushButton("flip")
btn_sharp = QPushButton("sharp")
btn_bw = QPushButton("b/w")

lst_files = QListWidget()
lb_pic = QLabel("卍")


layout_editor = QHBoxLayout()

col1 = QVBoxLayout()
col2 = QVBoxLayout()

row1 = QHBoxLayout()

col1.addWidget(btn_folder)
col1.addWidget(lst_files)

row1.addWidget(btn_left)
row1.addWidget(btn_right)
row1.addWidget(btn_flip)
row1.addWidget(btn_sharp)
row1.addWidget(btn_bw)

col2.addWidget(lb_pic)
col2.addLayout(row1)

layout_editor.addLayout(col1,1)
layout_editor.addLayout(col2,4)


workdir = QFileDialog.getExistingDirectory()
files = os.listdir(workdir)

def filter(filenames):
    result = []
    ext = ["jpg","png","jpeg","bmp","gif"]
    for file in filenames:
        if file.split(".")[-1] in ext:
            result.append(file)
            
    return result

window.setLayout(layout_editor)
window.show()
app.exec_()


