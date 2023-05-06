#! python3 


def compute():

    rows0 = [75]
    rows1 = [95, 64]
    rows2 = [17, 47, 82]
    rows3 = [18, 35, 87, 10]
    rows4 = [20, 4, 82, 47, 65]
    rows5 = [19, 1, 23, 75, 3, 34]
    rows6 = [88, 2, 77, 73, 7, 63, 67]
    rows7 = [99, 65, 4, 28, 6, 16, 70, 92]
    rows8 = [41, 41, 26, 56, 83, 40, 80, 70, 33]
    rows9 = [41, 48, 72, 33, 47, 32, 37, 16, 94, 29]
    rows10 = [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14]
    rows11 = [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57]
    rows12 = [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48]
    rows13 = [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31]
    rows14 = [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]

    row0 = [3]
    row1 = [7, 4]
    row2 = [2, 4, 6]
    row3 = [8, 5, 9, 3]

    rows = [rows14, rows13, rows12, rows11, rows10, rows9, rows8, rows7, rows6, rows5, rows4, rows3, rows2, rows1, rows0]
    rows2 = [row3, row2, row1, row0]


    for bottom_row in range(len(rows) - 1):
        top_row = bottom_row + 1
        top_num = 0
        for bottom_num in range(len(rows[bottom_row]) - 1):
            if rows[bottom_row][bottom_num] + rows[top_row][top_num] > rows[bottom_row][bottom_num + 1] + rows[top_row][top_num]:
                # replace top rows' num with new
                rows[top_row][top_num] = rows[bottom_row][bottom_num] + rows[top_row][top_num]
            else:
                rows[top_row][top_num] = rows[bottom_row][bottom_num + 1] + rows[top_row][top_num]
            top_num += 1
        print(rows[top_row])


compute()

exit()