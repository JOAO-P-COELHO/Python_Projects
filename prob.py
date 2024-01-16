class Hat:
    def __init__(self, red=0, orange=0, black=0, blue=0, pink=0, striped=0):
        self.red = red
        self.orange = orange
        self.black = black
        self.blue = blue
        self.pink = pink
        self.striped = striped
        self.contents = []
        self.colors = [self.red, self.orange, self.black, self.blue, self.pink, self.striped] 
        self.x = 0
         
        while self.x < self.red:
            self.contents.append("red")
            self.x +=  1
        self.x = 0
    
        while self.x < self.orange:
            self.contents.append("orange")
            self.x += 1
        self.x = 0
        
        while self.x < self.black:
            self.contents.append("black")
            self.x += 1
        self.x = 0
            
    
        while self.x < self.blue:
            self.contents.append("blue")
            self.x += 1
        self.x=0   
        
        while self.x < self.pink:
            self.contents.append("pink")
            self.x += 1
        self.x=0 
            
        while self.x < self.striped:
            self.contents.append("striped")
            self.x += 1
        self.x=0 
    
        print(self.contents)
    
    def draw(balls_taken):
        
        
    

Hat(red=2, orange=1, black=2, blue=1, pink=2, striped=1)
