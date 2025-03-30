from flask import Flask, jsonify
from bs4 import BeautifulSoup
import requests
import os

app = Flask(__name__)

@app.route('/extract-links', methods=['GET'])
def extract_links():
    url = "https://bingotingo.com/best-social-media-platforms/"  # Fixed URL

    try:
        # Fetch the webpage content
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(response.text, "html.parser")

        # Find all divs with class "su-button-center"
        divs = soup.find_all("div", class_="su-button-center")

        # Extract all href links
        links = [div.find("a")["href"] for div in divs if div.find("a") and div.find("a").has_attr("href")]

        return jsonify({"links": links})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Use Render's assigned port
    app.run(host='0.0.0.0', port=port)
