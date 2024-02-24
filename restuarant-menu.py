#Restuarant Menu App
# This app get order from cuatomer and return the total cost

#import pandas library to read excel files
import pandas as pd
try:
    df = pd.read_excel("menu.xlsx") 
    print('*************************************')
    print('Welcome to Python Cohort 1 Restuarant') 
    print('*************************************')
    print(df)
    print('-------------------------------------')
except FileNotFoundError:
    print("File not Found")
items_on_menu = {}
for val in df.values:
    item, value = val
    items_on_menu[item.casefold()]= value

# This stores user's selected menu and quantity
user_order={}

while True:
    user_select_menu = input("Please select the items you would like to purchase: ")
    
    #check if user's selected item is in the menu excel file
    if (user_select_menu in items_on_menu.keys()):
        user_select_menu_quantity = int(input("Please enter the quantity of the items you would like to purchase: "))
        #check if user selected item is not already in the user_order 
        if (user_select_menu not in user_order):
                user_order[user_select_menu.casefold()] = user_select_menu_quantity
        else:
            print("order can not be repeated, existing order can oly be updated")
            new_quantity= int(input("Please enter the new quantity for {0} : ".format(user_select_menu)))
            user_order[user_select_menu.casefold()] = new_quantity
        request= input("Do you want to add more (y / n ) : ")
        if (request == 'n'):
            print(user_order)
            break
        
        if (request == 'y'):
            continue
    else:
        print("Item not in menu list, try again")    



# total cost is user selected item * quantity selected * tax
#initialize total cost
total_cost = 0
#assuming tax is 13%
tax = 0.13
for item_user_order in user_order:
   total_cost = total_cost + (user_order[item_user_order] * items_on_menu[item_user_order] * 0.13 ) 
print("This order includes tax and total cost is : ${:.2f}".format(total_cost))


