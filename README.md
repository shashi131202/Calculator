# 🧮 Calculator CLI App

A simple command-line calculator built in **Python**.  
It supports the four basic arithmetic operations: **Addition, Subtraction, Multiplication, and Division**.  
The app runs in a loop until the user chooses to exit.  

---

## 🚀 Features
- Addition (+)  
- Subtraction (−)  
- Multiplication (×)  
- Division (÷) with **zero division error handling**  
- Input validation for non-numeric values  
- User-friendly menu-based interface  

---

## 📂 Project Structure
calculator/
│
├── calculator.py # Main program file
└── README.md # Project documentation


---

## ⚙️ How It Works
1. The app shows a menu with operation choices.  
2. The user selects an operation (1–4) or exits (5).  
3. The user enters two numbers.  
4. The app performs the operation and displays the result.  
5. The loop continues until the user selects Exit.  

---

## ▶️ Usage

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/calculator-cli.git
cd calculator-cli

2. Run the program
python calculator.py

3. Example Run
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

🛡️ Error Handling

Invalid Input → If the user enters a non-numeric value, the program shows an error.

Division by Zero → Gracefully handled with an error message.

Invalid Choice → Prompts user to select a valid option.

📌 Future Enhancements

Exponentiation and Square Root functions

Memory storage for last result

Support for more advanced operations


---
