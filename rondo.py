import sys, argparse

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
    print(f"{args.filename} {args.sql} : {args.export}")

    # Load csv as a database table with the header row as field names

    # Run transformations specified in a file

    # Process 1+ Export file

    # Optionally drop the user in to an interactive shell to query the database

    # Close database and exit

    print("End!")

if __name__ == "__main__":
    main()
