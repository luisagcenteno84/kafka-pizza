from kafka import KafkaConsumer
host = "kafka-3c53dbed-petsmart-48d7.aivencloud.com"
sasl_port = 14942
username = "avnadmin"
password = "3fdGSxA0BDr19LmH"

consumer = KafkaConsumer(
"demo-topic",
auto_offset_reset = "earliest", 
bootstrap_servers = '{}:{}'.format(host, sasl_port), 
client_id = "demo-client-1",
group_id = 'demo-group', 
sasl_mechanism = "SCRAM-SHA-256", 
sasl_plain_username = username, 
sasl_plain_password = password, 
security_protocol = "SASL_SSL",
ssl_cafile = "ca.pem"
)

#consumer code
# Call poll twice. First call will just assign partitions for our
# consumer without actually returning anything

for _ in range(2):
    raw_msgs = consumer.poll(timeout_ms=1000)
    for tp, msgs in raw_msgs.items():
        for msg in msgs:
            print("Received: {}".format(msg.value))

# Commit offsets so we won't get the same messages again

consumer.commit()