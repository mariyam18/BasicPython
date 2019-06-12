

import pymysql
connection = pymysql.connect('localhost','root','root','student')
cursor=connection.cursor()


def login():
	user1="admin"
	pass1="admin"
	user2=input("ENTER THE USERNAME:")
	pass2=input("ENTER THE PASSWORD:")
	if(user2 == user1 and pass2 == pass1):
		print("-----------!!!!!!WELCOME-ACCESS GRANTED!!!!!!-----------")
		NAME,GENDER,AGE,CLASS,MOB_no,MARKS,EMAIL = menu()
		return NAME,GENDER,AGE,CLASS,MOB_no,MARKS,EMAIL
	else:
		print("sorry can't access")

def add_detail():
	#ID=input("ENTER THE ID: ")
	NAME=input("ENTER THE NAME: ")
	GENDER=input("F OR M: ")
	AGE=input("ENTER YOUR AGE: ")
	CLASS=input("ENTER YOUR CLASS: ")
	MOB_no=input("ENTER THE MOBILE NUMBER: ")
	MARKS=input("ENTER YOUR MARKS: ")
	EMAIL=input("ENTER YOUR EMAIL: ")
	return NAME,GENDER,AGE,CLASS,MOB_no,MARKS,EMAIL



def view_detail():
	 print()
	 
def search():
	name=input("ENTER THE NAME YOU WANT TO SEARCH")
	cursor.execute("select * from detail where NAME=name")
	
def menu():
	c=int(input("""
			1:ENTER THE STUDENT DETAILS
			2:VIEW STUDENT DETAILS
			3:SEARCH BY ID NUMBER 
			4:EXIT
			
			PLEASE ENTER YOUR CHOICE: """))
	if(c is 1):
		NAME,GENDER,AGE,CLASS,MOB_no,MARKS,EMAIL = add_detail()
		return NAME,GENDER,AGE,CLASS,MOB_no,MARKS,EMAIL
	elif(c is 2):
		NAME,GENDER,AGE,CLASS,MOB_no,MARKS,EMAIL =view_detail()
		return NAME,GENDER,AGE,CLASS,MOB_no,MARKS,EMAIL 
	elif(c is 3):
		NAME,GENDER,AGE,CLASS,MOB_no,MARKS,EMAIL =search()
		return NAME,GENDER,AGE,CLASS,MOB_no,MARKS,EMAIL 
	elif(c is 4):
		return
	else:
		print("please enter valid number")
		menu()
	

NAME,GENDER,AGE,CLASS,MOB_no,MARKS,EMAIL = login()		
sql = "INSERT INTO detail (NAME,GENDER,AGE,CLASS,MOB_no,MARKS,EMAIL_NO) VALUE(%s,%s,%s,%s,%s,%s,%s)"
cursor.execute(sql, (NAME,GENDER,AGE,CLASS,MOB_no,MARKS,EMAIL))
cursor.execute("select * from detail")
data = cursor.fetchall()
	
	

	







