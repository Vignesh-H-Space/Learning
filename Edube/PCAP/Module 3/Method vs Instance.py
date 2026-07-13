class Factory:
    items = [] 

    @classmethod
    def produce(cls, item):
        cls.items.append(item)

    def mask_items(self):
        self.items = ["Fake Item"]

f1 = Factory()
f2 = Factory()

Factory.produce("Widget A")
f1.produce("Widget B")

