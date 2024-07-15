import json
import sqlite3
from datetime import datetime

# Load new data
with open('RiskFreeInterestRate-new.json') as f:
    new_data = json.load(f)

# Connect to SQLite database
conn = sqlite3.connect('historical_data.db')
cursor = conn.cursor()

# Insert new data with a timestamp
timestamp = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
for entry in new_data:
    cursor.execute('''
    INSERT INTO historical_data (timestamp, government_security_name, percent)
    VALUES (?, ?, ?)
    ''', (timestamp, entry['GovernmentSecurityName'], entry['Percent']))

conn.commit()
conn.close()
