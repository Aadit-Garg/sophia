DIALOGUES = [
    "Welcome to our exhibition, where art and innovation collide.",
    "Step right in and immerse yourself in a world of creativity and imagination.",
    "Discover the extraordinary in the ordinary at our unique exhibition.",
    "Experience the fusion of history and future in our timeless exhibits.",
    "Explore the depths of human creativity in every corner of our exhibition.",
    "Unveil the mysteries of the universe through our thought-provoking displays.",
    "Journey through time and space as you navigate our exhibits.",
    "Witness the power of ideas brought to life in our interactive displays.",
    "Engage with the past, present, and future in our immersive exhibition.",
    "Celebrate the triumph of human imagination at our grand exhibition. Enjoy your visit!"
]

def greeting():
    import datetime
    currentTime = datetime.datetime.now()
    currentTime.hour
    if currentTime.hour < 12: return('Good morning.')
    elif 12 <= currentTime.hour < 18: return('Good afternoon.')
    else: return('Good evening.')

FIXED_DIALOGUES = ["hello",f"{greeting()}, my name is Sophia.", "Welcome to S D Public School"]
