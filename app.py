from flask import Flask, render_template, request

app = Flask(__name__)

# Simple disease logic (can upgrade to ML later)
def predict_disease(symptoms):
    symptoms = symptoms.lower()

    if "fever" in symptoms and "headache" in symptoms:
        return "Viral Fever", "General Physician", "Take rest, drink fluids, paracetamol"
    
    elif "chest pain" in symptoms:
        return "Heart Issue", "Cardiologist", "Avoid stress, consult immediately"
    
    elif "skin rash" in symptoms:
        return "Allergy", "Dermatologist", "Use antihistamines, avoid allergens"
    
    elif "stomach pain" in symptoms:
        return "Gastritis", "Gastroenterologist", "Avoid spicy food, eat light meals"
    
    else:
        return "Unknown", "General Physician", "Consult a doctor"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    symptoms = request.form['symptoms']
    disease, doctor, precaution = predict_disease(symptoms)

    return render_template('index.html',
                           disease=disease,
                           doctor=doctor,
                           precaution=precaution)

if __name__ == '__main__':
    app.run(debug=True)