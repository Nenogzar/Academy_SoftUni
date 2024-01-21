def chek_point_location (x, y, rectangles):
    for rect in rectangles:
        x1, y1, x2, y2 = rect
        if ((x == x1 or x == x2) and y1 <= y <= y2) or ((y == y1 or y == y2) and x1 <= x <= x2):
            return "Border"
        else:
            return "Inside / Outside"
