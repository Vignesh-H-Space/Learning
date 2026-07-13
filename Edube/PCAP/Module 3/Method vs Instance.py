class Factory:
    items = [] 

    @classmethod
    def produce(cls, item):
        cls.items.append(item)


