import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from category_encoders import OrdinalEncoder
from sklearn.pipeline import make_pipeline
from sklearn.pipeline import Pipeline
import sklearn.metrics as metrics
from xgboost import XGBClassifier
import pickle
from sklearn.metrics import roc_auc_score

df = pd.read_csv('churn csv.csv')

#데이터 split
train, val = train_test_split(df, test_size=0.2, random_state=2)

#타겟 설정 
target = 'Churn'
features = ['tenure','MultipleLines','TechSupport','Contract','PaymentMethod','PaperlessBilling','TotalCharges']

X_train = train[features]
y_train = train[target]
X_val = val[features]
y_val = val[target]

#가중치 부여
ratio = 0.26/0.73

#xgboost model

pipe = make_pipeline(
    OrdinalEncoder(),
    XGBClassifier(n_estimators=900,random_state=12,n_jobs=-1,
                  max_depth=6,min_samples_split=5,scale_pos_weight=ratio)
)

churn_model = pipe.fit(X_train, y_train)
pred = pipe.predict(X_val)

# print('Accuracy: ', metrics.accuracy_score(y_val, pred))
# print('Recall: ',metrics.recall_score(y_val,pred,average='binary'))
# print('F1 score: ', metrics.f1_score(y_val, pred, average='binary'))
# print('AUC score: ',roc_auc_score(y_val,pred))

pickle.dump(churn_model,open('churn.pkl','wb'))