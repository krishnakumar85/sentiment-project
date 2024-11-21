from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS to handle cross-origin requests
import json
from openai import OpenAI
import os

model = "gpt-4o-mini"

app = Flask(__name__)

# Enable CORS for all routes in the application
CORS(app)  # This will allow all domains to access the API


# Alternatively, enable CORS for a specific route:
# CORS(app, resources={r"/data": {"origins": "*"}})


def fetch_sentiment(data):
    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
    )

    system_content = f""" You are a helpful assistant tasked with analyzing customer reviews to provide a concise and actionable summary of a product based solely on the provided reviews. Ensure the summary is concise and informative, aiding customers in making a purchase decision. Include insights about how customers feel about the product, emphasizing both positive and negative sentiments. Additionally, include information about the product's packaging quality and delivery time as mentioned in the reviews, highlighting any trends or notable feedback.

Use only the provided reviews for this analysis.

Instructions:

Analyze the text reviews provided for the product.
Generate a clear and concise summary of the product's overall performance, focusing on the general sentiment of customers—how they feel about the product. Include both positive and negative aspects.
Extract key features mentioned by customers, focusing on the following generic features:
Product Quality
Value for Money
Design & Appearance
Comfort (if applicable)
Ease of Use
Performance
Durability
Packaging
Size & Fit
Customer Support/Service
Battery Life (if applicable)
Noise Level
Ease of Installation/Setup
Cleaning & Maintenance
Portability (if applicable)
Temperature Control (if applicable)
Aesthetic Appeal
Versatility
Sustainability/Environmental Impact
Safety Features
Split the features into positive and negative points. Only include features that have a significant number of mentions; omit features that have very few positive or negative reviews.
Do not include explanations about the features; list features as concise bullet points without explanations.
Provide a brief overview of customers' overall feelings about the product, identifying if they are generally satisfied or dissatisfied, and any recurring themes that indicate strong customer sentiments.

Give your response in HTML.
 """

    my_messages = [
        {
            "role": "system",
            "content": system_content
        },
        {
            "role": "user",
            "content": data
        }
    ]

    completion = client.chat.completions.create(
        model=model,
        messages=my_messages,
        max_tokens=800,
        temperature=0.0,
        top_p=1.0,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None
    )

    # Retrieve just response from completion
    assistant_output = completion.choices[0].message.content
    print(assistant_output)

    return assistant_output



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
        sentiment = fetch_sentiment(res)
        sentiment = sentiment[7:-3]
        return jsonify({"status": "success","analysis":sentiment}), 200

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"status": "error"}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)  # Runs on localhost:5000


#def readcomments(data):
#    reviews = json.loads(data)
#    for obj in reviews:
#        print(f"Review: {obj['review']}")


