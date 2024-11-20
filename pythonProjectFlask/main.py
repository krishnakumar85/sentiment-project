from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS to handle cross-origin requests
import json

app = Flask(__name__)

# Enable CORS for all routes in the application
CORS(app)  # This will allow all domains to access the API


# Alternatively, enable CORS for a specific route:
# CORS(app, resources={r"/data": {"origins": "*"}})


# Route to receive data from the Chrome extension
@app.route('/data', methods=['POST'])
def receive_data():
    try:
        data = request.get_json()  # Get the data sent from the Chrome extension
        print(f"Received data: {data}")
        #print(data)
        #readcomments(data)
        reviews = json.loads(data)
        res = "" #this variable will have all reviews
        for obj in reviews:
            #print(f"Review: {obj['text']}")
            res = res + "\n" + obj['text']
        print(res)

        # Do something with the data (e.g., save it, process it)
        # For demonstration, just return the data back to the client
        #return jsonify({"status": "success", "received_data": data}), 200
        return jsonify({"status": "success","analysis":"looks good"}), 200

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"status": "error"}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)  # Runs on localhost:5000


#def readcomments(data):
#    reviews = json.loads(data)
#    for obj in reviews:
#        print(f"Review: {obj['review']}")


