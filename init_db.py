import sqlite3

# Connect to the SQLite database (creates the database file if it doesn't exist)
conn = sqlite3.connect('historical_data.db')
cursor = conn.cursor()

# Create a table to store the historical data
cursor.execute('''
CREATE TABLE IF NOT EXISTS historical_data (
    timestamp TEXT,
    government_security_name TEXT,
    percent REAL
)
''')

conn.commit()
conn.close()
