import streamlit as st

st.set_page_config(page_title="Mad Libs Game", page_icon="🎭", layout="centered")

st.title("🎭 Mad Libs Game")
st.write("Fill in the blanks and create your own *funny story!* ✨")

name = st.text_input("Enter a name:")
superpower = st.text_input("Enter a superpower:")
creature = st.text_input("Enter a creature:")
place = st.text_input("Enter a place:")
object = st.text_input("Enter a object:")
emotion = st.text_input("Enter a emotion:")
sound = st.text_input("Enter a funny sound:")

if st.button("Create a story! 🚀"):
    if name and superpower and creature and place and object and emotion and sound:
        story = f"""
        🌟✨ THE LEGEND OF {name.upper()} ✨🌟 

        One day, {name} woke up and discovered an incredible power: {superpower}! ⚡ 
        Determined to test this power, {name} traveled to the {place}. 🏰 
        
        Duddenly, a {creature} appeared! 😱It roared, making a loud "{sound}!"  🔊
        Without hesitation, {name} used their {superpower} and defeated the creature! 💥 

        Feeling {emotion}, {name} picked up a {object}, smiled, and became the **Hero of {place}!**🎉🏆
        """

        st.success("Your Mad Libs Adventure is Ready! 🎉")
        st.markdown(story)
    else:
        st.warning("⚠️ Please fill in all the blanks to create your story!")    

st.markdown("<div style='margin-top:50px; text-align:center; font-size:14px; color:#444; font-weight:bold;'>Developed by Zaryab Irfan 🚀</div>", unsafe_allow_html=True)
