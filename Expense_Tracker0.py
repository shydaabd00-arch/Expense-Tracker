import json
Show_menu =("Cost Management:\n1.Log Expense\n2.Show Expenses\n3.Total Expenses\n4.Delete Expense\n5.Exit")
list_ = []
def load_expenses():
    try:
        global list_
        with open("expenses.json","r") as file:
            list_ = json.load(file) 
    except FileNotFoundError:
        list_ = []         
load_expenses()
def get_expense():
    while True:
        try:
            get_price = float(input("Enter amount:"))
   
        except ValueError:
            print("We Have An Error!")
            continue
        get_dcp = input("Enter description:")
        get_cg = input("Enter category:")
        return get_price,get_dcp,get_cg
        

def add_expense(get_price,get_dcp,get_cg):
    my_dict = {
                "Amount":get_price,
                "Description":get_dcp,
                "Category":get_cg
            }
    list_.append(my_dict)
def show_expenses(): 
    if list_:
        for number,item in enumerate(list_):
            print(f"Expense {number}")
            print("Amount",item["Amount"])
            print("Description",item["Description"])
            print("Category",item["Category"])
    else:
        print("Sorry,The list is empty and there\'s nothing to display!")   
def total_Expenses():
    if list_: 
        total = 0
        for item in list_:
            total = total + item["Amount"]
        print(total)
    else:
        print("No expenses recorded!")    

def delete_Expenses(): 
    while True: 
        try:  
            if list_:
                Del_price = int(input("Enter expense number to delete:"))  
                if Del_price < len(list_) and Del_price >= 0:
                    list_.pop(Del_price)
                    return
                else:
                    print("Invalid expense number!")    
        
            else:
                print("No expenses to delete!")
                return 
        except ValueError:
            print("We Have An Error!")    
def save_expenses():
    with open("expenses.json","w") as file:
        json.dump(list_,file)  
           
                   
while True:
    print(Show_menu)
    try:
        x = int(input("Enter A Number:"))
    except ValueError:
        print("Pleas Enter A Vaild Number!")
        continue
    if x == 1:
        get_price,get_dcp,get_cg = get_expense()
        add_expense(get_price,get_dcp,get_cg)
        save_expenses()
        
    elif x == 2:
        show_expenses()   
    elif x == 3: 
        total_Expenses()   
    elif x == 4:
        delete_Expenses()
        save_expenses()
                       
    elif x == 5:
        break  
    else:
        print("Invaild Choice!")
    
       


    
