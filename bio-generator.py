def bio_generator():
    print('Welcome to the Bio Generator! Please answer the following questions:')

    # Collecting user input
    name = input('What is your name? ')  
    age = int(input('How old are you? '))  
    location = input('Where are you located? ')  
    profession = input('What is your profession? ')  
    hobbies = input('What are your hobbies or interests? ')  
    skills = input('What are your skills? ')  
    goals = input('What are your goals or aspirations? ')  
    achievements = input("What are your achievements? ")

    # Generating the bio
    bio = f'''
--- BIO ---
Name: {name}
Age: {age}
Location: {location}
Profession: {profession}
Hobbies/Interests: {hobbies}
Skills: {skills}
Goals/Aspirations: {goals}
Achievements: {achievements}
'''

    # Displaying the generated bio
    print('\nHere is your generated bio:\n')
    print(bio)


if __name__ == '__main__':
    bio_generator()