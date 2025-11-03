import pandas as pd

def add_file_headers(file_path,headers):
    try:
        df = pd.read_csv(file_path, header=None,encoding='latin-1')  # Read without header
        df.columns = headers                     # Assign new headers
        df.to_csv(file_path, index=False)         # Save back
        print(f"Header added successfully to '{file_path}'.")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Error: {e}")

file_path=r"C:\Users\Raghav\OneDrive\Desktop\Sentiment_Analysis_on_Social_Media\data\tweets.csv"
headers=['target','id','date','flag','user','text']
add_file_headers(file_path,headers)