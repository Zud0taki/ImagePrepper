import matplotlib.pyplot as plt
import numpy as np
from Input import *
import cv2 as cv

coords_temp = []
img_input = []
txt_input = []
label_count = 0
txt_counter = 0
linecounter = 0

for txt in glob.glob(r"C:\Users\bern_jl\Desktop\TestTxt\*"):
    txt_input.append(txt)
for img in glob.glob(r"C:\Users\bern_jl\Desktop\TestImg\*"):
    img_input.append(img)

for x in range(len(img_input)):

    txt_file_list = open(txt_input[x], "r")
    txt_file_list = txt_file_list.readlines()
    txt_file = open(txt_input[x], "r")
    save_name = txt_input[x]
    save_name = save_name.split("\\TestTxt")
    save_name = save_name[0]

    for line in txt_file:
        img = cv.imread(img_input[x], -1)
        img_shape = img.shape
        coords_temp = line.split()
        x1 = coords_temp[0]
        y1 = coords_temp[1]
        x2 = coords_temp[2]
        y2 = coords_temp[3]
        x3 = coords_temp[4]
        y3 = coords_temp[5]
        x4 = coords_temp[6]
        y4 = coords_temp[7]
        label_name = coords_temp[8]

        xarray = np.array([x1, x2, x3, x4]).astype(np.int64)
        xmax = xarray.max()
        xmin = xarray.min()

        yarray = np.array([y1, y2, y3, y4]).astype(np.int64)
        ymax = yarray.max()
        ymin = yarray.min()

        xcd = xmax - xmin
        xc = xmax - (xcd / 2)
        xc = int(xc)
        ycd = ymax - ymin
        yc = ymax - (ycd / 2)
        yc = int(yc)

        # upper left cropped pixel
        tx = xc - 208
        if tx < 0:
            txshift = tx
            tx = 0
        ty = yc - 208
        if ty < 0:
            tyshift = ty
            ty = 0
        # lower right cropped pixel
        lx = tx + 416
        if lx > img_shape[1]:
            lxshift = lx
            lx = img_shape[1]
            tx = lx - 416
        ly = ty + 416
        if ly > img_shape[0]:
            lyshift = ly
            ly = img_shape[0]
            ty = ly - 416
        cropped_coordinates = [tx, ty, lx, ly]


        # get boundarybox pixels and distances
        ucx = int(xmin) - tx
        lcx = int(xmax) - tx

        ucy = int(ymin) - ty
        lcy = int(ymax) - ty

        startpoint = [ucx, ucy]
        endpoint = [lcx, lcy]
        color = (0, 255, 0)
        thickness = 1

        xdistance = xmax - xmin
        ydistance = ymax - ymin
        xczeroed = xmin + (xdistance / 2)
        yczeroed = ymin + (ydistance / 2)

        # get correct label
        label_number = 0
        if(label_name == "plane"):
            label_number = 0
        elif(label_name == "ship"):
            label_number = 1
        elif (label_name == "storage"):
            label_number = 2
        elif (label_name == "tank"):
            label_number = 3
        elif (label_name == "baseball"):
            label_number = 4
        elif (label_name == "diamond"):
            label_number = 5
        elif (label_name == "tennis court"):
            label_number = 6
        elif (label_name == "basketball court"):
            label_number = 7
        elif (label_name == "ground track"):
            label_number = 8
        elif (label_name == "field"):
            label_number = 9
        elif (label_name == "harbor"):
            label_number = 10
        elif (label_name == "bridge"):
            label_number = 11
        elif (label_name == "large vehicle"):
            label_number = 12
        elif (label_name == "small vehicle"):
            label_number = 13
        elif (label_name == "helicopter"):
            label_number = 14
        elif (label_name == "roundabout"):
            label_number = 15
        elif (label_name == "soccer ball field"):
            label_number = 16
        elif (label_name == "swimming pool"):
            label_number = 17
        elif (label_name == "container crane"):
            label_number = 18

        if (label_number == 1):

            export_list = [label_number, xczeroed, yczeroed, xdistance, ydistance]


            print(img.shape)
            original = img[0:100, 0:100]
            print(original.shape)
            # first two values for rows - y values |||| second two values for columns - x values
            cropped = img[ty:ly, tx:lx]
            cropped = cv.rectangle(cropped, startpoint, endpoint, color, thickness)

            txt_name = save_name+"/TestRes/"+"t"+str(label_count)+".txt"
            txtfile = open(txt_name, 'w')
            for element in export_list:
                txtfile.write(str(element) + " ")
            txtfile.close()
            save = cv.imwrite(save_name+"/TestRes/"+"t"+str(label_count)+".tif", cropped)

            label_count += 1
    txt_counter += 1
        # plt.imshow(img, aspect="auto")
        # plt.show()
        # plt.imshow(cropped, aspect="auto")
        # plt.show()
        # dummy = "j"
