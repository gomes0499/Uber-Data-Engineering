from pyspark.sql import SparkSession
import configparser

# Get the full path to the config.ini file
config = configparser.ConfigParser()
config.read("/Users/gomes/Desktop/Projects/Data Engineer/7-Project/config/config.ini")

# Initialize Spark
spark = SparkSession.builder \
    .appName("processed-uber-rides-to-snowflake") \
    .config("spark.jars", "jars/gcs-connector-hadoop3-latest.jar,jars/snowflake-jdbc-3.13.11.jar,jars/spark-snowflake_2.12-2.11.2-spark_3.3.jar") \
    .config("spark.hadoop.fs.gs.impl", "com.google.cloud.hadoop.fs.gcs.GoogleHadoopFileSystem") \
    .config("spark.hadoop.fs.gs.auth.service.account.enable", "true") \
    .config("spark.hadoop.fs.gs.auth.service.account.json.keyfile", "../service-account/wu6project-3e0f2c673612.json") \
    .getOrCreate()


# Define input path
input_parquet_path = "gs://wu7process/process/uber_rides/"

# Read Parquet file
df = spark.read.format("parquet").load(input_parquet_path)

# Snowflake connection options
snowflake_options = {
    "sfUrl": config.get("snowflake", "sfUrl"),
    "sfUser": config.get("snowflake", "sfUser"),
    "sfPassword": config.get("snowflake", "sfPassword"),
    "sfDatabase": config.get("snowflake", "sfDatabase"),
    "sfSchema": config.get("snowflake", "sfSchema"),
    "sfWarehouse": config.get("snowflake", "sfWarehouse")
}

# Write the processed data to Snowflake
df.write \
    .format("snowflake") \
    .options(**snowflake_options) \
    .option("dbtable", "ubertable") \
    .mode("append") \
    .save()

# Stop Spark
spark.stop()
