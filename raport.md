# Podprojekt Szi

### Opis

Tematem podprojektu jest rozpoznawanie zamówień na podstawie historii zamówień.
Użyłem drzew decyzyjnych.

### Dane

Potrawy, ich nazwa, rodzaj oraz charakterystyka.



    menu = Context.fromstring(''' |meat|salad|meal|drink|cold|hot |
                       Pork       |  X |     |    |     |    |  X |
                       Espresso   |    |     |    |  X  |    |  X |
                       Latte      |    |     |    |  X  |    |  X |
                       Green Tea  |    |     |    |  X  | X  |    |
                       Greek Salad|    |  X  |    |     | X  |    |
                       Pizza      |    |     |  X |     |    |  X |''')




Dane uczące:
    
    training_data = [
        ['meat','hot','Pork'],
        ['salad','cold','Greek Salad'],
        ['drink','hot','Espresso'],
        ['drink','hot','Latte'],
        ['drink','cold','Green Tea'],
        ['meal','hot','Pizza'],
        ['meal','cold','Wheat Pita'],
    ]



Dane testowe jest tworzone losowo w funkcji:  
 
    def client_ordering():
        order = []

        dish = uniq_val_from_data(training_data, 0)
        temperature = uniq_val_from_data(training_data, 1)

        tmpr = random.sample(dish, 1)
        order.append(tmpr[0])

        tmpr = random.sample(temperature, 1)
        order.append(tmpr[0])
        order.append('order')
        return order
   




### Implementacja

####Drzewo:

Klasy: 

#####Question
    class Queestion:
        def __init__(self, col, value):
            self.col = col      #column
            self.value = value  #value of column
     
        def compare(self, example):
        #compare val in example with val in the question
            
        def __repr__(self):
        #just to print
        
#####Node
    class Decision_Node():
    #contain the question and child nodes
    def __init__(self, quest, t_branch, f_branch):
        self.quest = quest
        self.t_branch = t_branch
        self.f_branch = f_branch
        
#####Leaf
    class Leaf:
    #contain a number of how many times the label has appeared in dataset
    def __init__(self, rows):
        self.predicts = uniq_count(rows)

 
### Biblioteki

* concepts
* random
* numpy

