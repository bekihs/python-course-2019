import re

"hadas".find("as")
# print(re.findall("05[0,2,3,4,5,7]-[0-9]{6,7}" , "hada058-78838383889s"))
# print(re.search("^05[0-9]-[0-9]{6,7}$" , "058-78838383889"))
# print(re.match("^05[0-9]-[0-9]{6,7}$" , "058-78838383889"))
print(re.match("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$" , "bekih@hh.jjj."))




# path = os.getcwd()
# #Returns the current working directory.
# lstDir = os.listdir(path)
# [print(item) for item in lstDir]


# newFile = open("newFile.txt","r")
# data  = newFile.read()
# print(data)
 

# fh = open("myfile.txt", "r")
# print(fh.read()) 
# fh.close()
# fh = open("myfile.txt", "r")
# print(fh.readline())
# print(fh.readlines())
# fh.close()



# open a text file, use:
fh = open("myfile.txt", "r")
# read from the  text file:
print(fh.read()) 
#first linestill first linesecond linethirdLinethird line4 line
#read one line at a time:
fh.close()
fh = open("myfile.txt", "r")
print(fh.readline())
#first linestill first linesecond linethirdLinethird line4 line
#read a list of lines:
fh.close()
fh = open("myfile.txt", "r")
print(fh.readlines())
#[first linestill first linesecond linethirdLinethird line4 line]
fh.close()

# To write to a file, use:
fh = open("myfile.txt","w")
fh.write("Hello World")
# To write a list of lines to a file:
lines_of_text = ["a line of text\n", "another line of text\n", "a third line\n"]
fh.writelines(lines_of_text)
fh.close()

#Append to file:
fh = open("myfile.txt", "a")
fh.write("Hello World again")
fh.close()
