class DataCollector:
    def __init__(self, data=[]): 
        self.data = data

    def add_item(self, item):
        self.data.append(item)

d1 = DataCollector()
d2 = DataCollector()

d1.add_item("Apple")

d2.add_item("Banana")

print(d1.data)
print(d2.data)
