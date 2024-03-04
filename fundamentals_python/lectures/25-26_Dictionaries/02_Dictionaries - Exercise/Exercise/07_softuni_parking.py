class ParkingSystem:
    def __init__(self):
        self.users = {}  # Dictionary to store registered users and their license plates

    def register_user(self, username, license_plate):
        if username in self.users:
            print(f"ERROR: already registered with plate number {self.users[username]}")
        else:
            self.users[username] = license_plate
            print(f"{username} registered {license_plate} successfully")

    def unregister_user(self, username):
        if username not in self.users:
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            del self.users[username]

    def print_registered_users(self):
        for username, license_plate in self.users.items():
            print(f"{username} => {license_plate}")


# Main program
if __name__ == "__main__":
    n = int(input())
    parking_system = ParkingSystem()

    for _ in range(n):
        command_parts = input().split()
        command_type = command_parts[0]

        if command_type == "register":
            _, username, license_plate = command_parts
            parking_system.register_user(username, license_plate)
        elif command_type == "unregister":
            _, username = command_parts
            parking_system.unregister_user(username)

    parking_system.print_registered_users()
###################
"""  """

dict_registered = {}

reg_num = int(input())

for _ in range(reg_num):
    info_string = input().split(" ")

    if len(info_string) == 3:
        type_register, name, reg_num = [item for item in info_string]

        if type_register == "register":
            if name not in dict_registered:
                dict_registered[name] = reg_num
                print(f"{name} registered {reg_num} successfully")
            else:
                print(f"ERROR: already registered with plate number {dict_registered[name]}")

    elif len(info_string) == 2:
        type_register, name = [item for item in info_string]
        if type_register == "unregister":
            if name in dict_registered:
                del dict_registered[name]
                print(f"{name} unregistered successfully")
            else:
                print(f"ERROR: user {name} not found")

for name, license in dict_registered.items():
    print(f"{name} => {license}")

###################
""" I.Shopov """
parking = {}
n = int(input())
for i in range(n):
    command = input().split()
    action = command[0]

    if action == "register":
        key = command[1]
        value = command[2]
        if key in parking.keys():
            print(f"ERROR: already registered with plate number {parking[key]}")
        else:
            parking[key] = value
            print(f"{key} registered {value} successfully")
    elif action == "unregister":
        key = command[1]
        if key in parking.keys():
            del parking[key]
            print(f"{key} unregistered successfully")
        else:
            print(f"ERROR: user {key} not found")
for key in parking.keys():
    print(f"{key} => {parking[key]}")

####################
"""kuchovalcho """
def register(username: str, car_plate: str):
    if username in parking:
        return f"ERROR: already registered with plate number {car_plate}"

    parking[username] = car_plate
    return f"{username} registered {car_plate} successfully"


def unregister(username: str):
    if username not in parking:
        return f"ERROR: user {username} not found"

    parking.pop(username)
    return f"{username} unregistered successfully"


parking = {}

commands = {
    'register': register,
    'unregister': unregister,
    }

number_of_operations = int(input())
for _ in range(number_of_operations):
    command, name, *license_plate = input().split()

    print(commands[command](name, *license_plate))

for name, plate in parking.items():
    print(f"{name} => {plate}")
