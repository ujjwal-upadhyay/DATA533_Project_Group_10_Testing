# This is a sample Python script.


from customer.Customer import Customer
from customer.Search import Search
from produce.Fruit import Apple, Banana, Pear, Orange, Grape
from produce.Inventory import Inventory

if __name__ == '__main__':
    search = Search()
    while True:
        print('Welcome to ABC Fruit Market!')
        customer = Customer()
        search.set_customer(customer)
        operation=input('Press 1 to check product information in the store, press 2 start to purchase:')
        if(operation=='1'):
            print('The current stock is as follows:')
            search.get_inventory()
            if(input('Whether to sort by price，Y-Yes；N-No：')=='Y'):
                print('Query inventory by price, the results are as follows:')
                search.get_sort_price()
        if(operation=='2'):
            budget = input('Please enter your budget.')
            customer.set_budget(budget)
            while True:
                name=input('Please enter the name of the fruit you want to buy, press Q to exit:')
                if name=='Q':
                    break
                if(not search.fruit_detail(name)):
                    continue
                num=input('Please enter the number of fruits you want to buy：')
                customer.shop_item(name,num)
                customer.items_detail()
                isOver,all_price=search.get_current_price()
                if(not isOver):
                    choice_budget=input('The budget is exceeded, do you want to settle at this price？N-No Y-Yes: ')
                    if(choice_budget=='N'):
                        customer.clear_items()
                        continue
                    if(choice_budget=='Y'):
                        customer.items_detail()
                        print('Please settle at the current price.')
                        print(f'Total price is {all_price}.')
                        break
            search.sales()







