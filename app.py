# Import necessary Flask modules
from flask import Flask, render_template, request

# Initialize the Flask application
app = Flask(__name__)


# Define the home route that displays a form
@app.route('/')
def index():
    """
    Home page route that renders an HTML form.
    Returns an HTML form where users can enter their name.
    """
    return'''
        <html>
        <body>
            <form action = '/greet' method = "Post">
                Enter your name: <input type = "text" name = "username">
                <input type = "submit" value = "Submit">
                
            </form>
        </body>
        </html>
        '''

# Define the greet route that handles form submission
@app.route('/greet', methods=['POST'])
def greet():
    """
    Greet route that processes the form data.
    Retrieves the username from the form and returns a personalized greeting.
    """
    # Extract the username from the submitted form data
    user_input = request.form['username']
    # Return a personalized greeting message
    return f'Hello, {user_input}! ,welcome to our docker demonstrattion'

# Run the Flask application
if __name__ == '__main__':
    # Start the server on all network interfaces (0.0.0.0) at port 5000
    # This configuration is necessary for Docker containers to accept external connections
    app.run(host='0.0.0.0', port=5000)