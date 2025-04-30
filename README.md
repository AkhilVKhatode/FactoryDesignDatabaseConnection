# FactoryDesignDatabaseConnection

A clean Python implementation of the Factory Pattern for creating database connections (MySQL, PostgreSQL, SQLite).

## Features

- Factory interface for creating database connections
- Supports MySQL, PostgreSQL, and SQLite
- Consistent interface through abstract base class
- Easy to extend with new database types

## Basic Usage

```python
from db_connection_factory import DatabaseConnectionFactory

# Create a MySQL connection
mysql_conn = DatabaseConnectionFactory.create_connection(
    'mysql',
    host='localhost',
    user='your_user',
    password='your_pass',
    database='your_db'
)
conn = mysql_conn.connect()

# Execute queries...
cursor = conn.cursor()
cursor.execute("SELECT * FROM your_table")
print(cursor.fetchall())

# Close connection
mysql_conn.close()
```

### Supported Databases
- MySQL
```DatabaseConnectionFactory.create_connection('mysql', ...)```
- PostgreSQL
```DatabaseConnectionFactory.create_connection('postgresql', ...)```
- SQLite
```DatabaseConnectionFactory.create_connection('sqlite', db_file='database.db')```
