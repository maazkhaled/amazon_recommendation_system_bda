from flask import Flask, render_template, request, redirect, url_for
from kafka import KafkaConsumer
from kafka import KafkaProducer
import json
import pandas as pd

app = Flask(__name__)
global user_id
# Configure Kafka consumer
consumer = KafkaConsumer('recommendations', bootstrap_servers=['localhost:9092'], auto_offset_reset='earliest', enable_auto_commit=True)
producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

# Function to get recommendations from Kafka consumer
def get_recommendations():
    #user_id=28
    recommendations = []
    for message in consumer:
        # Decode message and split into user ID and product IDs
        msg = message.value.decode('utf-8')
        print(msg)
        product_ids=[]
        product_ids = msg.split(',')
        # Convert product IDs to a list
        #product_ids = product_ids.split(',')
        # Take the first 10 product IDs
        product_ids = product_ids[:10]
        
        recommendations.append((user_id, product_ids))
        if len(recommendations) == 1:
            # Stop consuming messages after receiving one set of recommendations
            break
    return recommendations

# Route to display recommendations
@app.route('/recommendations', methods=['GET'])
def display_recommendations():
    recommendations = get_recommendations()
    # If no recommendations are received yet, redirect to the waiting page
    if not recommendations:
        print("recom")
        return redirect(url_for('waiting'))
    # Otherwise, render the recommendations page and pass the recommendations as a parameter
    return render_template('recommendations.html', recommendations=recommendations)

# Route to display waiting page
@app.route('/waiting', methods=['GET'])
def waiting():
    return render_template('waiting.html')

# Route to take user ID as input and send it to Kafka producer
@app.route('/', methods=['GET', 'POST'])
def index():
    global user_id
    if request.method == 'POST':
        user_id = request.form['user_id']
        #userid=user_id
        # Send the user ID to Kafka producer
        message = str(user_id).encode('utf-8')
        producer.send('user', message)
        #return redirect(url_for('display_recommendations'))
        print("index")
        return redirect(url_for('display_recommendations'))
    
    return render_template('index.html')

if __name__ == '__main__':

   app.run(host="localhost", port=5001, debug=True)

