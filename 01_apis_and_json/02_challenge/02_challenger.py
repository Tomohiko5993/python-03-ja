import requests
import json

BASE_URL = "https://jsonplaceholder.typicode.com/posts"

def list_posts():
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        posts = response.json()
        for post in posts[:5]:  # 最初の5件のみ表示
            print(f"ID: {post['id']}, Title: {post['title']}")
    else:
        print(f"エラー: 投稿の取得に失敗しました。ステータスコード: {response.status_code}")

def create_post():
    title = input("タイトルを入力してください: ")
    body = input("本文を入力してください: ")
    data = {
        "title": title,
        "body": body,
        "userId": 1  # ダミーのユーザーID
    }
    response = requests.post(BASE_URL, json=data)
    if response.status_code == 201:
        print("投稿が正常に作成されました。")
        print(response.json())
    else:
        print(f"エラー: 投稿の作成に失敗しました。ステータスコード: {response.status_code}")

def update_post():
    post_id = input("更新する投稿のIDを入力してください: ")
    title = input("新しいタイトルを入力してください: ")
    body = input("新しい本文を入力してください: ")
    data = {
        "title": title,
        "body": body
    }
    response = requests.put(f"{BASE_URL}/{post_id}", json=data)
    if response.status_code == 200:
        print("投稿が正常に更新されました。")
        print(response.json())
    else:
        print(f"エラー: 投稿の更新に失敗しました。ステータスコード: {response.status_code}")

def delete_post():
    post_id = input("削除する投稿のIDを入力してください: ")
    response = requests.delete(f"{BASE_URL}/{post_id}")
    if response.status_code == 200:
        print("投稿が正常に削除されました。")
    else:
        print(f"エラー: 投稿の削除に失敗しました。ステータスコード: {response.status_code}")

def main():
    while True:
        print("\nブログ投稿管理ツール")
        print("1. 投稿一覧の表示")
        print("2. 新規投稿の作成")
        print("3. 投稿の更新")
        print("4. 投稿の削除")
        print("5. 終了")
        
        choice = input("操作を選択してください (1-5): ")
        
        if choice == "1":
            list_posts()
        elif choice == "2":
            create_post()
        elif choice == "3":
            update_post()
        elif choice == "4":
            delete_post()
        elif choice == "5":
            print("プログラムを終了します。")
            break
        else:
            print("無効な選択です。1から5の数字を入力してください。")

if __name__ == "__main__":
    main()