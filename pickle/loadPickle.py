import pickle

#-------unpickling

file = "myfile.pkl"
fileObj = open("file.txt",'rb') #
myData = pickle.load(fileObj)
print(myData)

