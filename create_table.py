import psycopg2
from psycopg2 import sql

# Connect to the PostgreSQL server
conn = psycopg2.connect(
    dbname="postgres",  # Default database name in PostgreSQL
    user="postgres",    # Default user
    password="mysecretpassword",  # Password from the Docker container
    host="postgres",   # Host, since we're running the container locally
    port="5432"         # Port, mapped to localhost
)

# Create a cursor to interact with the database
cur = conn.cursor()

# SQL to create a new table
create_table_query = '''
CREATE TABLE IF NOT EXISTS employee (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    department VARCHAR(100)
);
'''

# Execute the create table query
cur.execute(create_table_query)

# Commit changes and close the cursor and connection
conn.commit()

# Insert a record into the table
insert_query = '''
INSERT INTO employee (name, age, department)
VALUES (%s, %s, %s);
'''
cur.execute(insert_query, ('John Doe', 30, 'Engineering'))
conn.commit()

# Fetch and display the data to confirm it was inserted
cur.execute("SELECT * FROM employee;")
rows = cur.fetchall()
print("Employee Table Data:")
for row in rows:
    print(row)

# Clean up
cur.close()
conn.close()
