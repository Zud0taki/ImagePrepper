def calcExportList(cropped_coordinates, xmax_list, xmin_list, ymax_list, ymin_list, export_list, pos_in_list):
    label_number = 1
    uc_list = []
    lc_list = []
    cropped_coordinates = cropped_coordinates
    comparexmin = cropped_coordinates[0]
    comparexmax = cropped_coordinates[2]
    compareymin = cropped_coordinates[1]
    compareymax = cropped_coordinates[3]
    for i in range(len(xmax_list)):
        if (i != pos_in_list):
            if (xmax_list[i]<comparexmax):
                if(xmin_list[i]>comparexmin):
                    if(ymax_list[i]<compareymax):
                        if(ymin_list[i]>compareymin):

                            ucx = int(xmin_list[i]) - comparexmin
                            lcx = int(xmax_list[i]) - comparexmin

                            ucy = int(ymin_list[i]) - compareymin
                            lcy = int(ymax_list[i]) - compareymin
                            uc_list.append([ucx, ucy])
                            lc_list.append([lcx, lcy])
                            # transfer to 0...1 coordinates
                            xdistance = (lcx - ucx) / 416
                            ydistance = (lcy - ucy) / 416
                            xczeroed = (ucx / 416) + (xdistance / 2)
                            yczeroed = (ucy / 416) + (ydistance / 2)
                            concat = str(label_number) + " " + str(xczeroed) + " " + str(yczeroed) + " " + str(xdistance) + " " + str(ydistance)
                            export_list.append(concat)

    return [export_list, uc_list, lc_list]
