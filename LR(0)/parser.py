# parser.py

from utils import closure, goto
from grammar import Production, Item
from collections import defaultdict, deque

class LR0Parser:
    def __init__(self, raw_productions):
        self.states = []
        self.productions = defaultdict(list)
        self.parse_table = {}
        self.terminals = set()
        self.nonterminals = set()
        self.build_grammar(raw_productions)
        self.build_automaton()
        self.build_parse_table()

    def build_grammar(self, raw):
        for line in raw:
            head, body = line.strip().split("→")
            head = head.strip()
            for b in body.split("|"):
                prod = Production(head, b.strip().split())
                self.productions[head].append(prod)
                for symbol in prod.body:
                    if not symbol.isupper():
                        self.terminals.add(symbol)
                    else:
                        self.nonterminals.add(symbol)
        self.nonterminals.add("S'")
        self.productions["S'"] = [Production("S'", [list(self.productions.keys())[0]])]

    def build_automaton(self):
        start_item = Item(self.productions["S'"][0], 0)
        start_closure = closure({start_item}, self.productions)
        self.states.append(start_closure)
        transitions = {}

        queue = deque([start_closure])
        visited = {frozenset(start_closure): 0}

        while queue:
            curr = queue.popleft()
            idx = visited[frozenset(curr)]
            self.parse_table[idx] = {}

            symbols = {sym for item in curr if (sym := item.next_symbol())}
            for sym in symbols:
                goto_set = goto(curr, sym, self.productions)
                if not goto_set:
                    continue
                frozen = frozenset(goto_set)
                if frozen not in visited:
                    visited[frozen] = len(self.states)
                    self.states.append(goto_set)
                    queue.append(goto_set)
                self.parse_table[idx][sym] = visited[frozen]

        self.visited_states = visited

    def build_parse_table(self):
        self.action_table = {}
        for state_num, items in enumerate(self.states):
            self.action_table[state_num] = {}
            for item in items:
                if item.next_symbol() is None:
                    if item.prod.head == "S'":
                        self.action_table[state_num]['$'] = ('accept',)
                    else:
                        self.action_table[state_num]['$'] = ('reduce', item.prod)
                elif item.next_symbol() in self.terminals:
                    next_state = self.parse_table[state_num].get(item.next_symbol())
                    if next_state is not None:
                        self.action_table[state_num][item.next_symbol()] = ('shift', next_state)

    def parse(self, input_string):
        input_buffer = input_string.split() + ['$']
        stack = [0]
        index = 0

        print("\n--- Parsing Steps ---")
        while True:
            state = stack[-1]
            token = input_buffer[index]

            action = self.action_table.get(state, {}).get(token)
            print(f"State: {state}, Token: {token}, Action: {action}, Stack: {stack}")

            if not action:
                print("❌ Rejected: Invalid action.")
                return False
            if action[0] == 'accept':
                print("✅ Accepted!")
                return True
            elif action[0] == 'shift':
                stack.append(token)
                stack.append(action[1])
                index += 1
            elif action[0] == 'reduce':
                prod = action[1]
                to_pop = 2 * len(prod.body)
                stack = stack[:-to_pop]
                top = stack[-1]
                stack.append(prod.head)
                stack.append(self.parse_table[top][prod.head])
