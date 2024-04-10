likes = {"color": "blue", "fruit": "apple", "pet": "dog"}

while True:
    try:
        print(f"Dictionary length: {len(likes)}")
        item = likes.popitem()
        # Do something with the item here...
        print(f"Item {item} removed")
    except KeyError:
        print("Your dictionary is now empty.")
        break

        # Dictionary length: 3
        # Item ('pet', 'dog') removed
        # Dictionary length: 2
        # Item ('fruit', 'apple') removed
        # Dictionary length: 1
        # Item ('color', 'blue') removed
        # Dictionary length: 0
        # Your dictionary is now empty.

############################################

likes1 = {"color": "blue", "fruit": "apple", "pet": "dog"}
while likes1:
    print(f"Dictionary length: {len(likes1)}")
    item = likes1.popitem()
    # Do something with the item here ...
    print(f"Item {item} removed")
    # Dictionary length: 3
    # Item ('pet', 'dog') removed
    # Dictionary length: 2
    # Item ('fruit', 'apple') removed
    # Dictionary length: 1
    # Item ('color', 'blue') removed