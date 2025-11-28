import customtkinter as ctk
import numpy as np
import matplotlib.pyplot as plt
import random
import time


def monty_hall_sim(num_trials=100000, change_choice=False, num_doors=3):
    winning_doors = np.random.randint(0, num_doors, num_trials)
    selected_doors = np.random.randint(0, num_doors, num_trials)
    if change_choice:
        selected_doors = (winning_doors - selected_doors) % num_doors
    return np.mean(winning_doors == selected_doors)


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.title("🎮 Monty Hall PRO — Animated Edition")
root.geometry("950x700")

# Globals
choice = None
winning_door = None
removed = None
door_buttons = []


# ---------------- DEMO / INTRO PAGE ----------------
def go_to_game():
    demo_frame.pack_forget()
    game_frame.pack(fill="both", expand=True)


demo_frame = ctk.CTkFrame(root)
demo_frame.pack(fill="both", expand=True)

ctk.CTkLabel(
    demo_frame, text="🎲 Monty Hall Game — How It Works",
    font=("Arial", 32, "bold")
).pack(pady=20)

instructions = (
    "🎯 There are 3 doors:\n"
    "🚗 One hides a CAR\n🐐 Two hide GOATS\n\n"
    "STEP 1️⃣  You choose a door.\n"
    "STEP 2️⃣  Monty opens another door showing a GOAT.\n"
    "STEP 3️⃣  You choose to STAY or SWITCH.\n\n"
    "💡 FACT: Switching almost DOUBLES your chances of winning.\n\n"
    "📌 DEMO Example:\n"
    "You choose Door 1.\n"
    "Monty opens Door 0 → 🐐 Goat.\n"
    "Remaining: Door 1 & Door 2.\n"
    "If the CAR is in Door 2 → switching wins 🚗.\n\n"
    "You’ll now PLAY and FEEL this paradox yourself!"
)

ctk.CTkLabel(
    demo_frame, text=instructions,
    font=("Arial", 20),
    justify="center",
    text_color="white"
).pack(pady=10)

ctk.CTkButton(
    demo_frame,
    text="🚀 Got it – Start Playing",
    width=280,
    height=55,
    font=("Arial", 22, "bold"),
    command=go_to_game
).pack(pady=30)


# ---------------- GAME LOGIC WITH ANIMATION ----------------
def reset_doors_visual():
    """Reset all doors to closed state."""
    for i, btn in enumerate(door_buttons):
        btn.configure(
            text=f"🚪 Door {i}",
            fg_color="#1f538d",
            text_color="white",
            state="normal"
        )


def animate_monty_open():
    """Monty walks to the door and reveals a goat."""
    status.configure(
        text=f"Monty is walking towards Door {removed}...",
        text_color="yellow"
    )
    root.update()
    time.sleep(0.7)

    status.configure(
        text=f"Monty opens Door {removed}...",
        text_color="yellow"
    )
    root.update()
    time.sleep(0.7)

    # Show goat on that door
    door_buttons[removed].configure(
        text="🐐 GOAT",
        fg_color="#b30000",
        text_color="white",
        state="disabled"
    )
    status.configure(
        text=f"Door {removed} has a GOAT 🐐!\nDo you want to SWITCH your door?",
        text_color="orange"
    )
    switch_frame.pack(pady=15)


def start_round(selected):
    """User picks a door, Monty will open one of the others."""
    global choice, winning_door, removed
    reset_doors_visual()
    explanation_label.configure(text="")

    choice = selected
    winning_door = random.randint(0, 2)
    # Monty chooses a door that is not your choice and not the winning door
    removed = next(d for d in range(3) if d != choice and d != winning_door)

    status.configure(
        text=f"You selected Door {choice}.",
        text_color="white"
    )
    switch_frame.forget()
    root.update()
    time.sleep(0.8)

    animate_monty_open()


