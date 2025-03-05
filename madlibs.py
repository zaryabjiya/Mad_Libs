import streamlit as st
import random

# Set up the page configuration
st.set_page_config(page_title="Adventure Story Generator", page_icon="🧙‍♂️", layout="centered")

# Custom CSS for better styling
st.markdown("""
<style>
    body {
        background-color: #F5F5DC;
        color: #333;
        font-family: 'Arial', sans-serif;
        text-align: center;
    }
    .stTextInput > div > div > input {
        background: white;
        color: #333;
        border: 2px solid #8B4513;
        border-radius: 10px;
        padding: 12px;
        font-size: 16px;
    }
    .stButton button {
        background-color: #8B4513;
        color: white;
        font-size: 18px;
        border-radius: 10px;
        padding: 12px 20px;
        border: none;
        transition: 0.3s;
    }
    .stButton button:hover {
        background-color: #5D4037;
    }
    .footer {
        margin-top: 50px;
        text-align: center;
        font-size: 14px;
        color: #444;
        font-weight: bold;
        padding: 10px;
        background: #D2B48C;
        border-radius: 5px;
    }
</style>
""", unsafe_allow_html=True)

# Title and introduction
st.title("🧙‍♂️ Adventure Story Generator")
st.write("Fill in the blanks and create your own *magical adventure!* ✨")

# Input fields
name = st.text_input("Enter your name:", help="Your hero name in the story")
superpower = st.text_input("Enter a superpower:", help="Any magical ability")
creature = st.text_input("Enter a mythical creature:", help="Like dragon, unicorn, etc.")
place = st.text_input("Enter a mysterious place:", help="Like enchanted forest, haunted castle")
object = st.text_input("Enter a magical object:", help="Like sword, wand, shield")
emotion = st.text_input("Enter an emotion:", help="Like happy, scared, excited")
sound = st.text_input("Enter a funny sound:", help="Like BOOM, ZAP, KABOOM")

# Random actions
actions = [
    "flew across the sky like a shooting star 🌠",
    "turned invisible and sneaked past the enemy 👻",
    "fought bravely with unmatched power ⚔️🔥",
    "solved an ancient puzzle and unlocked hidden secrets 🏆",
    "tamed a wild beast and rode it like a champion 🐉🏇",
    "discovered a hidden portal and traveled to another dimension 🌌",
    "used magic to summon an army of tiny helpers 🧚‍♂️"
]
random_action = random.choice(actions)

# Random story twists
twists = [
    "But suddenly, the sky turned dark, and a hidden enemy emerged! ☠️",
    "Just when {name} thought it was over, the ground started shaking! 🌍⚡",
    "A mysterious voice whispered a secret that changed everything... 🤫",
    "The magical object started glowing, revealing a hidden message! ✨📜",
    "A portal opened, sucking {name} into another realm! 🌪️",
]
random_twist = random.choice(twists)

# Generate story button
if st.button("Create My Adventure! 🚀"):
    if name and superpower and creature and place and object and emotion and sound:
        story = f"""
        🌟✨ *THE LEGEND OF {name.upper()}* ✨🌟  
        
        One day, {name} woke up and discovered an incredible power: *{superpower}!* 🦸‍♂️⚡  
        Determined to test this power, {name} traveled to the *{place}*. 🌳🏰  
        
        Suddenly, a *{creature}* appeared! 😱 It roared, making a loud *'{sound}!'* 🔊  
        Without hesitation, {name} used their *{superpower}* and *{random_action}*! 💨⚡  
        
        The {creature} was so *{emotion}* that it fled instantly! 🏃‍♂️💨  
        Victorious, {name} picked up their *{object}*, smiled, and became the **Legend of {place}!* 🏆🔥  
        
        {random_twist.replace('{name}', name)}
        """
        
        st.success("Your Adventure is Ready! 🎉")
        st.markdown(story)
        
        # Restart button
        if st.button("Restart 🔄"):
            st.experimental_rerun()
    else:
        st.warning("⚠️ Please fill in all the blanks to create your story!")

# Footer
st.markdown("<div class='footer'>Developed by Zaryab Irfan 🚀</div>", unsafe_allow_html=True)
