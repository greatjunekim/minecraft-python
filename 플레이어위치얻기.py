from mcpi.minecraft import Minecraft
mc = Minecraft.create()
_id = mc.getPlayerEntityId('greatjune')
pos = mc.entity.getPos(_id)
print(pos)