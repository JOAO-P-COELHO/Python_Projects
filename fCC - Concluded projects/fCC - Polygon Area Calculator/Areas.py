# READ ME available in this folder

class Rectangle: # Main class
   
    def __init__(self, width, height): # Firstly the class always has to be iniated with a width and a height
        self.width = width
        self.height = height
        
    def __str__(self): # The __str__ (a dunder method - d(ouble) under score) returns the string representation of an object. When the object (the class) itself it's called and this method it's present, it returns the string writen in the return. If the class it's called and this method it's not present, it would return the value of a pointer "<__main__.Rectangle object at 0x000001DBB695FB50>" (the local in memory where it's stored)
        return f"Rectangle(width={self.width}, height={self.height})"
    
    def set_width(self, width): # This method it's used to re-set the value of width (width and height are set initially, when the class is initiated)
        self.width = width
    
    def set_height(self, height): # This method it's used to re-set the value of height (width and height are set initially, when the class is initiated)
        self.height = height
    
    def get_area(self):  # This method returns the area (width * height)
        area = self.width * self.height
        return area
    
    def get_perimeter(self): # This method returns the perimeter (2 * width + 2 * height)
        perimeter = 2 * (self.width) + 2 * (self.height)
        return perimeter
    
    def get_diagonal(self): # This method returns the diagonal ((width ** 2 + height ** 2) ** .5)
        diagonal = (self.width ** 2 + self.height ** 2) ** .5
        return diagonal
    
    def get_picture(self): # This method returns the picture of the rectangle/square, depending on its width or height
        
        if self.width>50 or self.height>50:
            return "Too big for picture." # If any of the parameters is >50 an error it's thrown
        
        else: # Method to "draw" the figure
            n = 0
            result = []
            while n < self.height:
                asteriks = "*"  
                result.append(self.width * asteriks) # This makes the width of the figure in asterisks - it appends each line to the previous, in a list
                n = n + 1 # This makes the next line 

                if n == self.height: # When the number of iterations it's equal to the height of the figure:
                    final = "\n".join(map(str,result)) # Each member of the map it's joined to the next with a "\n". How the map function works: map(function, iterable). To each member of the result array, the function str it's applied, and, then, each of this "new stringed" element is joined to the next, by the join function, with a line space "\n".
                    return f"{final}\n"
 
    def get_amount_inside(self, shape): # This method defines how many figures (set by the user) do fit in the first figure set.
        
        if shape.width > self.width or shape.height > self.height: # If width or height it's to short, it's impossible
            return 0
        
        elif shape.width <= self.width and shape.height > self.height: # If the width isn't too short, then, the figure can fit in horizontally "x" times
            first_p = int(self.width / shape.width)
            return first_p
        
        elif shape.height <= self.height and shape.height > self.height: # If the height isn't too short, then, the figure can fit in vertically "y" times
            second_p = int(self.height / shape.height)
            return second_p
        
        elif shape.width <= self.width and shape.height <= self.height: # If the width or the height are large enough, then, the figure can fit in  vertically and horizontally "x" and "y" times
            first_p = int(self.width / shape.width)
            second_p = int(self.height / shape.height)
            return first_p * second_p
            
class Square(Rectangle): # This is a subclass of the Rectangle class - it does the same as the main class, but, in this case, its "weight" and its "height" have the same value, and are called "sides"
    def __init__(self, side):
        self.width = side
        self.height = side
    
    def __str__(self): # The same __str__ method that makes sure that when the object itself it's called, the return it's a string and not a pointer
        return f"Square(side={self.width})"
    
    def set_side(self, side): # Method to re-set the sides of the rectangle
        self.width = side
        self.height = side
        
# Examples of use:

rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))

# The code returns, as it's supposed:

# 50
# 26
# Rectangle(width=10, height=3)
# **********
# **********
# **********

# 81
# 5.656854249492381
# Square(side=4)
# ****
# ****
# ****
# ****

# 8

## Project dificulty (out of 5): 2,5 
## Time spent: ~2,2 hours
## It passed all the 12 fCC's tests