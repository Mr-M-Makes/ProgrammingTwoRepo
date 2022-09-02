import csv
import sqlite3

def main():
    file_content = get_data_csv("weather_lr.csv")

    db = database()
    db.create_tables(file_content[0])


class database:
    def __init__(self):
        self.connection = sqlite3.connect("database.db")
        self.c = self.connection.cursor()

    def create_tables(self, headers):
        self.c.execute(
            f"""CREATE TABLE IF NOT EXISTS data (
                id INTEGER PRIMARY KEY,
                {headers[0]} TEXT NOT NULL,
                {headers[1]} TEXT NOT NULL,
                {headers[2]} TEXT NOT NULL,
                {headers[3]} TEXT NOT NULL,
                {headers[4]} TEXT NOT NULL,
                {headers[5]} TEXT NOT NULL,
                {headers[6]} TEXT NOT NULL,
                {headers[7]} TEXT NOT NULL
            );"""
        )


def get_data_csv(file):
    with open(file, "r") as csv_file:
        reader = csv.reader(csv_file, delimiter=",")
    
        return list(reader)
        

if __name__ == "__main__":
    main()