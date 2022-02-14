import glob
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy import ndimage


# set variables
txt_from_line = []
radius = 3
color = (0, 0, 120)
thickness = 2
angles = [-90, -180, -270]
export_list = []
txt_input = []
img_input = []

for txt in glob.glob(r"E:\YoloV5\AirbusTest\txt\*"):
    txt_input.append(txt)
for img in glob.glob(r"E:\YoloV5\AirbusTest\img\*"):
    img_input.append(img)


for z in range(len(img_input)):

    # read images and txt´s - check if names are the same
    img = cv2.imread(img_input[z], -1)
    txt_file = open(txt_input[z], "r")
    img_name = img_input[z]
    img_name = img_name.split("\\")
    img_name = img_name[len(img_name)-1]
    img_name = img_name.split(".")
    img_name = img_name[0]

    txt_name = txt_input[z]
    txt_name = txt_name.split("\\")
    txt_name = txt_name[len(txt_name) -1]
    txt_name = txt_name.split(".")
    txt_name = txt_name[0]

    if txt_name == img_name:

        stop = 0
        print("next")
        # get original center and expansion from txtfile and read corresponding img
        for line in txt_file:
            txt_from_line.append(line)
            txt_from_line = txt_from_line[0].split()
        x = txt_from_line[1]
        x = float(x)*416
        y = txt_from_line[2]
        y = float(y)*416
        xexpansion = txt_from_line[3]
        xexpansioncoords = float(xexpansion)*416
        yexpansion = txt_from_line[4]
        yexpansioncoords = float(yexpansion)*416
        txt_from_line = []
        center = (int(x), int(y))
        centerdistancex = 208 - x
        # if centerdistancex < 0:
        #     centerdistancex = centerdistancex * (-1)
        centerdistancey = 208 - y
        # if centerdistancey < 0:
        #     centerdistancey = centerdistancey * (-1)
        # stop = ""
        # img = cv2.circle(img, center, radius, color, thickness)
        # cv2.imshow("original", img)
        # cv2.waitKey(0)

        # rotate the img to create rotate images
        for g in range(len(angles)):
            angle = angles[g]
            if g == 0:
                newx = 208 + centerdistancey
                newy = 208 - centerdistancex
                center = (int(newx), int(newy))
                ul = (int(newx - (xexpansioncoords/2)), int(newy - (yexpansioncoords/2)))
                lr = (int(newx + (xexpansioncoords / 2)), int(newy + (yexpansioncoords / 2)))
                color = (120, 255, 0)
                rotated = ndimage.rotate(img, angle)
                # rotated = cv2.circle(rotated, center, radius, color, thickness)
                # rotated = cv2.rectangle(rotated, lr, ul, color, thickness)
                # cv2.imshow("rotated", rotated)
                cv2.imwrite(r"C:\Users\KIZwei\Desktop\uberprufen\img/" + img_name + "_" + str(g) + ".jpg", rotated)
                # cv2.waitKey(0)
                concat = str(1) + " " + str(int(newx)/416) + " " + str(int(newy)/416) + " " + str(yexpansion) + " " + str(xexpansion)
                export_list.append(concat)
                txt_name_export = (r"C:\Users\KIZwei\Desktop\uberprufen\txt/" + img_name + "_" + str(g) + ".txt")
                txtfile = open(txt_name_export, 'w')
                for element in export_list:
                    txtfile.write(str(element) + "\n")
                txtfile.close()
                export_list = []
            elif g == 1:
                newx = 208 + centerdistancex
                newy = 208 + centerdistancey
                center = (int(newx), int(newy))
                ul = (int(newx - (xexpansioncoords / 2)), int(newy - (yexpansioncoords / 2)))
                lr = (int(newx + (xexpansioncoords / 2)), int(newy + (yexpansioncoords / 2)))
                color = (255, 255, 0)
                rotated = ndimage.rotate(img, angle)
                # rotated = cv2.circle(rotated, center, radius, color, thickness)
                # rotated = cv2.rectangle(rotated, ul, lr, color, thickness)
                # cv2.imshow("rotated", rotated)
                cv2.imwrite(r"C:\Users\KIZwei\Desktop\uberprufen\img/" + img_name + "_" + str(g) + ".jpg", rotated)
                # cv2.waitKey(0)
                concat = str(1) + " " + str(int(newx) / 416) + " " + str(int(newy) / 416) + " " + str(xexpansion) + " " + str(yexpansion)
                export_list.append(concat)
                txt_name_export = (r"C:\Users\KIZwei\Desktop\uberprufen\txt/" + img_name + "_" + str(g) + ".txt")
                txtfile = open(txt_name_export, 'w')
                for element in export_list:
                    txtfile.write(str(element) + "\n")
                txtfile.close()
                export_list = []
            elif g == 2:
                newx = 208 - centerdistancey
                newy = 208 + centerdistancex
                center = (int(newx), int(newy))
                ul = (int(newx - (xexpansioncoords / 2)), int(newy - (yexpansioncoords / 2)))
                lr = (int(newx + (xexpansioncoords / 2)), int(newy + (yexpansioncoords / 2)))
                color = (0, 255, 255)
                rotated = ndimage.rotate(img, angle)
                # rotated = cv2.circle(rotated, center, radius, color, thickness)
                # rotated = cv2.rectangle(rotated, ul, lr, color, thickness)
                # cv2.imshow("rotated", rotated)
                cv2.imwrite(r"C:\Users\KIZwei\Desktop\uberprufen\img/" + img_name + "_" + str(g) + ".jpg", rotated)
                # cv2.waitKey(0)
                concat = str(1) + " " + str(int(newx) / 416) + " " + str(int(newy) / 416) + " " + str(yexpansion) + " " + str(xexpansion)
                export_list.append(concat)
                txt_name_export = (r"C:\Users\KIZwei\Desktop\uberprufen\txt/" + img_name + "_" + str(g) + ".txt")
                txtfile = open(txt_name_export, 'w')
                for element in export_list:
                    txtfile.write(str(element) + "\n")
                txtfile.close()
                export_list = []

