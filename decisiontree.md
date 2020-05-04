# Podprojekt
Podprojekt polegający na użyciu metody drzew decyzyjnych aby otrzymać optymalne ustawienia agenta na podstawie danych z losowo generowanych sytuacji.
# Implementacja
Agent po obsłużeniu wszystkich klientów zapisuje jakie ustawienia używał oraz czy całkowity czas działania jest większy od pożądanego.

#####
    if restaurant.left ==  0:
	    file.write(str(S_IDLE.index(IDLE)))
	    file.write(str(S_FIRST.index(FIRST)))
	    if totaltime >  1076:
	    file.write(str(0))
	    else:
	    file.write(str(1))
Pożądany czas działania w obecnym zestawie wielkości planszy i ilości klientów ustawiłem na 1076j na podstawie średniego czasu wszystkich ustawień. Agent czasami błędnie wykonuje zadania więc po upływie 1500j plansza jest resetowana.

    if ticks >  1500:
		restaurant = Restaurant(3,  5)
		waiter = Agent(2,2)
		..

Ustawienia agenta to decyzja gdzie stać gdy nie ma zadania (kuchnia, środek planszy, stać w miejscu) oraz czy najpierw obsłużyć klientów chcących zamówić czy klientów czekających na gotowe zamówienie.
#####
    S_IDLE =  ("kitchen",  "middle",  "inplace")
    S_FIRST =  ("order",  "food")
    

# Dane
Po uruchomieniu programu tworzony jest plik results.csv zawierający sformatowane dane wynikowe.

    idle,first,good
	0,1,0
	0,0,1
	2,0,1
	..
# Drzewo decyzyjne
Do utworzenia drzewa decyzyjnego użyłem biblioteki sklearn oraz graphviz do zobrazowania wyniku.

    #decisiontree.py
    col_names =  ['idle','first','good']
	data = pd.read_csv("results.csv", header=None, names=col_names)
	data = data.iloc[1:]
	data.head()
	feature_cols =  ['idle','first']
	X = data[feature_cols]
	y = data.good
Plik results.csv jest ładowany, jako klasę główną ustawiłem .good, czyli czy czas wykonania zadania był zadowalający.

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=1)
    clf = DecisionTreeClassifier(criterion="gini", max_depth=4)
    clf = clf.fit(X_train,y_train)
Dane są dzielone na 25% do testowania a następnie tworzone i trenowane jest drzewo o głębokości 4.
Na końcu drzewo jest wizualizowane za pomocą grafu.![](https://i.imgur.com/2lWRH0w.png)
Z grafu można odczytać że na podstawie 909 wyników dla obecnych ustawień planszy i agenta najlepszymi ustawieniami są idle == 2 i w równej mierze first == 0 i first == 1, czyli ustawienia 

    IDLE = "inplace"
    FIRST = "order"   
    ---
    IDLE = "inplace"
    FIRST = "food"
