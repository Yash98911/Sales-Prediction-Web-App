from flask import Flask, request, jsonify, render_template
import numpy as np 
from flask_cors import CORS # Import Flask-CORS

app = Flask(__name__)
CORS(app) # Enable CORS for all routes

# --- Hardcoded Model Parameters (Replace with your actual values) ---
MODEL_COEFFICIENTS = [0.01960636, 0.03494256, 0.0010502 ]

MODEL_INTERCEPT = 6.684996691788713# <<< APNI VALUES YAHAN DALO!
# --- End of Hardcoded Model Parameters ---

print("Model parameters loaded successfully!")

@app.route('/')
def home():
    """Renders the HTML template for the homepage."""
    print("Home page requested.")
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict_sales():
    """
    Handles POST requests to /predict, processes input,
    makes a prediction using the hardcoded model, and returns the result.
    """
    try:
        data = request.json
        print(f"Received data for prediction: {data}")

        tv = float(data.get('tv')) # Use .get() for safer access
        radio = float(data.get('radio'))

        if tv is None or radio is None:
            raise KeyError("Missing 'tv' or 'radio' in request data.")

        # FEATURE ENGINEERING: Create the EXACT 3 features your model expects
        # Assuming your model was trained on: TV, Radio, TV*Radio
        tv_radio_interaction = tv * radio # This is the third feature

        # Prepare the features for the model. It expects a 2D array with 3 features.
        # The order of features MUST match the order used during model training: [TV, Radio, TV*Radio]
        features_for_prediction = np.array([[tv, radio, tv_radio_interaction]])

        # Manual Prediction using hardcoded coefficients and intercept
        # Ensure MODEL_COEFFICIENTS is a NumPy array for dot product
        prediction = np.dot(features_for_prediction, np.array(MODEL_COEFFICIENTS).reshape(-1, 1)) + MODEL_INTERCEPT

        print(f"Features prepared for prediction: {features_for_prediction}")
        print(f"Shape of features sent to model: {features_for_prediction.shape}")
        print(f"Prediction made: {prediction[0][0]}") # Access the scalar value
        return jsonify({'predicted_sales': prediction[0][0]})

    except KeyError as e:
        print(f"KeyError in predict_sales: {e}")
        return jsonify({'error': f"Missing data: {e}. Please provide 'tv' and 'radio' values."}), 400
    except ValueError as e:
        print(f"ValueError in predict_sales: {e}")
        return jsonify({'error': f"Invalid input type: {e}. Ensure 'tv' and 'radio' are numbers."}), 400
    except Exception as e:
        print(f"Unexpected error in predict_sales: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
