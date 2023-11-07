#1:
from pyspark.sql import SparkSession
from pyspark import SparkContext, SQLContext

spark = SparkSession \
    .builder \
    .master("local[*]") \
    .appName("Exercicio Intro") \
    .getOrCreate()

df_nomes = spark.read.csv('/home/marlos-igor/sprint-8/tarefa-exercícios-apache-spark//nomes_aleatorios.txt')

df_nomes.show(5)

#2:
df_nomes = df_nomes.withColumnRenamed('_c0', 'Nomes')

df_nomes.printSchema()

df_nomes.show(10)

#3:
from pyspark.sql.functions import when, rand

df_nomes = df_nomes.withColumn('Escolaridade',
                               when(rand() < 0.33, 'Fundamental').otherwise(
                                   when(rand() < 0.5, 'Medio').otherwise('Superior')))

df_nomes.show(10)

#4:
from pyspark.sql.functions import udf
from random import choice

paises = ['Argentina', 'Bolívia', 'Brasil', 'Chile', 'Colômbia', 'Equador',
          'Guiana', 'Paraguai', 'Peru', 'Suriname', 'Uruguai', 'Venezuela',
          'Guiana Francesa']

udf_pais = udf(lambda: choice(paises))

df_nomes = df_nomes.withColumn('Pais', udf_pais())

df_nomes.show(10)

#5:
from pyspark.sql.functions import round

df_nomes = df_nomes.withColumn('AnoNascimento', round(rand() * 65 + 1945))

df_nomes.show(10)

#6:
df_select = df_nomes.filter(df_nomes.AnoNascimento >= 2000)

df_select.show(10)

#7:
df_nomes.createOrReplaceTempView("pessoas")

df_select = spark.sql("select * from pessoas where AnoNascimento >= 2000")

df_select.show(10)

#8:
millennials_count = df_nomes.filter((df_nomes.AnoNascimento >= 1980) & (df_nomes.AnoNascimento <= 1994)).count()

print(millennials_count)

#9:
millennials_count_sql = spark.sql("select count(*) from pessoas where AnoNascimento between 1980 and 1994").first()[0]

print(millennials_count_sql)

#10:
geracoes_df = spark.sql("""
    select 
        Pais,
        case 
            when AnoNascimento between 1944 and 1964 then 'Baby Boomers'
            when AnoNascimento between 1965 and 1979 then 'Geração X'
            when AnoNascimento between 1980 and 1994 then 'Millennials'
            when AnoNascimento between 1995 and 2015 then 'Geração Z'
        end as Geracao,
        count(*) as Quantidade
    from pessoas
    group by Pais, Geracao
    order by Pais, Geracao, Quantidade
""")

geracoes_df.show()


