from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time
water = 8
lava = 11
_id = mc.getPlayerEntityId('greatjune')
x = 213
y = 73
z = 198
pos = mc.entity.setPos(_id, x, y+9 , z)
while True:
    mc.setBlock( x-1, y+1, z-1, lava)

print("용암")