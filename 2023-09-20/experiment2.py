import requests

def main(url):
    r = requests.get(url)
    print(type(r))
    print(r.status_code)
    print(r.headers)
    print(r.text)

if __name__ == "__main__":
    main("https://baidu.com")
