from tkinter import Y
import mysql.connector
from PIL import Image
db1=mysql.connector.connect(host='localhost',user = 'root',password = '******',database = 'dbmsproj')
from datetime import date
today = date.today()
print(today)
print("Connection succesful")
cur = db1.cursor()
print('*'*150)
print("                                                      WELCOME TO THE LOGIN PAGE")
print('*'*150)
print("1) Login into an existing account")
print("2) Create a new account")
t = int(input("Enter the service you want to use: "))
if t == 1:
    for i in range (0,4):    
        x = input("Enter your user id: ")
        h = input("Enter your password: ")
        
        s = f'select passwords from login where user_id = "{x}"' 
        cur.execute(s)
        r = cur.fetchone()
        y = r

        if y == None:
            print("user does not exist")
        else:

            if h == y[0]:
                print("Login succesfully")
                break
            else:
                print("Incorrect password")
        if i == 2:
            print("Too many attempts ")
            exit()
if t == 2:
    a = 0 
    s = 'select count(customer_id) from users'
    cur.execute(s)
    r = cur.fetchall()
    a = r[0][0]+1
    i = f"CR0{a}"
    x = input("Enter you name: ")
    y = input("Enter your phone number: ")
    z = input("Input your gmail: ")
    s = 'INSERT INTO users values(%s,%s,%s,%s)'
    t = (i,x,y,z)
    cur.execute(s,t)
    db1.commit()
    k = input("Enter new password: ")
    s = 'INSERT INTO login values(%s,%s)' 
    t = (x,k)
    cur.execute(s,t)
    db1.commit
    s = f'CREATE TABLE {x}_cart(event_id varchar(4),event_name varchar(10),price int(4))'
    cur.execute(s)
    s = f'CREATE TABLE {x}_history(event_id varchar(4),event_name varchar(10),price int(4))'
    cur.execute(s)
