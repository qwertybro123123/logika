from PIL import Image, ImageFilter

class ImageEditor():
    def __init__(self, file_name):
        self.file_name = file_name
        self.original = None
        self.changed = []

    def open(self):
        try:
            self.original = Image.open(self.file_name)
            self.original.show()    
        except:
            print("File is not found")
    def do_left(self):
        left = self.original.transpose(Image.ROTATE_90)

        self.changed.append(left)
        left.save("rotate_" + self.file_name)
    def do_crop(self):
        box = (100,100,200,200)
        croped = self.original.crop(box)
        self.changed.append(croped)
        croped.save("cropped_"+self.file_name)




img = ImageEditor("sigma.jpg")
img.open()
img.do_left()

