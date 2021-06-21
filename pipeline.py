import pandas as pd
from sklearn.preprocessing import StandardScaler
import Model
import encode

from sklearn.svm import SVC

def fill_nulls(dataframe):
	dataframe['Age'].fillna(dataframe['Age'].mean(),inplace=True)
	dataframe['Fare'].fillna(dataframe['Fare'].mean(),inplace=True)
	return dataframe



def one_hot_encode(df):
	pass



def Model(x, y, a):
	
    pass



