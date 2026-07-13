class Factory:
    items = [] 

    @classmethod
    def produce(cls, item):
        cls.items.append(item)

    def mask_items(self):
        self.items = ["Fake Item"]

