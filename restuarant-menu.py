#Restuarant Menu App
# This app get order from cuatomer and return the total cost

#import pandas library to read excel files
import pandas as pd
try:
    df = pd.read_excel("menu.xlsx") 
    print()
    print('***************************************')
    print('Welcome to Python Cohort 1 Restuarant') 
    print('***************************************')
    print(df)
    print('---------------------------------------')
    print()
except FileNotFoundError:
    print("File not Found")
items_on_menu = {}
for val in df.values:
    item, value = val
    items_on_menu[item.casefold()]= value


# This stores user's selected menu and quantity
user_order={}
    
while True:
    user_select_menu = input("Please select the item you would like to purchase: ").casefold()
    #check if user's selected item is in the menu excel file
    if (user_select_menu in items_on_menu.keys()):
        
        user_select_menu_quantity = int(input("Please enter the quantity of the item you would like to purchase: "))
        #check if user selected item is not already in the user_order 
        if (user_select_menu not in user_order):
                user_order[user_select_menu.casefold()] = user_select_menu_quantity
        else:
            print("order can not be repeated, existing order can only be updated")
            new_quantity= int(input("Please enter the new quantity for {0} : ".format(user_select_menu)))
            user_order[user_select_menu.casefold()] = new_quantity
        request= input("Do you want to add more (y / n ) : ")
        if (request == 'n'):
            # print(user_order)
            print('\n **** Receipt **** \n')
            for selected_items,customer_quantity in user_order.items():
                print('{} {} @ ${} = ${}'.format(selected_items.capitalize(),customer_quantity,items_on_menu[selected_items],items_on_menu[selected_items] * customer_quantity))
            break
        
        if (request == 'y'):
            continue
    else:
        print("Item not in menu list, try again")    




#initialize total cost
total_cost = 0
#assume tax is 13%
tax = 0.13
for item_user_order in user_order:
    order_times_quantity = (user_order[item_user_order] * items_on_menu[item_user_order])
    total_cost = total_cost + order_times_quantity
# print (total_cost) cost without tax
total_cost_plus_tax = total_cost + (total_cost * 0.13) 
print("Total cost after tax(13%) is : ${:.2f} \n".format(total_cost_plus_tax))
# print("This order includes tax(13%) \n  total cost is : ${:.2f}".format(total_cost_plus_tax))


