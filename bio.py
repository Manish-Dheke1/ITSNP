



import random


def generate_bio(name: str, age: int, profession: str, hobbies: list, skills: list, achievements: list, goals: list) -> str:
    
    templates = [
        f"""
{name} is a {age}-year-old {profession} with a passion for {', '.join(hobbies)}. 
Skilled in {', '.join(skills)}, {name} has achieved {', '.join(achievements)}. 
Driven by the goal of {', '.join(goals)}, {name} continues to pursue excellence.
        """,

        f"""
Meet {name}, a talented {profession} aged {age}. With expertise in {', '.join(skills)},
{name} has accomplished {', '.join(achievements)}. In their free time, {name} enjoys {', '.join(hobbies)}.
Their aspirations include {', '.join(goals)}.
        """,

        f"""
{name}, a {age}-year-old {profession}, is known for their proficiency in {', '.join(skills)}.
They have successfully {', '.join(achievements)}, and enjoy {', '.join(hobbies)} during leisure.
With ambitions of {', '.join(goals)}, {name} is on a journey of growth and success.
        """
    ]

    return random.choice(templates)


def main():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    profession = input("Enter profession: ")
    hobbies = input("Enter hobbies (comma-separated): ").split(", ")
    skills = input("Enter skills (comma-separated): ").split(", ")
    achievements = input("Enter achievements (comma-separated): ").split(", ")
    goals = input("Enter goals (comma-separated): ").split(", ")

    bio = generate_bio(name, age, profession, hobbies, skills, achievements, goals)
    print("\nGenerated Bio:\n")
    print(bio)


if __name__ == "__main__":
    main()






# import random


# def generate_bio(data):
#     # Unpack the data dictionary
#     name = data.get("name", "Someone")
#     profession = data.get("profession", "a professional")
#     interests = data.get("interests", "various things")
#     skills = data.get("skills", "several skills")
#     tone = data.get("tone", "professional")
#     length = data.get("length", "medium")

#     # Define templates using a dictionary
#     tone_templates = {
#         "professional": [
#             f"{name} is a dedicated {profession} skilled in {skills}. Passionate about {interests}, {name} strives for excellence.",
#             f"As a {profession}, {name} specializes in {skills} with a strong interest in {interests}. Always focused on delivering quality results.",
#             f"Driven by a passion for {interests}, {name} excels as a {profession}, utilizing skills such as {skills}."
#         ],
        
#     }

#     # Print all tone templates
#     print("\n--- Tone Templates ---")
#     for tone_name, templates in tone_templates.items():
#         print(f"\n{tone_name.capitalize()} Templates:")
#         for template in templates:
#             print(f"- {template}")

#     # Choose a random template based on tone
#     template_list = tone_templates.get(tone, tone_templates["professional"])
#     template = random.choice(template_list)

#     # Adjusting length of the bio
#     if length == "short":
#         words = template.split()
#         template = " ".join(words[:15]) + "..."
#     elif length == "long":
#         template += f" With years of experience, {name} continues to push boundaries and excel."

#     return template


# user_data = {
#     "name": "Manish Dheke",
#     "profession": "Software Developer",
#     "interests": "technology, writing, and solving complex problems",
#     "skills": "Python, Django, React, and AI",
#     "tone": "professional",
#     "length": "medium"
# }

# bio = generate_bio(user_data)
# print("\nGenerated Bio:\n", bio)


