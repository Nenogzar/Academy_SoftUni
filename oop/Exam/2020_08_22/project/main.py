from project.rooms.alone_old import AloneOld
from project.rooms.alone_young import AloneYoung
from project.rooms.old_couple import OldCouple

AY = AloneYoung("Kaka", 250)
AL = AloneOld("Batko", 300)
OC = OldCouple("Kostovi", 10,10)
print(AY.members_count)

