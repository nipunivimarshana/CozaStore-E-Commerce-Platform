# We are using Flask, a lightweight web framework, to act as our API Gateway
# and to serve the frontend files for now.
from flask import Flask, send_from_directory, jsonify

# Initialize the Flask application
# We tell Flask where to find the static frontend files.
# The '..' means go up one directory from 'api-gateway' to the project root,
# then into the 'frontend' folder.
app = Flask(__name__, static_folder='../frontend', static_url_path='/')

# --- HTML Serving Routes ---

# This route serves the main homepage (index.html)
@app.route('/')
def index():
    # send_from_directory will securely find and send the file.
    return send_from_directory(app.static_folder, 'index.html')

# This is a "catch-all" route. It will serve any other .html file from the frontend folder.
# This allows us to navigate to /product.html, /about.html etc.
@app.route('/<path:filename>')
def serve_html(filename):
    # We ensure the filename ends with .html for security
    if filename.endswith(".html"):
        return send_from_directory(app.static_folder, filename)
    else:
        # If it's not an html file, it might be a static asset like css or js,
        # which Flask's static_folder handling will manage automatically.
        # We return a 404 Not Found error for any other direct path requests.
        return "File not found", 404

# This is the standard Python entry point.
# When you run 'python app.py', this code will execute.
if __name__ == '__main__':
    # We run the app in debug mode on port 5000.
    # Debug mode automatically reloads the server when you save changes.
    app.run(port=5000, debug=True)

    