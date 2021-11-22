import matplotlib.pyplot as plt
import numpy as np

from Input import *
import cv2 as cv
from BoundaryBoxCalc import *

img_path = r"C:\Users\DLR_OS_Testbench\Desktop\tempImg"
txt_path = r"C:\Users\DLR_OS_Testbench\Desktop\temptxt"
name = "P0032"

txt_file = open(txt_path + "/" + name +".txt", "r")
coords_temp = []
label_count = 0
for line in txt_file:
    coords_temp = line.split()
    x1 = coords_temp[0]
    y1 = coords_temp[1]
    x2 = coords_temp[2]
    y2 = coords_temp[3]
    x3 = coords_temp[4]
    y3 = coords_temp[5]
    x4 = coords_temp[6]
    y4 = coords_temp[7]

    xarray = np.array([x1, x2, x3, x4]).astype(np.int64)
    xmax = xarray.max()
    xmin = xarray.min()

    yarray = np.array([y1, y2, y3, y4]).astype(np.int64)
    ymax = yarray.max()
    ymin = yarray.min()

    if x1 == xmin:
        x1 = xmin
    elif x1 == xmax:
        x1 = xmax
    else:
        x1 = x1

    if x2 == xmin:
        x2 = xmin
    elif x2 == xmax:
        x2 = xmax
    else:
        x2 = x2

    if x3 == xmin:
        x3 = xmin
    elif x3 == xmax:
        x3 = xmax
    else:
        x3 = x3

    if x4 == xmin:
        x4 = xmin
    elif x4 == xmax:
        x4 = xmax
    else:
        x4 = x4

    if y1 == ymin:
        y1 = ymin
    elif y1 == ymax:
        y1 = ymax
    else:
        y1 = y1

    if y2 == ymin:
        y2 = ymin
    elif y2 == ymax:
        y2 = ymax
    else:
        y2 = y2

    if y3 == ymin:
        y3 = ymin
    elif y3 == ymax:
        y3 = ymax
    else:
        y3 = y3

    if y4 == ymin:
        y4 = ymin
    elif y4 == ymax:
        y4 = ymax
    else:
        y4 = y4
    dummy = ""

    xcd = xmax - xmin
    xc = xmax - (xcd / 2)
    xc = int(xc)
    ycd = ymax - ymin
    yc = ymax - (ycd / 2)
    yc = int(yc)

    readingpath = img_path + "/" + name+".png"
    img = cv.imread(readingpath, -1)
    img_shape = img.shape

    # upper left boundary pixel
    tx = xc - 208
    if tx < 0:
        txshift = tx
        tx = 0
    ty = yc - 208
    if ty < 0:
        tyshift = ty
        ty = 0
    # lower right boundary pixel
    lx = tx + 416
    if lx > img_shape[1]:
        lxshift = lx
        lx = img_shape[1]
    ly = ty + 416
    if ly > img_shape[0]:
        lyshift = ly
        ly = img_shape[0]

    boundarylist = []

    ucx = int(xmin) - tx
    lcx = int(xmax) - tx

    ucy = int(ymin) - ty
    lcy = int(ymax) - ty

    startpoint = [ucy, ucx]
    endpoint = [lcy, lcx]
    color = (0, 255, 0)
    thickness = 1

    xdistance = xmax - xmin
    ydistance = ymax - ymin
    xczeroed = xmin + (xdistance / 2)
    yczeroed = ymin + (ydistance / 2)

    export_list = [0, xczeroed, yczeroed, xdistance, ydistance]

    save_name = [name]
    save_name = save_name[0]
    save_name = r"C:\Users\DLR_OS_Testbench\Desktop\tempSave\ " + save_name
    print(img.shape)
    original = img[0:100, 0:100]
    print(original.shape)
    # first two values for rows - y values |||| second two values for columns - x values
    cropped = img[ty:ly, tx:lx]
    cropped = cv.rectangle(cropped, startpoint, endpoint, color, thickness)

    txt_name = save_name
    txt_name = txt_name+"_"+str(label_count)+ ".txt"
    txtfile = open(txt_name, 'w')
    for element in export_list:
        txtfile.write(str(element) + " ")
    txtfile.close()
    save = cv.imwrite(save_name+"_"+str(label_count)+".tif", cropped)

    label_count += 1

    # plt.imshow(img, aspect="auto")
    # plt.show()
    # plt.imshow(cropped, aspect="auto")
    # plt.show()
    # dummy = "j"
