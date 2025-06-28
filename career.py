# career.py

print("🎓 Welcome to the AI Career Path Recommender!\n")

name = input("Enter your name: ")
coding = input("Do you like coding? (yes/no): ").strip().lower()
math = input("Are you good at Math? (yes/no): ").strip().lower()
fav_subject = input("What's your favourite subject? [CS, Biology, Physics, etc.]: ").strip().lower()
marks = int(input("Your average marks in last exam (%): "))

# Logic for career recommendation
if coding == "yes" and math == "yes":
    if fav_subject in ["cs", "computer science", "math"]:
        career = "Data Science or AI Engineering"
    elif fav_subject == "physics":
        career = "Software Developer or Robotics"
    else:
        career = "Computer Applications"
elif coding == "no" and fav_subject == "biology":
    career = "Medical or Biotech Research"
elif math == "yes" and fav_subject == "commerce":
    career = "Finance, Data Analytics or Chartered Accountancy"
elif coding == "yes":
    career = "Web Development or UI/UX Design"
else:
    career = "Generalist or Management Roles"

print(f"\n✅ Hi {name}, based on your answers...")
print(f"🌟 Recommended Career Path: {career}")
