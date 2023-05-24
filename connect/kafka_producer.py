from confluent_kafka import Producer

def produce_message(topic, message):
    # Kafka producer configuration
    producer_config = {
        'bootstrap.servers': 'kafka:9092',  # Kafka bootstrap servers
    }

    # Create a Kafka producer
    producer = Producer(producer_config)

    # Produce the message to the specified topic
    producer.produce(topic, value=message)

    # Flush the producer to ensure the message is delivered
    producer.flush()

    # Close the producer
    