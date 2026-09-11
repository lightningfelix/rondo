import sys, argparse, sqlite3
import pandas as pd

def main():
    print("Begin!")

    # Read args
    parser = argparse.ArgumentParser(
            prog='Rondo',
            description='Transform .csv data using SQL')
    parser.add_argument('filename')
    parser.add_argument('-s', '--sql', type=str)
    parser.add_argument('-e', '--export', action='extend', nargs='*', type=str)
    args = parser.parse_args()

    # Load csv as a database table with the header row as field names
    connection = sqlite3.connect(':memory:')
    infile = pd.read_csv(args.filename)
    infile.to_sql('infile', connection, if_exists='replace', index=False)
    
    cursor = connection.cursor()
    output = cursor.execute("SELECT * FROM infile")

    # Run transformations specified in a file
    with open(args.sql, 'r') as sqlfile:
        for line in sqlfile:
            cursor.execute(line)
            connection.commit()

    # Process 1+ Export file
    for exports in args.export:
        export_args = exports.split(';', 1)
        query = export_args[1] if len(export_args) > 1 else "SELECT * FROM infile"
        data = pd.read_sql_query(query, connection)
        data.to_csv(export_args[0], index=False)

    # Close database and exit
    connection.close()
    print("End!")

if __name__ == "__main__":
    main()
