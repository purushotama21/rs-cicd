import psycopg2
conn = psycopg2.connect(
    host="redshift-cluster-2.cn8ui4uqu7fc.us-west-1.redshift.amazonaws.com",
    database="dev",
    user="awsuser",
    port=5439,
    password="Awsuser123")
cur = conn.cursor()
with open('student.sql') as f:
    cur.execute(f.read())
#sqlfile=open("emp.sql","r")
#cur.execute("sqlfile")
print("connection succussfully established")
cur.execute("select * from users limit 5")
print(cur.fetchall())
print(".........")
print()
