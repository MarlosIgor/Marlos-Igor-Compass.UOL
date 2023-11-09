import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue import DynamicFrame
from datetime import datetime


def sparkSqlQuery(glueContext, query, mapping, transformation_ctx) -> DynamicFrame:
    for alias, frame in mapping.items():
        frame.toDF().createOrReplaceTempView(alias)
    result = spark.sql(query)
    return DynamicFrame.fromDF(result, glueContext, transformation_ctx)


args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node Dados_Parquet_TRT
Dados_Parquet_TRT_node1697834717263 = glueContext.create_dynamic_frame.from_options(
    format_options={},
    connection_type="s3",
    format="parquet",
    connection_options={
        "paths": ["s3://data-lake-marlos-igor/TRT/TMDB/PARQUET/Movies/"],
    
    },
    transformation_ctx="Dados_Parquet_TRT_node1697834717263",
)

# Script generated for node SQL_Credits_REF
SqlQuery0 = """
SELECT
    tmp.id AS id_movie,
    cast.id as id_actor,
    cast.name as name_actor,
    cast.popularity as popularity
FROM
    (SELECT id, explode(credits.cast) AS cast FROM movies) tmp
"""
SQL_Credits_REF_node1698342601434 = sparkSqlQuery(
    glueContext,
    query=SqlQuery0,
    mapping={"movies": Dados_Parquet_TRT_node1697834717263},
    transformation_ctx="SQL_Credits_REF_node1698342601434",
)

# Script generated for node SQL_Production_Companies_REF
SqlQuery1 = """
SELECT
    tmp.id AS id_movie,
    production_companies.id as id_company,
    production_companies.name as company_name
FROM
    (SELECT id, explode(production_companies) AS production_companies FROM production_companies) tmp
"""
SQL_Production_Companies_REF_node1697834735926 = sparkSqlQuery(
    glueContext,
    query=SqlQuery1,
    mapping={"production_companies": Dados_Parquet_TRT_node1697834717263},
    transformation_ctx="SQL_Production_Companies_REF_node1697834735926",
)

# Script generated for node SQL_Data_Release_REF
SqlQuery2 = """
SELECT 
    id AS id_movie, 
    release_date
FROM movies
"""
SQL_Data_Release_REF_node1697834767339 = sparkSqlQuery(
    glueContext,
    query=SqlQuery2,
    mapping={"movies": Dados_Parquet_TRT_node1697834717263},
    transformation_ctx="SQL_Data_Release_REF_node1697834767339",
)

# Script generated for node SQL_Movies_REF
SqlQuery3 = """
SELECT 
    id AS id_movie, 
    title
FROM movies
"""
SQL_Movies_REF_node1697834800408 = sparkSqlQuery(
    glueContext,
    query=SqlQuery3,
    mapping={"movies": Dados_Parquet_TRT_node1697834717263},
    transformation_ctx="SQL_Movies_REF_node1697834800408",
)

# Script generated for node Salve_S3_Credits_REF
Salve_S3_Credits_REF_node1698342616183 = glueContext.write_dynamic_frame.from_options(
    frame=SQL_Credits_REF_node1698342601434,
    connection_type="s3",
    format="glueparquet",
    connection_options={
        "path": f"s3://data-lake-marlos-igor/REF/PARQUET/Movies/{datetime.now().strftime('%Y/%m/%d')}/credit/",
        "partitionKeys": [],
    },
    format_options={"compression": "snappy"},
    transformation_ctx="Salve_S3_Credits_REF_node1698342616183",
)

# Script generated for node Salve_S3_Production_Companies_REF
Salve_S3_Production_Companies_REF_node1697834934387 = glueContext.write_dynamic_frame.from_options(
    frame=SQL_Production_Companies_REF_node1697834735926,
    connection_type="s3",
    format="glueparquet",
    connection_options={
        "path": f"s3://data-lake-marlos-igor/REF/PARQUET/Movies/{datetime.now().strftime('%Y/%m/%d')}/production_company/",
        "partitionKeys": [],
    },
    format_options={"compression": "snappy"},
    transformation_ctx="Salve_S3_Production_Companies_REF_node1697834934387",
)

# Script generated for node Salve_S3_Data_Release_REF
Salve_S3_Data_Release_REF_node1697834935355 = (
    glueContext.write_dynamic_frame.from_options(
        frame=SQL_Data_Release_REF_node1697834767339,
        connection_type="s3",
        format="glueparquet",
        connection_options={
            "path": f"s3://data-lake-marlos-igor/REF/PARQUET/Movies/{datetime.now().strftime('%Y/%m/%d')}/data_release/",
            "partitionKeys": [],
        },
        format_options={"compression": "snappy"},
        transformation_ctx="Salve_S3_Data_Release_REF_node1697834935355",
    )
)

# Script generated for node Salve_S3_Movie_REF
Salve_S3_Movie_REF_node1697834936102 = glueContext.write_dynamic_frame.from_options(
    frame=SQL_Movies_REF_node1697834800408,
    connection_type="s3",
    format="glueparquet",
    connection_options={
        "path": f"s3://data-lake-marlos-igor/REF/PARQUET/Movies/{datetime.now().strftime('%Y/%m/%d')}/movie/",
        "partitionKeys": [],
    },
    format_options={"compression": "snappy"},
    transformation_ctx="Salve_S3_Movie_REF_node1697834936102",
)

job.commit()
