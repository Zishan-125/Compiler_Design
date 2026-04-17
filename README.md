# ⚙️ Compiler Design – Task 1

### *Lexical Analysis using Python (Regex-Based Tokenizer)*

<p align="center">
  <img src="https://img.shields.io/badge/Build-Passing-success?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Version-1.0-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Language-Python-yellow?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Concept-Lexical_Analysis-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Domain-Compiler_Design-red?style=for-the-badge" />
</p>

---

<p align="center">
  <img src="https://media.giphy.com/media/3oKIPEqDGUULpEU0aQ/giphy.gif" width="400"/>
</p>

<p align="center">
  ⚙️ Lexical Analyzer in Action — Tokenizing Source Code into Meaningful Units
</p>

---

## 📌 Overview

This project implements a **Lexical Analyzer (Tokenizer)** the first phase of a compiler using Python and Regular Expressions.

It converts raw source code into structured **tokens**, forming the foundation for further stages like parsing and semantic analysis.

---

## ⚡ Quick Glance (10-sec overview)

* 🔍 Converts source code → tokens
* 🧠 Identifies keywords, identifiers, operators, numbers
* ⚙️ Regex-powered efficient scanning
* 📚 Core compiler foundation

---

## 🧠 A → Z Explanation

### 🔹 Input Code

```c
int sum=10;
```

---

### 🔹 Step-by-Step Transformation

#### 🟢 Step 1: Raw Input

```
int sum=10;
```

#### 🟡 Step 2: Regex Scanning Starts

```
[int] [ ] [sum] [=] [10] [;]
```

#### 🔵 Step 3: Pattern Matching

```
int  → KEYWORD  
sum  → IDENTIFIER  
=    → OPERATOR  
10   → NUMBER  
;    → PUNCTUATION  
```

#### 🟣 Step 4: Final Output Table

```
Token        | Type
-------------------------
int          | KEYWORD
sum          | IDENTIFIER
=            | OPERATOR
10           | NUMBER
;            | PUNCTUATION
```

---

## 🎬 Code Flow Animation (Step-by-Step)

```mermaid
sequenceDiagram
    participant User
    participant Input
    participant RegexEngine
    participant Tokenizer
    participant Output

    User->>Input: Enter source code
    Input->>RegexEngine: Send raw string
    RegexEngine->>Tokenizer: Match patterns
    Tokenizer->>Tokenizer: Identify token type
    Tokenizer->>Tokenizer: Skip whitespace
    Tokenizer->>Output: Send structured tokens
    Output->>User: Display result
```

---

## 🔄 Internal Code Execution Flow

```mermaid
flowchart LR
    A((Start)) -->|letter| B[Identifier State]
    A -->|digit| C[Number State]
    A -->|operator| D[Operator State]
    A -->|;| E[Punctuation State]

    B -->|letter/digit/_| B
    B -->|other| F[Accept IDENTIFIER]

    C -->|digit| C
    C -->|other| G[Accept NUMBER]

    D --> H[Accept OPERATOR]
    E --> I[Accept PUNCTUATION]
```

---

## 🧩 Core Implementation

### 🔹 Token Patterns

```python
token_patterns = [
    ('KEYWORD',    r'\b(int|float|and|or|if|else|while)\b'),
    ('NUMBER',     r'\b\d+\b'),
    ('IDENTIFIER', r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'),
    ('OPERATOR',   r'[=\+\-\*/]'),
    ('PUNCTUATION',r';'),
    ('WHITESPACE', r'\s+'),
]
```

---

### 🔹 Master Pattern

```python
master_pattern = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_patterns)
```

✔ Combines all token rules into one optimized regex engine

---

### 🔹 Tokenization Logic

```python
for match in re.finditer(master_pattern, input_string):
```

✔ Scans → Matches → Classifies → Outputs

---

## 🧪 Example Execution

### 🔹 Input

```
int sum=10; and a+b= 20;
```

### 🔹 Output

| Token | Type        |
| ----- | ----------- |
| int   | KEYWORD     |
| sum   | IDENTIFIER  |
| =     | OPERATOR    |
| 10    | NUMBER      |
| ;     | PUNCTUATION |
| and   | KEYWORD     |
| a     | IDENTIFIER  |
| +     | OPERATOR    |
| b     | IDENTIFIER  |
| =     | OPERATOR    |
| 20    | NUMBER      |
| ;     | PUNCTUATION |

---

## 🧠 Debugger’s Insight (Expert Level)

* ✔ Regex priority ensures correct classification
* ✔ Named groups (`?P<>`) improve readability
* ✔ `finditer()` ensures sequential token detection
* ✔ Clean separation of logic improves scalability

---

## 🛠️ Tech Stack

* Python
* Regular Expressions (`re`)
* Compiler Design Concepts

---

## 🚀 Run

```bash
python Task_1.py
```

---

## 👤 Author

**Abdullah Al Mamun Zishan**  
🎓 CSE, Feni University  
📚 Batch: CSE 31st (UG)  
🆔 ID: 232031009  

🔗 https://www.linkedin.com/in/abdullah-al-mamun-zishan-606550282

---
