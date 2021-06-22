import pandas as pd
from sklearn.preprocessing import StandardScaler
import Model
import encode

from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

def fill_nulls(dataframe):
	dataframe['Age'].fillna(dataframe['Age'].mean(),inplace=True)
	dataframe['Fare'].fillna(dataframe['Fare'].mean(),inplace=True)
	return dataframe



def one_hot_encode(df):
    ohe_feats = df.select_dtypes(include=['categorical']).columns
    for f in ohe_feats:
        df_all_dummy = pd.get_dummies(df[f], prefix=f)
        df = df.drop([f], axis=1)
        df = pd.concat((df, df_all_dummy), axis=1)
        return df



def Model(train_df, test_df):
	
    

        X_train = train_df.drop("Survived", axis=1)
        Y_train = train_df["Survived"]
        X_test  = test_df.drop("PassengerId", axis=1).copy()
        X_train.shape, Y_train.shape, X_test.shape

        logreg = LogisticRegression()
        logreg.fit(X_train, Y_train)
        Y_pred = logreg.predict(X_test)
        acc_log = round(logreg.score(X_train, Y_train) * 100, 2)
        acc_log



