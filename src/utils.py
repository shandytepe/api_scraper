import pandas as pd

def current_time():
    # Get the current timestamp
    current_timestamp = pd.Timestamp.now()

    # Convert the Timestamp object to a formatted string
    formatted_timestamp = current_timestamp.strftime('%Y-%m-%d %H:%M:%S')
    
    return formatted_timestamp