def calcboundary(x1, x2, y1, y3):
    xhalfdistance = (x2 - x1)/2
    yhalfdistance = (y3 - y1)/2

    boundingx1 = 208 - xhalfdistance
    boundingy1 = 208 + yhalfdistance

    boundingx2 = 208 + xhalfdistance
    boundingy2 = boundingy1

    boundingx3 = boundingx2
    boundingy3 = 208 - yhalfdistance

    boundingx4 = boundingx1
    boundingy4 = boundingy3

    bounding_list =  [int(boundingx1), int(boundingy1), int(boundingx2), int(boundingy2), int(boundingx3), int(boundingy3), int(boundingx4), int(boundingy4)]
    return bounding_list

