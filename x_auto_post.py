import tweepy, datetime
import sys
sys.stdout = open("F:\\Python\\log\\x_auto_post_log.txt", "a", encoding="utf-8")
sys.stderr = sys.stdout

print("=== 実行開始:", datetime.datetime.now(), "===")

client = tweepy.Client(
    bearer_token="AAAAAAAAAAAAAAAAAAAAABL95AEAAAAAk3KIC54W%2F14b6THp2r%2FuXk16Hrg%3DB6hBQ9vGcJlfJLYB9YBozcQ1RWhQCCWJ9A3wECcelf3PTiSNqk",
    consumer_key="gPESZ6etvP9mpCSmTCW29c2t6",
    consumer_secret="Xbl1sthUeHZKnW9K9FZIFluCNGPqb8LtgdWLOjyDeVVjInvz44",
    access_token="1981013240126779392-3hoXrsjWqz7xxYAo4P536XedwgfykZ",
    access_token_secret="STTqA1ZvVfDVk6vVtGoe49fRZhBRYLXSxxOZysFnDeFKA"
)

msg = f"更新しました({datetime.datetime.now():%Y/%m/%d %H:%M:%S})\nhttps://note.com/glad_iguana8939/n/n46a6435d6e40"
client.create_tweet(text=msg)
