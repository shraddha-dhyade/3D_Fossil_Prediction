#references:
#https://excamera.com/articles/26/doc/intro.html
#https://excamera.com/articles/26/doc/openexr.html

import matplotlib
import numpy
import OpenEXR
import Imath
import matplotlib.pyplot as plt

pt = Imath.PixelType(Imath.PixelType.FLOAT)
cube = OpenEXR.InputFile("/home/trichmo/Forams/SyntheticDataGenerator/Neural_Networks_marrnet/generated_samples/Generated_Foraminifera/species_1/specimen_03/Views/View_02.exr")
#cube.header() shows the header of the exr file. It will show all channel names and data type.
dw = cube.header()['dataWindow']
size = (dw.max.x - dw.min.x +1, dw.max.y - dw.min.y +1)

#show normal vectors
redstr= cube.channel('normal.R',pt)
greenstr= cube.channel('normal.G',pt)
bluestr= cube.channel('normal.B',pt)
red = numpy.fromstring(redstr, dtype=numpy.float32)
blue = numpy.fromstring(bluestr, dtype=numpy.float32)
green = numpy.fromstring(greenstr, dtype=numpy.float32)
red.shape = (size[1],size[0])
blue.shape = (size[1],size[0])
green.shape = (size[1],size[0])
img = numpy.stack((red,blue,green),axis=2)
img += 1
img /= 2
img *= 255
img = img.astype(numpy.uint8)
plt.imshow(img,cmap='jet',interpolation='nearest')
plt.show()


#show color img
redstr= cube.channel('color.R',pt)
greenstr= cube.channel('color.G',pt)
bluestr= cube.channel('color.B',pt)
red = numpy.fromstring(redstr, dtype=numpy.float32)
blue = numpy.fromstring(bluestr, dtype=numpy.float32)
green = numpy.fromstring(greenstr, dtype=numpy.float32)
red.shape = (size[1],size[0])
blue.shape = (size[1],size[0])
green.shape = (size[1],size[0])
img = numpy.stack((red,blue,green),axis=2)
plt.imshow(img,cmap='hot',interpolation='nearest')
plt.show()

greystr= cube.channel('distance.Y',pt)
grey = numpy.fromstring(greystr, dtype=numpy.float32)
grey.shape = (size[1],size[0])
plt.imshow(grey,cmap='hot',interpolation='nearest')
plt.show()
#note values in the image are scaled 0 to 255. The matrix values cannot be directly viewed due to distances being >255
print(numpy.argmax(grey))
print(numpy.argmin(grey))

#if you want the silhouette, just get the indices from the distance matrix


