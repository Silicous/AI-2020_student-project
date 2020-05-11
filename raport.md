# Podprojekt Szi

### Opis

Tematem podprojektu jest rozpoznawanie posiłków.
Użyty jest algorytm genetyczny.

### Dane

Posiłki, ich nazwa oraz rodzaj.



    menu = Context.fromstring(''' |meat|salad|meal|drink|cold|hot |
                       Pork       |  X |     |  X |     |    |  X |
                       Espresso   |    |     |    |  X  |    |  X |
                       Green Tea  |    |     |    |  X  | X  |    |
                       Greek Salad|    |  X  |  X |     | X  |    |
                       Pizza      |    |     |  X |     |    |  X |''')


Za pomocy graphviz możemy narysować grafy z poniższego kodu:  


    digraph Lattice {
	node [label="" shape=circle style=filled width=.25]
	edge [dir=none labeldistance=1.5 minlen=2]
	c0
	c1
	c1 -> c1 [color=transparent headlabel=Pork labelangle=270]
	c1 -> c1 [color=transparent labelangle=90 taillabel=meat]
	c1 -> c0
	c2
	c2 -> c2 [color=transparent headlabel="Green Tea" labelangle=270]
	c2 -> c2 [color=transparent labelangle=90 taillabel=cold]
	c2 -> c0
	c3
	c3 -> c3 [color=transparent headlabel="Greek Salad" labelangle=270]
	c3 -> c3 [color=transparent labelangle=90 taillabel=salad]
	c3 -> c0
	c4
	c4 -> c4 [color=transparent headlabel=Espresso labelangle=270]
	c4 -> c4 [color=transparent labelangle=90 taillabel=drink]
	c4 -> c2
	c5
	c5 -> c1
	c5 -> c3
	c5 -> c4
    }

Dane testowe: 
    func_input = ['meal']

Dane wyjściowe: 

    ['Pork', 'Greek Salad', 'Pizza']


### Implementacja

Główna część:


    gen_num = 20   #generations
    gen_sol = 6     #solutions
    gen_par_mating = 2  #how many solutions we select
    
    mut_per_gen = 10
    mut_num_gen = None
    
    par_selc_type = "tournament"
    crossover = "two_points"
    muta_type = "scramble"
    par_keep = 1 #keep only one parent
    
    init_range_l = -2 #low
    init_range_h = -5 #high
    ...
    

 
### Biblioteki

* concepts
* pygad     (algorytm genetyczny)
* random
* numpy

