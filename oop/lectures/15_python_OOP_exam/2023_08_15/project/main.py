
"""
project/
│
├── equipment/
│   ├── __init__.py
│   ├── base_equipment.py
│   ├── elbow_pad.py
│   └── knee_pad.py
│
└── teams/
    ├── __init__.py
    ├── base_team.py
    ├── indoor_team.py
    └── outdoor_team.py
"""
from project.equipment.base_equipment import BaseEquipment
from project.teams.base_team import BaseTeam
from project.teams.outdoor_team import OutdoorTeam
from project.teams.indoor_team import IndoorTeam
from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.tournament import Tournament

# TEST

t = Tournament('SoftUniada2023', 2)

print(t.add_equipment('KneePad'))
print(t.add_equipment('ElbowPad'))

print(t.add_team('OutdoorTeam', 'Levski', 'BG', 250))
print(t.add_team('OutdoorTeam', 'Spartak', 'BG', 250))
print(t.add_team('IndoorTeam', 'Dobrich', 'BG', 280))

print(t.sell_equipment('KneePad', 'Spartak'))

print(t.remove_team('Levski'))
print(t.add_team('OutdoorTeam', 'Lokomotiv', 'BG', 250))

print(t.increase_equipment_price('ElbowPad'))
print(t.increase_equipment_price('KneePad'))

print(t.play('Lokomotiv', 'Spartak'))

print(t.get_statistics())

# OUTPUT
"""
KneePad was successfully added.
ElbowPad was successfully added.
OutdoorTeam was successfully added.
OutdoorTeam was successfully added.
Not enough tournament capacity.
Successfully sold KneePad to Spartak.
Successfully removed Levski.
OutdoorTeam was successfully added.
Successfully changed 1pcs of equipment.
Successfully changed 0pcs of equipment.
The winner is Spartak.
Tournament: SoftUniada2023
Number of Teams: 2
Teams:
Name: Spartak
Country: BG
Advantage: 365 points
Budget: 985.00EUR
Wins: 1
Total Equipment Price: 15.00
Average Protection: 120
Name: Lokomotiv
Country: BG
Advantage: 250 points
Budget: 1000.00EUR
Wins: 0
Total Equipment Price: 0.00
Average Protection: 0



"""
