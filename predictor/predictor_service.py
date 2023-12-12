from keras.models import load_model
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
import numpy as np
from django.conf import settings

def is_covid_positive(image_uri):
    model=load_model(settings.STATIC_PATH + '/chest_xray.h5')
    img=image.load_img(image_uri, target_size=(224,224))
    x=image.img_to_array(img)
    x=np.expand_dims(x, axis=0)
    img_data=preprocess_input(x)
    classes=model.predict(img_data)
    result=int(classes[0][0])
    return result==0
