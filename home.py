import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
_id = mc.getPlayerEntityId('greatjune')
x = 89.974
y = 79.000 + 100
z = 278.472
pos = mc.entity.setPos(_id, x, y-180, z-241)