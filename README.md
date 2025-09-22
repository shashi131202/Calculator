# 🧮 Calculator CLI App

A simple **Command-Line Calculator** built with Python.  
This project demonstrates the use of **functions, loops, and user input handling** in a clean and structured way.  

---

## 🚀 Features
- Perform basic arithmetic operations:
  - ➕ Addition  
  - ➖ Subtraction  
  - ✖️ Multiplication  
  - ➗ Division (with division-by-zero handling)  
- Loop continues until the user chooses to exit  
- Handles invalid input gracefully  
- Beginner-friendly, easy to extend  

---

## 📂 Project Structure
```

calculator-cli/
│
├── calculator.py   # Main Python program
└── README.md       # Documentation

````

---

## ⚙️ How It Works
1. The program displays a menu with operation choices.  
2. The user selects an option (`1–4`) or exits (`5`).  
3. The user enters two numbers.  
4. The program performs the selected operation and displays the result.  
5. The loop continues until the user selects **Exit**.  

---

## ▶️ Usage

### 1. Clone the repository
```bash
git clone https://github.com/your-username/calculator-cli.git
cd calculator-cli
````

### 2. Run the program

```bash
python calculator.py
```

---

## 🖥️ Example Run

```
--- Calculator Menu ---
1. Add (+)
2. Subtract (-)
3. Multiply (*)
4. Divide (/)
5. Exit
Enter choice (1-5): 1
Enter first number: 10
Enter second number: 5
Result: 15.0
```

---

## 🛡️ Error Handling

* **Invalid Input** → If the user enters non-numeric values, the program shows an error.
* **Division by Zero** → Gracefully handled with an error message.
* **Invalid Menu Choice** → Prompts the user to select from available options.

---

## 📌 Future Enhancements

* Add more operations (exponentiation, square root, modulus)
* Store and reuse the last result (memory feature)
* Improve UI with colorized terminal output
---
