# Identify the 3 code smells from the following list:
# Lists instead of numpy arrays
# For loops instead of vectorized operations
# Access credentials in the code
# Unsanitized queries
# Generic exception handling

db_credentials = {
    'user': 'my_user',
    'password': 'my_password',
    'host': 'localhost',
    'port': '5432',
    'database': 'car_database'
}
def fetch_car_records(model):
    query = f"SELECT * FROM cars WHERE model = '{model}'"

    connection = psycopg2.connect(**db_credentials)
    cursor = connection.cursor()
    cursor.execute(query)

    car_records = []
    for row in cursor.fetchall():
        car_records.append(row)

    connection.close()
    return car_records


if __name__ == '__main__':
    pass