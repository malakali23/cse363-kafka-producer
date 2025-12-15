from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

event = {
    "document_id": "doc789",
    "status": "processed",
    "service": "document-reader"
}

producer.send("document.processed", event)
producer.flush()

print("Event sent successfully")

