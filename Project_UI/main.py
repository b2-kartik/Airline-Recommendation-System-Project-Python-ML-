from flask import Flask, request, render_template
import pickle
from sklearn.preprocessing import StandardScaler

# create an application of Flask
app = Flask(__name__)

@app.route("/")
def root():
    return """
        <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Airline Recommendation System</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color:  # f4f4f4;
                margin: 0;
                padding: 20px;
            }
            .background {
                width: 100%;
                height: 100vh; /* Full viewport height */
                background-image: url('airplane.jpg');
                background-size: cover; /* Adjusts image size to cover the element */
                background-position: center; /* Centers the image */
                display: flex;
                background-repeat: no-repeat;
            }
            .container {
                max-width: 800px;
                margin: 0 auto;
                padding: 20px;
                background-color:  rgba(255,255,255,0.2);
                border-radius: 8px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }
            h1 {
                text-align: center;
                color:  # 333;
            }
            .form-group {
                margin-bottom: 15px;
            }
            .form-group label {
                display: block;
                margin-bottom: 5px;
                font-weight: bold;
            }
            .form-group input,.form-group select {
                width: 100 %;
                padding: 8px;
                border: 1px solid  # ddd;
                border-radius: 4px;
            }
            .form-group button {
                background-color:  # 28a745;
                color:  # fff;
                border: none;
                padding: 10px 15px;
                border-radius: 4px;
                cursor: pointer;
            }
            .form-group button:hover {
                background-color:  # 218838;
            }
            .recommendations {
                margin-top: 20px;
            }
            .recommendations h2 {
                color:  # 333;
            }
            .recommendation-item {
                padding: 10px;
                border: 1px solid  # ddd;
                border-radius: 4px;
                margin-bottom: 10px;
                background-color:  # f9f9f9;
            }
        </style>
    </head>
    <body>
        <div class="background">
            <div class="container">
                <h1>Airline Recommendation System</h1>

                <form id="recommendation-form">
                    <div class="form-group">
                        <label for="airline">Preferred Airline:</label>
                        <input type="number" id="airline" name="airline" required>
                    </div>

                    <div class="form-group">
                        <label for="Overall">Enter Rating out of 10:</label>
                        <input type="number" id="Overall" name="Overall" required>
                    </div>
                    
                    <div class="form-group">
                        <label for="traveller_type">Traveller Type:</label>
                        <input type="number" id="traveller_type" name="traveller_type" required>
                    </div>
                    
                    <div class="form-group">
                        <label for="cabin">Cabin:</label>
                        <input type="number" id="cabin" name="cabin" required>
                    </div>

                    <div class="form-group">
                        <button type="submit">Get Recommendations</button>
                    </div>
                </form>
            </div>
        </div>
    </body>
    </html>
    """

@app.route("/Get_Recommendation", methods=["POST"])
def Get_Recommendation():
    airline = request.form['airline']
    overall = request.form['overall']

    # laod the model from model.pkl file
    with open('./model.pkl', 'rb') as file:
        model = pickle.load(file)

    # get the recommendation using model
    recommendation = model.predict([airline, overall])
    print(f"Recommendation={recommendation}")

    if recommendation[0] == 1:
        result = "This Airline is Recommended"
    else:
        result = "Not Recommended This Airline"


    return f"""
    <html>
        <body>
            <h1>Recommended Airline:</h1>
            <p>Based on your Data : {result}</p>
        </body>
    </html>
    """


# start the application
app.run(host="0.0.0.0", port=4000, debug=True)