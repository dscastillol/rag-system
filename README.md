# RAG System with LangChain, LangGraph and PGVector

## Overview

This project implements a Retrieval-Augmented Generation (RAG) system using:

- LangChain
- LangGraph
- PostgreSQL + PGVector
- Ollama (Llama 3.2)
- Sentence Transformers

The system supports:

- Document ingestion
- Text chunking
- Embedding generation
- Vector storage
- Similarity retrieval
- Context-aware response generation
- User state management through LangGraph

## Setup

### Start database

```bash
docker compose up -d
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run document ingestion

```bash
python app/ingestion.py
```

### Run RAG system

```bash
python app/rag_graph.py
```

## Sample Input #1

```text
What is a variable in Python?
```

## Sample Output #1

```text
According to the provided context, a variable in Python is "something that can be changed after it has been defined".
```

## Sample Input #2

```text
What is a Python list?
```

## Sample Output #2

```text
According to the provided context, a Python list is "a collection of items in a particular order.
```

## Sample Input #3

```text
How do you access elements in a list?
```

## Sample Output #3

```text
To access an element in a list, write the name of the list followed by the index of the item enclosed in square brackets.
```

## Sample Input #4

```text
What is the difference between lists and tuples?
```

## Sample Output #4

```text
The answer is: Lists are mutable, meaning their elements can be changed, while tuples are immutable, meaning their elements cannot be changed.
```

## Sample Input #5

```text
What is a dictionary in Python?
```

## Sample Output #5

```text
A dictionary in Python is a collection of key-value pairs. Each key is connected to a value, and you can use a key to access the value associated with that key.
```

## Sample Input #6

```text
How can you add new elements to a dictionary?
```

## Sample Output #6

```text
To add new elements to a dictionary, you need to follow these steps:

1. Access the dictionary using its name.
2. Use square brackets `[]` after the dictionary name and assign the key-value pair inside them.

Example:
```
favorite_languages = {
    'languages.py': 'jen',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
```

becomes:

```
favorite_languages = {
    'languages.py': 'jen',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

# Adding a new element
favorite_languages['mike'] = 'java'
```
```

## Sample Input #7

```text
What are if statements used for?
```

## Sample Output #7

```text
If statements are used to execute code based on certain conditions. They allow you to put a conditional test in the first line and any action in the indented block following the test, and Python executes the code if the condition is met and ignores it otherwise.
```

## Sample Input #8

```text
What is a function in Python?
```

## Sample Output #8

```text
According to the provided context, a function in Python is defined by using the keyword "def" to inform Python that you're defining a function. The function definition includes the name of the function and any necessary information in parentheses, which are required even if no information is needed. The indented lines that follow the function definition make up the body of the function, which contains code that gets executed when the function is called.
```

## Sample Input #9

```text
What is the difference between arguments and parameters?
```

## Sample Output #9

```text
According to the provided context, the terms "arguments" and "parameters" are often used interchangeably. However, the text does not explicitly state a clear difference between them.

It can be inferred that:

- Parameters refer to the variables in a function definition.
- Arguments refer to the values passed from a function call to a function.

In other words, parameters are what the function uses to do its job, and arguments are the information passed to the function.
```

## Sample Input #10

```text
What is the purpose of a while loop?
```

## Sample Output #10

```text
The purpose of a while loop is "executes code that you want it to, when you want it to."
```

## Sample Input #11

```text
How do classes work?
```

## Sample Output #11

```text
I could not find the answer in the retrieved documents.
```

## Sample Input #12

```text
What is inheritance?
```

## Sample Output #12

```text
Inheritance is the process by which one class (the child or subclass) inherits all the attributes and methods of another class (the parent or superclass), while also being free to define new attributes and methods of its own.
```

## Sample Input #13

```text
How do APIs work?
```

## Sample Output #13

```text
According to the context, APIs (Application Programming Interfaces) are "a part of a website designed to interact with programs that use very specific URLs to request certain information." This is mentioned in Chapter 17 of the book.
```

## Sample Input #14

```text
What is Django used for?
```

## Sample Output #14

```text
Django is a web framework — a set of tools designed to help you build interactive websites.
```

## Sample Input #15

```text
What is data visualization?
```

## Sample Output #15

```text
Data visualization involves exploring data through visual representations.
```