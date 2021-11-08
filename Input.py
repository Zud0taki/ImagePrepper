# import necessary libraries
import cv2 as cv
import glob
from pandas import read_excel
import numpy as np


# define readExcel
# used to read the txt input with the filepath
def readExcel(filepath):
    sheet_name = 'coordsAI2'
    file_name = filepath
    df = read_excel(file_name, sheet_name=sheet_name)
    return df


# define checkEqualLength
# used to check if the image input and the text input are equally long
def checkEqualLength(img_input, txt_input):
    if len(img_input) == len(txt_input):
        equallength = True
    else:
        equallength = False
    return equallength


# define checkEqualNames
# used to check if the images and txt-files have the same names
def checkEqualNames(filepath):
    imgpath = glob.glob(r"" + filepath + "/*.tif")
    txtpath = glob.glob(r"" + filepath + "/*.txt")
    for x in range(len(imgpath)):
        imgname = str(imgpath[x])
        imgnamefirstsplit = imgname.split("\\")
        imgnametemp = imgnamefirstsplit[1]
        imgnamesecondsplit = imgnametemp.split(".tif")
        imgnamefinal = imgnamesecondsplit[0]
        txtname = str(txtpath[x])
        txtnamefirstsplit = txtname.split("\\")
        txtnametemp = txtnamefirstsplit[1]
        txtnamesecondsplit = txtnametemp.split(".txt")
        txtnamefinal = txtnamesecondsplit[0]
        if imgnamefinal == txtnamefinal:
            equalnames = True
        else:
            equalnames = False
            return equalnames
    return equalnames
