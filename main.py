from abc import ABC, abstractmethod
import mysql.connector
import psycopg2
import sqlite3

class DatabaseConnection(ABC):
    """Abstract base class for database connections"""
    
    @abstractmethod
    def connect(self):
        pass
    
    @abstractmethod
    def close(self):
        pass


class MySQLConnection(DatabaseConnection):
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        return self.connection

    def close(self):
        if self.connection:
            self.connection.close()


class PostgreSQLConnection(DatabaseConnection):
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        self.connection = psycopg2.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        return self.connection

    def close(self):
        if self.connection:
            self.connection.close()


class SQLiteConnection(DatabaseConnection):
    def __init__(self, db_file):
        self.db_file = db_file
        self.connection = None

    def connect(self):
        self.connection = sqlite3.connect(self.db_file)
        return self.connection

    def close(self):
        if self.connection:
            self.connection.close()


class DatabaseConnectionFactory:
    @staticmethod
    def create_connection(db_type, **kwargs):
        if db_type == 'mysql':
            return MySQLConnection(
                host=kwargs.get('host'),
                user=kwargs.get('user'),
                password=kwargs.get('password'),
                database=kwargs.get('database')
            )
        elif db_type == 'postgresql':
            return PostgreSQLConnection(
                host=kwargs.get('host'),
                user=kwargs.get('user'),
                password=kwargs.get('password'),
                database=kwargs.get('database')
            )
        elif db_type == 'sqlite':
            return SQLiteConnection(db_file=kwargs.get('db_file'))
        else:
            raise ValueError(f"Unsupported database type: {db_type}")

try:
    # MySQL connection
    mysql_conn = DatabaseConnectionFactory.create_connection(
        'mysql',
        host='localhost',
        user='root',
        password='password',
        database='test_db'
    )
    mysql_conn.connect()
    print("MySQL connection established")
    
    # PostgreSQL connection
    pg_conn = DatabaseConnectionFactory.create_connection(
        'postgresql',
        host='localhost',
        user='postgres',
        password='password',
        database='test_db'
    )
    pg_conn.connect()
    print("PostgreSQL connection established")
    
    # SQLite connection
    sqlite_conn = DatabaseConnectionFactory.create_connection(
        'sqlite',
        db_file='example.db'
    )
    sqlite_conn.connect()
    print("SQLite connection established")

finally:
    # Close all connections
    mysql_conn.close()
    pg_conn.close()
    sqlite_conn.close()
