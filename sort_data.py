import json
from datetime import datetime

# Load the JSON data from 'metals-history.json'
with open('metals-history.json', 'r') as file:
    data = json.load(file)

# Sort the data by the 'date' field (adjust this if necessary)
sorted_data = sorted(data, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'))

# Save the sorted data back to a new JSON file
with open('sorted_metals-history.json', 'w') as file:
    json.dump(sorted_data, file, indent=4)

print("Data sorted successfully!")
