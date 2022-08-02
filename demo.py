import psycopg2

conn = psycopg2.connect('dbname=examples')

cursor = conn.cursor()

cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS todo;")

cur.execute("""
    CREATE TABLE todos (
    id serial PRIMARY KEY,
    description VARCHAR NOT NULL,
    created_at TIMESTAMP 
    );
""")

conn.commit()

cur.close()
conn.close()