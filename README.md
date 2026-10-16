# Python Programming Exercises Collection

A curated collection of practical Python exercises and mini-projects designed to develop core programming skills through hands-on, real-world terminal applications.

---

## 📁 Project Structure

```text
Python_Projects/
├── ordring_system/
│   └── question_1.py       # Exercise 1: Snack & Drink Ordering System
├── groceries/
│   └── question_2.py       # Exercise 2: Grocery Cart & Billing System
├── to_do_list/
│   └── question_3.py       # Exercise 3: Interactive To-Do List Manager
├── question_4.py           # Exercise 4: Movie Ticket Booking Simulation
├── question_5.py           # Exercise 5: Multiple-Choice Quiz Game
├── question_6.py           # Exercise 6: Log Records Cleaning & Analysis
└── README.md               # Project documentation
```

---

## 📋 Exercises Overview

| # | Project / Exercise | File Path | Key Concepts Covered |
|:---:|:---|:---|:---|
| **1** | **Snack & Drink Ordering System** | `ordring_system/question_1.py` | Lists of dictionaries, menu loops, sentinel exit (`'done'`), receipt generation |
| **2** | **Grocery Cart & Billing System** | `groceries/question_2.py` | Nested dictionaries, cart state management, quantity accumulation, subtotal calculations |
| **3** | **Interactive To-Do List Manager** | `to_do_list/question_3.py` | CRUD operations, string parsing (`split`), error handling (`try/except`), task completion tracking |
| **4** | **Movie Ticket Booking Simulation** | `question_4.py` | Multi-level input validation, flexible showtime matching, order confirmation, cumulative totals |
| **5** | **Multiple-Choice Quiz Game** | `question_5.py` | Data structures (`list` of `dict`), input validation loops, score tracking, answer review |
| **6** | **Log Records Cleaning & Analysis** | `question_6.py` | Data cleaning, dictionary aggregations, frequency counting, finding maximums |

---

## 🚀 How to Run the Exercises

All scripts run on Python 3 with no external dependencies. Execute any exercise from the project root directory:

### Exercise 1: Snack & Drink Ordering System
Displays a numbered menu of snacks and drinks. Users add items by number and type `done` to print an itemized receipt with the total cost.
```bash
python3 ordring_system/question_1.py
```

### Exercise 2: Grocery Cart & Billing System
Presents a grocery catalog where users add items and quantities to a shopping cart until checkout, then prints an itemized bill with subtotals and grand total.
```bash
python3 groceries/question_2.py
```

### Exercise 3: Interactive To-Do List Manager
A full-featured terminal task manager allowing users to add tasks with priority (e.g. `Buy milk - high`), view task status, delete tasks, mark tasks complete, and view a completion summary.
```bash
python3 to_do_list/question_3.py
```

### Exercise 4: Movie Ticket Booking Simulation
Simulates a theater box office with available movies, showtimes, and ticket pricing. Supports flexible showtime selection, input validation, multiple bookings, and a final summary.
```bash
python3 question_4.py
```

### Exercise 5: Multiple-Choice Quiz Game
An interactive quiz with 5 questions covering Python fundamentals and general knowledge. Features input validation, score tracking, and an end-of-quiz review showing your answers versus correct answers.
```bash
python3 question_5.py
```

### Exercise 6: Log Records Cleaning & Analysis
Processes raw server logs to filter out invalid records (missing actions or empty users), builds user activity and action frequency dictionaries, and determines the most common action.
```bash
python3 question_6.py
```

---

## 💡 Core Topics Practiced

- **Control Flow:** `while` loops, sentinel values, conditional logic, break/continue.
- **Data Structures:** Dictionaries, lists of dictionaries, tuples, sets.
- **Input Validation:** Guarding against invalid inputs, whitespace stripping (`.strip()`), case normalization (`.lower()`), type casting safely with `try/except` and `.isdigit()`.
- **Data Transformation:** Filtering, mapping, accumulating totals, aggregating frequencies (`.get()`).
