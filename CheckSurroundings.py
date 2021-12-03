def check_surroundings(cropped_coordinates, txt_file, counter):
    coordinates = cropped_coordinates
    tx = cropped_coordinates[0]
    ty = cropped_coordinates[1]
    lx = cropped_coordinates[2]
    ly = cropped_coordinates[3]
    x_list = []
    y_list = []
    txt_list = []
    for line in txt_file:
        txt_list.append(line)
    for step in txt_list:
        temp = str.split(step)
        x = (temp[0], temp[2])
        y = (temp[1], temp[3])
        x_list.append(x)
        y_list.append(y)

    for x in x_list:
        if tx - 416 <= int(x[0]) <= tx + 416:
            print("ALARM")

    bla = 0
