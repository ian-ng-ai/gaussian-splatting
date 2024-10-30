import sqlite3

def db_to_txt_cameras(db_file, txt_file):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Check if the 'cameras' table exists
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='cameras';")
    if not cursor.fetchone():
        print("Table 'cameras' does not exist.")
        return

    with open(txt_file, 'w') as f:
        f.write("Table: cameras\n")
        f.write("=" * 40 + "\n")

        # Retrieve all rows from the 'cameras' table
        cursor.execute("SELECT * FROM cameras")
        rows = cursor.fetchall()

        # Get column names
        column_names = [description[0] for description in cursor.description]
        f.write("\t".join(column_names) + "\n")

        # Write each row to the text file
        for row in rows:
            f.write("\t".join(map(str, row)) + "\n")

    # Close the database connection
    conn.close()

# Usage example
# Usage example
db_to_txt_cameras('/home/ian_ng/Downloads/gs-data/fixed_camera_intrinsics_COLMAP/distorted/database.db', './output.txt')