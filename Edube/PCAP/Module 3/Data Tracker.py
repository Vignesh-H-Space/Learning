class DataTracker:
    # A Class Variable
    entries = []

    @classmethod
    def add_via_class(cls, val):
        # 'cls' acts like 'self', but for the Blueprint!
        cls.entries.append(val)
