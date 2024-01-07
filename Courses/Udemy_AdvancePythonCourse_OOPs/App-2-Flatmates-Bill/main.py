from fpdf import FPDF
import webbrowser 

class Bill:
   """
   Object that contain data about a bill. 
   members: Amount, Period
   """

   def __init__(self, amount, period):
      self.amount = amount
      self.period = period


class Flatmate:
   """
   Create a flatmate person who lives in a flat and pays a share of the bill
   """

   def __init__(self, name, days_in_house):
      self.name = name
      self.days_in_house = days_in_house 

   def pays(self, bill, other_flatmate):
      #TODO: Add a pays method, that calculate flatmate's share for the given bill amount
      weight = self.days_in_house / (self.days_in_house + other_flatmate.days_in_house)

      return weight * bill.amount

class PdfReport:
   """
   Creates a PDF files with bill and flatmate details with their individual shares
   """

   def __init__(self, filename):
      self.filename = filename 

   def generate(self, flatmate1, flatmate2, bill):
      #TODO: Add the generate method, that takes two flatmates, and a bill and creates the PDF
         pdf = FPDF()
    
         # Add a page
         pdf.add_page()


         # Set font
         pdf.set_font("Arial", size=16, style='B')
         
         # Header
         pdf.set_fill_color(52, 152, 219)  # Set header background color
         pdf.set_text_color(255, 255, 255)  # Set text color
         pdf.cell(200, 10, txt="Monthly Rental Bill", ln=True, align="C", fill=True)
         
         pdf.set_font("Arial", size=12)

         # Adding a line separator as part of the header
         pdf.set_line_width(0.5)
         pdf.line(10, 20, 200, 20)
         pdf.cell(200, 10, txt="", ln=True, align="C")  # Adding empty line
         
         # Period of the bill
         pdf.set_text_color(0, 0, 0)  # Reset text color
         pdf.cell(200, 10, txt=f"Period: {bill.period}", ln=True, align="L")
         
         # Total amount
         pdf.cell(200, 10, txt=f"Total Amount: ${bill.amount}", ln=True, align="L")
         pdf.cell(200, 10, txt="", ln=True, align="C")  # Adding empty line
         
         # Individual shares
         flatmate1_share = flatmate1.pays(bill, other_flatmate = flatmate2)
         flatmate2_share = flatmate2.pays(bill, other_flatmate = flatmate1)
         
         # Formatting the shares
         pdf.cell(200, 10, txt=f"Flatmate 1 Share: ${flatmate1_share:.2f} ({flatmate1.days_in_house} days)", ln=True, align="L")
         pdf.cell(200, 10, txt=f"Flatmate 2 Share: ${flatmate2_share:.2f} ({flatmate2.days_in_house} days)", ln=True, align="L")
         pdf.cell(200, 10, txt="", ln=True, align="C")  # Adding empty line
         
         # Adding a line separator
         pdf.line(10, pdf.get_y(), 200, pdf.get_y())
         pdf.cell(200, 10, txt="", ln=True, align="C")  # Adding empty line
         
         # Footer
         pdf.set_font("Arial", size=10)
         pdf.cell(0, 10, txt="Thank you for your payment.", ln=True, align="C")
         
         # Save the PDF with the name "rental_bill.pdf"
         pdf.output(f"{self.filename}.pdf")

         webbrowser.open(f"{self.filename}.pdf")

bill = Bill(amount = 120, period = 'March 2021')
flatmate1 = Flatmate(name = 'John', days_in_house = 20)
flatmate2 = Flatmate(name = 'Merry', days_in_house = 25)

share_of_flatmate1 = flatmate1.pays(bill, other_flatmate = flatmate2)
share_of_flatmate2 = flatmate2.pays(bill, other_flatmate = flatmate1)

print(f"""The total bill amount is : {bill.amount} \n
      {flatmate1.name} has to pay {share_of_flatmate1:2.1f}, \n
      and {flatmate2.name} has to pay {share_of_flatmate2:2.1f}""")


pdf = PdfReport(bill.period) 
pdf.generate(flatmate1, flatmate2, bill)

print("Program exited successfully.")
