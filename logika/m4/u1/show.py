from PIL import Image, ImageFilter
with Image.open("sigma.jpg") as original:

    print(original.size)
    print(original.format)
    print(original.mode)

    bw_original = original.convert("L")
    blur_original = original.filter(ImageFilter.BLUR)
    pic_up = original.transpose(Image.ROTATE_180)

    
    
    
    original.show()
    bw_original.show()
    blur_original.show()
    pic_up.show()

    bw_original.save("bw.jpg")
    blur_original.save("blur.jpg")
    pic_up.save("up.jpg")
