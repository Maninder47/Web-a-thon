import requests
from bs4 import BeautifulSoup
import sqlite3

# URL of the website you want to scrape
url = 'https://www.ibm.com/blog/category/cybersecurity/'
# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all elements with the class name you're interested in
    elements = soup.find_all(class_='container grid')
    # Connect to SQLite database
    conn = sqlite3.connect('scraped_data.db')
    cursor = conn.cursor()

    # Loop through and insert each element's text into the database
    for element in elements:
        content = element.get_text()
        cursor.execute('INSERT INTO data (content) VALUES (?)', (content,))
        print(content)
    # Commit changes and close the connection
    conn.commit()
    conn.close()

    print("Data successfully inserted into the database.")

else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
