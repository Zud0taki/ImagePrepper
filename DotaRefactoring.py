# import handling
from Input import *
import cv2 as cv
from calcExportList import *

# variable declaration
txt_file = []
img_input = []
txt_input = []
label_counter = 0
export_list = []

x_min_list = []
y_min_list = []
x_max_list = []
y_max_list = []

# input handling
for txt in glob.glob(r"C:\Users\KIZwei\Desktop\Dota\trainingstxt\*"):
    txt_input.append(txt)
for img in glob.glob(r"C:\Users\KIZwei\Desktop\Dota\trainingsbilder\*"):
    img_input.append(img)

# image processing
for x in range(len(img_input)):
    pos_in_list = 0
    # open txt_file
    txt_file = open(txt_input[x], "r")
    # read txt from the third line
    txt_file = txt_file.readlines()[2:]
    # get export_name from the input
    export_name = txt_input[x]
    export_name = export_name.split("\\trainingstxt")
    export_name = export_name[0]
    # iterate through all the lines from the txt_file
    coordinate_check_array = []
    for i in range(len(txt_file)):
        coordinate_check_array.append(txt_file[i].split())
        # save the coords of one of the bounding boxes in a temp var and then read the coordinates to related vars
        single_bounding_temp = coordinate_check_array[i]
        single_x1 = single_bounding_temp[0]
        single_y1 = single_bounding_temp[1]
        single_x2 = single_bounding_temp[2]
        single_y2 = single_bounding_temp[3]
        single_x3 = single_bounding_temp[4]
        single_y3 = single_bounding_temp[5]
        single_x4 = single_bounding_temp[6]
        single_y4 = single_bounding_temp[7]
        single_label = single_bounding_temp[8]
        if (single_label == "ship"):
            single_x_array = np.array([single_x1, single_x2, single_x3, single_x4]).astype(np.float)
            single_xmax = single_x_array.max()
            x_max_list.append(single_xmax)
            single_xmin = single_x_array.min()
            x_min_list.append(single_xmin)
            single_y_array = np.array([single_y1, single_y2, single_y3, single_y4]).astype(np.float)
            single_ymax = single_y_array.max()
            y_max_list.append(single_ymax)
            single_ymin = single_y_array.min()
            y_min_list.append(single_ymin)

        harbor_check_array = []
        harbor_list = []
        for j in range(len(txt_file)):
            harbor_check_array.append(txt_file[j].split())
            # save the coords of one of the bounding boxes in a temp var and then read the coordinates to related vars
            harborcheck = harbor_check_array[j]
            harborpointer = harborcheck[8]
            harborbool = False
            harbor_list.append(harborpointer)
        substring = "harbor"
        substring_in_list = any(substring in string for string in harbor_list)
        if(substring_in_list == False):
            if(len(x_max_list) > 0):
                for line in txt_file:
                    # print(str(line))
                    # read image related image from image input and get img_shape
                    img = cv.imread(img_input[x], -1)
                    img_shape = img.shape
                    # get x and y values of bounding box from txt_file
                    coords_temp = line.split()
                    x1 = coords_temp[0]
                    y1 = coords_temp[1]
                    x2 = coords_temp[2]
                    y2 = coords_temp[3]
                    x3 = coords_temp[4]
                    y3 = coords_temp[5]
                    x4 = coords_temp[6]
                    y4 = coords_temp[7]
                    #get label name from txt_file and check if its a ship
                    label_name = coords_temp[8]
                    if (label_name == "ship"):
                        # create array with x values and get min/max
                        xarray = np.array([x1, x2, x3, x4]).astype(np.float)
                        xmax = xarray.max()
                        xmin = xarray.min()
                        # create array with y values and get min/max
                        yarray = np.array([y1, y2, y3, y4]).astype(np.float)
                        ymax = yarray.max()
                        ymin = yarray.min()
                        # get x and y center values of bounding boxes
                        xcd = xmax - xmin
                        xc = xmax - (xcd / 2)
                        xc = int(xc)
                        ycd = ymax - ymin
                        yc = ymax - (ycd / 2)
                        yc = int(yc)

                        # calculate the new image snippet
                        # get upper left cropped pixel and check if it hits the image border
                        tx = xc - 208
                        if tx < 0:
                            txshift = tx
                            tx = 0
                        ty = yc - 208
                        if ty < 0:
                            tyshift = ty
                            ty = 0
                        # get lower right cropped pixel and check if it hits the image border
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
                        # save cropped_coordinates
                        cropped_coordinates = [tx, ty, lx, ly]

                        # calculate bounding-box pixels and distances
                        ucx = int(xmin) - tx
                        lcx = int(xmax) - tx

                        ucy = int(ymin) - ty
                        lcy = int(ymax) - ty

                        # set properties for green outline - bounding box
                        startpoint = [ucx, ucy]
                        print(startpoint)
                        endpoint = [lcx, lcy]
                        print(endpoint)
                        color = (0, 255, 0)
                        thickness = 1

                        # transfer to 0...1 coordinates
                        xdistance = (lcx - ucx) / 416
                        ydistance = (lcy - ucy) / 416
                        xczeroed = (ucx / 416) + (xdistance / 2)
                        yczeroed = (ucy / 416) + (ydistance / 2)


                        label_number = 1

                        # export_list = [label_number, xczeroed, yczeroed, xdistance, ydistance]
                        concat = str(label_number) +" "+ str(xczeroed) +" "+ str(yczeroed) +" "+ str(xdistance) +" "+ str(ydistance)
                        export_list.append(concat)
                        # check if other ships are fully visible in the cropped image
                        return_array = calcExportList(cropped_coordinates, x_max_list, x_min_list, y_max_list, y_min_list, export_list, pos_in_list)

                        #read new export_list from array as well as uc_list and lc_list for colored box drawings + counter up
                        export_list = return_array[0]
                        if (len(export_list)>1 and export_list[0] == export_list [1]):
                            export_list.pop(0)
                        uc_list = return_array[1]
                        lc_list = return_array[2]
                        pos_in_list += 1

                        # print(img.shape)
                        original = img[0:100, 0:100]
                        # print(original.shape)
                        # calc cropped image | first two values for rows - y values |||| second two values for columns - x values
                        cropped = img[ty:ly, tx:lx]
                        # draw first green outline of initial bounding box
                        # cropped = cv.rectangle(cropped, startpoint, endpoint, color, thickness)

                        # only needed if all outlines should be drawn + in a different color
                        # if len(uc_list) == len(lc_list):
                        #     for h in range(len(uc_list)):
                        #         secondstart = uc_list[h]
                        #         secondend = lc_list[h]
                        #         if (secondstart != startpoint and secondend != endpoint):
                        #             color2 = (0, 0, 255)
                        #             cropped = cv.rectangle(cropped, secondstart, secondend, color2, thickness)


                        # boxcount = len(export_list)
                        # export_list.append(boxcount)
                        txt_name = export_name + "/TestRes/" + "t" + str(label_counter) + ".txt"
                        txtfile = open(txt_name, 'w')
                        for element in export_list:
                            txtfile.write(str(element) + "\n")
                        txtfile.close()
                        export_list = []
                        save = cv.imwrite(export_name + "/TestRes/" + "t" + str(label_counter) + ".tif", cropped)

                        label_counter += 1
