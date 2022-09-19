from typing import Union
from fastapi import FastAPI
import mysql.connector

mydb = mysql.connector.connect(host="bmj7gpyrnnvddlwsuzmm-mysql.services.clever-cloud.com",
                                     user="uey0hhoxexn16bqq",
                                     password="NCPJvn5Y3ibyB6KWEHXR",
                                     database= "bmj7gpyrnnvddlwsuzmm")

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*']    
)
 
@app.get("/users")  
def getAllUser():
    cur = mydb.cursor()
    cur.execute("select * from Users")
    c = cur.fetchall()
    lst_json=[]
    for i in c:
        item={}
        item["id"] = i[0]
        item["username"] = i[1]
        item["password"] = i[2]
        item["firstname"] = i[3]
        item["lastname"] = i[4]
        item["email"] = i[5]
        lst_json.append(item)
    return lst_json   
