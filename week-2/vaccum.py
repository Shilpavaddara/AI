def vacuum_cleaner(location, room_A, room_B):
    if location == "A":
        if room_A == "Dirty":
            print("Suck: Cleaning Room A")
            room_A = "Clean"
        else:
            print("Room A is clean. Move Right to Room B")
            location = "B"

    elif location == "B":
        if room_B == "Dirty":
            print("Suck: Cleaning Room B")
            room_B = "Clean"
        else:
            print("Room B is clean. Move Left to Room A")
            location = "A"

    return location, room_A, room_B


# Example
location = "A"
room_A = "Dirty"
room_B = "Dirty"

for i in range(4):
    location, room_A, room_B = vacuum_cleaner(
        location, room_A, room_B
    )
