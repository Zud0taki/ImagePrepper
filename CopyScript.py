import glob
import shutil

input_from_folder = []
dest = r"C:\Users\KIZwei\Desktop\Airbus_Rotation\ships\images\train/"

for input_element in glob.glob(r"C:\Users\KIZwei\Desktop\Airbus_Rotation\ships\images\*.jpg"):
    input_from_folder.append(input_element)
for x in range(len(input_from_folder)):
    file = input_from_folder[x]
    shutil.move(file, dest)

    stop = 0