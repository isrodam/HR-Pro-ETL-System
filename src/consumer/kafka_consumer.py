from confluent_kafka import Consumer, KafkaError
import json
# Importing our database logic from the database folder
from src.database.mongo_client import get_mongo_collection, save_to_mongodb

def run_kafka_consumer():
    # Technical configuration for the Kafka connection
    conf = {
        'bootstrap.servers': 'localhost:9092',
        'group.id': 'hr-pro-team-mirae-raul', # Our specific team identifier
        'auto.offset.reset': 'earliest'
    }

    consumer = Consumer(conf)
    consumer.subscribe(['hr_pro_data']) 

    # Initializing the connection to MongoDB (Bronze Zone)
    # This uses the port 27017 we configured in Docker yesterday
    collection = get_mongo_collection()

    print("Consumer started. Storing data in MongoDB... (Press Ctrl+C to stop)")

    try:
        while True:
            # poll(1.0) checks for new messages every 1 second to protect your PC
            msg = consumer.poll(1.0)

            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    print(f"Consumer error: {msg.error()}")
                    break

            # Converting raw bytes to a Python dictionary
            data = json.loads(msg.value().decode('utf-8'))
            
            # Persisting the data into MongoDB instead of just printing it
            save_to_mongodb(data, collection)
            print(f"Successfully persisted data for employee: {data.get('full_name', 'Unknown')}")

    except KeyboardInterrupt:
        print("\nStopping consumer...")
    finally:
        # Professional cleanup of the connection
        consumer.close()

if __name__ == "__main__":
    run_kafka_consumer()