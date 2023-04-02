import psycopg2
import random
from faker import Faker
from datetime import timedelta, timezone
import pytz
import configparser

# Get the full path to the config.ini file
config = configparser.ConfigParser()
config.read("/Users/gomes/Desktop/Projects/Data Engineer/7-Project/config/config.ini")

# PostgreSQL connection details
host = config.get("postgres", "host")
port = config.get("postgres", "port")
database = config.get("postgres", "database")
user = config.get("postgres", "user")
password = config.get("postgres", "password")

# Connect to the PostgreSQL database
conn = psycopg2.connect(host=host, port=port, dbname=database, user=user, password=password)
cursor = conn.cursor()

# Create the Uber ride data table
cursor.execute("""
CREATE TABLE IF NOT EXISTS uber_rides (
    id SERIAL PRIMARY KEY,
    passenger_name VARCHAR(255),
    driver_name VARCHAR(255),
    pickup_lat FLOAT,
    pickup_lng FLOAT,
    dropoff_lat FLOAT,
    dropoff_lng FLOAT,
    ride_distance FLOAT,
    pickup_time TIMESTAMP,
    dropoff_time TIMESTAMP
);
""")
conn.commit()

# Generate and insert dummy data
fake = Faker()
num_records = 1000

for _ in range(num_records):
    passenger_name = fake.name()
    driver_name = fake.name()
    pickup_lat = fake.latitude()
    pickup_lng = fake.longitude()
    dropoff_lat = fake.latitude()
    dropoff_lng = fake.longitude()
    ride_distance = random.uniform(0.5, 20)  # Distance in miles, adjust range as needed
    pickup_time = fake.date_time_this_year(before_now=True, after_now=False, tzinfo=pytz.timezone(fake.timezone()))
    pickup_time = pickup_time.replace(tzinfo=timezone.utc)  # Add timezone information to pickup_time
    ride_duration = timedelta(minutes=random.randint(5, 60))
    dropoff_time = pickup_time + ride_duration
    dropoff_time = dropoff_time.replace(tzinfo=timezone.utc)  # Add timezone information to dropoff_time

    cursor.execute("""
    INSERT INTO uber_rides (passenger_name, driver_name, pickup_lat, pickup_lng, dropoff_lat, dropoff_lng, ride_distance, pickup_time, dropoff_time)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
    """, (passenger_name, driver_name, pickup_lat, pickup_lng, dropoff_lat, dropoff_lng, ride_distance, pickup_time, dropoff_time))

conn.commit()

print(f"Inserted {num_records} records into the uber_rides table.")

cursor.close()
conn.close()
