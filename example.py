from pyspark.sql import SparkSession
import pyspark.sql.functions as f

spark = SparkSession.builder.getOrCreate()

spark.read.parquet("/data/example") \
    .filter(f.col("command").isNull()) \
    .repartition(1) \
    .write.parquet("/user/abelousova/example")

