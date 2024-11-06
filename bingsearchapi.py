import requests
from bs4 import BeautifulSoup
from flask import Flask, request, jsonify

app = Flask(__name__)

# 请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Mobile Safari/537.36 EdgA/123.0.0.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Referer": "https://www.bing.com/",
}


# 提取搜索引擎主内容、智能问答
def extract_search_results(query):
    url = f"https://www.bing.com/search?q={query}"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        result_list = []
        interlocution = None  # 初始化智能问答

        # 提取搜索结果主内容
        for item in soup.find_all('li', class_='b_algo'):
            try:
                title = item.find('h2').text
                description_tag = item.find('p')
                description = description_tag.text if description_tag else "No description available"
                link = item.find('a')['href']
                result_list.append({'title': title, 'description': description, 'link': link})
            except Exception as e:
                print(f"An error occurred while extracting search results: {str(e)}")

        # 提取智能问答
        interlocution_div = soup.find('div', class_='qna-mf')
        if interlocution_div:
            try:
                interlocution = interlocution_div.get_text()
            except Exception as e:
                print(f"An error occurred while extracting interlocution: {str(e)}")

        return result_list, interlocution
    else:
        print(f"Error: Request failed with status code {response.status_code}")
        return [], None


# 主处理函数
def process_query(query):
    search_results, interlocution = extract_search_results(query)

    result = {
        "Search Results": search_results,
        "Interlocution": interlocution if interlocution else None,
    }

    return result


# API路由
@app.route('/search', methods=['POST'])
def search():
    query = request.json.get('query')
    if query:
        try:
            result = process_query(query)
            return jsonify({"data": result})
        except Exception as e:
            print(f"An error occurred while processing the query: {str(e)}")
            return jsonify({"error": "An error occurred while processing the query."})
    else:
        return jsonify({"error": "Invalid request format."})


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=10000)
