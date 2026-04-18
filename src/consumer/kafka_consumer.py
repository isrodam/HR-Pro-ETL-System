from confluent_kafka import Consumer, KafkaError
import json

def run_kafka_consumer():
    # Technical configuration for the Kafka connection
    conf = {
        'bootstrap.servers': 'localhost:9092',
        'group.id': 'hr-pro-team-mirae-raul', # Identifier for our team
        'auto.offset.reset': 'earliest'        # Start reading from the beginning
    }

    consumer = Consumer(conf)
    # Subscribing to the specific channel for HR data
    consumer.subscribe(['hr_pro_data']) 

    print("Consumer started. Waiting for messages... (Press Ctrl+C to stop)")

    try:
        while True:
            # poll(1.0) checks for new messages every 1 second
            # This prevents overloading your PC if thousands of data arrive 
            msg = consumer.poll(1.0)

            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    print(f"Consumer error: {msg.error()}")
                    break

            # Converting the raw bytes from Kafka into a Python dictionary (JSON) 
            data = json.loads(msg.value().decode('utf-8'))
            print(f"Received employee data: {data}")

    except KeyboardInterrupt:
        print("\nStopping consumer...")
    finally:
        # Crucial step: clean up and close the connection professionally [cite: 202]
        consumer.close()

if __name__ == "__main__":
    run_kafka_consumer()