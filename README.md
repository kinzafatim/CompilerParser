
# 📘 LR(0) Parser

This project implements an LR(0) Parser from scratch in Python. It reads a context-free grammar, constructs the LR(0) automaton, builds the parsing table, and parses an input string to determine whether it's valid. If accepted, it also generates and optionally visualizes the parse tree.

## 📂 Project Structure

```
LR(0)/
├── grammar.py          # Defines Production and Item classes
├── parser.py           # Main parser logic (LR(0) parsing, parse tree, etc.)
├── utils.py            # Contains closure and goto helper functions
├── test_cases/
│   ├── g1.txt          # Sample grammar file
│   ├── input1.txt      # Sample input string
```

## 🚀 Features

- ✅ Grammar parsing with productions and symbols
- ✅ Construction of LR(0) items and automaton
- ✅ LR(0) parsing table (ACTION and GOTO)
- ✅ Input string parsing with step-by-step trace
- ✅ Parse tree construction
- ✅ Optional visualization of parse tree using Graphviz

## 📥 How to Use

1. **Add Grammar**

   Edit or create a grammar file in `test_cases/g1.txt` using the format:

   ```
   E → E + T | T
   T → T * F | F
   F → ( E ) | id
   ```

2. **Add Input String**

   Put your input string (tokens space-separated) in `test_cases/input1.txt`:

   ```
   id + id * id
   ```

3. **Run the Parser**

   ```bash
   python parser.py
   ```

## Customization

- To use a different grammar or input, modify `test_cases/g1.txt` and `input1.txt`.
- You can extend the parser to LR(1) or SLR by modifying the item handling logic.
