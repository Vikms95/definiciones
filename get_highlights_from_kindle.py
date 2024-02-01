path = '/media/vikms/Kindle/documents/My Clippings.txt'

def get_highlights_from_kindle():
    quotes = []
    with open(path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            if(line.startswith('-')):
                quotes.append(lines[i + 2])
    return quotes