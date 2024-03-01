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
