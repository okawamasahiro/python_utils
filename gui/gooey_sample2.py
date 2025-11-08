from gooey import Gooey, GooeyParser

@Gooey(program_name="Gooey 基本サンプル")
def main():
    parser = GooeyParser(description="挨拶スクリプト")
    parser.add_argument("name", help="あなたの名前を入力してください")
    parser.add_argument("--repeat", type=int, default=1, help="繰り返し回数")
    args = parser.parse_args()

    for i in range(args.repeat):
        print(f"こんにちは、{args.name}さん！（{i+1}回目）")

if __name__ == "__main__":
    main()