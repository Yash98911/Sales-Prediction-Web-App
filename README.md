📈 Sales Prediction Web App (End-to-End ML Deployment)
Project Overview
This project demonstrates a complete end-to-end Machine Learning pipeline for predicting product sales based on advertising spending on TV and Radio. It features a trained Linear Regression model deployed as a web application, allowing users to get real-time sales forecasts through an interactive interface.

This version is optimized for deployment on platforms with limited resources (like PythonAnywhere's free tier). The model's coefficients and intercept are hardcoded directly into the application, removing the need for large machine learning libraries during deployment.

Live Website Link 🎉
Click here to see the Sales Prediction Web App live on PythonAnywhere:
Live App on PythonAnywhere

Features
Feature Engineering: Creates an interaction feature (TV_Radio) by multiplying TV and Radio advertising budgets.

Hardcoded Model: Uses pre-trained Linear Regression coefficients and intercept directly within the application for predictions, removing heavy ML library dependencies.

Web Application (Flask Backend): A Python Flask API that processes user input and provides sales predictions.

Interactive Frontend: A responsive web interface built with HTML, Tailwind CSS, and JavaScript for user input and displaying prediction results.

Technologies Used
Python Libraries (Deployment):

Flask for the web framework

NumPy for numerical operations (specifically for dot product in prediction)

Flask-CORS for handling cross-origin requests

Gunicorn for production-ready WSGI server on PythonAnywhere

Web Technologies:

HTML5

CSS (Tailwind CSS)

JavaScript (ES6+)

Version Control: Git & GitHub

Getting Started (Local Development - Original Approach)
Note: The deployed version on PythonAnywhere uses hardcoded model parameters due to resource constraints. For full local development including model training with scikit-learn, refer to your original sales_prediction.ipynb and requirements.txt.

Follow these steps to set up and run the optimized project locally on your machine.

Prerequisites
Python 3.11+

pip (Python package installer)

Git

1. Clone the Repository
First, clone this GitHub repository to your local machine:

git clone https://github.com/Yash98911/Sales-Prediction-Web-App.git
cd Sales-Prediction-Web-App

(Replace Yash98911 with your actual GitHub username if different)

2. Set Up Python Environment
It's recommended to create a virtual environment:

python -m venv venv
# On Windows
.\venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

3. Install Dependencies (Optimized for Deployment)
Install only the essential Python libraries for the optimized app:

pip install -r requirements.txt

4. Run the Flask Application (Locally)
Navigate to the project root directory in your terminal and run the Flask app:

python app.py

You should see output indicating that the Flask server is running on http://127.0.0.1:5000. Keep this terminal running.

5. Access the Web App (Locally)
Open your web browser and go to:

http://127.0.0.1:5000

You should see the "Sales Predictor" interface. Enter TV and Radio advertising budgets to get predictions!

Project Structure
├── app.py                      # Flask backend application (with hardcoded model params)
├── requirements.txt            # Python dependencies (optimized for deployment)
├── templates/
│   └── index.html              # Frontend HTML for the web interface
└── README.md                   # Project description and instructions

Contribution
Feel free to fork this repository, open issues, or submit pull requests.

License
This project is open-source and available under the MIT License.
