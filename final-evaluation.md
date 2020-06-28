# Automatyczny kelner


## Krótki opis

Agent porusza się po kracie, przyjmuje zamówienia

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

### Projekt 3

Podprojekt polegający na użyciu metody drzew decyzyjnych aby wybrać danie na podstawie zamówienia przez klienta.

Wywołanie podprojektu jest po wciśnięciu '2':

    #Execute project
    if event.key == pygame.K_2:
        print("Passed: %s. Prediction: %s" % (client_ordering(), print_leaf(classify(client_ordering(),tree))))

##### Serhii Hromov s442778

### Projekt 4

Podprojekt polegający na użyciu metody drzew decyzyjnych, aby stworzyć model, na podstawie którego klient wybierze danie jakie chce zamówić.

#### Piotr Dębski s444362
