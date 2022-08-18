import sqlite3


def main():
    f = open('../sql/init.sql', 'r')
    conn = sqlite3.connect('../candy.db')
    rawsql = f.read().replace("\n", "").split(";")
    for i in rawsql:
        conn.execute(i)
    conn.close()
    print('Success!')


if __name__ == '__main__':
    main()
