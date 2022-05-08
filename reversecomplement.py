def reverse_complement(file):
    seq = open(file, 'r') # Open file and store in seq
    # Initialize empty strings
    bases = "" 
    complement = ""
    # readlines() stores into each line into elements of list
    for line in seq.readlines():
        # Checks if line starts with base and concatenates to base string (ignores headliners)
        if line[0] == "A" or line[0] == "T" or line[0] == "G" or line[0] == "C" or line[0] == "N":
            bases += line
    # Goes each char in bases string to store complement base sequence in complement string
    for char in bases:
        if char == "A":
            complement += "T"
        elif char == "T":
            complement += "A"
        elif char == "G":
            complement += "C"
        elif char == "C":
            complement += "G"
        elif char == "N":
            complement += "N"
    # Stores reverse of complement
    rev_complement = complement[::-1]
    # Print reverse complement
    print (rev_complement)

