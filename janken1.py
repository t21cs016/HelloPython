'''
Created on 2023/10/13

@author: t21cs016
'''
import random

def janken():
    # グー、チョキ、パーを数字で表す
    choices = [0, 1, 2]
    
    # プレイヤー１とプレイヤー２の手をランダムに選ぶ
    player1_choice = random.choice(choices)
    player2_choice = random.choice(choices)
    
    # 手の対応を表示
    choices_dict = {0: "グー", 1: "チョキ", 2: "パー"}
    print(f"プレイヤー１の手: {choices_dict[player1_choice]}")
    print(f"プレイヤー２の手: {choices_dict[player2_choice]}")
    
    # 勝敗判定
    if player1_choice == player2_choice:
        result = "引き分け"
    elif (player1_choice == 0 and player2_choice == 1) or (player1_choice == 1 and player2_choice == 2) or (player1_choice == 2 and player2_choice == 0):
        result = "プレイヤー1の勝ち"
    else:
        result = "プレイヤ−２の勝ち"
    
    print(result)

# じゃんけんを実行

