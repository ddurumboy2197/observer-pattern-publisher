from typing import List

class Publisher:
    def __init__(self):
        self.subscribers: List['Subscriber'] = []

    def subscribe(self, subscriber: 'Subscriber'):
        self.subscribers.append(subscriber)

    def unsubscribe(self, subscriber: 'Subscriber'):
        self.subscribers.remove(subscriber)

    def notify(self, message: str):
        for subscriber in self.subscribers:
            subscriber.update(message)


class Subscriber:
    def __init__(self, name: str):
        self.name = name

    def update(self, message: str):
        print(f"{self.name} received message: {message}")


# Test
publisher = Publisher()

subscriber1 = Subscriber("Subscriber 1")
subscriber2 = Subscriber("Subscriber 2")

publisher.subscribe(subscriber1)
publisher.subscribe(subscriber2)

publisher.notify("Hello, world!")

publisher.unsubscribe(subscriber2)

publisher.notify("Goodbye, world!")
```

Kodda `Publisher` klassi yangilik chiqqanda barcha obunachilarga xabar berish uchun javobgardir. `Subscriber` klassi obunachi sifatida ishlaydi va yangilikni qabul qiladi. `notify` metodi yangilikni barcha obunachilarga yuboradi. `subscribe` va `unsubscribe` metodi obunachilarni ro'yxatga olish va ro'yxatdan chiqarish uchun javobgardir.
