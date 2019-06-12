"""
Write a program that repeatedly asks the user to enter product names and prices. Store all
of these in a dictionary whose keys are the product names and whose values are the prices.
When the user is done entering products and prices, allow them to repeatedly enter a product
name and print the corresponding price or a message if the product is not in the dictionary.
"""

store={}
for i in range (3):
    product_name=input("enter product name: ")
    product_price=eval(input("enter product price: "))
    print()
    store[product_name]=product_price

for i in range (2):
    product_name=input("enter product name: ")
    if product_name in store:
        print("price of",product_name," is",store[product_name])
    else:
        print("we don't have ", product_name)

"""
Using the dictionary created in the previous problem, allow the user to enter a dollar amount
and print out all the products whose price is less than that amount
"""
dollar_amount=eval(input("enter an dollar amount: "))
product_less=[name for name in store if store[name]<dollar_amount]
print("the product(s) whose price is less than that amount: ", product_less) #muuốn hiển thị mà không có những dấu ngoặc phải làm sao?

    

