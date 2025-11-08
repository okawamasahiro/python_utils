import tkinter as tk

# === ウィンドウ生成 ===
root = tk.Tk()
root.title("Tkinter Sample")
root.geometry("300x200")

# === ラベルとボタン ===
label = tk.Label(root, text="Hello Tkinter!", font=("Arial", 14))
label.pack(pady=10)

def on_click():
    label.config(text="ボタンが押されました！")

button = tk.Button(root, text="クリック", command=on_click)
button.pack()

# === メインループ ===
root.mainloop()