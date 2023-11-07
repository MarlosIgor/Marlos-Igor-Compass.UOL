import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from datetime import datetime


args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node Data_Catalog_Series_TRT
Data_Catalog_Series_TRT_node1697832419820 = (
    glueContext.create_dynamic_frame.from_catalog(
        database="db_trt_series",
        table_name="series",
        transformation_ctx="Data_Catalog_Series_TRT_node1697832419820",
    )
)

# Script generated for node Data_Catalog_Movies_TRT
Data_Catalog_Movies_TRT_node1697743209188 = (
    glueContext.create_dynamic_frame.from_catalog(
        database="db_trt_movies",
        table_name="movies",
        transformation_ctx="Data_Catalog_Movies_TRT_node1697743209188",
    )
)

# Script generated for node Change_Schema_Series_TRT
Change_Schema_Series_TRT_node1697832492135 = ApplyMapping.apply(
    frame=Data_Catalog_Series_TRT_node1697832419820,
    mappings=[
        ("first_air_date", "string", "first_air_date", "date"),
        ("id", "int", "id", "int"),
        ("name", "string", "name", "string"),
        ("production_companies", "array", "production_companies", "array"),
        ("credits.cast", "array", "credits.cast", "array"),
        ("credits.crew", "array", "credits.crew", "array"),
        ("credits.id", "int", "credits.id", "int"),
    ],
    transformation_ctx="Change_Schema_Series_TRT_node1697832492135",
)

# Script generated for node Change_Schema_Movies_TRT
Change_Schema_Movies_TRT_node1697743220750 = ApplyMapping.apply(
    frame=Data_Catalog_Movies_TRT_node1697743209188,
    mappings=[
        ("id", "int", "id", "int"),
        ("production_companies", "array", "production_companies", "array"),
        ("release_date", "string", "release_date", "date"),
        ("title", "string", "title", "string"),
        ("credits.id", "int", "credits.id", "int"),
        ("credits.cast", "array", "credits.cast", "array"),
        ("credits.crew", "array", "credits.crew", "array"),
        ("credits.success", "boolean", "credits.success", "boolean"),
        ("credits.status_code", "int", "credits.status_code", "int"),
        ("credits.status_message", "string", "credits.status_message", "string"),
    ],
    transformation_ctx="Change_Schema_Movies_TRT_node1697743220750",
)

# Script generated for node Salve_S3_series_TRT
Salve_S3_series_TRT_node1697833059238 = glueContext.write_dynamic_frame.from_options(
    frame=Change_Schema_Series_TRT_node1697832492135,
    connection_type="s3",
    format="glueparquet",
    connection_options={
        "path": f"s3://data-lake-marlos-igor/TRT/TMDB/PARQUET/Series/{datetime.now().strftime('%Y/%m/%d')}/Series/",
        "partitionKeys": [],
    },
    format_options={"compression": "snappy"},
    transformation_ctx="Salve_S3_series_TRT_node1697833059238",
)

# Script generated for node Salve_S3_movies_TRT
Salve_S3_movies_TRT_node1697743295857 = glueContext.write_dynamic_frame.from_options(
    frame=Change_Schema_Movies_TRT_node1697743220750,
    connection_type="s3",
    format="glueparquet",
    connection_options={
        "path": f"s3://data-lake-marlos-igor/TRT/TMDB/PARQUET/Movies/{datetime.now().strftime('%Y/%m/%d')}/Movies/",
        "partitionKeys": [],
    },
    format_options={"compression": "snappy"},
    transformation_ctx="Salve_S3_movies_TRT_node1697743295857",
)

job.commit()
