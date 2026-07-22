import os      
os.environ['TF_CPP_MIN_LOG_LEVEL']='3'
os.environ['TF_ENABLE_ONEDNN_OPTS']='0'

import tensorflow as tf 
import keras 

from keras.models import Sequential
from keras.layers import Dense, Input, Flatten
from keras.datasets import fashion_mnist
import matplotlib.pyplot as plt    
import numpy as np    

(X_train, y_train), (X_test, y_test)=fashion_mnist.load_data()

print("Training the data shape:",X_train.shape)
print("Testing the data shape:",X_test.shape)
print("Unique Labels:",np.unique(y_train))

class_names=[
    "Top",
    "Pants",
    "Sweatshirt",
    "Dress",
    "Coat",
    "Sandal",
    "Shirt",
    "Sneakers",
    "Bag",
    "Boots"
]

X_train= X_train/255.0
X_test= X_test/255.0

model =Sequential([
    Input(shape=(28,28)),
    Flatten(),
    Dense(128,activation='relu', name='Hidden_Layer'),
    Dense(10,activation='softmax', name='Output_Layer')
])

print("---Model Summary---")
model.summary()

model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

print("---Trainig Phase---")
memory=model.fit(
    X_train,y_train,
    epochs=5,
    validation_split=0.2,
    batch_size=32
)

print("---Model Evaluation---")
test_loss,test_accurate=model.evaluate(X_test,y_test,verbose=0)

print("Test Loss:",test_loss)
print("Test Accuracy:",test_accurate)


plt.figure(figsize=(8,5))
plt.plot(memory.history["accuracy"],label="Training Accuracy",color="blue")
plt.plot(memory.history["val_accuracy"],label="Validation Accuracy",color="orange")
plt.title("Model Accuracy History")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.legend()
plt.savefig("Day10/Training_Accuracy_Graph.png")
print("Accuracy graph saved as 'Training_Accuracy_Graph.png'.")
plt.close()


predictions=model.predict(X_test[5:10],verbose=0)

plt.figure(figsize=(12,3))
for i in range(5):
    predicted_label=np.argmax(predictions[i])
    actual_label=y_test[i+5]

    print("Image",i+1)
    print("Predicted:",class_names[predicted_label])
    print("Actual:",class_names[actual_label])
    
    plt.subplot(1,5,i+1)
    plt.imshow(X_test[i+5],cmap="gray")
    plt.title(class_names[predicted_label],fontsize=10)
    plt.axis("off")
    
plt.tight_layout()
plt.savefig("Day10/Sample_Predictions.png")
print("Prediction visual sheet saved as 'Sample_Predictions.png'.")
plt.close()   



