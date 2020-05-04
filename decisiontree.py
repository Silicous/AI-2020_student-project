
import pandas as pd
from sklearn.tree import DecisionTreeClassifier 
from sklearn.model_selection import train_test_split 
from sklearn import metrics 

col_names = ['idle','first','good']
data = pd.read_csv("results.csv", header=None, names=col_names)
data = data.iloc[1:]
data.head()

feature_cols = ['idle','first']
X = data[feature_cols] 
y = data.good 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=1) 

clf = DecisionTreeClassifier(criterion="gini", max_depth=4)

clf = clf.fit(X_train,y_train)

from sklearn.externals.six import StringIO  
from IPython.display import Image  
from sklearn.tree import export_graphviz
import pydotplus
dot_data = StringIO()
export_graphviz(clf, out_file=dot_data,  
                filled=True, rounded=True,
                special_characters=True, feature_names = feature_cols,class_names=['0','1'])
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
graph.write_png('results.png')
Image(graph.create_png())