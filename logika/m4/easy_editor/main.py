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
lb_pic = QLabel("")   


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



def filter(filenames):
    result = []
    ext = ["jpg","png","jpeg","bmp","gif"]
    for file in filenames:
        if file.split(".")[-1] in ext:
            result.append(file)
            
    return result

def show_files():
    global workdir
    workdir = QFileDialog.getExistingDirectory()
    files = os.listdir(workdir)
    graphic_files = filter(files)

    lst_files.clear()
    lst_files.addItems(graphic_files)

class ImageProcessor():
    def __init__(self) -> None:
        self.original = None
        self.filename = None
        self.save_dir = "Modified/"

    def load_image(self, filename):
        self.filename = filename
        full_path = os.path.join(workdir, filename)
        self.original = Image.open(full_path)

    def show_image(self, path):
        lb_pic.hide()

        pixmapimage = QPixmap(path)
        w,h = lb_pic.width(), lb_pic.height()

        pixmapimage = pixmapimage.scaled(w,h,Qt.KeepAspectRatio)

        lb_pic.setPixmap(pixmapimage)
        lb_pic.show()

    def saveAndShowImage(self):
        path = os.path.join(workdir, self.save_dir)

        if not (os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)

        image_path = os.path.join(path,self.filename)
        self.original.save(image_path)
        self.show_image(image_path)

def showChosenItem():
    filename = lst_files.currentItem().text()
    workimage.load_image(filename)
    full_path = os.path.join(workdir, filename)
    workimage.show_image(full_path)

workimage = ImageProcessor()



lst_files.currentRowChanged.connect(showChosenItem)

btn_folder.clicked.connect(show_files)

window.setLayout(layout_editor)
window.show()
app.exec_()


