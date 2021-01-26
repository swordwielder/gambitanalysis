import pandas as pd

read_file = pd.read_csv (r'message.txt')
read_file.to_csv (r'sportsdata.csv', index=None)