def reveal_final(is_switch):
    """Reveal the final door with animation and explanation."""
    global choice

    if is_switch:
        choice = next(d for d in range(3) if d != choice and d != removed)

    status.configure(text="Opening your final door...", text_color="cyan")
    root.update()
    time.sleep(0.9)

    # Win or lose?
    if choice == winning_door:
        door_buttons[choice].configure(
            text="🚗 CAR!",
            fg_color="green",
            text_color="black"
        )
        status.configure(text="🎉 YOU WON THE CAR! 🚗💨", text_color="lime")
    else:
        door_buttons[choice].configure(
            text="🐐 GOAT",
            fg_color="#b30000",
            text_color="white"
        )
        status.configure(text="💀 You got a GOAT 🐐", text_color="red")

    # Explanation about probability
    explanation_label.configure(
        text=(
            "\n🧠 WHY DOES SWITCHING WORK?\n"
            "When you FIRST choose a door, you only have a 1/3 chance of picking the car.\n"
            "That means the OTHER two doors together have a 2/3 chance.\n\n"
            "Monty then opens ONE of those other doors and shows a GOAT on purpose.\n"
            "He never opens the car door. This pushes the entire 2/3 chance\n"
            "onto the LAST remaining closed door.\n\n"
            "🎯 If you SWITCH, you get that 2/3 chance ⇒ ~66.6% win rate.\n"
            "😬 If you STAY, you are stuck with your original 1/3 chance ⇒ ~33.3%.\n\n"
            "So in the LONG RUN, switching wins ABOUT TWICE as often as staying."
        ),
        text_color="white",
        font=("Arial", 18),
        justify="center"
    )


def on_switch():
    switch_frame.forget()
    reveal_final(is_switch=True)


def on_stay():
    switch_frame.forget()
    reveal_final(is_switch=False)


def show_sim():
    trials = [5000, 10000, 20000, 50000, 100000]
    stay = []
    switch = []
    for t in trials:
        stay.append(monty_hall_sim(t, False))
        switch.append(monty_hall_sim(t, True))

    plt.figure(figsize=(9, 6))
    plt.plot(trials, stay, marker="o", label="Stay Strategy")
    plt.plot(trials, switch, marker="o", label="Switch Strategy")
    plt.title("Switching vs Staying — Win Probability")
    plt.xlabel("Number of Trials")
    plt.ylabel("Winning Probability")
    plt.grid(True)
    plt.legend()
    plt.show()


# ---------------- GAME UI ----------------
game_frame = ctk.CTkFrame(root)

ctk.CTkLabel(
    game_frame,
    text="Pick a Door and Test the Paradox",
    font=("Arial", 30, "bold"),
    text_color="cyan"
).pack(pady=15)

door_frame = ctk.CTkFrame(game_frame)
door_frame.pack(pady=10)

for i in range(3):
    btn = ctk.CTkButton(
        door_frame,
        text=f"🚪 Door {i}",
        width=170,
        height=70,
        font=("Arial", 20, "bold"),
        command=lambda i=i: start_round(i)
    )
    btn.pack(side="left", padx=12)
    door_buttons.append(btn)

status = ctk.CTkLabel(game_frame, text="", font=("Arial", 24, "bold"))
status.pack(pady=25)

switch_frame = ctk.CTkFrame(game_frame)

ctk.CTkButton(
    switch_frame,
    text="🔄 SWITCH DOOR",
    fg_color="orange",
    width=190,
    height=50,
    font=("Arial", 20, "bold"),
    command=on_switch
).pack(side="left", padx=12)

ctk.CTkButton(
    switch_frame,
    text="⛔ STAY",
    fg_color="gray",
    width=150,
    height=50,
    font=("Arial", 20, "bold"),
    command=on_stay
).pack(side="left", padx=12)

explanation_label = ctk.CTkLabel(game_frame, text="", font=("Arial", 18))
explanation_label.pack(pady=20)

ctk.CTkButton(
    game_frame,
    text="📊 Show Simulation Graph",
    command=show_sim,
    width=260,
    height=45,
    font=("Arial", 18, "bold")
).pack(pady=10)

root.mainloop()
