from pyspark.sql import SparkSession
import os

# Ensure the logs directory exists
log_dir = "/app/logs"
os.makedirs(log_dir, exist_ok=True)

# Configure logging (optional)
import logging
logging.basicConfig(
    filename=os.path.join(log_dir, 'app.log'),
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

logger.info("Starting the Spark application")

# Initialize Spark session with Delta Lake support
spark = SparkSession.builder \
    .appName("DeltaLakeApp") \
    .config("spark.jars.packages", "io.delta:delta-core_2.12:1.0.0") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
    .getOrCreate()

logger.info("Spark session created")

# Create a sample DataFrame
data = [("Alice", 1), ("Bob", 2), ("Cathy", 3)]
columns = ["name", "value"]

df = spark.createDataFrame(data, columns)

# Define the path for the Delta table
delta_table_path = "/tmp/delta/my_table"

# Write the DataFrame to a Delta table
df.write.format("delta").mode("overwrite").save(delta_table_path)

# Read the Delta table
df = spark.read.format("delta").load(delta_table_path)
df.show()

logger.info("Delta table read and displayed")

# Stop the Spark session
spark.stop()
logger.info("Spark session stopped")