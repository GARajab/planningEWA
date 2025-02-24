import psycopg2


def main():
    conn = psycopg2.connect(
        "postgres://avnadmin:AVNS_n5QucdaEBLuejT7yqNA@pg-177ad353-planningweb.l.aivencloud.com:16115/defaultdb?sslmode=require"
    )

    query_sql = "SELECT VERSION()"

    cur = conn.cursor()
    cur.execute(query_sql)

    version = cur.fetchone()[0]
    print(version)


if __name__ == "__main__":
    main()
