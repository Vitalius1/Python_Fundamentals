print " x 1 2 3 4 5 6 7 8 9 10 11 12"
for row in range(1, 13):
    row_string = ""
    for col in range(0, 13):
        if col is 0:
            row_string += " " + str(row)
        else:
            row_string += " " + str(col * row)
    print row_string