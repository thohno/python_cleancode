# For loops instead of vectorized operations
# Access credentials in the code
# Unsanitized queries

class DatabaseConfig:
    DB_URL = 'postgresql://my_user:my_password@localhost:5432/car_database'

class CarRecords:
    @classmethod
    def fetch_car_records(cls, model):
        query = text("SELECT * FROM cars WHERE model = :model")
        engine = create_engine(DatabaseConfig.DB_URL)
        Session = sessionmaker(bind=engine)
        session = Session()

        result = session.execute(query, {'model': model}).fetchall()
        car_records = np.array(result)

        session.close()

        return car_records


if __name__ == '__main__':
    pass