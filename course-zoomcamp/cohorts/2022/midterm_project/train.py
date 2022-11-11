import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer

from sklearn.ensemble import RandomForestClassifier

import xgboost as xgb

import bentoml


# Input the data from the URL.
data = "./data/diabetes_data_upload.csv"

df = pd.read_csv(data)

#prepare the data
df.columns = df.columns.str.lower().str.replace(' ', '_')
df.rename(columns={'class': 'diabetes_risk'}, inplace=True)
string_columns = list(df.dtypes[df.dtypes == 'object'].index)

for col in string_columns:
    df[col] = df[col].str.lower().str.replace(' ', '_')

# target variable - convert values named "positive" and "negative" to "1" and "0"
df.diabetes_risk = (df.diabetes_risk == 'positive').astype(int)

df_train, df_test = train_test_split(df, test_size=0.2, random_state=11)

y_train = df_train.diabetes_risk.values
y_test = df_test.diabetes_risk.values

del df_train['diabetes_risk']
del df_test['diabetes_risk']

df_train.reset_index (drop=True)
df_test.reset_index (drop=True)


dv = DictVectorizer(sparse=False)

train_dicts = df_train.to_dict(orient='records')
X_train = dv.fit_transform(train_dicts)

test_dicts = df_test.to_dict(orient='records')
X_test = dv.transform(test_dicts)


# XGBoost
dtrain = xgb.DMatrix(X_train, label=y_train)

xgb_params = {
    'eta': 0.1, 
    'max_depth': 3,
    'min_child_weight': 1,

    'objective': 'binary:logistic',
    'eval_metric': 'auc',

    'nthread': 8,
    'seed': 1,
    'verbosity': 1,
}

model = xgb.train(xgb_params, dtrain, num_boost_round=175)


#BentoML

print (
    bentoml.xgboost.save_model(
    'diabetes_risk_model', model,
    custom_objects={
        'dictVectorizer': dv
    })
)
