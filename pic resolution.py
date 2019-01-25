#import image
from PIL import Image

#image name
pic = "1.jpg"

#image open
Pic1=Image.open(pic)

#image resolution
resolution=Pic1.size

#image resolution print
print "Image Resolution is :-",resolution
