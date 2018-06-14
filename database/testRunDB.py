from database import *

mydb = database()

mydb.createTable()
#mydb.deleteTable('origins, taged, results')
#mydb.insert("results", "1, 'D:', 0")
mydb.update("1", "imgPath", "'E:'", "origins")
mydb.update("1", "isTaged", "1", "origins")
mydb.select("id, imgPath, isTaged", "results")