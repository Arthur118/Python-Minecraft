#step1 connect minecraft with spyder
from mcpi.minecraft import Minecraft
mc=Minecraft.create()

#step2 create a variable for later use
air =0

#step3 print the info
print("****自動建築機器人****")

#step4 ask for info
name = input("請問你的名字為: ")
l = int(input(name + ",請問你要多長的建築: "))
w = int(input(name + ",請問你要多寬的建築: "))
h= int(input(name + ",請問你要多高的建築: "))

#step5 covert the input data type
blockType = int(input("請輸入你要放入的建材方塊ID: "))
while len(l,w,h)>0:
    #step6 get the player's position and set blocks
    x,y,z = mc.player.getTilePos()
    mc.setBlocks(x, y, z, x+w-1, y+h-1, z+l-1, blockType)
    mc.setBlocks(x+1, y+1, z+1, x+w-2, y+h-2, z+l-2, air)

    #step7 show info in minecraft
    mc.postToChat(name+",您所使用的建材ID為: "+str(blockType))
    mc.postToChat("正在幫您生成長"+str(l)+"個方塊，"+"寬"+str(w)+"個方塊，高"+str(h)+"個方塊的建築物")
    