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