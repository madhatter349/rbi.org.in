import requests
import pandas as pd
from selectolax.parser import HTMLParser

def riskFreeInterestRate(url='https://www.rbi.org.in/'):
    try:
        user_agent = requests.get('https://techfanetechnologies.github.io/latest-user-agent/user_agents.json').json()[-2]
        headers = {'user-agent': user_agent}

        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            html_content = response.content
            parser = HTMLParser(html_content)
            selector = '#wrapper > div:nth-child(10) > table'
            nodes = parser.css(selector)
            if nodes:
                data = nodes[0].html
                df = pd.read_html(data)[0].iloc[4:13]
                df.columns = ['GovernmentSecurityName', 'Percent']
                df['GovernmentSecurityName'] = df['GovernmentSecurityName'].str.strip()
                df['Percent'] = df['Percent'].str.rstrip('% #*').str.lstrip(': ').astype('float32')
                json_data = df.to_json(orient='records')
                with open('RiskFreeInterestRate-new.json', 'w') as jsonFile:
                    jsonFile.write(json_data)
                print("Data fetched and saved successfully.")
            else:
                print("No table found with the given selector.")
        else:
            print(f'Failed to fetch the URL: {response.status_code}')
    except Exception as e:
        print(f"An error occurred: {e}")

riskFreeInterestRate()
