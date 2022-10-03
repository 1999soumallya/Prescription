from mysql.connector import connect

mydb = connect(host="localhost", user="root", database="studentdate")
mycursor = mydb.cursor()
filename = 'Images/wp3231265.jpg'
with open(filename, 'rb') as file:
    binarydata = file.read()
insertquary = "insert into `student details`(Name, Sex, Address, `Mobile No`, `Email Id`,Report) values (%s, %s, %s, " \
              "%s, %s,%s) "
value = ('Soumallya Dey', 'Male', 'Bhordaha', 9, '1999soumallya@Gmail.com', binarydata)
mycursor.execute(insertquary, value)

result = mycursor.fetchone()[6]
print(result)
storepath = 'images/img.jpg'
# for valu in result:
#     with open(storepath, 'wb') as f:
#     f.write(valu[6])
#     f.close()

'''def retrivefile(name):
    quary = "select * from `student details` where name='Soumallya Dey'"
    mycursor.execute(quary.format(str(name)))
    myresult = mycursor.fetchone()[6]
    storefile
'''

# filename = 'wp3231265.jpg'
# insertimage(filename)
