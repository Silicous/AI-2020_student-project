# Automatyczny kelner


## Krótki opis

Agent porusza się po kracie, przyjmuje zamówienia, zamówienia zanosi do kuchni, czeka na dania, zanosi dania do klientów.


## Technologie:
- Python3
- Drzewa decyzyjne
- Tensorflow with Keras API
- Pandas
- Scikit-learn
- Joblib

## Podprojekty:

### Projekt 1
#### Rozpoznawanie obrazu wykorzystując konwolucyjną sieć neuronową
Podprojekt polegający na użyciu konwolucyjnej sieci neuronowej do rozpoznania ze potrawy ze zdjęcia.

##### Karol Idaszak s444383

### Projekt 2

Podprojekt polegający na użyciu metody drzew decyzyjnych aby otrzymać optymalne ustawienia agenta na podstawie danych z losowo generowanych sytuacji.

Po wciśnięciu '1' i 'F5' program generuje losowe sytuacje z których otrzymuje wyniki na których w pliku decisiontree.py jest tworzone drzewo decyzyjne z najbardziej optymalnymi opcjami dla klienta.

### Projekt 3

Podprojekt polegający na użyciu metody drzew decyzyjnych aby wybrać danie na podstawie zamówienia przez klienta.

Wywołanie podprojektu jest po wciśnięciu '2':

    #Execute project
    if event.key == pygame.K_2:
        temp_order = client_ordering()
        print("Passed: %s. Prediction: %s" % (temp_order, print_leaf(classify(temp_order, tree))))
        
Wtedy w terminalu jest wypisany wynik działania:

    #Example
    Passed: ['salad', 'hot', 'Europe', 'baked', 2, 'order']. Prediction: {'Shrimp and Escarole Salad': '100%'}

##### Serhii Hromov s442778

### Projekt 4

Podprojekt polegający na użyciu metody drzew decyzyjnych, aby stworzyć model, na podstawie którego klient wybierze danie jakie chce zamówić.

#### Piotr Dębski s444362
