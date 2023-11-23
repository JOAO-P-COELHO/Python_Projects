class Animal:
    propriedade1 = {"key_1": "value 1", "key_2": "value2"} # Uma propriedade que é um dictionary/object
    propriedade2 = ["valor1", "valor2", "valor3"] # Uma propriedade que é uma list/array
    _private_property = "Com um underscore antes do nome da variável, estamos a indicar que esta é uma propriedade privada e não deve ser acedida fora da classe"
    
    def remove_name(self,name): # Isto é 1 método dentro de 1 class, q na prática = a uma função dentro de uma class. O "self" é um argumento obrigatório, é como se fosse um "this" em JavaScript
        self.propriedade2.remove(name)# Uso o "self" precisamente para aceder a propriedades dentro da própria classe. Neste caso aceso a "propriedade2" e removo um elemento com o valor atribuido a name.
        return self.propriedade2 # Devolvo a nova propriedade, a "propriedade2", com um return, e esta é atualizada
    
    def add_name(self, name): 
        self.propriedade2.append(name) # Mesmo método, mas adiciona elementos
        return self.propriedade2
    
animal = Animal() # Ativação da class
print(animal.propriedade1["key_2"]) # Neste caso chamo o "key_2" com aspas porque isto é um objeto (não tem índices, logo, não tem números-indice)
print(animal.propriedade2[1]) # Aqui já posso chamar um elemento da lista com números porque é uma lista, e cada elemento tem um índice

print(Animal.propriedade2) # Outra forma de aceder à classe, deste modo, diretamente, sem instanciar a class (já que estamos a aceder diretamente a ela)

animal.remove_name("valor2") # Chamo a propriedade "remove_name" do "animal", que neste caso é um método e passo-lhe o argumento "valor2", que será o valor de name
print(animal.propriedade2) # Verifico que a class foi editada e o valor da propriedade2 foi atualizado, já que foi removido o "valor2"
# animal.remove_name("key_1") # Eu não consigo remover coisas da propriedade1, porque este é um dict e o método remove não funciona em dict

animal.add_name("valor4") # Mesmo raciocínio, mas neste caso estou a acrescentar e não a remover - faço isto recorrendo ao método "add_name", dentro da class Animal (instancianda como "animal")
print(animal.propriedade2)

