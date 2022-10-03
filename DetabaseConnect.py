from mysql.connector import connect
import time
import os

UniqueID = input("Enter PatientID: ")
mydb = connect(host="localhost", user="root", database="studentdate")
mycursor = mydb.cursor()
mycursor.execute("select * from `student details`")
result = mycursor.fetchall()


def read_file(filepath):
    with open(filepath, 'rb') as file:
        binaryfile = file.read()
    return binaryfile


def write_file(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)


for valu in result:
    if UniqueID == valu[0]:
        mycursor.execute("select * from `student details` where ID = 'UniqueID'")
        # filename = input('Enter your file Path: ')
        # binaryfile = read_file(filename)
        # sql = "insert into `student details` report where ID = 'UniqueID' values (%s)"
        # query = "UPDATE `student details` SET report = %s WHERE id  = %s"
        # val = (binaryfile, UniqueID)
        # mycursor.execute(query, val)
        # report = valu[7]
        # ReportFileName = 'Photo.jpg'
        # write_file(report, ReportFileName)
        # mydb.commit()
        # os.remove(filename)
    else:
        Clientname = input("Enter PatientName: ").lower()
        ver = Clientname.split()
        arivaltime = str(int(time.time()))
        ID = (arivaltime + ver[0][0] + ver[1][0])
        Gender = input("What is gender: ")
        Address = input("What is the address:")
        mobileNumber = int(input("Enter Patient mobile number: "))
        emailId = input("What is the Email Address: ")
        filename = input('Enter your file Path: ')
        binaryfile = read_file(filename)
        sql = "insert into `student details`(ID,Name, Sex, Address, `Mobile No`, `Email Id`,report) values (%s ,%s, %s, " \
              "%s, %s, %s,%s) "
        val = (ID, Clientname, Gender, Address, mobileNumber, emailId, binaryfile)
        mycursor.execute(sql, val)