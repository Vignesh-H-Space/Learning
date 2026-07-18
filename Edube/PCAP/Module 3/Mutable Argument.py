class DataCollector:
    def __init__(self, data=[]): 
        self.data = data

    def add_item(self, item):
        self.data.append(item)


