import pymysql as sql

sc=sql.connect('localhost','root','root','college')  	#to connect with database
cursor=sc.cursor()


sql="""INSERT INTO SCHOOL(FIRST_NAME,
	LAST_NAME,AGE,SEX)
	VALUES('MARIYAM','SHAIKH',19,'F')"""
cursor.execute(sql)
sc.commit()
sc.close()

