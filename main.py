import random
game_name = "SlayQuest" 
print("Welcome To SlayQuest!") # TODO, print greetings with game name
print("=====================") # TODO, add or remove equal symbol to align the greetings
print("Before we begin what's your character's name?")
 # Ask for the character's name
name = input()
print(f"Great, {name}! Let's begin the adventure!") 
 
 # Build player dictionary
player = {
    "name": name,
    "health": 100,
    "coin": 0
}

# Build events list
events = ["find a coin", "meet a monster", "do nothing"]

# Randomly choose one event
event = random.choice(events)
print(f"While exploring, you {event}!")

# Update stats based on event
if event == "find a coin":
    player["coin"] += 1
    print(f"{player['name']} found a coin, {player['name']} now has {player['coin']} coins.")
elif event == "meet a monster":
    player["health"] -= 10
    print(f"{player['name']} got hurt during the combat with monster, health is now {player['health']}.")
else:
    # do nothing
    pass
