import numpy as np
import os
import cv2
from keras.layers import Dense,GlobalAveragePooling2D
from keras.applications import ResNet50
from keras.preprocessing import image
from keras.applications.mobilenet import preprocess_input
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Model
from keras.optimizers import Adam
from PIL import Image

     
def pred(ob):
    gray= ob.to_dict()
    base_model=ResNet50(weights='imagenet',include_top=False) #imports the mobilenet model and discards the last 1000 neuron layer.
    x=base_model.output
    x=GlobalAveragePooling2D()(x)
    x=Dense(1024,activation='relu')(x) #we add dense layers so that the model can learn more complex functions and classify for better results.
    x=Dense(1024,activation='relu')(x) #dense layer 2
    x=Dense(512,activation='relu')(x) #dense layer 3
    preds=Dense(3,activation='softmax')(x) #final layer with softmax activation
    model=Model(inputs=base_model.input,outputs=preds)
    class_names = ["Cycle", "Car", "Bike/Scooter"]
    for layer in model.layers[:-4]:
        layer.trainable=False
    for layer in model.layers[-4:]:
        layer.trainable=True
    model.compile(optimizer='Adam',loss='categorical_crossentropy',metrics=['accuracy'])
    fn =  "vehicle.h5"
    cwd = os.getcwd()
    fn2 = cwd+"\\firstdeep\deeplearn"+"\\"+fn
    print(fn2)
    model.load_weights(fn2)
    src_path=r"C:\Users\HP\eclipse-workspace\firstdeep\media"
    try:
        gray = cv2.imread(src_path+"\\tmp.jpg", cv2.IMREAD_COLOR)
        gray = cv2.resize(gray,(224, 224))
    except Exception as e:
        print(str(e))
    pr = model.predict(gray.reshape(1, 224, 224, 3))
    for i in range(len(pr)):
        z=[np.argmax(pr[i])]
        print("pr=%s, Predicted=%s" % (pr, z))
    return class_names[z[0]]