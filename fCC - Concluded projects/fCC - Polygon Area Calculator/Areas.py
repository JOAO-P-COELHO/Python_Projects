class Rectangle:
   
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def __str__(self): # PERCEBER O QUE É ISTO DO MÉTODO _STR_ JÁ É A SEGUNDA VEZ QUE APARECE NO FCC!
        return f"Rectangle(width={self.width}, height={self.height})"
    
    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height
    
    def get_area(self):  # Returns area (width * height)
        area = self.width * self.height
        return area
    
    def get_perimeter(self): # Returns perimeter (2 * width + 2 * height)
        perimeter = 2 * (self.width) + 2 * (self.height)
        return perimeter
    
    def get_diagonal(self): # Returns diagonal ((width ** 2 + height ** 2) ** .5)
        diagonal = (self.width ** 2 + self.height ** 2) ** .5
        return diagonal
    
    def get_picture(self):
        if self.width>50 or self.height>50:
            return "Too big for picture."
        else:
            n = 0
            result = []
            while n<self.height:
                asteriks = "*"  
                result.append(self.width * asteriks)
                n = n + 1

                if n==self.height:
                    final = "\n".join(map(str,result))
                    return f"{final}\n"
 
    def get_amount_inside(self, shape):
        
        if shape.width > self.width or shape.height > self.height:
            return 0
        
        elif shape.width <= self.width and shape.height > self.height:
            first_p = int(self.width / shape.width)
            return first_p
        
        elif shape.height <= self.height and shape.height > self.height:
            second_p = int(self.height / shape.height)
            return second_p
        
        elif shape.width <= self.width and shape.height <= self.height:
            first_p = int(self.width / shape.width)
            second_p = int(self.height / shape.height)
            return first_p * second_p
            
class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side
    
    def __str__(self):
        return f"Square(side={self.width})"
    
    def set_side(self, side):
        self.width = side
        self.height = side