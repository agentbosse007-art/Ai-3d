import os
import sqlite3

class ModelLibrary:
    def __init__(self, db_name='model_library.db'):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        with self.conn:
            self.conn.execute('''CREATE TABLE IF NOT EXISTS models (
                                    id INTEGER PRIMARY KEY,
                                    name TEXT NOT NULL,
                                    file_type TEXT NOT NULL,
                                    file_path TEXT NOT NULL
                                );''')

    def add_model(self, name, file_type, file_path):
        with self.conn:
            self.conn.execute('INSERT INTO models (name, file_type, file_path) VALUES (?, ?, ?)', (name, file_type, file_path))

    def get_model(self, model_id):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM models WHERE id = ?', (model_id,))
        return cursor.fetchone()

    def get_all_models(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM models')
        return cursor.fetchall()

    def delete_model(self, model_id):
        with self.conn:
            self.conn.execute('DELETE FROM models WHERE id = ?', (model_id,))

    def close(self):
        self.conn.close()


if __name__ == '__main__':
    library = ModelLibrary()
    # Example usage:
    # library.add_model('Sample Model', 'STL', '/path/to/sample_model.stl')
    # print(library.get_all_models())
    library.close()