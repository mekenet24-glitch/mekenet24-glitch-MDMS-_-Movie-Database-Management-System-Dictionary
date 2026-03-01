#Absolute and Relative Paths


file = open('./data/my_file.txt', encoding='cp1252') #open the file with the correct encoding
print(file.name)
print(file.mode)
print(file.read()) 
print(file.encoding)    

#close the file
file.close()    