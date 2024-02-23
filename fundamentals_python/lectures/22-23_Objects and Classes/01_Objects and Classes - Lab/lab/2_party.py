class Party:
    def __init__(self):
        self.people = []


party_people = Party()
data_input = input()
while data_input != "End":
    party_people.people.append(data_input)
    data_input = input()

print(f"Going: {', '.join(party_people.people)}")
print(f"Total: {len(party_people.people)}")

