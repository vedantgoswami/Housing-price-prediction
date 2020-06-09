# importing the necessary module 
from sklearn import datasets
import pandas as pd
import numpy as np
#loading the Dataset
boston=datasets.load_boston()
#feature_name
print(boston['feature_names'])
#Transform the dataset into a data frame
df_x=pd.DataFrame(boston.data,columns=boston.feature_names)
df_y=pd.DataFrame(boston.target)
#Transform the dataset into a data frame
df_x=pd.DataFrame(boston.data,columns=boston.feature_names)
df_y=pd.DataFrame(boston.target)
#Model Training and Intialization
from sklearn.ensemble import RandomForestRegressor
clf=RandomForestRegressor()
clf.fit(x_train,y_train)
prediction=clf.predict(x_test)
score=clf.score(x_test,y_test)
print("Accuracy of the classifier is ",score)
