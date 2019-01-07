from PIL import Image, ImageOps
import os
from skimage import io, transform, filters, exposure

def m7():
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

            # exp = exposure.adjust_sigmoid(region)
            # io.imsave("edited/sig_"+adj_fn +".png", exp)
            # io.imsave("edited/sig_"+adj_fn +".01.png", exposure.adjust_sigmoid(region, cutoff=0.01))
            # io.imsave("edited/sig_"+adj_fn +".05.png", exposure.adjust_sigmoid(region, cutoff=0.05))
            # io.imsave("edited/sig_"+adj_fn +".30.png", exposure.adjust_sigmoid(region, cutoff=0.3))


            adhist = exposure.equalize_adapthist(region)
            io.imsave("edited/adhist_"+adj_fn +".png", adhist)

            # adhist = exposure.equalize_hist(region)
            # io.imsave("edited/"+adj_fn +"adj_hist.png", adhist)

            #roberts, sobel, scharr, prewitt
            # edges = filters.sobel(adhist)
            # io.imsave("edited/sob_"+adj_fn +".png", edges)
            
            
def m8():
    Image.MAX_IMAGE_PIXELS = None
    for fn in os.listdir("all"):
        if fn.endswith("TIF"):
            adj_fn = fn.split("_B")[1]
            if len(adj_fn) == 5:
                adj_fn = "0" + adj_fn
            adj_fn = "A_" + adj_fn[:-4]
            print(adj_fn)

            image = io.imread("all/" + fn)

            if fn.endswith("8.TIF"):
                pass
                region = image[3500*2:3900*2, 800*2:1200*2]
            else:
                region = image[3500:3900, 800:1200]
                region = transform.resize(region, (800,800), anti_aliasing=False)
            
            if fn.endswith("8.TIF"):
                #io.imsave("edited/"+adj_fn +".png", region)

                adhist = exposure.equalize_adapthist(region)
                io.imsave("edited/adhist_"+adj_fn +".png", adhist)
                print(adhist[200,200])



m8()