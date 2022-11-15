import sqlite3


class Database:
    word_list = ["RAFAY", "LION", "PANDA", "TIGER", "DOG", "CAT", "RABBIT", "MOUSE"]

    # Connection Initialization
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS DICTIONARY (ID INTEGER PRIMARY KEY, WORD TEXT NOT NULL )")
        self.con.commit()

    # Insert Function
    def insert_valid_guessing_word(self, guessing_word):
        self.cur.execute("INSERT INTO DICTIONARY VALUES (NULL,?)", (guessing_word,))
        self.con.commit()

    # Get a Record in DB
    def get_valid_guessing_word(self, id):
        self.cur.execute("SELECT * FROM DICTIONARY WHERE id=?", (id,))
        valid_word = self.cur.fetchone()
        print(valid_word)
        return valid_word

    def add_valid_guessing_word(self):
        for word in self.word_list:
            self.insert_valid_guessing_word(word)
