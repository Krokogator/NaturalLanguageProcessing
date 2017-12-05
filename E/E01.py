import re
import urllib.request

szlifierki= []
for i in range(40):
    response = urllib.request.urlopen("https://www.ceneo.pl/Szlifierki_i_polerki/Rodzaj:Szlifierki_katowe;szukaj-szlifierka+katowa;0020-30-0-0-%d.htm" % i)
    page_source = response.read().decode("utf-8")
    szlifierki += re.findall(r'data-source-tag="">([A-Za-z0-9 ]+)</a>', page_source)
for szlifierka in szlifierki:
    print(szlifierka)