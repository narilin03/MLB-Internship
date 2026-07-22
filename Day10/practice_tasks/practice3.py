import os      
os.environ['TF_CPP_MIN_LOG_LEVEL']='3'
os.environ['TF_ENABLE_ONEDNN_OPTS']='0'

import tensorflow as tf 

from keras.models import Sequential
from keras.layers import Dense, Input

activation=['relu','sigmoid','tanh']

for i in activation:
    print("---Model Building with:",i.upper(),"Actvation---")
    
    testing=Sequential([
        Input(shape=(10,)),
        Dense(32,activation=i,name='Hidden'+ i),
        Dense(1,activation='linear')
    ])
    
    testing.summary()    