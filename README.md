Program 1: Merge Gold and Silver Data
This Python program fetches historical data for Gold and Silver prices (from yfinance for Gold and cryptocompare for Silver), formats and merges them, and exports the results as a JSON file. The data is structured by alternating between Gold and Silver data entries, ensuring that the price history is neatly formatted.

Features:
Fetches historical price data for Gold and Silver.
Merges the data into a single, alternating sequence: Gold, Silver, Gold, Silver...
Outputs the formatted data as a JSON file named metals-history.json.

Program 2: Sort Metals Price History Data
This Python program reads the existing metals-history.json file containing historical data for Gold and Silver, sorts the data based on the date field, and saves the sorted data to a new file named sorted_metals-history.json.

Features:
Loads data from the metals-history.json file.
Sorts the data by the date field in ascending order.
Outputs the sorted data to a new file, sorted_metals-history.json.
