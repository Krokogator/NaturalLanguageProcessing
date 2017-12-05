import re
import urllib.request
import urllib.parse

szlifierki = []
for i in range(1):
    rok = 2008 + i;
    rok2 = 2008 + i + 1
    adres = "(" + str(rok) + "/" + str(rok2) + ")"
    url = "https://pl.wikipedia.org/wiki/Ekstraklasa_w_" + urllib.parse.quote("piłce_nożnej_") + "(" + str(
        rok) + "/" + str(rok2) + ")"
    print(url)
    response = urllib.request.urlopen(url)
    page = response.read().decode("utf-8")
    table = re.search(r'1\.<\/td>([\s\S]*?)</table>', page)
    wynik = re.findall(r'">([A-Za-z0-9łąęćśżźóńŁŃĄĆŚŻŹÓĘ ]*?)<\/a>((.|\n)*?)<td>30<\/td>', str(table))
    ##szlifierki += re.findall(r'<table class="wikitable" style="text-align: center;">([A-Za-z0-9łąęćśżźóńŁŃĄĆŚŻŹÓĘ\>\< ]+)</table>', page)
    ##print(re.findall(r'<table class="wikitable" style="text-align: center;">([\s\S]*)</table>', page))
    print(table.group(1))