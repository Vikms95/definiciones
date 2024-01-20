import csv

spanish_blacklist = []
english_blacklist = []

def load_spanish_blacklist(file_name='spanish_blacklist.csv'):
    try:
        with open(file_name, newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) > 1:
                    spanish_blacklist.extend(row)
                else:
                    spanish_blacklist.append(row[0])
            return spanish_blacklist
    except FileNotFoundError:
        return []