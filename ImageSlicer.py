import matplotlib.pyplot as plt
from Input import *
import cv2 as cv
from BoundaryBoxCalc import *

img_path = r"C:\Users\julia\Desktop\TestImage"
excel_input = readExcel(r"C:\Users\julia\Desktop\TestExcel\SiemensTestCoords.xlsx")

excel_info = excel_input['img_name']
excel_list = excel_info.values.tolist()
for x in range(len(excel_list)):
    img_name = str(excel_list[x])
    x1 = excel_input['x1']
    x1 = x1[x]
    y1 = excel_input['y1']
    y1 = y1[x]
    x2 = excel_input['x2']
    x2 = x2[x]
    y2 = excel_input['y2']
    y2 = y2[x]
    x3 = excel_input['x3']
    x3 = x3[x]
    y3 = excel_input['y3']
    y3 = y3[x]
    x4 = excel_input['x4']
    x4 = x4[x]
    y4 = excel_input['y4']
    y4 = y4[x]

    xcd = x2 - x1
    xc = x2 - (xcd / 2)
    xc = int(xc)
    ycd = y3 - y1
    yc = y3 - (ycd / 2)
    yc = int(yc)

    # bounding_list = calcboundary(x1, x2, y1, y3)
    # boundaryul = bounding_list[0:2]
    # boundaryur = bounding_list[2:4]
    # boundarylr = bounding_list[4:6]
    # boundaryll = bounding_list[6:8]

    readingpath = r"" + (img_path) + "/" + img_name
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

    boundaryx1 = x1 - tx
    #boundaryx1 = boundaryx1 - tx
    boundaryx1 = int(boundaryx1)
    boundarylist.append(boundaryx1)

    boundaryy1 = y1 - ty
    #boundaryy1 = boundaryy1 - ty
    boundaryy1 = int(boundaryy1)
    boundarylist.append(boundaryy1)

    boundaryx2 = x2 - tx
    boundaryx2 = int (boundaryx2)
    boundarylist.append(boundaryx2)

    boundaryy2 = y2 - ty
    boundaryy2 = int(boundaryy2)
    boundarylist.append(boundaryy2)

    boundaryx3 = x3 - tx
    boundaryx3 = int(boundaryx3)
    boundarylist.append(boundaryx3)

    boundaryy3 = y3 - ty
    boundaryy3 = int(boundaryy3)
    boundarylist.append(boundaryy3)

    boundaryx4 = x4 - tx
    boundaryx4 = int(boundaryx4)
    boundarylist.append(boundaryx4)

    boundaryy4 = y4 - ty
    boundaryy4 = int(boundaryy4)
    boundarylist.append(boundaryy4)

    print(boundarylist)

    with open("file.txt", "w") as output:
        output.write(str(boundarylist))


    save_name = img_name.split(".")
    save_name = save_name[0]
    print(img.shape)
    original = img[0:100, 0:100]
    print(original.shape)
    # first two values for rows - y values |||| second two values for columns - x values
    cropped = img[ty:ly, tx:lx]
    cropped[boundaryx1, boundaryy1] = [0, 0, 255]
    cropped[boundaryx2, boundaryy2] = [0, 0, 255]
    cropped[boundaryx3, boundaryy3] = [0, 0, 255]
    cropped[boundaryx4, boundaryy4] = [0, 0, 255]
    save = cv.imwrite(save_name+"_1.tif", cropped)

    # plt.imshow(img, aspect="auto")
    # plt.show()
    # plt.imshow(cropped, aspect="auto")
    # plt.show()
