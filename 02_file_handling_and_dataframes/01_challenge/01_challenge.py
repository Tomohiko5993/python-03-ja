# ここにコードを書いてください
import os
from pathlib import Path

# ディレクトリのパスを設定
data_dir = Path("/Users/tomohiko.ozaki/Documents/python/python-03-ja/02_file_handling_and_dataframes/01_challenge/data/text_files")
library_dir = data_dir.parent / "library"

# 1. ファイルの操作
def import_books_to_dict_and_save():
    books_dict = {}
    # ディレクトリ内のファイルを反復処理
    for file_path in data_dir.iterdir():
        if file_path.is_file() and not file_path.name.startswith("Chapter_"):
            # ファイルを辞書にインポート
            with open(file_path, 'r', encoding='utf-8') as file:
                books_dict[file_path.name] = file.read()

    # 辞書の内容を1つのテキストファイルに保存
    with open(data_dir / "combined_books.txt", 'w', encoding='utf-8') as combined_file:
        for title, content in books_dict.items():
            combined_file.write(f"Title: {title}\n{content}\n\n")

# 2. ディレクトリの設定
def create_library_directory_and_move_chapters():
    # 新しいディレクトリを作成
    library_dir.mkdir(exist_ok=True)

    # Chapter_x.txt ファイルを library ディレクトリに移動
    for file_path in data_dir.iterdir():
        if file_path.is_file() and file_path.name.startswith("Chapter_"):
            destination = library_dir / file_path.name
            file_path.rename(destination)

    # pathlib を使用して library ディレクトリに移動し、ファイルとサイズを一覧表示
    for file_path in library_dir.iterdir():
        if file_path.is_file():
            print(f"{file_path.name}: {file_path.stat().st_size} bytes")

# 実行
if __name__ == "__main__":
    import_books_to_dict_and_save()
    create_library_directory_and_move_chapters()