f1 = open('file1','x') #creating the file
from importlib.resources import contents

#----------------------reading the file--------

f2 = open('file2','r')
f1 = open('file1')     #----if we not write any mode, by the default it is in reading mode
data = f2.read(200)   #---read first 200 character
data = f2.readline()   #---read one line at a time
data2 = f2.readline()
data3 = f2.readlines()  #---read all line at a time
print(data)
print(data2)
print(data3)

#------------------writing in file-------------

f2 = open('file2','w') #------ it create new file if file do not exist
f1 = open('file1','w')
f1.write('hy! i am saurabh , welcome to my hood') #--------- erase whatever written previously in f1 and write this ....
f2.write('hello are you new here')
print(f1.read()) #---------- it will give error because file is in writing mode but we are trying to read the content
f3 = open('file3','w')
lines = ['i am felling good','  i am learning python']
f3.writelines(lines)
f3.close()


#--------------------read than write in file--------------------

f3 = open('file3','r+') #-----------it will give error if file doest exit
f1 = open('file1','r+')
print(f1.read())
print(f1.tell()) #------------tell the pointer at this moment
f1.write('''
i am learning python
 ''')

#---------inserting sentence between to line----

with open('file1', 'r') as file:
    content = file.read()
    print(content)
parts = content.split('.')
print(parts)
new_content = parts[0]+'.'+'this is new line'+'.'+parts[1]
with open('file1','w') as file:
    file.write(new_content)

#------------------writing then reading ------

with open('file1','w+') as file1:  # --------it will create a file if file not exit,
  print(file1.tell())   # -------if exit it eraser the previously writen content
  file1.write('hello buddy')
  print(file1.tell())
  file1.write('''
  success is just behind the effort
  ''')
  print(file1.tell())
  file1.seek(0)  #-----------it brought the pointer at the beginning of file
  print(file1.tell())
  data=file1.read()
  print(data)
  print(file1.tell())
  file1.close()

#----------append and write ----------

with open('file1','a+') as file_1: #it will create file if file not exit , if exit it will read and append
    print(file_1.tell())
    file_1.seek(0)
    print(file_1.read())
    file_1.write("keep learning and keep going")


#----------outside file--------

f2 = open("C:/Users/codes/OneDrive/Desktop/file/file1/hello boys ,how is going.txt",'r') #-----give the complete path
print(f2.read())

#------working with binary file----


#------handling file exception ----

try:
    f = open('file4','r')
except FileNotFoundError:
    print("File not found!")
finally:
    if 'f' in locals():
        f.close()


#----------check file existence----

# import  os
# if os.path.exists('file3'):
#     print('file exist')
# else:
#     print('no such file')
#

#--------------------------------------

# import  os
# files = os.listdir()
# print(files)

#-----------------------------

# import os
# open("file3",'w').close() #create empty file
# os.remove('file3')

#---------------------------clearing the file----


# with open('file1','r+') as file__1:
#     file__1.truncate(0) # this cut the file to 0 byte

#--------count word ------

with open("file1",'r') as fil:
    text = fil.read()
    word = text.split()
    print("counted word",len(word))

