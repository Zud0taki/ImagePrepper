# import handling
from Input import *
import cv2 as cv
from calcExportList import *

# variable declaration
img_input = []
txt_input = []
label_counter = 0
export_list = []

x_list = []
y_list = []

# input handling
with open(r"C:\Users\KIZwei\Desktop\Ship_Detection\input\airbus-ship-detection\train_ship_segmentations_v2.csv") as f:
    lines = f.read().splitlines()
for img in glob.glob(r"C:\Users\KIZwei\Desktop\Ship_Detection\input\airbus-ship-detection\train_v2\*"):
    img_input.append(img)

#
# read txt_file to a certain pos in img_input
#

for line in lines:
    x_list = []
    y_list = []
    current_line = line.split()
    if len(current_line) > 1:
        img_name = current_line[0].split(",")
        hull_values = [img_name[1]]
        variable_counter = 2
        for i in range(int(len(current_line) / 2) - 1):
            hull_values.append(current_line[variable_counter])
            variable_counter += 2
        for g in range(len(hull_values)):
            main_value = float(hull_values[g])
            x_calc = main_value / 768
            remainder = str(x_calc)
            remainder = remainder.split(".")
            x = float(remainder[0])
            y_calc = "0." + remainder[1]
            y = float(y_calc) * 768
            x_list.append(x)
            y_list.append(y)
            # TODO: VISUALIZE ALL POINTS TO CHECK IF ITS A HULL

        if any(img_name[0] in s for s in img_input):
            img_load_name = "\\" + img_name[0]
            img = cv.imread(r"C:\Users\KIZwei\Desktop\Ship_Detection\input\airbus-ship-detection\train_v2" + img_load_name, -1)
            img_shape = img.shape
            stop = 0

            xarray = np.array(x_list).astype(float)
            xmax = round(xarray.max())
            xmin = round(xarray.min())
            yarray = np.array(y_list).astype(float)
            ymax = round(yarray.max())
            ymin = round(yarray.min())

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
            concat = str(label_number) + " " + str(xczeroed) + " " + str(yczeroed) + " " + str(xdistance) + " " + str(ydistance)
            export_list.append(concat)
            txt_load_name = img_load_name
            txt_load_name = txt_load_name.split(".")
            txt_name = (r"C:\Users\KIZwei\Desktop\AirbusTest\txt" + txt_load_name[0] + ".txt")
            txtfile = open(txt_name, 'w')
            for element in export_list:
                txtfile.write(str(element) + "\n")
            txtfile.close()
            export_list = []

            original = img[0:100, 0:100]
            # print(original.shape)
            # calc cropped image | first two values for rows - y values |||| second two values for columns - x values
            cropped = img[ty:ly, tx:lx]
            # draw first green outline of initial bounding box
            #   cropped = cv.rectangle(cropped, startpoint, endpoint, color, thickness)
            save = cv.imwrite(r"C:\Users\KIZwei\Desktop\AirbusTest\img" + img_load_name, cropped)

