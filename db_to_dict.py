import sqlite3
# cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
path = '/media/vikms/Kindle/system/vocabulary/vocab.db'

def db_to_dict():
    conn = sqlite3.connect(path)
    cursor = conn.cursor()

    cursor.execute("""
               SELECT words.word, MIN(lookups.usage) as usage FROM words 
               LEFT JOIN lookups ON words.id = lookups.word_key
               WHERE words.lang = 'es'
               GROUP BY words.word;
               """
               )
    
    words_with_usage = cursor.fetchall()
    return words_with_usage