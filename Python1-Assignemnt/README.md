# Que-1 Explain the key features of Python that make it a popular choice for programming
**Ans:**
- **Simple & Readability:** Python uses a clean syntax that emphasizes readability, often resembling English, which lowers the barrier for beginners.

- **Interpreted Language:** Code is executed line-by-line, which enables easier debugging and rapid testing (no separate compilation step needed).

- **Dynamically Typed:** Variables do not need explicit type declarations; the type is determined at runtime, offering flexibility.

- **Extensive Libraries ("Batteries Included"):** Python provides a massive standard library for tasks like file I/O, web browsing, and data manipulation.

- **Multi-Paradigm:** It supports procedural, object-oriented (OOP), and functional programming, allowing developers to choose the best style.

- **Cross-Platform Portability:** Code written on one OS (Windows, Mac, Linux) runs on others with little to no modification.
---
---
# Que-2 Describe the role of predefined keywords in Python and provide examples of how they are used in a program.
**Ans:**
- Keywords are the fundamental building blocks of Python code and are crucial for the interpreter to understand the program's logic.
- Predefined keywords are reserved words with special meanings that define the language's syntax and structure.
- They cannot be used as variable names, function names, or any other identifiers, as this would cause a SyntaxError.

**Examples:**
- if, else, while, def, class, import, True, False, None, break.

**Usage:**
- Control Flow (if/elif/else): 
    - if x > 10: print("High")

- Looping (for/while): 
    - for i in range(5): print(i)
---
# Que-3 Compare and contrast mutable and immutable objects in Python with examples.
**Ans**
- In Python, mutable objects can be changed after they are created, while immutable objects cannot.

- **Mutable Objects:**
    - Mutable objects allow in-place modification of their internal state without changing their unique identity (memory address).

    - Examples:

        - Lists: Ordered collections of items, allowing additions, removals, and modifications of elements.

        - Dictionaries: Collections of key-value pairs, where entries can be added, updated, or removed.

        - Sets: Unordered collections of unique elements, which can be modified by adding or removing items.


        - User-defined classes: Most custom classes in Python are mutable by default.

- **Immutable Objects:**

    - Immutable objects cannot be altered after creation. Any operation that appears to modify an immutable object actually creates a new object in memory, and the variable is then reassigned to this new object.

    - Examples:

        - Numbers (int, float, complex, bool): Numeric values are fixed once created.

        - Strings (str): Sequences of characters whose content cannot be changed.

        - Tuples: Ordered collections of elements (similar to lists but immutable). The contents cannot be changed, although a tuple can contain mutable items.

        - Frozensets: An immutable version of a set.
        - Bytes: Immutable sequences of bytes.
---
# Que-4. Discuss the different types of operators in Python and provide examples of how they are used.
**Ans:**

**Python supports several types of operators to manipulate data:**

- Arithmetic: +, -, *, /, % (modulus), ** (exponentiation), // (floor division).

- Comparison: == (equal), != (not equal), >, <, >=, <=.

- Logical: and, or, not.

- Assignment: =, +=, -=, *=, /=.

- Membership: in, not in (checks for existence).

- Identity: is, is not (checks if objects are the same memory location). 