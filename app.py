from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np
from flask_cors import CORS # Import Flask-CORS

app = Flask(__name__)
CORS(app) # Enable CORS for all routes

# Load the trained model
# Make sure 'sales_prediction_model.pkl' is in the same directory as this app.py file
try:
    model = joblib.load('sales_prediction_model.pkl')
    print("Model loaded successfully!")
except Exception as e:
    print(f"Error loading model: {e}")
    # Exit if the model cannot be loaded, as the app won't function without it.
    exit()

@app.route('/')
def home():
    """Renders the HTML template for the homepage."""
    print("Home page requested.")
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict_sales():
    """
    Handles POST requests to /predict, processes input,
    makes a prediction using the loaded model, and returns the result.
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
        
        print(f"Features prepared for prediction: {features_for_prediction}")
        # Print the shape of the features to debug any mismatch
        print(f"Shape of features sent to model: {features_for_prediction.shape}") 
        
        prediction = model.predict(features_for_prediction)
        
        print(f"Prediction made: {prediction[0]}")
        return jsonify({'predicted_sales': prediction[0]})

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
