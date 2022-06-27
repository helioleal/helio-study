import os # To define an env variable.

# Define a dynamic env variable for using in spark.
os.environ["SPARK_HOME"] = "C:\spark\spark-3.2.1-bin-hadoop3.2"
os.environ["HADOOP_HOME"] = "C:\spark\spark-3.2.1-bin-hadoop3.2\hadoop"

# This tool helps to find where spark is installed.
import findspark
findspark.init()

# Lib pySpark is inside the installation of spark.
# If you import Env Variable, it is not necessary to install this lib in your station.
from pyspark.sql import SparkSession

# Create a session
# local[*] -> Runs locally and uses all CPUS available
spark = SparkSession.builder.master('local[*]').appName("Iniciando com o Spark").config('spark.ui.port','4050').getOrCreate()

data = [('Zeca','35'), ('Eva', '29')]
colNames = ['Nome', 'Idade']
df = spark.createDataFrame(data, colNames)
# df.toPandas()

print(df)
print(df.show())