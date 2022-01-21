import glob
import shutil


img_input_src = []
img_input_res = []
img_src = r"C:\Users\KIZwei\Desktop\ImageSearcher\imgsrc"
img_end = r"C:\Users\KIZwei\Desktop\ImageSearcher\end"
for srcimg in glob.glob(img_src + r"\*"):
    img_input_src.append(srcimg)
for resimg in glob.glob(r"C:\Users\KIZwei\Desktop\ImageSearcher\imgres\*"):
    img_input_res.append(resimg)

srcimg_list = []
for f in img_input_src:
    srcimg_name = f.split("\\imgsrc\\")
    srcimg_name = srcimg_name[1].split(".png")
    srcimg_name = srcimg_name[0].split("_")
    srcimg_list.append(srcimg_name[0])

resimg_list = []
for f in img_input_res:
    resimg_name = f.split("\\imgres\\")
    resimg_name = resimg_name[1].split(".png")
    resimg_name = resimg_name[0].split("_")
    resimg_list.append(resimg_name[0])

b_counter = 0
for a in srcimg_list:
    anchor = a
    anchor_in_list = any(anchor in string for string in resimg_list)
    b_counter = 0
    if anchor_in_list:
        for b in resimg_list:
            if b == anchor:
                b_counter = b_counter
                copy_path = img_input_res[b_counter]
                shutil.copy2(copy_path, img_end)
            else:
                b_counter += 1



hello = ""