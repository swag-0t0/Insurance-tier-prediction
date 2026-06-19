import pickle
import pandas as pd 

with open('Model/model.pkl','rb') as f:
    model = pickle.load(f)


MODEL_VERSION = '1.0.0'

class_labels= model.classes_.tolist()

def predict_output(user_input:dict):
    df = pd.DataFrame([user_input])

    predict_class = model.predict(df)[0]
    
    Probabilities = model.predict_proba(df)[0]
    confidence = max(Probabilities)
    

    class_probs = dict(zip(class_labels, map(lambda p: round(p, 4), Probabilities)))

    return{
        'predicted_category':predict_class,
        'confidence':round(confidence,4),
        'class_probabilities':class_probs
    }