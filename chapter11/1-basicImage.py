from PIL import Image, ImageFilter

kitten = Image.open("./files/kitten.jpg")
blurryKitten = kitten.filter(ImageFilter.GaussianBlur)
blurryKitten.save("./files/kitten_blurred.jpg")
blurryKitten.show()