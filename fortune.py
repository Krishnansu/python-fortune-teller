# fortune.py

# Personal details
full_name = "Krishnansu Mohapatra"
admission_number = "21JE0483"

# Welcome message
print(f"🔮 Welcome to {full_name}'s Fortune Teller ({admission_number}) 🔮")

# Prompt user for mood
mood = input("How are you feeling today? (happy/sad/neutral): ").strip().lower()

# Fortune messages based on mood
if mood == "happy":
    print(f"✨ Your fortune: Great things await you, {full_name}! Keep smiling. ✨")
elif mood == "sad":
    print(f"✨ Your fortune: This too shall pass, {full_name}. Stay strong. ✨")
elif mood == "neutral":
    print(f"✨ Your fortune: Embrace the calm, {full_name}. Good things are coming. ✨")
else:
    print("⚠️ Sorry, I couldn't recognize that mood. Please enter happy, sad, or neutral.")