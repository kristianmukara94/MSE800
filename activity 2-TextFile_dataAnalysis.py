# Create a function to open the filename junk.txt
with open("junk.txt", "r") as data:
     content = data.readlines()
     for line in content:
# Create a variable to count the lines inside the junk file
          total_lines =len(content)
    
# Print the total number of lines inside the junk file          
          print(content)
          print ("Total number of lines:", total_lines)
data.close()     

# Create a function to open the junk file and then write data inside the txt
with open("junk.txt", "a") as writedata:
     writedata.write("\n`text file nanalyssis`\n")
writedata.close()

# Create a function to read the junk file 
with open("junk.txt", "r") as data2:
     convert = data2.read()
data2.close()

# Create a function to convert all data to lowercase
with open("junk.txt", "w") as convertdata:
     convertdata.write(convert.lower())
convertdata.close()




    