from pyspark.sql import SparkSession

# Initialize Spark
spark = SparkSession.builder \
    .appName("process-uber-rides") \
    .config("spark.jars", "jars/gcs-connector-hadoop3-latest.jar") \
    .config("spark.hadoop.fs.gs.impl", "com.google.cloud.hadoop.fs.gcs.GoogleHadoopFileSystem") \
    .config("spark.hadoop.fs.gs.auth.service.account.enable", "true") \
    .config("spark.hadoop.fs.gs.auth.service.account.json.keyfile", "../service-account/wu6project-3e0f2c673612.json") \
    .getOrCreate()

# Define input and output paths
input_parquet_path = "gs://wu7raw/raw/uber_rides/*"
output_parquet_path = "gs://wu7process/process/uber_rides/"

# Read Parquet file
df = spark.read.format("parquet").load(input_parquet_path)

# Apply transformations
# Filter rides with a specific condition, such as distance > 2 miles
df_filtered = df.filter(df["ride_distance"] > 2)

# Write the processed data to the output path
df_filtered.write.parquet(output_parquet_path)

# Stop Spark
spark.stop()
