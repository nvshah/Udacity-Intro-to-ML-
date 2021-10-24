import sys
from class_vis import prettyPicture
from prep_terrain_data import makeTerrainData

import numpy as np
import pylab as pl
from sklearn import tree, metrics

features_train, labels_train, features_test, labels_test = makeTerrainData()


#################################################################################


########################## DECISION TREE #################################


# your code goes here
clf = tree.DecisionTreeClassifier()
clf.fit(features_train, labels_train)
predict_test = clf.predict(features_test)

acc = metrics.accuracy_score(predict_test, labels_test)
# be sure to compute the accuracy on the test set


def submitAccuracies():
    return {"acc": round(acc, 3)}
