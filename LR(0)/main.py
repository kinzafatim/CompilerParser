

from parser import LR0Parser

def load_grammar(file_path):
    with open(file_path, 'r') as f:
        return [line.strip() for line in f.readlines() if line.strip()]

def load_input(file_path):
    with open(file_path, 'r') as f:
        return f.read().strip()

if __name__ == "__main__":
    grammar_lines = load_grammar('LR(0)/test_cases/g1.txt')
    test_string = load_input('LR(0)/test_cases/input1.txt')

    parser = LR0Parser(grammar_lines)

    print(f"\n📥 Parsing input: {test_string}")
    result = parser.parse(test_string)

    if result:
        print("\n✅ The string is valid!")
    else:
        print("\n❌ The string is invalid.")
        
