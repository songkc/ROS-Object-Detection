import os
import sys
sys.path.append(r'./database')

from database import *

# database part
mydb = database()

mydb.createTable()
mydb.deleteTable('origins, tagged, results')
mydb.createTable()

# mydb.insert("origins", "'C:'")
# mydb.insert("tagged", "'D:', FALSE")
# mydb.insert("results", "'E:'")

# mydb.select("id, imgPath", "origins")
# mydb.select("id, imgPath, isTagged", "tagged")
# mydb.select("id, imgPath", "results")

# image file part
def del_file(path):
    ls = os.listdir(path)
    for i in ls:
        c_path = os.path.join(path, i)
        if os.path.isdir(c_path):
            del_file(c_path)
        else:
            os.remove(c_path)

del_file('database/origins')
del_file('database/tagged')
del_file('database/results')