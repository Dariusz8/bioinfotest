#chap 5 - bioinformatics a practical approach with python
#Dariusz Czeczuk
#Start date: 1-6-2025
#Last mod: 1-6-2025

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,LSTM,Embedding #LongShortTermMemory

#define sequential model
model=Sequential()

#add an embedding layer to process the sequence data
model.add(Embedding(input_dim=20,output_dim=64)) #20 AA

#add an LSTM layer for sequence learning
model.add(LSTM(units=128))

#add a dense layer for output prediction
model.add(Dense(units=3,activation='softmax')) #3 classes for secondary structure

#compile model
model.compile(optimizer='adam',loss='categorial_crossentropy',metrics=['accuracy'])

#model summary
model.summary()