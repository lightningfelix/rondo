import sys, argparse, sqlite3
import pandas as pd
from pathlib import Path

def create_database(conn: sqlite3.Connection, files: list[str]) -> sqlite3.Cursor:
    for file in files:
        infile = pd.read_csv(file)
        infile.to_sql(Path(file).stem, conn, if_exists='replace', index=False)
    return conn.cursor()

def main():
    print("Begin!")

    # Read args
    parser = argparse.ArgumentParser(
            prog='Rondo',
            description='Transform .csv data using SQL')
    parser.add_argument('-f', '--filename', action='extend', nargs='+', type=str)
    parser.add_argument('-s', '--sql', nargs='?', type=str)
    parser.add_argument('-e', '--export', action='extend', nargs='*', type=str)
    args = parser.parse_args()

    # Load csv as a database table with the header row as field names
    connection = sqlite3.connect(':memory:')
    cursor = create_database(connection, args.filename)

    # Run transformations specified in a file
    with open(args.sql, 'r') as sqlfile:
        for line in sqlfile:
            cursor.execute(line)
            connection.commit()

    # Process 1+ Export file
    for exports in args.export:
        export_args = exports.split(';', 1)
        query = export_args[1] if len(export_args) > 1 else f"SELECT * FROM {Path(args.filename[0]).stem}"
        data = pd.read_sql_query(query, connection)
        data.to_csv(export_args[0], index=False)

    # Close database and exit
    connection.close()
    print("End!")

if __name__ == "__main__":
    main()
