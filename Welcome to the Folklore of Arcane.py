def main():
    print("Welcome to the Folklore of Arcane...\n")
    print("Whisper your words into the misty shadows below.\n")

    character = input("Name a legendary figure from Arcane: ")
    emotion = input("Name an emotion (e.g., sorrow, rage): ")
    relic = input("Name a magical object or relic: ")
    action = input("An old-world action (e.g., wander, vanish, strike): ")
    creature = input("A mystical creature (real or imagined): ")
    location = input("A place in Piltover or Zaun: ")
    symbol = input("A symbolic item (e.g., flame, mask, crown): ")

    print("\n--- The Whispered Tale ---\n")

    print(f"In the time before hextech, when shadows ruled the alleys of {location},")
    print(f"there lived a soul named {character}, born of {emotion} and fire.")
    print(f"With a heart bound to the ancient {relic}, they would often {action} beneath the gaslit haze.")
    print(f"Legends say they once tamed a {creature} with nothing but a glance,")
    print(f"and vanished beneath the city, leaving only a {symbol} behind.")
    print(f"To this day, when the wind howls through {location},")
    print(f"some say you can still hear {character}'s name carried in the echo.\n")

    print("Such is the tale — remembered by few, feared by many.")

if __name__ == '__main__':
    main()
