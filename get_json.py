import urllib.request                                                                                
import bs4
import json
import pickle
import sys
 
# 検索対象url番号
start, end = int(sys.argv[1]), int(sys.argv[2])
 
# 取得する数
nb_menu = 1000000
 
# 取得した数
num = 0
 
# 検索を再開するurl番号
tmp = start
 
# 終わり方
menu_keys = ['@context', '@type', 'name',
             'author', 'image', 'datePublished',
             'description', 'recipeYield', 'recipeIngredient',
             'recipeInstructions', 'cookTime']
 
#menu_template = dict([(key, 'None') for key in menu_keys]) # 複製には deepcopy を使う
 
menu = []
 
while(num < nb_menu and tmp < end): # nb_menu個見つけるか、startがendになるまで
 
    for i in range(tmp, end):
        tmp = i+1 # 次に検索し始めるurl番号を記録
        url = 'https://cookpad.com/recipe/' + str(i)
        try:
            _menu = bs4.BeautifulSoup(urllib.request.urlopen(url).read(), "lxml")
            print("found:", str(start) + '-' + str(end), num, url)
            _menu = json.loads(_menu.find("script", {"type": "application/ld+json"}).get_text())
            menu.append(_menu)
            num += 1
            break
        except urllib.error.HTTPError as e:
            continue
 
 
with open('data_json/menu-' + str(start) + '-' + str(end) + '.pkl', 'wb') as f:
    pickle.dump(menu, f)

