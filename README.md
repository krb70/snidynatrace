##  Dynatrace OneAgent SDK Auto Instrumentation for Python

This snidynatrace package is a fork of the autodynatrace package.

This package will instrument your python code with the OneAgentSDK.

### Usage

`pip install snidynatrace`

For most technologies, just import it in your code.

`import snidynatrace`

### Technologies supported:

- celery
- confluent_kafka
- django
- flask
- pymongo
- redis
- sqlalchemy
- urllib3
- custom annotations

### Django

For Django, add `"snidynatrace.wrappers.django"` to `INSTALLED_APPS`

### Confluent Kafka

confluent_kafka is written in C, which means we cannot patch the objects, to use it, just replace the `confluent_kafka.Consumer` and `confluent_kafka.Producer` imports with `snidynatrace.wrappers.confluent_kafka.Producer` and `snidynatrace.wrappers.confluent_kafka.Consumer`

```python
import snidynatrace
from snidynatrace.wrappers.confluent_kafka import Consumer, Producer
import time
from concurrent.futures import ThreadPoolExecutor

p = Producer({"bootstrap.servers": "localhost:32769"})
c = Consumer({"bootstrap.servers": "localhost:32769", "group.id": "mygroup", "auto.offset.reset": "earliest"})
c.subscribe(["mytopic"])


@snidynatrace.trace
def produce():
    message = "Hello world!"
    p.produce("mytopic", message.encode("utf-8"))


def producer():
    while True:
        produce()
        time.sleep(2)


def consumer():
    while True:
        msg = c.poll(1.0)

        if msg is None:
            continue
        if msg.error():
            print("Consumer error: {}".format(msg.error()))
            continue

        print("Received message: {}".format(msg.headers()))

    c.close()


def main():
    with ThreadPoolExecutor(max_workers=2) as e:
        e.submit(producer)
        e.submit(consumer)


if __name__ == "__main__":
    main()
```

### Environment variables

* `AUTODYNATRACE_CAPTURE_HEADERS`: Default: `False`, set to `True` to capture request headers
* `AUTODYNATRACE_LOG_LEVEL`: Default `WARNING`
