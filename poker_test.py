#連線到 Minecraft
#Step1. Connect python to Minecraft
from mcpi.minecraft import Minecraft
mc= Minecraft.create()

#匯入隨機功能
#Step2. import random function for later use
import random

#儲存撲克牌資訊
#Step3. Create lists for data storage
cards_symbol = ["梅花","方塊","愛心","黑桃"]
cards_number = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
player1_card = []
player2_card = []

#Step4. print name of the game
print("***card game***")
#Step5. Create the function I want
def Player1(status):
    # Step7. Determine User's answer
    #確認使用者狀態
    if status == "ok":
        # Step8. Print info 
        print("Player1's card: ")
        # Step9. Start picking cards randomly
        #隨機抽出3張牌
        for i in range(1,4):  
            card_combine = [random.choice(cards_symbol)+random.choice(cards_number)]
            # Step10. Store data into another list
            player1_card.append(card_combine)
        print(player1_card)
        #隨機抽出3張牌
        # Step11. get Player's position getTilePos() and Show the results in minecraft
        x, y, z = mc.player.getTilePos()
        mc.setSign(x, y, z, 63, 0,"Player1's card",player1_card[0],player1_card[1],player1_card[2])
    else:
        print("get ready!")
#Step6. Collect User's answer
Player1(input("Player1 enter your status(ok or not ok): "))