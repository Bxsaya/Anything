import json
import csv

# Load the JSON file
with open(r'C:\Users\user\Diani_Data.json', 'r') as f:
    data = json.load(f)

# Extract the headers from the JSON file
headers = list(data[0].keys())

# Open a CSV file for writing
with open(r'C:\Users\user\Diani_Hotels.csv', 'w', newline='') as f:
    writer = csv.writer(f)

    # Write the headers to the CSV file
    writer.writerow(headers)

    # Write each row of data to the CSV file
    for row in data:
        writer.writerow(row.values())
