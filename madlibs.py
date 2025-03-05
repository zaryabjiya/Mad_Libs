# Welcome message
print("🎭 Welcome to the Mad Libs Game! Fill in the blanks and create a funny story. ✨")

# Taking user inputs
name = input("Enter a name: ")
superpower = input("Enter a superpower: ")
creature = input("Enter a mythical creature: ")
place = input("Enter a mysterious place: ")
object = input("Enter a magical object: ")
emotion = input("Enter an emotion: ")
sound = input("Enter a funny sound: ")

# Mad Libs story template
story = f"""
🌟✨ THE LEGEND OF {name.upper()} ✨🌟  

One day, {name} woke up and discovered an incredible power: {superpower}! ⚡  
Determined to test this power, {name} traveled to the {place}. 🏰  

Suddenly, a {creature} appeared! 😱 It roared, making a loud "{sound}!" 🔊  
Without hesitation, {name} used their {superpower} and defeated the creature! 💥  

Feeling {emotion}, {name} picked up a {object}, smiled, and became the **Hero of {place}!** 🎉🏆  
"""

# Print the final story
print("\nYour Mad Libs Adventure is Ready! 🚀\n")
print(story)
