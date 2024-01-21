from PIL import Image
import numpy as np 
import os 

class Canvas:
   """
   Create a canvas of size width * height of a given color
   """
   def __init__(self, width, height, color):
      self.width=width
      self.height=height
      self.color=color 


      self.data = np.zeros((self.width, self.height, 3), dtype=np.uint8)

      self.data[:] = self.color

   def make(self):
      #TODO: create a function for making an writing image to directory
      
      img = Image.fromarray(self.data, 'RGB')
      img.save("Shape.png")
         
class Rectangle:
   """
   Creates a rectangle of a given size width * height starting from (x, y) coordinates of given color.
   """
   def __init__(self, x, y, width, height, color):
      self.x = x
      self.y = y 
      self.width = width 
      self.height = height 
      self.color = color 

   def draw(self, canvas):
      
      #sanity 
      if(self.x + self.width > canvas.width or self.y + self.height > canvas.height):
         print("Shape will stretch beyond the Canvas")

      if(self.x > canvas.width or self.y > canvas.height):
         print("Shape is outside of Canvas")

      canvas.data[self.x:(self.width+self.x), self.y:(self.height+self.y)] = self.color

class Square:
   """
   Create a square of given size side * side starting from (x, y) of given color 
   """
   def __init__(self, x, y, side, color):
      self.x = x 
      self.y = y 
      self.side = side 
      self.color = color 

   def draw(self, canvas):
      #sanity 
      if(self.x + self.side > canvas.width or self.y + self.side > canvas.height):
         print("Shape will stretch beyond the Canvas")

      if(self.x > canvas.width or self.y > canvas.height):
         print("Shape is outside of Canvas")

      canvas.data[self.x:(self.side+self.x), self.y:(self.side+self.y)] = self.color

   
if __name__ == "__main__":

   print("Welcome to the Math Painter Game.")

   print("Please start by creating a Canvas")
   width = int(input("Enter the width of Canvas:"))
   height = int(input("Enter the height of the Canvas:"))
   color = int(input("What color canvas do you want enter 0 for black and 255 for white"))

   canvas = Canvas(width, height, color)

   while(True):
      
      shape = input("Enter the shape you want to draw, write quit to quit")

      if(shape.lower() == 'rectangle'):
         width = int(input("Provide the width of Rectangle:"))
         height = int(input("Provide the height of Rectangle:"))

         red,blue,green = [int(x) for x in input("Provide the color for the rectangle in RGB format - R, G, B:").split(sep=',')]
         coords_x = int(input("Provide the starting x coordinate:"))
         coords_y = int(input("Provide the starting y coordinate:"))

         rectangle = Rectangle(x = coords_x, y = coords_y, width = width, height = height, color = (red, blue, green))

         rectangle.draw(canvas) 

      if(shape.lower() == 'square'):
         side = int(input("Provide the side of Square:"))
         red,blue,green = [int(x) for x in input("Provide the color for the rectangle in RGB format - R, G, B:").split(sep=',')]
         coords_x = int(input("Provide the starting x coordinate:"))
         coords_y = int(input("Provide the starting y coordinate:"))

         square = Square(x = coords_x, y = coords_y, side = side, color = (red, blue, green))

         square.draw(canvas) 

      if(shape.lower() == 'quit'):
         break

   print("Thanks for playing Maths painter.")
   print("Generating your Art....")

   canvas.make()

