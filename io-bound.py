from urllib.request import Request, urlopen
from urllib.parse import unquote
import concurrent.futures

links = open('res.txt', encoding='utf8').read().split('\n')

with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    resp = [executor.submit(Request,url,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 9.0; Win65; x64; rv:97.0) Gecko/20105107 Firefox/92.0'})
                for url in links]
    for future in concurrent.futures.as_completed(resp):
        try:
            data = future.result()
            with urlopen(data,timeout=5) as resp:
                    code = resp.code
                    print(code)
        except Exception as e:
            print(data.full_url, e)