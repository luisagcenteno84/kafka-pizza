# This script connects to Kafka and send a few messages

from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers="kafka-3c53dbed-petsmart-48d7.aivencloud.com:14931",
    security_protocol="SSL",
    ssl_cafile="ca.pem",
    ssl_certfile="service.cert",
    ssl_keyfile="service.key",
)


message = '{"id":1, "name":"luis"}'
producer.send("demo-topic-json", message.encode("utf-8"))
print('sent {}'.format(message))


# Force sending of all messages

producer.flush()