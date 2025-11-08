import gradio as gr

def calc(a, b, op):
    if op == "加算":
        result = a + b
    elif op == "減算":
        result = a - b
    elif op == "乗算":
        result = a * b
    else:
        result = a / b if b != 0 else "∞"
    return f"結果: {result}"

demo = gr.Interface(
    fn=calc,
    inputs=[
        gr.Number(label="数値A"),
        gr.Number(label="数値B"),
        gr.Radio(["加算", "減算", "乗算", "除算"], label="演算種別")
    ],
    outputs="text",
    title="簡単電卓"
)
demo.launch()