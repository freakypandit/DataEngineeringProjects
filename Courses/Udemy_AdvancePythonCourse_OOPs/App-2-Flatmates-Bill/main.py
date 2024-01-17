from Flat import Bill, Flatmate
from Reports import PdfReport

#TODO: Create a CLI interface for the application 
amount = int(input("Hey User, enter the bill amount"))
period = input("Provide the period for this bill.")

print("Enter Details for first flatmate")
name_first = input("Name:")
days_in_house_first = int(input("Duration of Stay in days:"))

print("Enter Details for second flatmate")
name_second = input("Name:")
days_in_house_second = int(input("Duration of Stay in days:"))

bill = Bill(amount = amount, period = period)
flatmate1 = Flatmate(name = name_first, days_in_house = days_in_house_first)
flatmate2 = Flatmate(name = name_second, days_in_house = days_in_house_second)

share_of_flatmate1 = flatmate1.pays(bill, other_flatmate = flatmate2)
share_of_flatmate2 = flatmate2.pays(bill, other_flatmate = flatmate1)

print(f"""The total bill amount is : {bill.amount} \n
      {flatmate1.name} has to pay {share_of_flatmate1:2.1f}, \n
      and {flatmate2.name} has to pay {share_of_flatmate2:2.1f}""")


pdf = PdfReport(bill.period) 
pdf.generate(flatmate1, flatmate2, bill)

print("Program exited successfully.")
