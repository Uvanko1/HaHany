import sqlite3

# создаем базу данных
con = sqlite3.connect('../saves/save_data.db')
cur = con.cursor()


def get_save_position():
    cur.execute("""CREATE TABLE IF NOT EXISTS spawn(
           id INTEGER PRIMARY KEY AUTOINCREMENT
             NOT NULL
             UNIQUE,
           SpawnX INTEGER NOT NULL,
           SpawnY INTEGER NOT NULL);""")

    data = cur.execute('''SELECT SpawnX, SpawnY FROM spawn''').fetchall()
    spawn_pos_x = 9600
    spawn_pos_y = 9600
    if not data:
        cur.execute('''INSERT INTO spawn (SpawnX, SpawnY)
                                                        VALUES (?, ?)''', [spawn_pos_x, spawn_pos_y])

    data = cur.execute('''SELECT SpawnX, SpawnY FROM spawn''').fetchall()
    print(data[-1][0], data[-1][1])
    return [data[-1][0], data[-1][1]]


def save_position(x, y):
    cur.execute('''INSERT INTO spawn (SpawnX, SpawnY)
                            VALUES (?, ?);''', [x, y])
    print(cur.execute('''SELECT SpawnX, SpawnY FROM spawn''').fetchall())