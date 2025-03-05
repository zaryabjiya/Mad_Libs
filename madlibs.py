import streamlit as st

# Set up the page configuration
st.set_page_config(page_title="Mad Libs Game", page_icon="🎭", layout="centered")

# Title and introduction
st.title("🎭 Mad Libs Game")
st.write("Fill in the blanks and create your own *funny story!* ✨")

# Input fields
name = st.text_input("Enter a name:")
superpower = st.text_input("Enter a superpower:")
creature = st.text_input("Enter a mythical creature:")
place = st.text_input("Enter a mysterious place:")
object = st.text_input("Enter a magical object:")
emotion = st.text_input("Enter an emotion:")
sound = st.text_input("Enter a funny sound:")

# Generate story button
if st.button("Create My Story! 🚀"):
    if name and superpower and creature and place and object and emotion and sound:
        story = f"""
        🌟✨ THE LEGEND OF {name.upper()} ✨🌟  
        
        One day, {name} woke up and discovered an incredible power: {superpower}! ⚡  
        Determined to test this power, {name} traveled to the {place}. 🏰  
        
        Suddenly, a {creature} appeared! 😱 It roared, making a loud "{sound}!" 🔊  
        Without hesitation, {name} used their {superpower} and defeated the creature! 💥  
        
        Feeling {emotion}, {name} picked up a {object}, smiled, and became the **Hero of {place}!** 🎉🏆  
        """
        
        st.success("Your Mad Libs Adventure is Ready! 🎉")
        st.markdown(story)
    else:
        st.warning("⚠️ Please fill in all the blanks to create your story!")

# Footer
st.markdown("<div style='margin-top:50px; text-align:center; font-size:14px; color:#444; font-weight:bold;'>Developed by Zaryab Irfan 🚀</div>", unsafe_allow_html=True)
