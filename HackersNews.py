import time
import requests


def search_top():
    response = requests.get(
        "https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty"
    )

    dic = response.json()  # パース

    numbers = []
    for number in range(0, 50):
        numbers.append(dic[number])

    return numbers


def get_info(number):

    for r in number:
        article_number = r
        response = requests.get(
            f"https://hacker-news.firebaseio.com/v0/item/{article_number}.json?print=pretty"
        )

        dic = response.json()  # パース
        # print(dic)

        title = dic["title"]

        if "url" in dic:
            url = dic["url"]
            print(f"'title': '{title}', 'link': '{url}'")

        else:
            print(f"'title': {title}")

        # 備忘このやり方も調べたい。
        # try:
        #     dic["url"]
        # except KeyError:
        #     print("'title': {title}")

        # url = dic["url"]

        time.sleep(1)  # 1秒停止


def main():

    numbers = search_top()
    get_info(numbers)


if __name__ == "__main__":
    main()
