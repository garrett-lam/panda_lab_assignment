def task1(file):
    seq = open(file, 'r') # Open file and store in seq
    for line in seq.readlines(): # readlines() stores into each line into elements of list
        # Checks if line element in list starts with ">S", only print out line up to index 9
        if line[0:2] == ">S":
            print (line[:9])
        # Checks if line element in list starts with ">", only print out line up to index 11
        elif line[0] == ">":
            print (line[:11])
        # Prints line, without producing new line character
        else:
            print (line, end = "")
