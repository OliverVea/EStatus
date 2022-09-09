class Index:
    def __init__(self, index: str, health: str, **kwargs):
        self.index = index
        self.health = health
        self.document_count = kwargs['docs.count']
        self.created = kwargs['creation.date']
