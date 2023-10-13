import random

def get_player_count():
    while True:
        try:
            player_count = int(input("プレイヤーの人数を入力してください: "))
            if player_count >= 3:
                return player_count+1
            else:
                print("3人以上のプレイヤーが必要です。")
        except ValueError:
            print("無効な入力です。整数を入力してください。")

def generate_janken_result(player_count):
    hands = ["グー", "チョキ", "パー"]
    player_names = [f"プレイヤー {i}" for i in range(1, player_count)]
    
    for _ in range(3):
        results = [random.randint(0, 2) for _ in range(player_count)]
        
        for i, player_name in enumerate(player_names):
            print(f"{player_name}の手: {hands[results[i]]}")
        
        winners = find_winners(results)
        if len(winners) == 1:
            print(f"{player_names[winners[0]]}が勝者です!\n")
        else:
            print("引き分けです!\n")

def find_winners(results):
    winners = []
    for i in range(len(results)):
        if results.count(results[i]) == len(results) // 2 + 1:
            winners.append(i)
    return winners

if __name__ == "__main__":
    player_count = get_player_count()
    generate_janken_result(player_count)