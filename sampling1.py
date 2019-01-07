from PIL import Image, ImageOps
import os
from skimage import io, transform, filters, exposure, color
import numpy as np
from numpy import ndarray
import reader
import copy
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

RAWDIR = "all"
OUTDIR = "out"



def coords(s):
    for line in s.splitlines():
        try:
            x, y = line.split()
            yield int(y), int(x)
        except:
            pass

creeks = list(coords("""
130 207
300 322
190 324
455 600
553 300
430 319
"""))

other = list(coords("""
200 100
300 100
400 100
500 100
650 100

200 400
300 400
440 400
500 400
600 400
700 400

"""))




def rgbtest():
    raws, exps = reader.get_images()
    print(exps.keys())

    # rg = color.gray2rgb(adhist)
    # red_multiplier = [1, 0, 0]
    # yellow_multiplier = [1, 1, 0]
    # rg = red_multiplier * rg
    r = exps['04']
    g = exps['05']
    b = exps['06']
    zipped = np.dstack((r, g, b))
    io.imsave(OUTDIR + "/color.png", zipped)

    # r = exps['08']
    # g = exps['06']
    # b = exps['05']
    b2 = 1-(2*exps['05'])
    io.imsave(OUTDIR + "/inv.png", b2)

    io.imsave(OUTDIR + "/color2.png", 
        np.dstack((exps['08'], exps['05'], exps['06'])))
    io.imsave(OUTDIR + "/color3.png", 
        np.dstack((exps['04'], exps['05'], exps['08'])))
    io.imsave(OUTDIR + "/color4.png", 
        np.dstack((exps['08'], exps['05'], exps['04'])))
    io.imsave(OUTDIR + "/color6.png", 
        np.dstack((exps['04'], exps['08'], b2)))
    io.imsave(OUTDIR + "/true_color.png", 
        np.dstack((exps['04'], exps['03'], exps['02'])))
    io.imsave(OUTDIR + "/true_color_raw.png", 
        np.dstack((raws['04'], raws['03'], raws['02'])))

def make_grid():
    raws, exps = reader.get_images()

    orig = exps['08']
    r = copy.copy(orig)
    g = copy.copy(orig)
    b = copy.copy(orig)


    for i in range(800):
        for j in range(800):
            
            if i % 500 == 0 or j % 500 == 0:
                b[i, j] = 1
            elif i % 100 == 0 or j % 100 == 0:
                r[i, j] = 1
            elif i % 10 == 0 and j % 10 == 0:
                g[i, j] = 1


    #b = np.vectorize(lambda x: min(x, 1.0))(b)

    zipped = np.dstack((r, g, b))
    io.imsave(OUTDIR + '/s_grid.png', zipped)

def show_sample(pos, neg):
    raws, exps = reader.get_images()

    orig = exps['08']
    r = copy.copy(orig)
    g = copy.copy(orig)
    b = copy.copy(orig)

    for p in pos:
        r[p] = 1

    for p in neg:
        g[p] = 1

    zipped = np.dstack((r, g, b))
    io.imsave(OUTDIR + '/sample.png', zipped)

def train(pos, neg):
    raws, exps = reader.get_images()

    # flat_raws = [ndarray.flatten(raw) for raw in raws.values()]    
    # print(flat_raws[0].shape)
    # flattened = np.dstack(flat_raws)[0]
    # print(flattened.shape, flattened[0])

    grid = np.dstack(raws.values())
    print(grid.shape)

    X = []
    y = []
    for p in pos:
        X.append(grid[p])
        y.append(1)

    for p in neg:
        X.append(grid[p])
        y.append(0)

    classifier = KNeighborsClassifier(1)
    classifier = RandomForestClassifier()
    classifier.fit(X, y)

    testpoints = list(coords("""
        553 298
        430 610
        500 300
        500 240
    """))
    testX = [grid[p] for p in testpoints]
    print(classifier.predict(testX))

    pred_image = np.zeros((800,800))
    for i in range(800):
        print(i)
        # for j in range(800):
        pred_image[i] = classifier.predict(grid[i])
    
    io.imsave(OUTDIR + '/pred.png', pred_image)

    orig = exps['08']
    r = copy.copy(orig)
    g = copy.copy(orig)
    b = copy.copy(orig)

    b = b + pred_image
    b = np.vectorize(lambda x: min(x, 1.0))(b)

    overlay = np.dstack((r, g, b))
    io.imsave(OUTDIR + '/pred_overlay.png', overlay)


def get_sample(fn):
    image = io.imread(fn)
    #print(image.shape)

    green_points = []
    red_points = []
    for i in range(800):
        for j in range(800):
            r, g, b = image[i,j]
            # if i + j == 1:
            #     print(r,g,b)
            if r > b and r > g:
                red_points.append((i,j))
            if g > b and g > r:
                green_points.append((i,j))

    return red_points, green_points
    

pos, neg = get_sample("out/pred_overlay_ed.png")
# show_sample(pos, neg)
train(pos+creeks, neg+other)
