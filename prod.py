from kafka import KafkaProducer
from kafka.errors import KafkaError
from pyspark.sql import SparkSession
from pyspark.ml.feature import StringIndexer
from pyspark.ml.recommendation import ALS
import json


# Create a Spark Session
spark = SparkSession.builder.appName("RecommendationSystem") \
 .config("spark.driver.memory", "8g") \
 .config("spark.executor.memory", "8g") \
.getOrCreate()

# Set the log level to ERROR
spark.sparkContext.setLogLevel("ERROR")

# Load data from the Parquet file 
df = spark.read.parquet("/home/yayaq/Documents/amzdata.parquet")

# You may need to index string type 'reviewerID' and 'asin' to integer type if they are not
indexer1 = StringIndexer(inputCol="reviewerID", outputCol="userId")
df = indexer1.fit(df).transform(df)

indexer2 = StringIndexer(inputCol="asin", outputCol="productId")
df = indexer2.fit(df).transform(df)

df = df.withColumn("rating", df["overall"].cast("float"))

# Build the recommendation model using ALS on the full data
als = ALS(maxIter=5, regParam=0.01, userCol="userId", itemCol="productId", ratingCol="rating",
          coldStartStrategy="drop")
model = als.fit(df)

# Create a Kafka producer
producer = KafkaProducer(bootstrap_servers=['localhost:9092'], value_serializer=lambda v: json.dumps(v).encode('utf-8'))

# Function to generate product recommendations for a user and send them to Kafka
def generate_recommendations(user_id):
    
    # Generate top 10 product recommendations for the specified user
    user_rec = model.recommendForAllUsers(10).filter(f"userId == {user_id}").toPandas()
    #user_rec = model.recommendForAllUsers(10).filter("userId == 28").toPandas()
    # Convert product IDs to strings
    user_rec['productId'] = user_rec['recommendations'].apply(lambda x: [str(row.productId) for row in x])

    # Flatten the recommendations and create a comma-separated string
    user_rec['productId'] = user_rec['productId'].apply(lambda x: ','.join(x))

    # Convert the user ID to string and create the message
    message = {'user_id': str(user_id), 'product_ids': user_rec['productId'].iloc[0]}
    print(message)
    # Send the message to Kafka
    producer.send('recommendations', value=message)

# Close the Kafka producer
producer.close()

# Stop Spark session
spark.stop()

