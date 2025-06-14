# grammar.py

class Production:
    def __init__(self, head, body):
        self.head = head
        self.body = body

    def __repr__(self):
        return f"{self.head} → {' '.join(self.body)}"

class Item:
    def __init__(self, prod, dot_pos):
        self.prod = prod
        self.dot_pos = dot_pos

    def __eq__(self, other):
        return (self.prod.head == other.prod.head and 
                self.prod.body == other.prod.body and 
                self.dot_pos == other.dot_pos)

    def __hash__(self):
        return hash((self.prod.head, tuple(self.prod.body), self.dot_pos))

    def __repr__(self):
        body = self.prod.body.copy()
        body.insert(self.dot_pos, '•')
        return f"{self.prod.head} → {' '.join(body)}"

    def next_symbol(self):
        if self.dot_pos < len(self.prod.body):
            return self.prod.body[self.dot_pos]
        return None

    def advance(self):
        return Item(self.prod, self.dot_pos + 1)
