from tensorflow.keras.models import load_model
classes_list = ['hello', 'goodbye', 'please', 'thank you', 'my', 'name', 'is', 'spock']

model = load_model('location of model file')
class_pred = model.predict(numpy_array_here)

hand_gesture = classes_list[class_pred]