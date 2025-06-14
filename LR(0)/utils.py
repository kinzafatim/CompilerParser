# utils.py

from collections import defaultdict
from grammar import Item

def closure(items, productions):
    closure_set = set(items)
    added = True

    while added:
        added = False
        new_items = set()
        for item in closure_set:
            symbol = item.next_symbol()
            if symbol and symbol.isupper():  # Non-terminal
                for prod in productions[symbol]:
                    new_item = Item(prod, 0)
                    if new_item not in closure_set:
                        new_items.add(new_item)
                        added = True
        closure_set |= new_items

    return closure_set

def goto(items, symbol, productions):
    next_items = set()
    for item in items:
        if item.next_symbol() == symbol:
            next_items.add(item.advance())
    return closure(next_items, productions)
