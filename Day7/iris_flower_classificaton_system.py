import numpy as np  
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay
)

iris=load_iris()

df=pd.DataFrame(data=iris.data,columns=iris.feature_names)
df['target']=iris.target


print("----Iris Flower Classification System----")
print("Features:",iris.feature_names)
print("Target Class:",iris.target_names,"(encoded as 0,1,2)")
print("Dataset Shape:",df.shape)
print("\nFirst 5 rows of Dataset:\n",df.head(5))


X=iris.data
y=iris.target

X_train,X_test, y_train, y_test=train_test_split(
    X,y,test_size=0.2,random_state=42
)

#logistic regression model
print("\n----Logistic Regression Model----")
logic_model=LogisticRegression(max_iter=200)
logic_model.fit(X_train,y_train)
logic_predict=logic_model.predict(X_test)


print("----Model Evaluation----")

logic_accuracy=accuracy_score(y_test,logic_predict)
logic_precision=precision_score(y_test,logic_predict,average='weighted')
logic_recall=recall_score(y_test,logic_predict,average='weighted')
logic_f1=f1_score(y_test,logic_predict,average='weighted')


print("Accuracy: %.4f"% logic_accuracy)
print("Precision: %.4f"%logic_precision)
print("Recall: %.4f"%logic_recall)
print("F1-Score: %.4f"%logic_f1)

print("\n----Classification Report----")
print(classification_report(y_test,logic_predict,target_names=iris.target_names))


print("----Confusion Matrix----")
logic_cm=confusion_matrix(y_test,logic_predict)
print(logic_cm)


#decision tree model
print("\n----Decision Tree Model----")
decision_model=DecisionTreeClassifier(random_state=42)
decision_model.fit(X_train,y_train)
decision_predict=decision_model.predict(X_test)


print("----Model Evaluation----")

decision_accuracy=accuracy_score(y_test,decision_predict)
decision_precision=precision_score(y_test,decision_predict,average='weighted')
decision_recall=recall_score(y_test,decision_predict,average='weighted')
decision_f1=f1_score(y_test,decision_predict,average='weighted')


print("Accuracy: %.4f"% decision_accuracy)
print("Precision: %.4f"%decision_precision)
print("Recall: %.4f"%decision_recall)
print("F1-Score: %.4f"%decision_f1)

print("\n----Classification Report----")
print(classification_report(y_test,decision_predict,target_names=iris.target_names))


print("----Sample Predictions VS Actual Values----")
for i in range(10):
    name=iris.target_names[y_test[i]]
    logic_name=iris.target_names[logic_predict[i]]
    decision_name=iris.target_names[decision_predict[i]]
    print("%2d|%14s|%17s|%17s"%(i,name,logic_name,decision_name))
print()


displayMatrix=ConfusionMatrixDisplay(confusion_matrix=logic_cm,display_labels=iris.target_names)
displayMatrix.plot(cmap=plt.cm.Blues)
plt.title("Logistics Regression Confusion Matrix")
plt.savefig("Day7/confusion_matrix.png",dpi=300,bbox_inches="tight") 
plt.close()
print("Saved Confusion Matrix!")   
    