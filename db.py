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
    mycursor.execute("SELECT * FROM Transactions")
    rows=mycursor.fetchall()
    transactions = []
    for row in rows:
        transactions.append({
            "id": row[0],
            "amount": row[1],
            "category": row[2],
            "type": row[3],
            "date": row[4],
            "description": row[5]
        })
    return transactions
def add_transaction(amount, category, transaction_type, date, description):
    values = (amount, category, transaction_type, date, description)
    mycursor.execute(
        "INSERT INTO Transactions (amount, category, type, date, description) "
        "VALUES (%s, %s, %s, %s, %s)",
        values
    )
    db.commit()
    return True
def update_transaction(transaction_id, choice, value):
    if choice==1:
        mycursor.execute(
            "UPDATE Transactions SET Amount=%s WHERE id= %s",
            (value, transaction_id)
        )
    elif choice==2:
        mycursor.execute(
            "UPDATE Transactions SET Category=%s WHERE id= %s",
            (value, transaction_id)
        )
    elif choice==3:
        mycursor.execute(
            "UPDATE Transactions SET Type=%s WHERE id= %s",
            (value, transaction_id)
        )
    elif choice==4:
        mycursor.execute(
            "UPDATE Transactions SET Date=%s where id= %s",
            (value, transaction_id)
        )
    elif choice==5:
        mycursor.execute(
            "UPDATE Transactions SET Description=%s WHERE id= %s",
            (value, transaction_id)
        )
    db.commit()
    print("Transaction updated successfully")
def delete_transaction():
    transaction_id=int(input("Enter Transaction Id: "))
    transaction_id=(transaction_id,)#Act as tuple
    mycursor.execute("delete from Transactions where id =%s",transaction_id)
    db.commit()
    print("Transaction deleted successfully")