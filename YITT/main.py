from src.Search import Search


def main():
    search = Search()
    search.searchTitle("Central Cee", 5)
    print(*search.list_all_res())
    search.play_video(2)
    # search.play_audio(0)

if __name__ == "__main__":
    main()

