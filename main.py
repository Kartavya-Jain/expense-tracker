from db import view_transactions, add_transaction, update_transaction, delete_transaction
def Menu():
    print("----------Expense Tracker----------")
    print("1. View Transactions")
    print("2. Add Transactions")
    print("3. Update Transactions")
    print("4. Delete Transactions")
    print("5. Exit")
    while True:
        try:
            choice=int(input("Enter your choice: "))
            if 1<=choice<=5:
                break
            else:
                print("Invalid choice")
        except ValueError:
            print("Invalid input! Please enter a valid number")
    if choice==1:
        view_transactions()
    elif choice==2:
        add_transaction()
    elif choice==3:
        update_transaction()
    elif choice==4:
        delete_transaction()
    elif choice==5:
        return False
    return True
while True:
    if Menu()==False:
        break