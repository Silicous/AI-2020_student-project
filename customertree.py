import pandas as pandas
import graphviz
import pydot
from learning_db import *
from joblib import dump
from sklearn import tree
from sklearn.metrics import accuracy_score
from sklearn.externals.six import StringIO
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

customers = pandas.DataFrame({"gender": gender,
                              "age": age,
                              "outfit": outfit,
                              "cash": cash,
                              "time": time,
                              "vege": vege,
                              "food": food,
                              "drink": drink
                              })


customers["gender"], gender_objects = pandas.factorize(customers["gender"])
customers["age"], age_objects = pandas.factorize(customers["age"])
customers["outfit"], outfit_objects = pandas.factorize(customers["outfit"])
customers["cash"], cash_objects = pandas.factorize(customers["cash"])
customers["time"], time_objects = pandas.factorize(customers["time"])
customers["vege"], vege_objects = pandas.factorize(customers["vege"])
customers["food"], food_objects = pandas.factorize(customers["food"])
customers["drink"], drink_objects = pandas.factorize(customers["drink"])

objects = []
objects.append(gender_objects)
objects.append(age_objects)
objects.append(outfit_objects)
objects.append(cash_objects)
objects.append(time_objects)
objects.append(vege_objects)
objects.append(food_objects)
objects.append(drink_objects)


#X = customers.drop(["food","drink"], axis=1)
#y = customers["food"]

#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=None)

#food_classifier = DecisionTreeClassifier(criterion = "entropy", random_state=1)
#food_classifier.fit(X_train, y_train)

#porównanie kryterium: index Giniego i entropia

#food_classifier1 = DecisionTreeClassifier()
#food_classifier1.fit(X_train, y_train)

#food_classifier2 = DecisionTreeClassifier(criterion = "entropy")
#food_classifier2.fit(X_train, y_train)

#y_pred1 = food_classifier1.predict(X_test)
#y_pred2 = food_classifier2.predict(X_test)


#if accuracy_score(y_test, y_pred1) >  accuracy_score(y_test, y_pred2):
#    dump(food_classifier,'models/food_model.joblib')
#else:
#    dump(food_classifier2,'models/food_model.joblib')

#dot_data=StringIO()
#tree = tree.export_graphviz(food_classifier, out_file = dot_data,
#                            feature_names = X.columns,
#                            class_names = food_objects,
#                            filled = True, rounded = True)
#graph = pydot.graph_from_dot_data(dot_data.getvalue())
#graph[0].write_pdf("graphs/food_model.pdf")

#X = customers.drop(["food","drink"], axis=1)
#y = customers["drink"]

#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.45, random_state=1)

#drink_classifier = DecisionTreeClassifier(criterion = "entropy")
#drink_classifier.fit(X_train, y_train)

#drink_classifier1 = DecisionTreeClassifier()
#drink_classifier1.fit(X_train, y_train)

#drink_classifier2 = DecisionTreeClassifier(criterion = "entropy")
#drink_classifier2.fit(X_train, y_train)

#y_pred1 = drink_classifier1.predict(X_test)
#y_pred2 = drink_classifier2.predict(X_test)

#if accuracy_score(y_test, y_pred1) >  accuracy_score(y_test, y_pred2):
#    dump(drink_classifier1,'models/drink_model.joblib')
#else:
#    dump(drink_classifier2,'models/drink_model.joblib')

#dot_data=StringIO()
#tree = tree.export_graphviz(drink_classifier, out_file = dot_data,
#                            feature_names = X.columns,
#                            class_names = drink_objects,
#                            filled = True, rounded = True)
#graph = pydot.graph_from_dot_data(dot_data.getvalue())
#graph[0].write_pdf("graphs/drink_model.pdf")
