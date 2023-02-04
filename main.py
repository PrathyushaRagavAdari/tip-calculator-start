#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")
bill = float(input("Total Bill? "))
tip = int(input("TIP? "))
guests = int(input("How many guests? "))

tippercent = tip / 100
tipamount = bill * tippercent
totalbill = bill + tipamount
per_guest = totalbill / guests
Amount = round(per_guest, 2)
print(Amount)