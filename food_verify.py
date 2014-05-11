import mysql.connector
from database import login_info
List_animals = []
List_fed = []

db = mysql.connector.Connect(**login_info)
cursor = db.cursor()


cursor.execute("select id from animal")
for id in cursor.fetchall():
	List_animals.append(id[0])	

cursor.execute("select anid from food")
for anid in cursor.fetchall():
	if anid[0] not in List_fed:
		List_fed.append(anid[0])

for x in List_animals:
	if x not in List_fed:
		print ("Animal with ID # %s has not received any food." %x)
		
for value in List_fed:
	if value in List_animals:
		List_animals.remove(value)
	if len(List_animals)==0:
		print ("All animals have eaten at least one food")