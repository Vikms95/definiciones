import sqlite3

path = '/media/vikms/Kindle/system/vocabulary/vocab.db'

def get_words_from_kindle():
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