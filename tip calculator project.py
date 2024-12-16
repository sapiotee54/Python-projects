print("Welcome to the tip calculator")
total_bill = float(input("How much is the total bill?\nN"))
tip_percent = int(input("How much tip will you like to give?\n 5, 7, 10, 15\n"))
num_people = int(input("How many people will you split the bill with?\n"))
val_tip_percent = (tip_percent/100) * total_bill
total_bill += round(val_tip_percent,2)
individual_pay = round(total_bill/num_people,2)
print(f"Your bill is N{total_bill}, so each person will pay N{individual_pay}")

