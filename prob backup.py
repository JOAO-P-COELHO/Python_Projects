import random

class Hat:
    def __init__(self, red=0, orange=0, black=0, blue=0, pink=0, striped=0, green=0, yellow=0):
        self.red = red
        self.orange = orange
        self.black = black
        self.blue = blue
        self.pink = pink
        self.striped = striped
        self.green = green
        self.yellow = yellow
        self.contents = []
        self.colors = [self.red, self.orange, self.black, self.blue, self.pink, self.striped, self.green, self.yellow] 
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

        while self.x < self.green:
            self.contents.append("green")
            self.x += 1
        self.x=0

        while self.x < self.yellow:
            self.contents.append("yellow")
            self.x += 1
        self.x=0
        
    def draw(self, balls_to_take):
        
        if balls_to_take >= len(self.contents):
            return self.contents
        
        else: 
            taken_balls = []  
            while balls_to_take > 0:
                list_to_remove = self.contents
                print("lista inicial: ", list_to_remove)
                y = random.randint(0, len(self.contents)-1)
                print("posição aleatoria: ", y)
                z = list_to_remove.pop(y)
                taken_balls.append(z)
                print("bola tirada:", z)
                print("lista de bolas tiradas:", taken_balls)
                print("lista inicial, menos as bolas tiradas:", list_to_remove)
                balls_to_take -= 1
            
            return list_to_remove
        
def experiment(hat, expected_balls, num_balls_drawn, num_experiments): 

    hat = hat.draw(num_balls_drawn)
    lista = hat

    dict_to_list = []
    
    list_expected_balls = expected_balls
    for element in list_expected_balls:
        number_reps = list_expected_balls[element]
        while number_reps > 0:
            dict_to_list.append(element)
            number_reps -= 1
    
    verificacao = dict_to_list

    red, orange, black, blue, pink, striped, green, yellow = 'red', 'orange', 'black', 'blue', 'pink', 'striped', 'green', 'yellow'

    count_lista_red, count_verificao_red = lista.count(red), verificacao.count(red)
    count_lista_orange, count_verificao_orange = lista.count(orange), verificacao.count(orange)
    count_lista_black, count_verificao_black = lista.count(black), verificacao.count(black)
    count_lista_blue, count_verificao_blue  = lista.count(blue), verificacao.count(blue)
    count_lista_pink, count_verificao_pink = lista.count(pink), verificacao.count(pink)
    count_lista_striped, count_verificao_striped = lista.count(striped), verificacao.count(striped)
    count_lista_green, count_verificao_green = lista.count(green), verificacao.count(green)
    count_lista_yellow, count_verificao_yellow = lista.count(yellow), verificacao.count(yellow)
    
    m=0
    variable_num_experiments = num_experiments
    while variable_num_experiments > 0:
        print("variable_num_experiments: ", variable_num_experiments)
        
        
        if count_lista_red >= count_verificao_red and count_lista_orange >= count_verificao_orange and count_lista_black >= count_verificao_black and count_lista_blue >= count_verificao_blue and count_lista_pink >= count_verificao_pink and count_lista_striped >= count_verificao_striped and count_lista_green >= count_verificao_green and count_lista_yellow >= count_verificao_yellow  :
            print("m dentro do if: ", m)
            m = m + 1
        variable_num_experiments = variable_num_experiments - 1
    print("m:", m)
    print("num_experiments: ", num_experiments)

    probabilidade = m / num_experiments
    print("probabilidade: ", probabilidade) 
    return probabilidade
        
         

hat_instance = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat_instance, expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=10)

print(probability)
