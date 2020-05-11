#Podprojekt Szi

###Opis

Tematem podprojektu jest rozpoznawanie posiłków.
Użyty jest algorytm genetyczny.

###Dane

Posiłki, ich nazwa oraz rodzaj.

#####

    menu = Context.fromstring(''' |meat|salad|meal|drink|cold|hot |
                       Pork       |  X |     |  X |     |    |  X |
                       Espresso   |    |     |    |  X  |    |  X |
                       Green Tea  |    |     |    |  X  | X  |    |
                       Greek Salad|    |  X  |  X |     | X  |    |
                       Pizza      |    |     |  X |     |    |  X |''')



###Implementacja

Główna część:
#####

    gen_num = 20    #generations
    gen_sol = 6     #solutions
    gen_par_mating = 2  #how many solutions we select
    
    mut_per_gen = 10
    mut_num_gen = None
    
    crossover = "two_points"
    muta_type = "scramble"
    par_keep = 1 #keep only one parent
    
    init_range_l = -2 #low
    init_range_h = -5 #high
    ...
    
 
###Biblioteki

* concepts
* pygad     (algorytm genetyczny)
* random
* numpy

