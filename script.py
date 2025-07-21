# リスト
fruits = ["りんご", "バナナ", "いちご"]
print(fruits)
print(fruits[0])  # りんご

fruits[2] = "めろん"
print(fruits)

fruits.append("ぶどう")
print(fruits)

# 辞書
my_profile = {"name": "りんちゃん", "age": 17, "language": "Python"}

print(my_profile)

my_profile["age"] = 18
print(my_profile)

my_profile["skill"] = "プログラミング"
print(my_profile)

# 課題
# 好きなゲーム
favorite_games = ["ゼルダの伝説", "ゴーストオブツシマ", "ゼンレスゾーンゼロ"]
print(favorite_games[0])

# PCのスペック
my_pc = {"CPU": "9800x3D", "memory": "64GB", "GPU": "RTX 5070Ti"}
print(my_pc["CPU"])
