print("========================================")
print("        RaceCraft Garage Recipe         ")
print("========================================")

# Customer Information
customer_name = input("Customer Name: ")
contact_number = input("Contact Number: ")
address = input("Address: ")

# Product 1
print("Product 1")
product1 = input("Product Name: ")
price1 = float(input("Price:"))
quantity1 = int(input("Quantity: "))

# Product 2
print("Product 2")
product2 = input("Product Name: ")
price2 = float(input("Price: "))
quantity2 = int(input("Quantity: "))

# Product 3
print("Product 3")
product3 = input("Product Name: ")
price3 = float(input("Price: "))
quantity3 = int(input("Quantity: "))

# Calculate product amounts
amount1 = price1 * quantity1
amount2 = price2 * quantity2
amount3 = price3 * quantity3

# Calculate subtotal
subtotal = amount1 + amount2 + amount3

# Discount
discount = float(input("\nDiscount (%): "))
discount_amount = subtotal * (discount / 100)

# Final total
total = subtotal - discount_amount

# Display Receipt
print("========================================")
print("     RaceCraft Garage Recipe              ")
print("========================================")
print(f"Customer Name : {customer_name}")
print(f"Contact No.   : {contact_number}")
print(f"Address       : {address}")
print("----------------------------------------")
print(f"{'Product':<15}{'Price':>8}{'Qty':>5}{'Amount':>10}")
print("----------------------------------------")

print(f"{product1:<15}{price1:>8.2f}{quantity1:>5}{amount1:>10.2f}")
print(f"{product2:<15}{price2:>8.2f}{quantity2:>5}{amount2:>10.2f}")
print(f"{product3:<15}{price3:>8.2f}{quantity3:>5}{amount3:>10.2f}")

print("----------------------------------------")
print(f"{'Subtotal':<28}{subtotal:>10.2f}")
print(f"{'Discount':<28}{discount_amount:>10.2f}")
print("----------------------------------------")
print(f"{'TOTAL':<28}{total:>10.2f}")
print("========================================")
print("       Thank you for shopping!          ")
print("========================================")

C:\Users\Boss K\PycharmProjects\WelcomeScreen\.venv\Scripts\python.exe" "C:\Users\Boss K\PycharmProjects\WelcomeScreen\ITE-260_P1_ACTIVITY_BSIT1_S8_CAJIPE, KEVIN ROI G..py" 
========================================
        RaceCraft Garage Recipe         
========================================
Customer Name: CAJIPE KEVIN ROI GUILLEN
Contact Number: 09648997046
Address: SNDE
Product 1
Product Name: ROLL CAGE
Price:20
Quantity: 1
Product 2
Product Name: FULL EXHAUST 
Price: 30
Quantity: 1
Product 3
Product Name: Yokohama Advan A050 TIRE 
Price: 61
Quantity: 4
Discount (%): 30
========================================
     RaceCraft Garage Recipe              
========================================
Customer Name : CAJIPE KEVIN ROI GUILLEN
Contact No.   : 09648997046
Address       : SNDE
----------------------------------------
Product           Price  Qty    Amount
----------------------------------------
ROLL CAGE         20.00    1     20.00
FULL EXHAUST      30.00    1     30.00
Yokohama Advan A050 TIRE    61.00    4    244.00
----------------------------------------
Subtotal                        294.00
Discount                         88.20
----------------------------------------
TOTAL                           205.80
========================================
       Thank you for shopping!          
========================================

Process finished with exit code 0
