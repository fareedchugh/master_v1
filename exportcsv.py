import pandas as pd
import oracledb as cx_Oracle
cx_Oracle.init_oracle_client(lib_dir=r"C:\oracle\instantclient_19_12\instantclient_23_9")

# Oracle database connection parameters
username = 'TCS_FAREED'
password = 'TCS_FAREED'
dsn = 'localhost:1521/XE'

# SQL query
query = "SELECT * FROM Department"

# Connect to Oracle
connection = cx_Oracle.connect(user=username, password=password, dsn=dsn)

# Read data into a pandas DataFrame
df = pd.read_sql(query, con=connection)

# Export DataFrame to CSV
df.to_csv('oracle_data.csv', index=False)

print("Data exported successfully to oracle_data.csv")

# Close the connection
connection.close()
#commented on v1