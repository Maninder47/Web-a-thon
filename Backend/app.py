from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# Route for the homepage
@app.route('/')
def index():
    # Connect to the SQLite database
    conn = sqlite3.connect('scraped_data.db')
    cursor = conn.cursor()
    
    # Retrieve all data from the database
    cursor.execute('SELECT content FROM data')
    data = cursor.fetchall()
    
    # Close the database connection
    conn.close()
    
    # Render the data on the webpage
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)