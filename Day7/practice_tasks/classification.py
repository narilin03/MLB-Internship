import numpy as np   
import pandas as pd    
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)

iris=load_iris()

df=pd.DataFrame(data=iris.data,columns=iris.feature_names)
df['target']=iris.target

print("Dataset Information:")
print("Features:",iris.feature_names)
print("Target Class:",iris.target_names,"(encoded as 0,1,2)")
print("Dataset Shape:",df.shape)
print("\nFirst 5 rows of Dataset:\n",df.head(5))


X=iris.data
y=iris.target

X_train,X_test, y_train, y_test=train_test_split(
    X,y,test_size=0.2,random_state=42
)

model=LogisticRegression(max_iter=200)
model.fit(X_train,y_train)


y_predict=model.predict(X_test)


print("\n----Model Evaluation----")

accuracy=accuracy_score(y_test,y_predict)
precision=precision_score(y_test,y_predict,average='weighted')
recall=recall_score(y_test,y_predict,average='weighted')
f1=f1_score(y_test,y_predict,average='weighted')


print("Accuracy: %.4f"% accuracy)
print("Precision: %.4f"%precision)
print("Recall: %.4f"%recall)
print("F1-Score: %.4f"%f1)

print("\n----Classification Report----")
print(classification_report(y_test,y_predict,target_names=iris.target_names))


print("----Confusion Matrix----")
ConfusionM=confusion_matrix(y_test,y_predict)
print(ConfusionM)