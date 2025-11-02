actual_cost=int(input("Enter the actual cost of item:"))
selling_price=int(input("Enter the selling price of item:"))

if selling_price>actual_cost:
    profit=selling_price-actual_cost
    print("Profit: ",profit)

elif selling_price<actual_cost:
    loss=actual_cost-selling_price
    print("Loss: " ,loss)

else:
    print("No Profit, No loss")