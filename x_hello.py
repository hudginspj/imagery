from PIL import Image, ImageOps
import os
from skimage import io, transform

def m1():
    im = Image.open("test.jpg")
    print(im.format, im.size, im.mode)
    #im.show()
    #input("press enter")
    box = (800, 3500, 1200, 3900)
    region = im.crop(box)
    print(region.size)
    region.save("test2.jpg")
    #region.show()
    im = Image.open("test2.jpg")
    print(im.format, im.size, im.mode)

def m2():
    Image.MAX_IMAGE_PIXELS = None
    for fn in os.listdir("all"):
        if fn.endswith("TIF"):
            adj_fn = fn.split("_B")[1]
            if len(adj_fn) == 5:
                adj_fn = "0" + adj_fn
            adj_fn = "all/cropped_" + adj_fn
            print(adj_fn)

            im = Image.open("all/" + fn)
            print(im.format, im.size, im.mode)

            if adj_fn == "all/cropped_08.TIF":
                box = (800*2, 3500*2, 1200*2, 3900*2)
                region = im.crop(box)
                region.save(adj_fn) 
            else:
                box = (800, 3500, 1200, 3900)
                region = im.crop(box)
                region.save(adj_fn)

def m3():
    Image.MAX_IMAGE_PIXELS = None
    for fn in os.listdir("all"):
        if fn.endswith("TIF"):
            adj_fn = fn.split("_B")[1]
            if len(adj_fn) == 5:
                adj_fn = "0" + adj_fn
            adj_fn = "edited/A_" + adj_fn
            print(adj_fn)

            im = Image.open("all/" + fn)
            print(im.format, im.size, im.mode)

            if fn.endswith("8.TIF"):
                box = (800*2, 3500*2, 1200*2, 3900*2)
                region = im.crop(box)
            else:
                box = (800, 3500, 1200, 3900)
                region = im.crop(box)
                region = region.resize((800,800))
            
            region = ImageOps.equalize(region)
            region.save(adj_fn)
            print(region.size)

def m4():
    Image.MAX_IMAGE_PIXELS = None
    for fn in os.listdir("all"):
        if fn.endswith("TIF"):
            adj_fn = fn.split("_B")[1]
            if len(adj_fn) == 5:
                adj_fn = "0" + adj_fn
            adj_fn = "edited/A_" + adj_fn
            print(adj_fn)

            #im = Image.open("all/" + fn)
            image = io.imread("all/" + fn)
            print(image.shape)
            #cropped = image[x1:x2,y1:y2]
            #print(im.format, im.size, im.mode)

            if fn.endswith("8.TIF"):
                pass
                # box = (800*2, 3500*2, 1200*2, 3900*2)
                # region = im.crop(box)
            else:
                # box = (800, 3500, 1200, 3900)
                # region = im.crop(box)
                # region = region.resize((800,800))
                #region = image[800:1200, 3500:3900]
                region = image[3500:3900, 800:1200]
                io.imsave(adj_fn, region)
                print(region.shape)

                region = transform.resize(image, (800,800))
                print(region.shape)
                io.imsave("B"+adj_fn, region)

            
            # region = ImageOps.equalize(region)
            # region.save(adj_fn)
            # print(region.size)



m4()