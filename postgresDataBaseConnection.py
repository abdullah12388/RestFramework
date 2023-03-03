import psycopg2

#database connection variables
host='localhost'
port= 5432
user='postgres'
password='As123'
database='products'

conn = None

try:
    with psycopg2.connect(dbname=database,
                                user=user,
                                password=password,
                                host=host,
                                port=port,) as conn:
        with conn.cursor() as cur:

            #Drop table every time I run the script
            cur.execute('DROP TABLE IF EXISTS Cloth')

            #create table
            create_script = '''CREATE TABLE IF NOT EXISTS Cloth (
                                    id          int PRIMARY KEY,
                                    name        varchar(40))'''
            cur.execute(create_script)
            
            #Inser or create data
            insert_script = '''INSERT INTO Cloth (id, name) VALUES (%s, %s)'''
            insert_values = [(1, 'asdasd'), (2, 'dsadsa'), (3, 'qweqwe'), (4, 'ewqewq'), (5, 'Ali'),]
            for record in insert_values:
                cur.execute(insert_script, record)

            #Update data
            update_script = ''' UPDATE Cloth
                                SET name = %s
                                where id = %s;
            '''
            update_values = ('Ahmed',1)
            cur.execute(update_script, update_values)

            #Delete data
            delete_script = 'DELETE FROM Cloth WHERE name = %s'
            delete_values = ('Ali',)
            cur.execute(delete_script, delete_values)

            #Read data
            read_script = ''' SELECT * FROM CLOTH '''
            cur.execute(read_script)
            for row in cur.fetchall():
                print(row[0],row[1])

except Exception as ex:
    print(ex)
finally:
    if conn is not None:
        conn.close()