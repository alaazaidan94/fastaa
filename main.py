from typing import Union
from fastapi import FastAPI
import sqlite3

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*']    
)
 

@app.post("/users/addUsers")
def add_users(userName,passWord,firstName,lastName,email):
    db = sqlite3.connect("DataBase.db")
    cur = db.cursor()
    cur.execute(f"select username from users where username = '{userName}'")
    c = cur.fetchall()
    lst = []
    for i in c:
        lst.append(i)
    x = 0    
    if (not lst):
        x = 1
        db.execute(f"insert into users(username,password,firstname,lastname,email) values ('{userName}','{passWord}','{firstName}','{lastName}','{email}')")
        db.commit()
        db.close()
    else:
        x = 0
        
    return x



@app.post("/users/delUser")
def get_user(id):
    db = sqlite3.connect("DataBase.db")
    cur = db.cursor()
    cur.execute(f"delete from users where id = {id}")  
    db.commit()
    db.close()
    return 1

@app.get("/users")  
def getAllUser():
    db = sqlite3.connect("DataBase.db")
    cur = db.cursor()
    cur.execute("SELECT * from users")
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


@app.get("/management")
def getManagements():
    db = sqlite3.connect("DataBase.db")
    cur = db.cursor()
    cur.execute("SELECT * from management")
    c = cur.fetchall()
    lst_json=[]
    for i in c:
        item={}
        item["id"] = i[0]
        item["username"] = i[1]
        item["password"] = i[2]
        lst_json.append(item)
    return lst_json  

@app.post("/management/addManagement")
def addManagement(userName,passWord):
    db = sqlite3.connect("DataBase.db")
    db.execute(f"INSERT INTO management(username,password) VALUES ('{userName}','{passWord}')")
    db.commit()
    db.close()
    return 1

@app.post("/management/removeManagement")
def removeManagement(id):
    db = sqlite3.connect("DataBase.db")
    cur = db.cursor()
    cur.execute(f"delete from management where id = {id}")  
    db.commit()
    db.close()
    return 1
    
@app.get("/questions")
def getQuestions():
    db = sqlite3.connect("DataBase.db")
    cur = db.cursor()
    cur.execute("SELECT * from questions")
    c = cur.fetchall()
    lst_json=[]
    for i in c:
        item={}
        item["id"] = i[0]
        item["question"] = i[1]
        item["choice1"] = i[2]
        item["choice2"] = i[3]
        item["choice3"] = i[4]
        item["choice4"] = i[5]
        item["grouperadio"] = i[6]
        lst_json.append(item)
    return lst_json  

@app.post("/questions/addQuestion")
def addQuestion(question,choice1,choice2,choice3,choice4):
    db = sqlite3.connect("DataBase.db")
    db.execute(f"INSERT INTO questions(question,choice1,choice2,choice3,choice4) VALUES ('{question}','{choice1}','{choice2}','{choice3}','{choice4}')")
    db.commit()
    db.close()
    return 1

@app.post("/questions/removeQuestions")
def removeQuestion(id):
    db = sqlite3.connect("DataBase.db")
    cur = db.cursor()
    cur.execute(f"delete from questions where id = {id}")  
    db.commit()
    db.close()
    return 1    

@app.post("/questions/updateQuestion")
def updateQuestion(id,question,choice1,choice2,choice3,choice4):
    db = sqlite3.connect("DataBase.db")
    db.execute(f"update questions set question = '{question}',choice1 = '{choice1}',choice2 = '{choice2}',choice3 = '{choice3}',choice4 = '{choice4}' where id = {id}")
    db.commit()
    db.close()
    return 1    
    
@app.get("/verification/manger")
def verificationManger(username,password):
    db = sqlite3.connect("DataBase.db")
    cur = db.cursor()
    cur.execute(f"SELECT username,password from management where username = '{username}'and password = '{password}'")
    c = cur.fetchall()
    lst_json=[]
    for i in c:
        lst_json.append(i)
    x = 0
    if (not lst_json):
        x = 0
    else:
        x = 1

    return x    

@app.get("/verification/user")
def verificationUser(username,password):
    db = sqlite3.connect("DataBase.db")
    cur = db.cursor()
    cur.execute(f"SELECT username,password from users where username = '{username}'and password = '{password}'")
    c = cur.fetchall()
    lst_json=[]
    for i in c:
        lst_json.append(i)
    x = 0
    if (not lst_json):
        x = 0
    else:
        x = 1

    return x  




    
              
    
    
    
    
    
    
    
    
    
    