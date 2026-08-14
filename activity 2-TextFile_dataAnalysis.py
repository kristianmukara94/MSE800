file_path = r"C:\Users\krist\Downloads\junk.txt"

with open(file_path, "r") as data:
     content = data.readlines()
     for line in content:

          total_lines =len(content)
    
          
          print(content)
          print ("Total number of lines:", total_lines)
data.close()     

with open(file_path, "a") as writedata:
     writedata.write("\n`text file nanalyssis`\n")
writedata.close()

with open(file_path, "r") as data2:
     convert = data2.read()
data2.close()

with open(file_path, "w") as convertdata:
     convertdata.write(convert.lower())
convertdata.close()




    