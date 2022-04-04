import kafka
host = "kafka-3c53dbed-petsmart-48d7.aivencloud.com"
sasl_port = 14942
username = "avnadmin"
password = "3fdGSxA0BDr19LmH"

client = kafka.KafkaProducer(
   bootstrap_servers=f"{host}:{sasl_port}",
   sasl_mechanism="PLAIN",
   sasl_plain_password=password,
   sasl_plain_username=username,
   security_protocol="SASL_SSL",
   ssl_cafile="ca.pem",
)

client.send("demo-topic", b"test")
client.flush()