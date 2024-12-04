import pandas as pd
import matplotlib.pyplot as plt
import re

# Load data
file_path = 'G:/My Drive/08 X2/Wellbeing Y8/8X2 Wellbeing 20-11-2024.xlsx'
data = pd.read_excel(file_path)

# List of questions
questions = [
    "I am good at gaming", "It is important to me that I look good",
    "Boys and girls are completely different",
    "The best job for you is one that matches your skills, abilities and personal qualities",
    "Maths is boys’ subject", "Being the only male/female in a class would put me off choosing that subject",
    "Nursing is a profession best suited to women", "Girls do better in school than boys",
    "Your gender should have no impact on your subject choices", "Most girls don’t want to be scientists",
    "Crying in front of people is ok if I am upset", "Girls are always caring and nurturing",
    "I listen to more female artists than male artists", "I look up to people of the same gender as me",
    "My parents expect me to behave in a certain way", "Boys and girls should go to different schools",
    "Males and females are equal", "Boys are more immature than girls",
    "I am expected to act a certain way at school because of my gender"
]

def clean_filename(text):
    """ Remove unusual punctuation from text, keeping spaces and alphanumerics. """
    return re.sub(r'[^\w\s]', '', text)

response_colors = {
    'Strongly agree': '#1cfc03',
    'Agree': '#cafc03',
    'Neutral': '#fceb03',
    'Disagree': '#fc9803',
    'Strongly disagree': '#fc3103'
}

preferred_order = ['Strongly agree', 'Agree', 'Disagree', 'Strongly disagree']

# Process each question
for question in questions:
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    for i, gender in enumerate(['M', 'F']):
        # Filter data by gender
        gender_data = data[data['Gender'] == gender]
        
        # Count responses
        response_counts = gender_data[f'Questions [{question}]'].value_counts()
        response_counts = response_counts.reindex(preferred_order)
        print(f'Questions [{question}]',response_counts)
        # Plot
        colors = [response_colors[label] for label in response_counts.index if label in response_colors]
        axes[i].pie(response_counts, labels=response_counts.index, autopct='%1.1f%%', startangle=90, colors=colors)
        axes[i].set_title(f'{question} ({gender})')
    
    plt.tight_layout()
    plt.savefig("G:/My Drive/08 X2/Wellbeing Y8/4 Dec/"+clean_filename(question) + '.png', dpi=300)
    plt.close()