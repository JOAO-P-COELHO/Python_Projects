import random
import copy

class Hat:
    def __init__(self, red=0, orange=0, black=0, blue=0, pink=0, striped=0, green=0, yellow=0, test=0):
        
        self.contents = []
        self.colors_string = ['red', 'orange', 'black', 'blue', 'pink', 'striped', 'green', 'yellow', 'test']
        self.colors_nr = [red, orange, black, blue, pink, striped, green, yellow, test]

        for color, count in zip(self.colors_string, self.colors_nr): # For each color (as a string) [namely, color] and for each number associated [namely, count] in a zip do: "x". A zip object it's the result of the pairing of lists/other tuples. Example of the structure of a zip x: x= ((color1, number_of_times_color_1), (color2, number_of_times_color_2)) - to be readable, the tuple() function has to be called on the object, like this: tuple(x)
            self.contents.extend([color] * count) # The extend method is responsible for adding the specific element to the end of the list that is being extended
    
            
    def draw(self, balls_to_take, nr_experiments=1):
        initial_list_of_balls = copy.copy(self.contents)
        taken_balls = []  
        
        if nr_experiments==1:
            if balls_to_take >= len(initial_list_of_balls):
                return initial_list_of_balls
            
            else: 
                while balls_to_take > 0:
                    
                    y = random.randint(0, len(self.contents)-1)
                    z = self.contents.pop(y)
                    taken_balls.append(z)
                    balls_to_take -= 1

                copy_initial_list_of_balls = copy.copy(self.contents)
            return taken_balls    
            
            
        else:        
            if balls_to_take >= len(initial_list_of_balls):
                return initial_list_of_balls
            
            else: 
                copy_initial_list_of_balls = copy.copy(self.contents)
                while balls_to_take > 0:
                    y = random.randint(0, len(copy_initial_list_of_balls)-1)

                    z = copy_initial_list_of_balls.pop(y)
                    taken_balls.append(z)
                    balls_to_take -= 1

                copy_initial_list_of_balls = copy.copy(self.contents)
        
            return taken_balls
    
        
def experiment(hat, expected_balls, num_balls_drawn, num_experiments): 

    dict_to_list = [] # Dictionary where the expected balls are stored
    list_expected_balls = expected_balls
    for element in list_expected_balls:
        number_reps = list_expected_balls[element]
        while number_reps > 0:
            dict_to_list.append(element)
            number_reps -= 1   

    m=0
    variable_num_experiments = num_experiments
    
    while variable_num_experiments > 0:

        lista = hat.draw(num_balls_drawn, num_experiments) # A cada repetição (condicionada pelo valor de variable_num_experiments) vai buscar o método à instância hat, que devolve uma lista. 
        verificacao = dict_to_list

        red, orange, black, blue, pink, striped, green, yellow = 'red', 'orange', 'black', 'blue', 'pink', 'striped', 'green', 'yellow'
        test = 'test'

        count_lista_red, count_verificao_red = lista.count(red), verificacao.count(red)
        count_lista_orange, count_verificao_orange = lista.count(orange), verificacao.count(orange)
        count_lista_black, count_verificao_black = lista.count(black), verificacao.count(black)
        count_lista_blue, count_verificao_blue  = lista.count(blue), verificacao.count(blue)
        count_lista_pink, count_verificao_pink = lista.count(pink), verificacao.count(pink)
        count_lista_striped, count_verificao_striped = lista.count(striped), verificacao.count(striped)  
        count_lista_green, count_verificao_green = lista.count(green), verificacao.count(green)
        count_lista_yellow, count_verificao_yellow = lista.count(yellow), verificacao.count(yellow)
        count_lista_test, count_verificao_test = lista.count(test), verificacao.count(test)
  
        if count_lista_red >= count_verificao_red and count_lista_orange >= count_verificao_orange and count_lista_black >= count_verificao_black and count_lista_blue >= count_verificao_blue and count_lista_pink >= count_verificao_pink and count_lista_striped >= count_verificao_striped and count_lista_green >= count_verificao_green and count_lista_yellow >= count_verificao_yellow and count_lista_test >= count_verificao_test:
            m = m + 1

        variable_num_experiments = variable_num_experiments - 1

    probabilidade = m / num_experiments
    print("probabilidade: ", probabilidade) 
    return probabilidade
        
# Testes
 
# hat = Hat(blue=2,red=2, green=2)
# probability = experiment(hat=hat,
#                   expected_balls={"blue":2,"green":1},
#                   num_balls_drawn=3,
#                   num_experiments=1000)


hat = Hat(blue=3,red=2,green=6)
probability = experiment(hat=hat,
                  expected_balls={"blue":2,"green":1},
                  num_balls_drawn=4,
                  num_experiments=1000)

# hat = Hat(yellow=5,red=1,green=3,blue=9,test=1)
# probability = experiment(hat=hat,
#                   expected_balls={"yellow":2,"blue":3,"test":1},
#                   num_balls_drawn=20,
#                   num_experiments=100)

# hat = Hat(red=2,blue=2)
# hat.draw(2)