📈 Sales Prediction Web App (End-to-End ML Deployment)

Project Overview

This project demonstrates a complete end-to-end Machine Learning pipeline for predicting product sales based on advertising spending on TV and Radio. It features a trained Linear Regression model deployed as a web application, allowing users to get real-time sales forecasts through an interactive interface.

Features:- 

1.) Data Loading & EDA: Initial exploration of the advertising dataset.

2.) Data Cleaning: Handled unnecessary columns.

3.) Feature Engineering: Created an interaction feature (TV_Radio) by multiplying TV and Radio advertising budgets, which significantly improved model performance.

4.) Model Training: Utilized Linear Regression to build a predictive model.

5.) Model Evaluation: Assessed model performance using metrics like R-squared, Mean Squared Error (MSE), and Mean Absolute Error (MAE), along with cross-validation.

6.) Model Persistence: Saved the trained model using pickle for easy loading and deployment.

7.) Web Application (Flask Backend): A Python Flask API to load the trained model and serve predictions.

8.) Interactive Frontend: A responsive web interface built with HTML, Tailwind CSS, and JavaScript for user input and displaying prediction results.

Technologies Used:- 

1.) Python Libraries:

2.) pandas for data manipulation

3.)numpy for numerical operations

4.) scikit-learn for machine learning (Linear Regression, train_test_split, metrics)

5.) matplotlib and seaborn for data visualization

6.) Flask for the web framework

7.) Flask-CORS for handling cross-origin requests

8.) pickle for model serialization

Web Technologies:

HTML5

CSS (Tailwind CSS)

JavaScript (ES6+)

Version Control: Git & GitHub

Getting Started
Follow these steps to set up and run the project locally on your machine.

Prerequisites
Python 3.8+

pip (Python package installer)

Git :- 

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

3. Install Dependencies
Install all the required Python libraries:

pip install -r requirements.txt

(You might need to create a requirements.txt file first: pip freeze > requirements.txt)

4. Ensure Model File Exists
Make sure your sales_prediction_model.pkl file is present in the project root directory. If not, run the Jupyter Notebook (sales_prediction.ipynb) to train and save the model.

5. Run the Flask Application
Navigate to the project root directory in your terminal and run the Flask app:

python app.py

You should see output indicating that the Flask server is running on http://127.0.0.1:5000.

6. Access the Web App
Open your web browser and go to:

http://127.0.0.1:5000

You should see the "Sales Predictor" interface. Enter TV and Radio advertising budgets to get predictions!

Project Structure:-

├── app.py                      # Flask backend application

├── sales_prediction.ipynb      # Jupyter Notebook for EDA, model training & evaluation

├── sales_prediction_model.pkl  # Trained Linear Regression model (pickle format)

├── requirements.txt            # Python dependencies

├── templates/
│   └── index.html              # Frontend HTML for the web interface

└── README.md                   # Project description and instructions


Visualizations from Notebook


* **Correlation Heatmap**
    ![Correlation Heatmap](images/correlation_heatmap.png)
* **TV vs Sales Regression Plot**
    ![TV vs Sales Regression Plot](images/tv_sales_regplot.png)
* **Radio vs Sales Regression Plot**
    ![Radio vs Sales Regression Plot](images/radio_sales_regplot.png)
