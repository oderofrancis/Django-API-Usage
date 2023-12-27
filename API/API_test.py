import requests
import pandas as pd


def data(company=None):
    url = 'http://127.0.0.1:8000/advocate/?format=json'
    # get json data
    try:
        r = requests.get(url)
        data = r.json()
    except Exception as e:
        print(f"Error fetching JSON data: {e}")
        return None
    
    # convert json data to dataframe
    try:
        df = pd.DataFrame(data)
        df = pd.concat([df.drop(['company'], axis=1), pd.json_normalize(df['company'])], axis=1)

        if company == None:
            df = df
        else:
            df = df[df['name'] == company]
        return df   
    except Exception as e:
        print(f"Error converting JSON data to DataFrame: {e}")
        return None


def event(user=None):
    url = f'http://127.0.0.1:8000/advocate/{user}?format=json'
    # Get the JSON data
    try:
        response = requests.get(url)
        data = response.json()
    except Exception as e:
        print(f"Error fetching JSON data: {e}")
        return None

    # Convert JSON data to a DataFrame
    try:
        df = pd.DataFrame([data])
        df = pd.concat([df.drop(['company'], axis=1), pd.json_normalize(df['company'])], axis=1)
        return df
    except Exception as e:
        print(f"Error converting JSON data to DataFrame: {e}")
        return None