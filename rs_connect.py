import psycopg2
def handler(event,context):
    conn = psycopg2.connect(
        host="redshift-cluster-1.cn8ui4uqu7fc.us-west-1.redshift.amazonaws.com",
        database="dev",
        user="admin",
        port=5439,
        password="Admin123")
    cur = conn.cursor()
    print("connection succussfully established")
    cur.execute("select * from users")
    print(cur.fetchall())
    print(".........")
    print()
    conn.close()