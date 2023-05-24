from confluent_kafka import Consumer, KafkaException
import uuid

# Generate a random UUID

def consume_messages(topic):
    # Kafka consumer configuration
    random_id = uuid.uuid4()
    change = 1
    consumer_config = {
        'bootstrap.servers': 'kafka:9092',  # Kafka bootstrap servers
        'group.id': f'{random_id}',     # Consumer group ID
        'auto.offset.reset': 'earliest'      # Start consuming from the beginning of the topic
    }

    # Create a Kafka consumer
    consumer = Consumer(consumer_config)

    # Subscribe to the specified topic
    consumer.subscribe([topic])
    # Consume messages
    try:
        while True:
            # Poll for new messages
            msg = consumer.poll(1.0)

            # Check if a message was received
            if msg is None:
                continue

            # Process the received message
            print(f'Received message: {msg.value().decode()}')

    except KafkaException as e:
        # Handle Kafka exceptions
        print(f'Kafka exception: {str(e)}')

    finally:
        # Close the consumer to release its resources
        consumer.close()