# 🎮 Monty Hall Problem Game 🚀
### A visually stunning and educational simulation of the world-famous Monty Hall probability paradox

The **Monty Hall Problem** is one of the most surprising and mind-bending puzzles in probability mathematics.  
This desktop application turns the paradox into a **fun, interactive game show** with:

- 🎬 **Door-opening animations**
- 🐐 **Goat and 🚗 Car visual reveal**
- 🎲 **Full guided demo tutorial**
- 🧠 **Post-round explanation to understand WHY switching works**
- 📊 **Simulation graph to see probability in action**
- 🌙 **Modern dark-mode UI with premium game layout**

---

## ✨ Features
| Feature | Status |
|--------|:------:|
| Animated doors opening like a real game show | ✔ |
| Goat & car visual reveal effects | ✔ |
| Step-by-step guided demo before gameplay | ✔ |
| Clear instructions & learning explanation | ✔ |
| Switch vs Stay interactive choice | ✔ |
| Probability simulation graph (matplotlib) | ✔ |
| Beautiful modern UI built with CustomTkinter | ✔ |

---

## 🧠 What is the Monty Hall Problem?
An educational paradox about decision-making and probability.

There are **3 doors**:
- 🚗 One contains a **car**
- 🐐 Two contain **goats**

### **How the game works**
1. You choose a door.
2. Monty (the host) opens another door that he **knows contains a GOAT**
3. You must choose:
   - **Stay** with your original door, or
   - **Switch** to the remaining closed door

### ⚖ The shocking truth:
| Strategy | Win chance |
|-----------|-----------|
| Stay | ❌ 33.3% |
| Switch | 🏆 66.6% (double the chance!) |

Monty revealing a goat gives additional information, shifting probability to the other door.

---

## 🖥 Concept Layout
🚪 Door 0 🚪 Door 1 🚪 Door 2
↓ You pick a door
Monty opens Door 0 → 🐐 Goat
Remaining: Door 1 & Door 2

---

## 📦 Requirements
Install dependencies:
```bash
pip install customtkinter numpy matplotlib
```
---
## 🧰 Technologies Used
- Library	Purpose
- CustomTkinter	Stunning GUI and dark mode
- Matplotlib	Probability chart & visualization
- NumPy	Simulation engine
- Python	Core logic and interface
---
## 🧠 Learning Outcomes

- Better understanding of probability & conditional reasoning
- Shows how intuition can be misleading
- Demonstrates how information affects probability
---
## 🧪 Future Enhancements

🔊 Add sound effects and celebration animations
👥 Multiplayer mode with leaderboard
➕ Adjustable number of doors (3-10)
🧠 AI strategy learning model

---
