from PIL import Image, ImageOps
import os
from skimage import io, transform, filters, exposure


def m4():
    Image.MAX_IMAGE_PIXELS = None
    for fn in os.listdir("all"):
        if fn.endswith("TIF"):
            adj_fn = fn.split("_B")[1]
            if len(adj_fn) == 5:
                adj_fn = "0" + adj_fn
            adj_fn = "A_" + adj_fn[:-4]
            print(adj_fn)

            image = io.imread("all/" + fn)
            print(image.shape)

            if fn.endswith("8.TIF"):
                pass
                region = image[3500*2:3900*2, 800*2:1200*2]
            else:
                region = image[3500:3900, 800:1200]
                region = transform.resize(region, (800,800), anti_aliasing=False)
            
            io.imsave("edited/"+adj_fn +".png", region)
           


def m5():
    Image.MAX_IMAGE_PIXELS = None
    for fn in os.listdir("all"):
        if fn.endswith("TIF"):
            adj_fn = fn.split("_B")[1]
            if len(adj_fn) == 5:
                adj_fn = "0" + adj_fn
            adj_fn = "A_" + adj_fn[:-4]
            print(adj_fn)

            image = io.imread("all/" + fn)
            print(image.shape)

            if fn.endswith("8.TIF"):
                pass
                region = image[3500*2:3900*2, 800*2:1200*2]
            else:
                region = image[3500:3900, 800:1200]
                region = transform.resize(region, (800,800), anti_aliasing=False)
            
            io.imsave("edited/"+adj_fn +".png", region)

            exp = exposure.equalize_adapthist(region)
            io.imsave("edited/"+adj_fn +"adj_adaphist.png", exp)
            
            region = exposure.equalize_hist(region)
            io.imsave("edited/"+adj_fn +"adj_hist.png", region)


            exp = exposure.adjust_sigmoid(region)
            io.imsave("edited/"+adj_fn +"adj_sig.png", exp)
            exp = exposure.adjust_gamma(region)
            io.imsave("edited/"+adj_fn +"adj_gam.png", exp)
            exp = exposure.adjust_log(region)
            io.imsave("edited/"+adj_fn +"adj_log.png", exp)
            # exp = exposure.equalize_hist(region)
            # io.imsave("edited/"+adj_fn +"adj_hist.png", exp)
            


            #roberts, sobel, scharr, prewitt
            edges = filters.roberts(exp)
            io.imsave("edited/"+adj_fn +"f_rob.png", edges)

            edges = filters.sobel(exp)
            io.imsave("edited/"+adj_fn +"f_sob.png", edges)

def m6():
    Image.MAX_IMAGE_PIXELS = None
    for fn in os.listdir("all"):
        if fn.endswith("TIF"):
            adj_fn = fn.split("_B")[1]
            if len(adj_fn) == 5:
                adj_fn = "0" + adj_fn
            adj_fn = "A_" + adj_fn[:-4]
            print(adj_fn)

            image = io.imread("all/" + fn)
            print(image.shape)

            if fn.endswith("8.TIF"):
                pass
                region = image[3500*2:3900*2, 800*2:1200*2]
            else:
                region = image[3500:3900, 800:1200]
                region = transform.resize(region, (800,800), anti_aliasing=False)
            
            io.imsave("edited/"+adj_fn +".png", region)

            adhist = exposure.equalize_adapthist(region)
            io.imsave("edited/"+adj_fn +"adj_adhist.png", adhist)
            exp = exposure.adjust_sigmoid(adhist)
            io.imsave("edited/"+adj_fn +"adj_adsig.png", exp)


            #roberts, sobel, scharr, prewitt
            edges = filters.roberts(adhist)
            io.imsave("edited/"+adj_fn +"f_rob.png", edges)
            edges = filters.sobel(adhist)
            io.imsave("edited/"+adj_fn +"f_sob.png", edges)
            edges = filters.scharr(adhist)
            io.imsave("edited/"+adj_fn +"f_sch.png", edges)
            edges = filters.prewitt(adhist)
            io.imsave("edited/"+adj_fn +"f_prew.png", edges)
            
            
            adhist = exposure.equalize_hist(region)
            io.imsave("edited/"+adj_fn +"adj_hist.png", adhist)
            exp = exposure.adjust_sigmoid(adhist)
            io.imsave("edited/"+adj_fn +"adj_sig.png", exp)


            
m6()