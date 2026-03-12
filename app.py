from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

symptom_map = {
    "fever": {
        "cause": "Possible infection such as flu or viral illness",
        "diagnosis": "Monitor temperature and consult a doctor if fever persists"
    },
    "cough": {
        "cause": "Respiratory irritation or infection",
        "diagnosis": "May be cold, flu, or respiratory infection"
    },
    "headache": {
        "cause": "Stress, dehydration, migraine, or lack of sleep",
        "diagnosis": "Rest, hydrate, and reduce screen exposure"
    },
    "nausea": {
        "cause": "Digestive disturbance or food poisoning",
        "diagnosis": "Drink fluids and avoid heavy meals"
    },
    "fatigue": {
        "cause": "Stress, illness, or anemia",
        "diagnosis": "Rest and consult a doctor if persistent"
    }
}

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    text = data["message"].lower()

    for symptom in symptom_map:
        if symptom in text:
            result = symptom_map[symptom]
            return jsonify({
                "response": f"Possible cause: {result['cause']}. Suggested action: {result['diagnosis']}."
            })

    return jsonify({
        "response": "Symptoms unclear. Please describe them more clearly."
    })

if __name__ == "__main__":
    app.run(debug=True)