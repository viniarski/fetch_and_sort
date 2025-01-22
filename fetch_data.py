import yfinance as yf
import json
from datetime import datetime

# Function to format data
def format_data(ticker_data, metal_name):
    formatted_data = []
    for data_point in ticker_data:
        date = data_point[0]  # This is the date (Timestamp)
        formatted_data.append({
            "date": date.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3],  # Format as ISO 8601
            "close": float(data_point[4]),  # Close price
            "volume": float(data_point[5]),  # Volume
            "open": float(data_point[1]),  # Open price
            "high": float(data_point[2]),  # High price
            "low": float(data_point[3]),  # Low price
            "metal": metal_name  # Metal name (either 'gold' or 'silver')
        })
    return formatted_data

# Fetch gold and silver data from 2004-01-01 to 2025-01-22
gold_data = yf.download('GC=F', start='2004-01-01', end='2025-01-22', interval='1d').itertuples(index=True, name=None)
silver_data = yf.download('SI=F', start='2004-01-01', end='2025-01-22', interval='1d').itertuples(index=True, name=None)

# Format the data
gold_formatted = format_data(gold_data, "gold")
silver_formatted = format_data(silver_data, "silver")

# Sort the data by date to ensure they are ordered correctly (if not already sorted)
gold_formatted.sort(key=lambda x: x["date"])
silver_formatted.sort(key=lambda x: x["date"])

# Interleave the gold and silver data, starting with gold
combined_data = []
for gold_entry, silver_entry in zip(gold_formatted, silver_formatted):
    combined_data.append(gold_entry)  # Add gold first
    combined_data.append(silver_entry)  # Then add silver

# If one of the lists is longer than the other, append the remaining items
combined_data.extend(gold_formatted[len(silver_formatted):])
combined_data.extend(silver_formatted[len(gold_formatted):])

# Save the combined data to a JSON file
with open('metals-history.json', 'w') as file:
    json.dump(combined_data, file, indent=4)

print("Data has been saved to 'metals-history.json'.")