u=1
while u>0:
    print('*'*150)
    print("                                                      WELCOME TO THE TICKET BOOKING")
    print('*'*150)
    s = 'select* from booking'
    cur.execute(s)
    r = cur.fetchall()
    for i in  r :
        for p in i:
            print(p,end=" ")
        print()
    print("1) Book a ticket for the ISL match")
    print("2) Book a ticket for the movie")
    print("3) Go to your cart")
    print("4) Go to your history")
    print("0) Exit")
    g = int(input("Enter the number of service you want to use today: "))
    if g == 0:
        print("Thank you")
        exit()
    if g == 1:                                                                                
        img = Image.open('Stadium_new.jpg')
       
        img.show()
        inp = input("Enter the section where you want to book your tickets to exit enter E: ").upper()
        if inp == 'E':
            print()
        elif inp == "A":
                s = 'select price from stadium where seat_lounge ="A"'
                cur.execute(s)
                r = cur.fetchall()
                print(f"The price of the tickets are {r[0]}",end=" ")
                y = input("Add to cart?(Y/N): ").upper()
                if y == "Y":
                    b = 'select available from stadium where seat_lounge ="A"'
                    cur.execute(b)
                    r = cur.fetchall()
                    gg = r[0][0]-1
                    b = f"UPDATE stadium SET available = {gg} WHERE seat_lounge ='A'" 
                    cur.execute(b)
                    db1.commit
                    id_event = "ST01"
                    event_name = "ISL match"
                    price = 400
                    s = f'INSERT INTO {x}_cart values(%s,%s,%s)'
                    t = (id_event,event_name,price)
                    cur.execute(s,t)
                    db1.commit()                    
                else:
                    print( )
        elif inp == "B":
                s = 'select price from stadium where seat_lounge ="B"'
                cur.execute(s)
                r = cur.fetchall()
                print(f"The price of the tickets are {r[0]}",end=" ")
                y = input("Add to cart?(Y/N): ").upper()
                if y == "Y":
                    b = 'select available from stadium where seat_lounge ="B"'
                    cur.execute(b)
                    r = cur.fetchall()
                    gg = r[0][0]-1
                    b = f"UPDATE stadium SET available = {gg} WHERE seat_lounge ='B'"
                    cur.execute(b)
                    db1.commit       
                    id_event = "ST01"
                    event_name = "ISL match"
                    price = 500
                    s = f'INSERT INTO {x}_cart values(%s,%s,%s)'
                    t = (id_event,event_name,price)
                    cur.execute(s,t)
                    db1.commit()                    
                else:
                    print( ) 
        elif inp == "C":
                s = 'select price from stadium where seat_lounge ="C"'
                cur.execute(s)
                r = cur.fetchall()
                print(f"The price of the tickets are {r[0]}",end=" ")
                y = input("Add to cart?(Y/N): ").upper()
                if y == "Y":
                    b = 'select available from stadium where seat_lounge ="C"'
                    cur.execute(b)
                    r = cur.fetchall()
                    gg = r[0][0]-1
                    b = f"UPDATE stadium SET available {gg} WHERE seat_lounge ='C'"  
                    cur.execute(b)
                    db1.commit     
                    id_event = "ST01"
                    event_name = "ISL match"
                    price = 300
                    s = f'INSERT INTO {x}_cart values(%s,%s,%s)'
                    t = (id_event,event_name,price)
                    cur.execute(s,t)
                    db1.commit()                    
                else:
                    print( ) 
        elif inp == "D":
                s = 'select price from stadium where seat_lounge ="D"'
                cur.execute(s)
                r = cur.fetchall()
                print(f"The price of the tickets are {r[0]}",end=" ")
                y = input("Add to cart?(Y/N): ").upper()
                if y == "Y":
                    b = 'select available from stadium where seat_lounge ="D"'
                    cur.execute(b)
                    r = cur.fetchall()
                    gg = r[0][0]-1
                    b = f"UPDATE stadium SET available {gg} WHERE seat_lounge ='D'" 
                    cur.execute(b)
                    db1.commit      
                    id_event = "ST01"
                    event_name = "ISL match"
                    price = 400
                    s = f'INSERT INTO {x}_cart values(%s,%s,%s)'
                    t = (id_event,event_name,price)
                    cur.execute(s,t)
                    db1.commit()                    
                else:
                    print( )                
    if g == 2:
        img = Image.open('theater.jpg')
       
        img.show()        
        s = 'select * from theater where available = "Y" '
        cur.execute(s)
        r = cur.fetchall()
        number = int(input("How tickets would you like to buy: "))
        q=0
        for l in range(0,number):
            for i in  r :
                for j in i:
                    print(j,end=" ")
                print()
            seat = input("Which seat would you prefer 100 per seat: ").upper()
            s = f'update theater set available = "N" where seat_no = "{seat}"'
            cur.execute(s)
            db1.commit()
            event_id = "MV01"
            event_name = "theater"
            p = 100
            s = f'INSERT INTO {x}_cart values(%s,%s,%s)'
            t = (event_id,event_name,p)
            cur.execute(s,t)
            db1.commit() 
    if g == 3:
        s = f'select * from {x}_cart'
        cur.execute(s)
        r = cur.fetchall()
        if cur.rowcount == 0:
            print("Empty cart")
        else:
            for i in  r :
                for p in i:
                    print(p,end = " ")
                print()
            ans = input("Do you want to proceed to pay(Y/N): ").upper()
            if ans == "Y":
                s = f'select sum(price) from {x}_cart'
                cur.execute(s)
                r = cur.fetchall()
                print(f"The total amount of payment is {r[0]}/-", end = " ")
                print("Thank you")
                s = f'Insert into {x}_history (event_id ,event_name,price) (select event_id ,event_name,price from {x}_cart)'
                cur.execute(s)
                s1 = f'delete from {x}_cart'
                cur.execute(s1)
                db1.commit()
            else:
                print("Going back to main page")   
    if g == 4:
        s = f"select * from {x}_history"
        cur.execute(s)
        r = cur.fetchall()
        for i in  r :
            for p in i:
                print(p,end=" ")
            print()