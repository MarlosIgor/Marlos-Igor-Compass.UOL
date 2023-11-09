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
Dados_Parquet_TRT_node1697836443552 = glueContext.create_dynamic_frame.from_options(
    format_options={},
    connection_type="s3",
    format="parquet",
    connection_options={
        "paths": ["s3://data-lake-marlos-igor/TRT/TMDB/PARQUET/Series/"],
     
    },
    transformation_ctx="Dados_Parquet_TRT_node1697836443552",
)

# Script generated for node SQL_First_Air_Date_REF
SqlQuery0 = """
SELECT
    id AS id_serie, 
    first_air_date AS first_viewing
FROM series
"""
SQL_First_Air_Date_REF_node1697836486265 = sparkSqlQuery(
    glueContext,
    query=SqlQuery0,
    mapping={"series": Dados_Parquet_TRT_node1697836443552},
    transformation_ctx="SQL_First_Air_Date_REF_node1697836486265",
)

# Script generated for node SQL_Production_Companies_REF
SqlQuery1 = """
SELECT
    tmp.id AS id_serie,
    production_companies.id as id_company,
    production_companies.name as company_name
    
FROM
    (SELECT id, explode(production_companies) AS production_companies FROM series) tmp
"""
SQL_Production_Companies_REF_node1697836487261 = sparkSqlQuery(
    glueContext,
    query=SqlQuery1,
    mapping={"series": Dados_Parquet_TRT_node1697836443552},
    transformation_ctx="SQL_Production_Companies_REF_node1697836487261",
)

# Script generated for node SQL_Series_REF
SqlQuery2 = """
SELECT
    id AS id_serie, 
    name AS name_serie
FROM series
"""
SQL_Series_REF_node1697836484945 = sparkSqlQuery(
    glueContext,
    query=SqlQuery2,
    mapping={"series": Dados_Parquet_TRT_node1697836443552},
    transformation_ctx="SQL_Series_REF_node1697836484945",
)

# Script generated for node SQL_Credits_REF
SqlQuery3 = """
SELECT
    tmp.id AS id_serie,
    cast.id as id_actor,
    cast.name as name_actor,
    cast.popularity as popularity
FROM
    (SELECT id, explode(credits.cast) AS cast FROM series) tmp
"""
SQL_Credits_REF_node1698341776272 = sparkSqlQuery(
    glueContext,
    query=SqlQuery3,
    mapping={"series": Dados_Parquet_TRT_node1697836443552},
    transformation_ctx="SQL_Credits_REF_node1698341776272",
)

# Script generated for node Salve_S3_First_Air_Date_REF
Salve_S3_First_Air_Date_REF_node1697837218315 = (
    glueContext.write_dynamic_frame.from_options(
        frame=SQL_First_Air_Date_REF_node1697836486265,
        connection_type="s3",
        format="glueparquet",
        connection_options={
            "path": f"s3://data-lake-marlos-igor/REF/PARQUET/Series/{datetime.now().strftime('%Y/%m/%d')}/first_air_date/",
            "partitionKeys": [],
        },
        format_options={"compression": "snappy"},
        transformation_ctx="Salve_S3_First_Air_Date_REF_node1697837218315",
    )
)

# Script generated for node Salve_S3_Production_Companies_REF
Salve_S3_Production_Companies_REF_node1697837209374 = glueContext.write_dynamic_frame.from_options(
    frame=SQL_Production_Companies_REF_node1697836487261,
    connection_type="s3",
    format="glueparquet",
    connection_options={
        "path": f"s3://data-lake-marlos-igor/REF/PARQUET/Series/{datetime.now().strftime('%Y/%m/%d')}/production_company/",
        "partitionKeys": [],
    },
    format_options={"compression": "snappy"},
    transformation_ctx="Salve_S3_Production_Companies_REF_node1697837209374",
)

# Script generated for node Salve_S3_Series_REF
Salve_S3_Series_REF_node1697837223654 = glueContext.write_dynamic_frame.from_options(
    frame=SQL_Series_REF_node1697836484945,
    connection_type="s3",
    format="glueparquet",
    connection_options={
        "path": f"s3://data-lake-marlos-igor/REF/PARQUET/Series/{datetime.now().strftime('%Y/%m/%d')}/serie/",
        "partitionKeys": [],
    },
    format_options={"compression": "snappy"},
    transformation_ctx="Salve_S3_Series_REF_node1697837223654",
)

# Script generated for node Salve_S3_Credits_REF
Salve_S3_Credits_REF_node1698341786942 = glueContext.write_dynamic_frame.from_options(
    frame=SQL_Credits_REF_node1698341776272,
    connection_type="s3",
    format="glueparquet",
    connection_options={
        "path": f"s3://data-lake-marlos-igor/REF/PARQUET/Series/{datetime.now().strftime('%Y/%m/%d')}/credit/",
        "partitionKeys": [],
    },
    format_options={"compression": "snappy"},
    transformation_ctx="Salve_S3_Credits_REF_node1698341786942",
)

job.commit()
