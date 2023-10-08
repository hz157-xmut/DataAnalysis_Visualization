import urllib.request

def main(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0"}
    r = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(url)
    response2 = urllib.request.urlopen(r)
    html = response.read()
    f = open("./AL9-7.txt", 'wb')
    f.write(html)
    f.close()

if __name__ == "__main__":
    main("https://baidu.com")