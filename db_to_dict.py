import sqlite3
# cursor.execute(f"PRAGMA table_info({'words'});")
path = '/media/vikms/Kindle/system/vocabulary/vocab.db'

def db_to_dict():
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    cursor.execute("SELECT word FROM words WHERE lang='es';")
    words = cursor.fetchall()
    return words