# This script connects to Kafka and send a few messages

from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers="kafka-3c53dbed-petsmart-48d7.aivencloud.com:14931",
    security_protocol="SSL",
    ssl_cafile="ca.pem",
    ssl_certfile="service.cert",
    ssl_keyfile="service.key",
)

for i in range(1, 4):
    message = "message number {}".format(i)
    print("Sending: {}".format(message))
    producer.send("demo-topic", message.encode("utf-8"))

# Force sending of all messages

producer.flush()