Piotr Jakub Dębski 																																						01.06.2020


## Automatyczny kelner: raport podprojektu indywidualnego

	W tym dokumencie opisane zostały podstawy i najważniejsze informacje dotyczące powstania 
	oraz funkcjonowania podprojektu indywidualnego.

### Cel projektu

	Celem projektu jest dodanie do projektu Zautomatyzowanego Kelnera sztucznej inteligencji u 
	klientów restauracji, która na podstawie kilku przypisanych do obiektu klienta cech pozwoli mu 
	na samodzielne wybranie zamówionego dania oraz napoju. Osobny moduł będzie miał za zadanie 
	stworzyć modele drzewa decyzyjnego, które będą używane w głownym pliku projektu.

### Biblioteki

	Do wykonania projektu wykorzystane zostały następujące biblioteki Pythona:
	 - random
	 - joblib
	 - pandas
	 - sklearn
	 - pydot
	oraz dodatkowo:
	 - graphviz
	za pomocą którego wygenerowane została reprezentacja wizualna drzew decyzyjnych 
	food_tree.pdf oraz drink_tree.pdf znajdujących się w folderze graphs.
		 
### Dane

	Dane na których podstawie algorytm ma stworzyć modele drzew decyzyjnych umieszczone zostały w
	pliku learning_db.py i podzielone na 6 binarnych kategorii:
		- gender - płeć ( M - mężczyzna  K - kobieta )
		- age - wiek ( Adult - dorosły  Child - dziecko )
		- outfit - ubiór ( Casual - codzienny  Elegant - reprezentacyjny )
		- cash - pieniądze ( "+" - dużo  "-" - mało )
		- vege - dieta wegetariańska ( "Yes" "No" )
		- time - czas ( "Afternoon" - popołudnie  "Evening" - wieczór )
	oraz na 2 kategorie, które mają zostać sklasyfikowane :
	 - food - dania ( 35 wyborów )
	 - drink - napoje ( 8 wyborów )
	Dane zawierają 200 przykładów.
	
### Tworzenie drzewa

	1. Za pomocą funkcji pandas.DataFrame() program łączy ze sobą wszystkie przykłady w 
	dwuwymiarową strukturę danych o wymiarach 9x200 (kategorie+index)x(przykłady).
	2. Za pomocą funkcji pandas.factorize() program dostosowuje dane w każdej kolumnie do naszych
	potrzeb i obliczeń.
	3. Następnie model danych zostaje podzielony na X - zbiór przykładów oraz y - odpowiadający 
	przykładom wynik czyli rodzaj dania.
	4. Zestaw danych zostaje podzielony na testowy dzięki funkcji train_test_split()
	( 25% - food , 40% - drink) i treningowy ( 75% - food , 60% - drink )
	5. Dzięki funkcji DecisionTreeClassifier() oraz tą samą funkcją z argumentem wymagającym przyjęcia 
	do kryterium entropii tworzą się dwa klasyfikatory (wyniki będą porównywane by wybrać 
	dokładniejszą metodę)
	6. Zestaw treningowy przekazany zostaje do funkcji fit() dzięki czemu można teraz 
	przeprowadzić predykcję za pomocą funkcji predict(), której w miejsce argumentu wprowadzamy 
	zestaw testowy.
	7. W wyniku wielokrotnych porównań dokładności funkcji predict() na klasyfikatorach, entropia 
	okazuje się lepszym kryterium od indeksu Giniego na zadanym zestawie danych, więc model drzewa
	korzystający z tego kryterium zostaje zapisany do użycia w głównym ciele projektu.
	8. Kroki 3-7 zostały powtórzone dla drzewa napojów, a odpowiednie wizualizacje drzew decyzyjnych
	zapisane są w folderze graphs.
	
### Synchronizacja w projekcie

	Modele food_model i drink_model zostaną załadowane do programu z folderu models.
	Do obsługi stworzonego modelu stworzona jest klasa Client oraz funkcja client_ordering(ctr) 
	Klasa Client poprzez swój konstruktor automatycznie losuje wszystkie cechy, na podstawie
	których funkcja predict() wybiera danie oraz napój, natomiast funkcja client_ordering(ctr) wymaga
	w swoim argumencie posiadania obiektu klasy Client, z której pobierze wszystkie wartości cech 
	i przeniesie je do funkcji predict() zwracając otrzymane wyniki. 
