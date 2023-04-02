# Data-Engineer - Uber - Study CaseS

## Uber

The primary objective of this project is to develop a data engineering pipeline to ingest, store, process, and analyze Uber ride data for analytics and demand forecasting. The insights generated from this pipeline will help Uber make data-driven decisions on resource allocation, pricing strategies, and improving the overall user experience.

### Data Pipeline Steps

1. **Infrastructure**: Provision necessary GCP resources using Terraform.
2. **Data Modeling**: Use Python API Faker to generate realistic Uber ride data, including pick-up and drop-off locations, ride distances, timestamps, passenger details, and driver details.
3. **Data Storage**: Store the dummy data in PostgreSQL
4. **Data Ingestion**: Ingest the generated data into the pipeline using Airbyte.
5. **Data Lake Raw Zone**: Store the ingested data from PostgreSQL in the raw zone of a GCP Storage data lake.
6. **Data Processing**: Process and clean the raw data using Spark.
7. **Data Lake Processing Zone**: Store the processed data in the processing zone of the GCP Storage data lake.
8. **Data Warehouse**: Load the transformed data into Snowflake, a cloud-based data warehouse, for further analysis and reporting.
9. **Data Transformation**: Create a View for analytics using DBT.

### Pipeline Diagram

![alt text](https://github.com/makima0499/Data-Engineer-Uber-K8S/blob/dev/7.DataPipeline.png)

### Tools

* Python
* Terraform
* Postgres
* Airbyte
* Spark
* GCP GKE
* GCP GCS
* Snowflake
* DBT

### Note

This repository is provided for study purposes only, focusing on data engineering pipelines.

## License

[MIT](https://choosealicense.com/licenses/mit/)
