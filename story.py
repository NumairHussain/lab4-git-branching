def intro():
    print("You wake up in a dark forest. You can go left or right.")
    choice = input("Which direction do you choose? (left/right): ").strip().lower()
    if choice == "left":
        left_path()
    elif choice == "right":
        right_path()
    else:
        print("You stand still, unsure what to do. The forest swallows you.")

def left_path():
    print("You walk left and find a mysterious glowing sword stuck in a stone.")
    print("You reach for the sword and are able to pull it out of the stone with ease")
    print("Whilst holding the sword, the area arround you brightens with little glowing orbs directing you a certain direction")
    print("Following the glowing orbs, you find your way out of the dark forest. Congrats!")

def right_path():
    print("You walk right and encounter a talking squirrel who challenges you to a duel.")

if __name__ == "__main__":
    intro()
