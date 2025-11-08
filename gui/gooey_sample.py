from gooey import Gooey, GooeyParser
import time

@Gooey(progress_regex=r"^progress: (\d+)%$",
       progress_expr="progress: %d%%",
       program_name="Gooey プログレスバーサンプル")
def main():
    parser = GooeyParser(description="進捗バー表示デモ")
    parser.add_argument("--steps", type=int, default=10, help="ステップ数")
    args = parser.parse_args()

    for i in range(args.steps):
        time.sleep(0.3)
        print(f"progress: {int((i+1)/args.steps*100)}%")

if __name__ == "__main__":
    main()