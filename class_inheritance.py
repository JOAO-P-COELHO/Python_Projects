class Animal: # É estabelecida a class "parent"
    # cor_pelo:"Cinzento" # Não precisamos disto porque lá em baixo temos "self.cor_pelo=cor_pelo", logo, já atribui a minha cor_pelo
    
    def eat(self): # Usa-se sempre um self nos argumentos dos métodos
        print("Ele come salmão")
    
    def speak(self):
        print("Ele fala")
        
    def chase (self, animal="bicho"):
        print(f"Ele persegue {animal}") # Neste caso, além dos argumentos dos métodos, usa-se o próprio argumento "required positional argument"
    
    def __init__(self,cor_pelo): # Com este método(dunder method, dado como __innit__ (são dois underscore)), a primeira coisa a ser iniciada é este método. Neste caso ele inicia com o argumento "Azul", pus lá em baixo
        print("A cor é", cor_pelo)
        self.cor_pelo=cor_pelo # Isto permite-nos então usar cor_pelo em qualquer outro método porque com o a atribuição .self estabeleci que o argumento "cor_pelo" passa a ser propriedade desta classe (e pode ser usado até noutras  "extended" classes)
        
    def get_cor_pelo(self):
        print("A cor desta segunda vez é: ", self.cor_pelo)
        

class Elefante(Animal): # Extende-se a class anterior, Animal, numa outra classe "Elefante"
    def speak(self):
        print ("Ele usa a tromba")
    
    def eat(self):
        super().eat() # Para conseguir usar os dois métodos eat e ter os dois print, sem fazer overwriting, tenho de usa a função super(), esta vai à class "parent" e usa o método .eat lá, que depois resulta num print "Ele come salmão"
        print("E ele come também feijão") # Continuando a leitura do código e após o print "Ele come salmão", ele faz print "E ele também come feijão"
    
    def chase (self, animal): # Aqui vai-se utilizar um "required positional argument", além do próprio "self" obrigatório
        super().chase(animal) # Volta-se a usar o super() que vai chamar, neste caso, o método .chase, mas ao parent, onde é fornecido também um argumento que o método lá dentro do parent) pede. É feito o print "Ele persegue {animal}"
        print ("E ele captura", animal) # # Continuando a leitura do código e após o print "Ele persegue {animal}", ele faz print "E ele captura {animal}"
        
    def __innit_(self, cor_pelo_):
        super().__init__(cor_pelo)
    
elefante = Elefante("Azul")
elefante.eat()
elefante.chase("ave")
elefante.get_cor_pelo()

