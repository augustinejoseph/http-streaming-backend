# sentences.py

import random

SENTENCES = [
    "There is some good in this world, and it’s worth fighting for. In the darkest times, even a small act of kindness can make a tremendous difference.",
    "The only limit to our realization of tomorrow will be our doubts of today. Embrace challenges, for they are the stepping stones to success.",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. Learn from every experience, and let neither success nor failure define you.",
    "In the middle of difficulty lies opportunity. When faced with challenges, see them as opportunities for growth and learning.",
    "The future belongs to those who believe in the beauty of their dreams. Dream big and work towards turning those dreams into reality.",
    "Do not wait to strike till the iron is hot, but make it hot by striking. Procrastination is the enemy of progress; take initiative and create your opportunities.",
    "It always seems impossible until it’s done. Break down your goals into smaller tasks, and take one step at a time.",
    "Believe you can and you're halfway there. Confidence is the key to success; believe in yourself and your abilities.",
    "I can't change the direction of the wind, but I can adjust my sails to always reach my destination. Adaptability is a valuable skill in navigating life's challenges.",
    "A person who never made a mistake never tried anything new. Embrace failure as a part of the learning process.",
    "The only way to do great work is to love what you do. Find passion in your work, and success will follow.",
    "You miss 100% of the shots you don't take. Take risks and seize opportunities for growth.",
    "To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment. Stay true to your values and authenticity.",
    "What lies behind us and what lies before us are tiny matters compared to what lies within us. Your inner strength and character define your journey.",
    "The only person you are destined to become is the person you decide to be. Take control of your destiny and shape your own future.",
    "I've learned that people will forget what you said, people will forget what you did, but people will never forget how you made them feel. Be kind and leave a positive impact on others.",
    "In three words I can sum up everything I've learned about life: it goes on. Embrace the impermanence of life and focus on the present.",
    "The best way to predict the future is to create it. Take proactive steps to shape your desired future.",
    "It is not the strongest of the species that survive, nor the most intelligent, but the one most responsive to change. Adaptability is a key factor in long-term success.",
]

def get_random_sentence():
    return random.choice(SENTENCES)
