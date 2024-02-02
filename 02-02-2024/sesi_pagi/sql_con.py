import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
host="localhost",
user="root",
port= 3307,
password="asdasd",
database="sakila"
)

mycursor = mydb.cursor()

# # Code Insert
# mycursor.execute("insert into actor(actor_id, first_name, last_name, last_update) values(222,'marbun','bir','2024-02-15 04:34:33')")
# # data1 = ("marbun","marbun","2024-02-02")
# # mycursor.execute(query,data1)
# mydb.commit
# print("Data sudah berhasil disimpen")

# #select
# mycursor.execute("select * from actor where actor_id=222;") 
# myresult = mycursor.fetchall()
# print(myresult)

# # Code Update
# # query2 = "update actor set last_name = %s where actor_id = %s"
# mycursor.execute("update actor set last_name='minum bir aja' where actor_id=222")
# # mycursor.execute(query2)
# mydb.commit
# print("Data sudah berhasil disimpen")

# # Code Delete
# query3 = "Delete from actor where actor_id = '205'"
# mycursor.execute(query3)
# mydb.commit
# print("Data sudah berhasil disimpen")


# Code Select with pandassss
# query = "select * from actor;"
# pds_result = pd.read_sql(query,mydb)
# print(pds_result)


# #select
# mycursor.execute("select first_name from actor where last_name like 'BE%';") 
# myresult = mycursor.fetchall()
# print(myresult)

# # Code Select with pandassss where
# query = "select first_name from actor where last_name like 'BE%';"
# pds_result = pd.read_sql(query,mydb)
# print(pds_result)



# Code Select with pandassss where
# query = " select city.city, address.address from city left join address on city.city_id = address.city_id order by city.city_id limit 60;"
query1 = " select city.city, address.address from city left join address on city.city_id = address.city_id order by city.city_id limit 60;"

xxx=1
while xxx < 60:
    pds_result = pd.read_sql(query1,mydb)
    print(pds_result.to_string())
    xxx+=1
    if xxx==60:
        break