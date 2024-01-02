def create_table(db, table_name, *columns):
    columns = (', ').join(columns)
    con = db.get_conection()
    cursor = db.get_cursor(con)
    cursor.execute(f"""CREATE TABLE IF NOT EXISTS {table_name}({columns})""")
    db.commit_and_close(con)

def insert_data(db, table_name, data_list):
    data_schema = '(' + ('?,'*len(data_list[0]))[:-1] + ')' # e.g (?,?,?)
    con = db.get_conection()
    cursor = db.get_cursor(con)
    cursor.executemany(f'INSERT OR IGNORE INTO {table_name} VALUES {data_schema}', data_list)
    db.commit_and_close(con)

def retrieve_data(db, table, query):
    db.check_table_exists(table)
    if query == 'all' and table == 'books':
        sql_cmd = ''
    elif table == 'books':
        sql_cmd = f"WHERE book_name LIKE '%{query}%' OR author LIKE '%{query}%'"
    elif table == 'quotes':
        sql_cmd = f"WHERE book_id LIKE '{query}'"
    con = db.get_conection()
    cursor = db.get_cursor(con)
    cursor.execute(f"SELECT * FROM {table} {sql_cmd}")
    data = cursor.fetchall()
    db.commit_and_close(con)
    return data
