import sqlite3
import matplotlib.pyplot as plt
from datetime import datetime

# Connect to SQLite database
conn = sqlite3.connect('historical_data.db')
cursor = conn.cursor()

# Query the historical data
cursor.execute('''
SELECT timestamp, government_security_name, percent
FROM historical_data
''')
rows = cursor.fetchall()

# Organize the data by security name
data_by_security = {}
for row in rows:
    timestamp = datetime.strptime(row[0], '%Y-%m-%dT%H:%M:%SZ')
    name = row[1]
    percent = row[2]
    if name not in data_by_security:
        data_by_security[name] = []
    data_by_security[name].append((timestamp, percent))

# Create time series graph
plt.figure(figsize=(10, 5))
for name, values in data_by_security.items():
    values.sort()
    dates, percents = zip(*values)
    plt.plot(dates, percents, label=name)

plt.xlabel('Date')
plt.ylabel('Percent')
plt.title('Government Security Percent Changes Over Time')
plt.legend()
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig('docs/comparison_graph.png')
