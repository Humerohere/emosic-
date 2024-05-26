import numpy as np
from sklearn.metrics import confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sns
from keras.models import Sequential, Model
from keras.layers import Dense, Flatten, GlobalAveragePooling2D, Input
from keras.optimizers import Adam
from keras.preprocessing.image import ImageDataGenerator
from keras.applications import VGG19
from keras.applications.vgg19 import preprocess_input
from keras.regularizers import l2

train_dir = 'data/train'
val_dir = 'data/test'

batch_size = 64
learning_rate = 0.0001

train_datagen = ImageDataGenerator(
    rescale=1. / 255,
    fill_mode='nearest', )
val_datagen = ImageDataGenerator(
    rescale=1. / 255,
)

train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(48, 48),
    batch_size=batch_size,
    class_mode='categorical'
)

val_generator = val_datagen.flow_from_directory(
    val_dir,
    target_size=(48, 48),
    batch_size=batch_size,
    class_mode='categorical'
)

vgg19_model = VGG19(weights='imagenet', include_top=False, input_shape=(48, 48, 3))

for layer in vgg19_model.layers[-4:]:
    layer.trainable = True

x = GlobalAveragePooling2D()(vgg19_model.output)
x = Dense(4096, activation='relu', kernel_regularizer=l2(0.01))(x)
predictions = Dense(1024, activation='softmax')(x)

model = Model(inputs=vgg19_model.input, outputs=predictions)

model.compile(loss='categorical_crossentropy', optimizer=Adam(learning_rate=learning_rate), metrics=['accuracy'])

model_info = model.fit(
    train_generator,
    steps_per_epoch=len(train_generator),
    epochs=6,
    validation_data=val_generator,
    validation_steps=len(val_generator)
)

model.save_weights('vgg19_model.h5')

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(model_info.history['loss'], label='Training Loss')
plt.plot(model_info.history['val_loss'], label='Validation Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Training and Validation Loss')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(model_info.history['accuracy'], label='Training Accuracy')
plt.plot(model_info.history['val_accuracy'], label='Validation Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.title('Training and Validation Accuracy')
plt.legend()

plt.show()
