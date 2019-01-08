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

def train(pos, neg, raws):
    # raws, exps = reader.get_images()

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
    return pred_image


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
    

def overlay(rps, gps, b_image, exp, fn):
    # raws, exps = reader.get_images()

    r = copy.copy(exp)
    g = copy.copy(exp)
    b = copy.copy(exp)

    for p in rps:
        r[p] = 1

    for p in gps:
        g[p] = 1
    
    b = b + b_image
    b = np.vectorize(lambda x: min(x, 1.0))(b)

    overlay = np.dstack((r, g, b))
    io.imsave(OUTDIR + '/' + fn, overlay)

pos, neg = get_sample("out/train8.png")

raws, exps = reader.get_images(3500,3900,800,1200)
# show_sample(pos, neg)
pred_image = train(pos, neg, raws)
overlay(pos, neg, 0.5*pred_image, exps['05'], 'pred_and_train.png')
overlay([], [], 0.5*pred_image, exps['08'], 'pred_overlay.png')
