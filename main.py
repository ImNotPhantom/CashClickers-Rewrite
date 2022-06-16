import os
from time import sleep
from Modules import dataModule

# Game Objects
d = dataModule.data()

# Game variables
data = {
    'cash': 0,
    'multiplier': 1
}

# Game functions
def addCash(cash, multiplier):
    cash += multiplier
    return cash

# Before the game starts check if they have save data
if os.path.isfile('data.json'):
    data = d.load()

# Game loop
run = True
while run:
    # Save data
    d.save(data)

    # User input
    wtd = input(f"You have ${data['cash']}\nEnter to get cash💵\n1. Stats📄\n2. Quit❌\n")

    # Add cash
    if wtd == "":
        data['cash'] = addCash(data['cash'], data['multiplier'])
    
    # Show stats
    if wtd == "1":
        print(f"\n\n💰 You have ${data['cash']} 💰")
        print(f"✖️  You have {data['multiplier']} multiplier/s ✖️\n\n")
        sleep(2)
    
    # Quit game
    if wtd == "2":
        print("\n\nGoodbye! 👋")
        sleep(1)
        run = False
