# get out unique value from each column (dish, temperature or label)
def uniq_val_from_data(rows, col):
    return set([row[col] for row in rows])


# format to print a tree and something more
tree_format = ["dish", "served", "origin", "cooked", "ingredients", "name"]

# course
'''
dish -  (salad/meal/coffee/tea/non-alcho drink)
served - (cold/hot/warm)
origin - (Worldwide/America/Europe/Asia)
cooked - (baked/boiled/mixed)
ingridients - (2/4)
'''

training_data = [

    ['salad', 'warm',  'Europe', 'mixed', 4, 'Cappon magro'],
    ['salad', 'hot',  'Europe', 'mixed', 4, 'Panzanella'],
    ['salad', 'cold',  'Europe', 'mixed', 4, 'Greek Salad'],

    ['salad', 'warm',  'Worldwide', 'mixed', 4, 'Jello salad'],
    ['salad', 'cold',  'Worldwide', 'mixed', 4, 'Macaroni salad'],
    ['salad', 'hot',  'Worldwide', 'mixed', 4, 'Fruit salad'],

    ['salad', 'cold',  'America', 'mixed', 4, 'Ambrosia Salad'],
    ['salad', 'warm', 'America', 'mixed', 4, 'Crab Louie'],
    ['salad', 'hot', 'America', 'mixed', 4, 'Taco salad'],

    ['salad', 'warm',  'Asia', 'mixed', 4, 'Singju'],
    ['salad', 'cold',  'Asia', 'mixed', 4, 'Rojak'],
    ['salad', 'hot',  'Asia', 'mixed', 4, 'Shirazi salad'],

['salad', 'warm',  'Europe', 'mixed', 2, 'Urnebes'],
    ['salad', 'hot',  'Europe', 'mixed', 2, 'Shopska salad'],
    ['salad', 'cold', 'Europe', 'mixed', 2, 'Wurstsalat'],

    ['salad', 'warm',  'Worldwide', 'mixed', 2, 'Garden Salad'],
    ['salad', 'cold',  'Worldwide', 'mixed', 2, 'Mesclun'],
    ['salad', 'hot',  'Worldwide', 'mixed', 2, 'Egg salad'],

    ['salad', 'cold',  'America', 'mixed', 2, 'Watergate salad'],
    ['salad', 'warm',  'America', 'mixed', 2, 'Michigan salad'],
    ['salad', 'hot', 'America', 'mixed', 2, ''],

    ['salad', 'warm',  'Asia', 'mixed', 2, 'Yam thua phu'],
    ['salad', 'cold',  'Asia', 'mixed', 2, 'Som tam'],
    ['salad', 'hot',  'Asia', 'mixed', 2, 'Yam pla duk fu'],

['salad', 'warm', 'Europe', 'baked', 4, 'Roasted Pepper Panzanella'],
    ['salad', 'hot', 'Europe', 'baked', 4, 'Walnut Salad with Fried Eggs'],
    ['salad', 'cold', 'Europe', 'baked', 4, 'Frisée and Wild Mushroom Salad with Poached Egg'],

    ['salad', 'warm',  'Worldwide', 'baked', 4, 'Grilled Mushrooms and Carrots with Sesame'],
    ['salad', 'cold', 'Worldwide', 'baked', 4, 'Coleslaw'],
    ['salad', 'hot',  'Worldwide', 'baked', 4, 'Smashed Potato Salad'],

    ['salad', 'cold',  'America', 'baked', 4, 'Wintery Beetroot and Lentil Salad'],
    ['salad', 'warm',  'America', 'baked', 4, 'Cookie salad'],
    ['salad', 'hot',  'America', 'baked', 4, 'Curtido'],

    ['salad', 'warm', 'Asia', 'baked', 4, 'Urap'],
    ['salad', 'cold',  'Asia', 'baked', 4, 'Quinoa Salad'],
    ['salad', 'hot',  'Asia', 'baked', 4, 'Kosambari'],

['salad', 'warm',  'Europe', 'baked', 2, 'Wilted Escarole Salad'],
    ['salad', 'hot',  'Europe', 'baked', 2, 'Shrimp and Escarole Salad'],
    ['salad', 'cold',  'Europe', 'baked', 2, 'Cappon magro'],

    ['salad', 'warm',  'Worldwide', 'baked', 2, 'Carrot Salad'],
    ['salad', 'cold',  'Worldwide', 'baked', 2, 'Smashed Potato Salad'],
    ['salad', 'hot', 'Worldwide', 'baked', 2, 'Bistro Salad with Roasted Vegetables'],

    ['salad', 'cold', 'America', 'baked', 2, 'Charred Romanesco with Anchovies and Mint'],
    ['salad', 'warm',  'America', 'baked', 2, 'Warm Cauliflower and Herbed Barley Salad'],
    ['salad', 'hot',  'America', 'baked', 2, 'Steak Salad with Horseradish Dressing'],

    ['salad', 'warm',  'Asia', 'baked', 2, 'Steak Salad with Horseradish Dressing'],
    ['salad', 'cold',  'Asia', 'baked', 2, 'Green papaya salad'],
    ['salad', 'hot',  'Asia', 'baked', 2, 'Grilled Sesame Shrimp with Herb Salad'],

['coffee', 'hot',  'Worldwide', 'boiled', 2, 'Espresso'],
    ['coffee', 'warm',  'Worldwide', 'boiled', 2, 'Latte'],
    ['coffee', 'cold',  'Worldwide', 'boiled', 2, 'Cappuccino'],

    ['coffee', 'hot', 'Europe', 'boiled', 2, 'Affogato'],
    ['coffee', 'warm',  'Europe', 'boiled', 2, 'Botz'],
    ['coffee', 'cold',  'Europe', 'boiled', 2, 'Affogato'],

    ['coffee', 'hot',  'America', 'boiled', 2, 'Café de olla'],
    ['coffee', 'warm',  'America', 'boiled', 2, 'Double Double Coffee'],
    ['coffee', 'cold',  'America', 'boiled', 2, 'Pocillo'],

    ['coffee', 'hot',  'Asia', 'boiled', 2, 'Melya'],
    ['coffee', 'warm', 'Asia', 'boiled', 2, 'borgia'],
    ['coffee', 'cold',  'Asia', 'boiled', 2, 'Kaapi'],

['coffee', 'hot',  'Worldwide', 'mixed', 2, 'Nescafé'],
    ['coffee', 'warm',  'Worldwide', 'mixed', 2, 'Moccona'],
    ['coffee', 'cold', 'Worldwide', 'mixed', 2, 'Kenco'],

    ['coffee', 'hot',  'Europe', 'mixed', 2, 'Frappé'],
    ['coffee', 'warm',  'Europe', 'mixed', 2, 'Marocchino'],
    ['coffee', 'cold',  'Europe', 'mixed', 2, 'Shakerato'],

    ['coffee', 'hot',  'America', 'mixed', 2, 'Mazagran'],
    ['coffee', 'warm',  'America', 'mixed', 2, 'Medici'],
    ['coffee', 'cold',  'America', 'mixed', 2, 'Palazzo'],

    ['coffee', 'hot', 'Asia', 'mixed', 2, 'Qishr.'],
    ['coffee', 'warm', 'Asia', 'mixed', 2, 'Egg Coffee'],
    ['coffee', 'cold', 'Asia', 'mixed', 2, 'Yuanyang'],

['tea', 'warm', 'Asia', 'boiled', 2, 'Bubble Tea'],
    ['tea', 'hot',  'Asia', 'boiled', 2, 'White Tea'],
    ['tea', 'cold',  'Asia', 'boiled', 2, 'Pu Erh'],

['tea', 'warm', 'Asia', 'boiled', 4, 'Hong Kong-Style Milk Tea'],
    ['tea', 'hot',  'Asia', 'boiled', 4, 'Darjeeling'],
    ['tea', 'cold',  'Asia', 'boiled', 4, 'Butter Tea'],

    ['tea', 'warm',  'Europe', 'boiled', 2, 'Earl Grey'],
    ['tea', 'hot',  'Europe', 'boiled', 2, 'Wild Lily Tea'],
    ['tea', 'cold',  'Europe', 'boiled', 2, 'Chamomilla Bohemica'],

    ['tea', 'warm',  'America', 'boiled', 2, 'Argo Tea'],
    ['tea', 'hot',  'America', 'boiled', 2, 'Bigelow Tea'],
    ['tea', 'cold',  'America', 'boiled', 2, 'American Tea'],

    ['tea', 'warm',  'Worldwide', 'boiled', 2, 'Yellow tea'],
    ['tea', 'hot',  'Worldwide', 'boiled', 2, 'Mulberry black tea'],
    ['tea', 'cold',  'Worldwide', 'boiled', 2, 'Chai'],

['non-alcho drink', 'warm',  'Worldwide', 'mixed', 2, 'Lager'],
    ['non-alcho drink', 'hot',  'Worldwide', 'mixed', 2, 'Chocoart'],
    ['non-alcho drink', 'cold', 'Worldwide', 'mixed', 2, 'Pucko'],

    ['non-alcho drink', 'warm', 'Europe', 'mixed', 2, 'Pinolillo'],
    ['non-alcho drink', 'hot', 'Europe', 'mixed', 2, 'Pópo'],
    ['non-alcho drink', 'cold', 'Europe', 'mixed', 2, 'Pozol'],

    ['non-alcho drink', 'warm',  'Asia', 'mixed', 2, 'Milo'],
    ['non-alcho drink', 'hot',  'Asia', 'mixed', 2, 'Tejate'],
    ['non-alcho drink', 'cold',  'Asia', 'mixed', 2, 'Soju'],

    ['non-alcho drink', 'warm',  'America', 'mixed', 2, 'Xicolatada'],
    ['non-alcho drink', 'hot',  'America', 'mixed', 2, 'Swiss Miss'],
    ['non-alcho drink', 'cold',  'America', 'mixed', 2, 'Mate'],

    ['non-alcho drink', 'warm',  'Worldwide', 'boiled', 2, 'Barley water'],
    ['non-alcho drink', 'hot',  'Worldwide', 'boiled', 2, 'Egg cream'],
    ['non-alcho drink', 'cold', 'Worldwide', 'boiled', 2, 'Mulled apple juice'],

    ['non-alcho drink', 'warm',  'Europe', 'boiled', 2, 'Cola Cao'],
    ['non-alcho drink', 'hot',  'Europe', 'boiled', 2, 'Kókómjólk'],
    ['non-alcho drink', 'cold',  'Europe', 'boiled', 2, 'Tascalate'],

    ['non-alcho drink', 'warm',  'Asia', 'boiled', 2, 'Choc-Ola'],
    ['non-alcho drink', 'hot',  'Asia', 'boiled', 2, 'Akta-Vite'],
    ['non-alcho drink', 'cold',  'Asia', 'boiled', 2, 'Banania'],

    ['non-alcho drink', 'warm',  'America', 'boiled', 2, 'Caipirinha'],
    ['non-alcho drink', 'hot', 'America', 'boiled', 2, 'Pisco sour'],
    ['non-alcho drink', 'cold', 'America', 'boiled', 2, 'Rum swizzle'],

['meal', 'warm',  'Worldwide', 'mixed', 2, 'Lasagna'],
    ['meal', 'hot',  'Worldwide', 'mixed', 2, 'Chicken Pot Pie'],
    ['meal', 'cold',  'Worldwide', 'mixed', 2, 'Smothered Pork Chops'],

    ['meal', 'warm',  'Europe', 'mixed', 2, 'Gumbo'],
    ['meal', 'hot',  'Europe', 'mixed', 2, 'Chicken Tortilla Soup'],
    ['meal', 'cold',  'Europe', 'mixed', 2, 'Potato Pinwheels'],

    ['meal', 'warm',  'Asia', 'mixed', 2, 'Tex-Mex'],
    ['meal', 'hot', 'Asia', 'mixed', 2, 'Manti'],
    ['meal', 'cold',  'Asia', 'mixed', 2, 'Khichdi'],

    ['meal', 'warm',  'America', 'mixed', 2, 'Kansas City-style barbecue'],
    ['meal', 'hot',  'America', 'mixed', 2, 'Barbecue in Texas'],
    ['meal', 'cold',  'America', 'mixed', 2, 'Sloppy joe'],

    ['meal', 'warm',  'Worldwide', 'boiled', 2, 'Hot dog'],
    ['meal', 'hot',  'Worldwide', 'boiled', 2, 'Pesto Boiled Potatoes'],
    ['meal', 'cold', 'Worldwide', 'boiled', 2, 'Spinach Soup'],

    ['meal', 'warm',  'Europe', 'boiled', 2, 'Jambalaya'],
    ['meal', 'hot', 'Europe', 'boiled', 2, 'Black Chickpeas'],
    ['meal', 'cold', 'Europe', 'boiled', 2, 'Vegetable Soup'],

    ['meal', 'warm', 'Asia', 'boiled', 2, 'Gumbo'],
    ['meal', 'hot', 'Asia', 'boiled', 2, 'Dirty Rice'],
    ['meal', 'cold', 'Asia', 'boiled', 2, 'Hawaiian haystack'],

    ['meal', 'warm', 'America', 'boiled', 2, 'Goetta'],
    ['meal', 'hot', 'America', 'boiled', 2, 'Chaudin'],
    ['meal', 'cold', 'America', 'boiled', 2, 'Goetta'],

['meal', 'warm',  'Worldwide', 'baked', 2, 'Chicken Curry'],
    ['meal', 'hot', 'Worldwide', 'baked', 2, 'Fugazza'],
    ['meal', 'cold', 'Worldwide', 'baked', 2, 'Halloumi and watermelon'],

    ['meal', 'warm', 'Europe', 'baked', 2, 'Moussaka'],
    ['meal', 'hot', 'Europe', 'baked', 2, 'Köttbullar'],
    ['meal', 'cold', 'Europe', 'baked', 2, 'Haggis'],

    ['meal', 'warm', 'Asia', 'baked', 2, 'Hainanese Chicken Rice'],
    ['meal', 'hot', 'Asia', 'baked', 2, 'Chicken bog'],
    ['meal', 'cold', 'Asia', 'baked', 2, 'Yeung Chow fried rice'],

    ['meal', 'warm', 'America', 'baked', 2, 'Mexican pizza'],
    ['meal', 'hot', 'America', 'baked', 2, 'California-style pizza'],
    ['meal', 'cold', 'America', 'baked', 2, 'Chocolate pizza'],

['meal', 'warm',  'Worldwide', 'mixed', 4, 'Pizza cake'],
    ['meal', 'hot', 'Worldwide', 'mixed', 4, 'Pan Pizza'],
    ['meal', 'cold', 'Worldwide', 'mixed', 4, 'Neapolitan pizza'],

    ['meal', 'warm', 'Europe', 'mixed', 4, 'Palatschinken'],
    ['meal', 'hot', 'Europe', 'mixed', 4, 'Currywurst'],
    ['meal', 'cold', 'Europe', 'mixed', 4, 'Potica'],

    ['meal', 'warm', 'Asia', 'mixed', 4, 'Sushi'],
    ['meal', 'hot', 'Asia', 'mixed', 4, 'Satay'],
    ['meal', 'cold', 'Asia', 'mixed', 4, 'Laksa'],

    ['meal', 'warm', 'America', 'mixed', 4, 'Simple Shepherd’s Pie'],
    ['meal', 'hot', 'America', 'mixed', 4, 'Apple Pie'],
    ['meal', 'cold', 'America', 'mixed', 4, 'American burnt onion dip'],

    ['meal', 'warm', 'Worldwide', 'boiled', 4, 'Fries'],
    ['meal', 'hot', 'Worldwide', 'boiled', 4, 'Cheese fondue'],
    ['meal', 'cold', 'Worldwide', 'boiled', 4, 'Goulash'],

    ['meal', 'warm', 'Europe', 'boiled', 4, 'Arancini'],
    ['meal', 'hot', 'Europe', 'boiled', 4, 'Pierogi'],
    ['meal', 'cold', 'Europe', 'boiled', 4, 'Waffles'],

    ['meal', 'warm', 'Asia', 'boiled', 4, 'Tom Yum'],
    ['meal', 'hot', 'Asia', 'boiled', 4, 'Calas'],
    ['meal', 'cold', 'Asia', 'boiled', 4, 'Dim Sum'],

    ['meal', 'warm', 'America', 'boiled', 4, 'Glorified rice'],
    ['meal', 'hot', 'America', 'boiled', 4, 'Hominy Grits'],
    ['meal', 'cold', 'America', 'boiled', 4, 'Spring Rolls'],

['meal', 'warm',  'Worldwide', 'baked', 4, 'Fish and Chips'],
    ['meal', 'hot', 'Worldwide', 'baked', 4, 'Fried Rice'],
    ['meal', 'cold', 'Worldwide', 'baked', 4, 'Black Bean Burger'],

    ['meal', 'warm', 'Europe', 'baked', 4, 'Sweet Potato Pasta Bake'],
    ['meal', 'hot', 'Europe', 'baked', 4, 'Oven-Baked Meatballs'],
    ['meal', 'cold', 'Europe', 'baked', 4, 'Sheet-Pan Greek Chicken and Veggies'],

    ['meal', 'warm', 'Asia', 'baked', 4, 'Fish Balls'],
    ['meal', 'hot', 'Asia', 'baked', 4, 'Thai Coconut Braised Chicken and Potatoes'],
    ['meal', 'cold', 'Asia', 'baked', 4, 'Teriyaki Tofu and Broccoli'],

    ['meal', 'warm', 'America', 'baked', 4, 'Pecan pie with maple cream'],
    ['meal', 'hot', 'America', 'baked', 4, 'Breaded Chicken Spinach Burgers'],
    ['meal', 'cold', 'America', 'baked', 4, 'Oven-Baked Fajitas'],
]

dish = uniq_val_from_data(training_data, 0)
served = uniq_val_from_data(training_data, 1)
origin = uniq_val_from_data(training_data, 2)
cooked = uniq_val_from_data(training_data, 3)
ingredients = uniq_val_from_data(training_data, 4)

# We can also use this function instead of the direct appending to the list
'''
rand_data = []

for each in range(0, len(training_data)-1):
    rand_data.append(uniq_val_from_data(training_data, each))
'''

rand_data = [dish, served, origin, cooked, ingredients]


def client_ordering():
    #generate an order
    order = []

    for i in range(0, len(tree_format)-1):
        tmpr = random.sample(rand_data[i], 1)
        order.append(tmpr[0])

    order.append('order')
    return order

#print(len(training_data))
