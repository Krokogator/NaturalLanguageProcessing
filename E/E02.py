import re
import urllib.request

tabela = ""
wyniki = dict()
year = 2008
for i in range(10):
    print("processing " + str(year) + "/" + str(year + 1))
    response = urllib.request.urlopen(
        "https://pl.wikipedia.org/wiki/Ekstraklasa_w_pi%C5%82ce_no%C5%BCnej_(" + str(year) + "/" + str(year + 1) + ")")
    page_source = response.read().decode("utf-8")
    tabela_raw = re.search(r'<td>1\.<\/td>([\s\S]*?)</table>', page_source)
    druzyny = re.findall(r'title="(.*?).*">(\1)<\/a>[\s\S]*?<b>(\d{1,2})<\/b>', tabela_raw.group(1))
    year = year + 1
    for idx, druzyna in enumerate(druzyny):
        if druzyna[1] in wyniki:
            wyniki[druzyna[1]] = wyniki[druzyna[1]] + int(druzyna[2])
        else:
            wyniki[druzyna[1]] = int(druzyna[2])
print("\n       WYNIKI \n")
for k, v in sorted(wyniki.items(), key=lambda x: x[1], reverse=True):
    print(k + " | " + str(v))