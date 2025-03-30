from flask import Flask, jsonify
from bs4 import BeautifulSoup
import requests
import os

app = Flask(__name__)

@app.route('/extract-links', methods=['GET'])
def extract_link():
    url = "https://bingotingo.com/best-social-media-platforms/"  # Fixed URL

    try:
        # Fetch the webpage content
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(response.text, "html.parser")

        # Find the first div with class "su-button-center"
        div = soup.find("div", class_="su-button-center")

        # Extract the first link inside it
        if div:
            a_tag = div.find("a")  # Find first <a> inside the div
            if a_tag and a_tag.has_attr("href"):
                return jsonify({"link": a_tag["href"]})

        return jsonify({"error": "No valid link found"}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Use Render's assigned port
    app.run(host='0.0.0.0', port=port)
