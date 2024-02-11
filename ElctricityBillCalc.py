#Here you prompt the user to enter the following details
customerID= int(input("Enter Customer ID : "))
customeName= input("Enter Customer Name : ")
unitsConsumed= int(input("Enter Number of Units Consumed : "))


#if--else statement to determine fine rate
if unitsConsumed <= 199:
    charges=1.20
elif unitsConsumed >= 200 and unitsConsumed < 400:
    charges=1.50
elif unitsConsumed >= 400 and unitsConsumed < 600:
    charges=1.80
elif unitsConsumed >= 600:
    charges=2.00
#using the charges obtained to calculate the total amount
bill = charges * unitsConsumed
#fi statement to calculte surchage if the bill exceeds 400
if bill > 400:
    surcharge=0.15
    totalbill = bill*surcharge
    print("Add  Ksh.",totalbill," to the Total Amount below to get your Total Bill")

#output
print("\n")
print("Customer ID : ",customerID)
print("Customer Name : ",customeName)
print("Units Consumed : ",unitsConsumed)
print("Charges per Unit : ",charges)
print("Total Amount : Ksh.",bill)