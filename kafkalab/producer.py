from kafka import KafkaProducer
import json
from datetime import datetime

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

print("Введите user_id и action через пробел (10 purchase). 'exit' для выхода.")

while True:
    inp = input("> ")
    if inp.lower() == "exit":
        break
    try:
        user_id, action = inp.split()
        msg = {
            "user_id": int(user_id),
            "action": action,
            "timestamp": datetime.now().isoformat()
        }
        producer.send("user_actions", msg)
        print("Отправлено:", msg)
    except Exception as e:
        print("[ERROR] Ошибка ввода:", e)

producer.flush()