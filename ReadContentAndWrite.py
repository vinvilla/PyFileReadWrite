# Taking "gfg input file.txt" as input file
# in reading mode
with open("inputFile.txt", "r") as input:
      
    # Creating "outputFile.txt" as output
    # file in write mode
    with open("outputFile.txt", "w") as output:
          
        # Writing each line from input file to
        # output file using loop
        for line in input:
            output.write(line)