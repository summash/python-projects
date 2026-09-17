import pandas as pd
import os


#input
user=str(input('''what do you want to do:
1.check savings 2.calculate profit or loss 3.input saving data 4.withdraw money
type here: '''))


#profit or loss calculator
def profit_or_loss(cost,sell):
    if cost>sell:
        
        print(f'a loss of {cost-sell}')
    else:
        print(f'a profit of {sell - cost}')
        
#file name 
filename='expense.xlsx'
#savings data 
def saving_data():
    date = input("Enter the date (YYYY-MM-DD): ")
    description = input("Enter the expense description: ")
    amount = float(input("Enter the amount: "))
    category = input("Enter the category (Food, Transport, etc.): ")
# Create a new DataFrame with the user input
    new_data = pd.DataFrame([[date, description, amount, category]], 
                            columns=["Date", "Description", "Amount", "Category"])    
    # Check if the file exists
    if os.path.exists(filename):
        # Load existing data
        existing_data = pd.read_excel(filename)
        # Append new data
        updated_data = pd.concat([existing_data, new_data], ignore_index=True)
    else:
        updated_data = new_data  # If file doesn't exist, create new

    # Save back to Excel
    updated_data.to_excel(filename, index=False)
    print("✅ Expense saved successfully!")
    
    
#if 1
if user=='deposit money' or 3:
    saving_data()
else:
    pass
#if 2
if user=='calculate profit or loss' or 2:
    cost=int(input('enter the price of the thing you bought: '))
    sell=int(input('enter the price in which you selled the item.'))
    profit_or_loss(cost, sell)
else:
    pass

deposit=int()


#a storage unit which saves amount of savings in a data
#a way to deposit money
#a way to withdraw money from the savings





