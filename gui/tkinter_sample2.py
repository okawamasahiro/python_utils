import tkinter as tk
from tkinter import filedialog, scrolledtext

def open_file():
    path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not path:
        return
    with open(path, "r", encoding="utf-8") as f:
        text_area.delete("1.0", tk.END)
        text_area.insert(tk.END, f.read())

def save_file():
    path = filedialog.asksaveasfilename(defaultextension=".txt")
    if not path:
        return
    with open(path, "w", encoding="utf-8") as f:
        f.write(text_area.get("1.0", tk.END))

root = tk.Tk()
root.title("テキストエディタ風サンプル")
root.geometry("600x400")

# === メニュー ===
menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="開く", command=open_file)
filemenu.add_command(label="保存", command=save_file)
filemenu.add_separator()
filemenu.add_command(label="終了", command=root.quit)
menubar.add_cascade(label="ファイル", menu=filemenu)
root.config(menu=menubar)

# === テキストエリア ===
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD)
text_area.pack(expand=True, fill="both")

root.mainloop()