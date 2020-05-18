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
    ]



Dane testowe: 
    test_data = [
        ['meat','hot','Latte'],
        ['salad','hot','Greek Salad'],
        ['drink','hot','Pork'],
        ['drink','cold','Green Tea'],
        ['drink','hot','Greek Salad'],
    ]




### Implementacja

Główna część:

    In process

    ...
    

 
### Biblioteki

* concepts
* random
* numpy

