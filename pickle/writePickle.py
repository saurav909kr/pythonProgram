import pickle

#-------pickling a python object

list1 = [1,2,3,4,5]
file = "myfile.pkl"
fileObj = open("file.txt","wb") #wb means write binary
pickle.dump(list1, fileObj)
fileObj.close()



