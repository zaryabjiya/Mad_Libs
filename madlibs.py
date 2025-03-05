import random

# Welcome message
print("\033[1;35m🔥 Welcome to Zaryab's Epic Mad Libs Adventure! 🔥\033[0m\n")
print("\033[1;34m😆 Fill in the blanks and create your own hilarious story! 🎭✨\033[0m\n")

# Taking user inputs
name = input("\033[1;32m🔹 Enter your name: \033[0m")
superpower = input("\033[1;33m⚡ Enter a superpower: \033[0m")
weird_creature = input("\033[1;36m🐉 Enter a weird creature: \033[0m")
place = input("\033[1;31m📍 Enter a magical place: \033[0m")
food = input("\033[1;35m🍕 Enter your favorite food: \033[0m")
object = input("\033[1;34m🎩 Enter a random object: \033[0m")
emotion = input("\033[1;32m😊 Enter an emotion: \033[0m")
sound = input("\033[1;33m🔊 Enter a funny sound (like 'Boom' or 'Zing'): \033[0m")

# Random action choices
actions = [
    "started breakdancing like a robot 🤖💃",
    "flew high like a rocket 🚀🔥",
    "turned invisible and pranked everyone 👻😂",
    "sang a rap song about coding 🎤🎶",
    "juggled flaming swords like a pro 🔥⚔️"
]

random_action = random.choice(actions)

# Creating the story
story = f"""
\033[1;35m✨🌟 YOUR LEGENDARY MAD LIBS STORY 🌟✨\033[0m

📌 One fine day, {name} 😎 woke up with a mysterious power: {superpower}! 🦸‍♂️💥
   Excited, {name} traveled to {place} 🏰 to test it out.

🐉 Suddenly, a giant {weird_creature} appeared, blocking the way! 😱
   Without hesitation, {name} used {superpower} and {random_action.upper()} 🌀💨.

🎉 The {weird_creature} was so {emotion} 🤩 that it made a loud '{sound}!' 🔊 and ran away!

🍛 After this crazy adventure, {name} sat down, picked up a {object} 🎩, and enjoyed {food} 🤤.

🏆🔥 And that, my friend, is how {name} became the Hero of {place}! 🎭🎉
"""

# Printing the final story
print("\n" + "="*60)
print(story)
print("="*60 + "\n")