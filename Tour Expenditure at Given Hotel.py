Tour Expenditure at Given Hotel 

The family has spent the vacation in Goa and now they are returning home to do so they will have to check out from the hotel.

Tariff on Room: Delux Room- 7500 INR

                            Non AC Room- 4500 INR 

You  as a developer has to create a program for a hotel owner which has the following requirements,

The program should begin with taking input from the checkout counter 

Type of room booked 
Total number of days 
Total Amount on Food (Amount is expected )
There are the following cases to be considered while generating a bill.

The tax on food amount is dependent on the type of room booked.

Tax on food for the deluxe room will be billed  18% of the total food amount.

Tax on food for the Non AC room will be billed  5% of the total food amount.

You are supposed to include a tip of 10% on the food amount.

The output from your program should include;

The  Room Tariff on the number of days spend, GST on a meal(Breakdown of GST is necessary based on CGST and SGST and same has to get reflected on console ) 

The tip amount, and the grand total for the meal including both the tax and the tip.

Format the output so that all of the values are displayed using two decimal places.


def Hotel(type, days, Amf):
    if type == "Delux Room":
        Room_price = 7500*days
        print("Your Room Tariff for Delux Room is:",Room_price)
        tf = 0.18*Amf #tax on food
        print("Total GST on your meal is:",tf)
        cgst = 0.09*Amf
        sgst = 0.09*Amf
        print("CGST:",cgst)
        print("SGST:",sgst)
        tip = 0.1*Amf
        print("The tip given by you is:",tip)
        total = Amf + tf + tip
        return total
    if type == "Non AC Room":
        Room_price = 4500*days
        print("Your Room Tariff for Non AC Room is:",Room_price)
        tf = 0.05*Amf #tax on food
        print("Total GST on your meal is:",tf)
        cgst = 0.025*Amf
        sgst = 0.025*Amf
        print("CGST:",cgst)
        print("SGST:",sgst)
        tip = 0.1*Amf
        print("The tip given by you is:",tip)
        total = Amf + tf + tip
        return total
    

type = input()
days = int(input())
Amf = int(input())
print("The grand total for meal is:", Hotel(type,days,Amf))
