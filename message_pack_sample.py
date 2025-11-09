import msgpack

data = {
    "name": "Okawa",
    "hp": 120,
    "pos": [1, 2, 3]
}

# --- シリアライズして保存 ---
with open("player.dat", "wb") as f:  # b = バイナリモード
    packed = msgpack.packb(data, use_bin_type=True)
    f.write(packed)

print("✅ 保存完了: player.dat")

# --- 保存したデータを読み込んで復元 ---
with open("player.dat", "rb") as f:
    loaded = msgpack.unpackb(f.read(), raw=False)

print("📦 復元結果:", loaded)