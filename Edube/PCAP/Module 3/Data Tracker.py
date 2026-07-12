class DataTracker:
    # A Class Variable
    entries = []

    @classmethod
    def add_via_class(cls, val):
        # 'cls' acts like 'self', but for the Blueprint!
        cls.entries.append(val)
        
    @staticmethod
    def add_via_static(val):
        # Static methods don't get 'self' OR 'cls'. They are just normal functions!
        DataTracker.entries.append(val)

tracker = DataTracker()
