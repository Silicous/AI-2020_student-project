
# Raport Planowanie Ruchu

### Definicja pętli głównej strategii przeszukiwania
    def astar(self):
        print("finding path to", self.goal)
        fringe = PriorityQueue()
        explored = []
        start = Node((self.x, self.y, self.dir), False, False)
        fringe.put((1, start)) 
Utworzenie kolejki fringe, listy przebytych Node oraz dodanie do kolejki poczatkowego Node.

        while True:
            if fringe.empty():
                return False
            elem = fringe.get()[1]
Jeśli kolejka jest pusta, zwraca False jako wystąpienie błędu.
W innym przypadku pobiera pierwszy element z kolejki fringe.

            if self.goaltest(elem.state):
                self.path = []
                while elem.action is not False:
                    self.path.insert(0, elem.action)
                    elem = elem.parent
                print(self.path)
                return True
Jeśli pobrany element jest celem to za pomocą dodanych pól parent i action tworzona jest lista ruchów do wykonania przez agenta.

            explored.append(elem.state)
            for (akcja, stan) in self.succ(elem.state):
                x = Node(stan, elem, akcja)
                p = self.f(x)
W innym przypadku element ten jest dodany do listy przebytych i otrzymane są jego następniki. 
              
                if not(stan in fringe.queue) and not(stan in explored):
                    fringe.put((p, x))
                elif (stan in fringe.queue):
                    fringe.queue.remove(elem)
                    fringe.put((p, x))
Jeśli następnik będący stanem nie był wcześniej dodany do kolejki to zostaje dodany teraz, jeśli był to jego priorytet jest aktualizowany jeśli jest niższy od wcześniejszego.

### Definicja funkcji następnika
	def succ(self, state):		        
	    s = []
        r = state[2] - 1
        if r == 0: 
            r = 4
        s.append((("rotate", "right"), (state[0], state[1], r)))

        l = state[2] + 1
        if l == 5:
            l = 1
        s.append((("rotate", "left"), (state[0], state[1], l)))
        if self.canWalk(state):
            if state[2] == 1:
                w = state[1] - 1
                s.append((("walk"), (state[0], w, state[2])))
            elif state[2] == 2:
                w = state[0] - 1
                s.append((("walk"), (w, state[1], state[2])))
            elif state[2] == 3:
                w = state[1] + 1
                s.append((("walk"), (state[0], w, state[2])))
            elif state[2] == 4:
                w = state[0] + 1
                s.append((("walk"), (w, state[1], state[2])))
        return s
        
Funkcja następnika zwraca stany otrzymane poprzez obrót w prawo i lewo, oraz jeśli to możliwe to ruch do przodu.

### Definicja przyjętej heurystyki
    def f(self, node):
        cost = restaurant.tiles[self.goal[1]][self.goal[0]].cost
        return heuristic((node.state[0], node.state[1]), self.goal) + cost
       
   Przyjęta heurystyka zwraca dystans pomiędzy dwoma punktami w linii prostej do którego jest dodany koszt pola, gdzie pole ma koszt 1 dla zwykłego i koszt 5 dla pola z kałużą.