import csv
import pandas

def read(file):
    mydict = {}
    #opeining the file to read
    with open(file, "r") as f:
        #spliting the lines and using their name as the key 
        for line in f:
            items = line.split(",")
            key, values =items[0], items[1:]
            mydict[key] =  values
    # returns the dictionary
    return mydict

#convert the dictionary into a panda data frame
#WE MAKE OUR DICTIONARY 
dictionary = read("companies.csv")
#print(dictionary)

df = pandas.DataFrame(dict([ (k,pandas.Series(v)) for k,v in dictionary.items() ]))
print(df)




#initialize the model 
# forward = givinhg input and getting a output 
# some math that finds patterns between the data 