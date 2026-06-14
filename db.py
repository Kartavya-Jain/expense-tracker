import mysql.connector
db=mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="root",
    database="expense_tracker")
mycursor=db.cursor()
#Use execute and run query of sql to get data of table transactions
#mycursor.execute("Select * from transactions")
#Fetching all data of the rows from table transactions
#for row in mycursor.fetchall():
#   print(row)
def view_transactions():
    mycursor.execute("Select * from Transactions")
    for row in mycursor.fetchall():
        print(row)
def add_transaction():
    amount=int(input("Enter amount: "))
    category=str(input("Enter category: "))
    transaction_type=str(input("Enter type: "))
    date=str(input("Enter date (YYYY-MM-DD): "))
    description=str(input("Enter description: "))
    values=(amount, category, transaction_type, date, description)
    mycursor.execute("insert into Transactions (amount, category, type, date, description) values (%s,%s,%s,%s,%s)", values)
    db.commit()
    print("Transaction added successfully")
def update_transaction():
    id=int(input("Enter transaction id: "))
    choice=int(input("What do you want to update?:\n1. Amount\n2. Category\n3. Transaction Type\n4. Date\n5. Description"))
    if choice==1:
        new_amount=int(input("Enter new amount: "))
        amount_data=(new_amount,id)
        mycursor.execute("Update Transactions set Amount=%s where id= %s",amount_data)
    elif choice==2:
        new_category=str(input("Enter new category: "))
        category_data=(new_category,id)
        mycursor.execute("Update Transactions set Category=%s where id= %s",category_data)
    elif choice==3:
        new_transaction_type=int(input("Enter new type: "))
        transaction_type_data=(new_transaction_type,id)
        mycursor.execute("Update Transactions set Type=%s where id= %s",transaction_type_data)
    elif choice==4:
        new_date=str(input("Enter new date: "))
        date_data=(new_date,id)
        mycursor.execute("Update Transactions set Date=%s where id= %s",date_data)
    elif choice==5:
        new_description=str(input("Enter new description: "))
        description_data=(new_description,id)
        mycursor.execute("Update Transactions set Description=%s where id= %s",description_data)
    db.commit()
    print("Transaction updated successfully")
def delete_transaction():
    transaction_id=int(input("Enter Transaction Id: "))
    transaction_id=(transaction_id,)#Act as tuple
    mycursor.execute("delete from Transactions where id =%s",transaction_id)
    db.commit()
    print("Transaction deleted successfully")