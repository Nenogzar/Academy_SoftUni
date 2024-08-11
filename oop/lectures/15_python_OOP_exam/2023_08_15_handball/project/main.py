from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.indoor_team import IndoorTeam
from project.tournament import Tournament
#
# eqk = KneePad()
# print(eqk.price, "price")
# eqk.increase_price()
# print(eqk.price, "increases price")
# print(eqk.protection, "protection")
# print("-------")
# eqe = ElbowPad()
# print(eqe.price, "price")
# eqe.increase_price()
# print(eqe.price, "increases price")
# print(eqe.protection, "protection")
#
#
# print("-------")
#
# try:
#     tur = Tournament("Koko123", 250)
#
#
#
# except ValueError as t:
#     print(t)

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

