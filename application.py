from flask import Flask, render_template, request
from pipeline.prediction_pipeline import hybrid_recommendation

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home():
    recommendation = None
    
    if request.method == 'POST':    
        try:
            
            user_id = int(request.form["userID"])          
            recommendation = hybrid_recommendation(user_id)
           
        except Exception as e:          
            print("Error occured!!! ",e)
            
    return render_template('index.html',recommendation=recommendation)


if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
           
        
            