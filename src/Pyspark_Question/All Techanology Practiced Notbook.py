# Databricks notebook source
df=spark.read.csv("dbfs:/FileStore/user.csv").show()

# COMMAND ----------

from pyspark.sql.functions import lit
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
from pyspark.sql.functions import col


# Define the path to your CSV file
csv_path = "dbfs:/FileStore/user.csv"

custom_schema = StructType([
    StructField("user_id", IntegerType(), True),
    StructField("emailid", StringType(), True),
    StructField("nativelanguage", StringType(), True),
    StructField("location", StringType(), True),
])
# Read CSV file with specified schema and options
df = spark.read.option("header", "true").schema(custom_schema).csv(csv_path)

# Show the DataFrame
#df.show()
#df.printSchema()
df.withColumnRenamed("user_id","SL_NO")#.show()
df.withColumn("Company",lit("Diggibyte"))#.show()
df.filter((df.location=="mumbai")&(df.nativelanguage=="hindi"))#.show()
df.filter((df.location=="mumbai")|(df.nativelanguage=="hindi"))#.show()
df2=df.withColumn("emailid", col("emailid").cast("int"))
df2.show()
df2.printSchema()



