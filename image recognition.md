## Rozpoznawanie obrazu wykorzystująć konwolucyjną sieć neuronową

## Opis
Konwolucyjna sieć neuronowa wyuczona na 10000 zdjęć o wymiarze 64x64x3 służąca do rozpoznawania zdjeć dań.
## Dane
Rodzaje dań dostępnych do zamówienia
```
CATEGORIES = [
"apple_pie",
"club_sandwich",
"greek_salad",
"hamburger",
"hot_dog",
"ice_cream",
"lasagna",
"pizza",
"steak",
"waffles"
]
```
## Implementacja
Zostaje wybrane losowo zdjęcie, następnie na podstawie wyuczonego modelu sieci neuronowej następuje rozpoznanie potrawy. Jeśli potrawa jest tą którą zamówił klient następuje przerwanie pętli.
```
def image_recognition():
    for _ in range(100):
        photo = random.choice(menu)
        prediction = model.predict(np.expand_dims(photo[0], axis=0))
        max_value = prediction[0].max()
        idx = np.where(prediction[0]==max_value)
        if CATEGORIES[idx[0][0]] == waiter.order_list[-1]:
            break
        waiter.order_list.pop()
```
