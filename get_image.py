import sys
import os
import io
import pickle
import urllib.request
from PIL import Image

# pickleファイルを格納しているディレクトリを指定（10万URL分くらい?）
path_pkl = sys.argv[1] + '/'
# 画像を保存するディレクトリを指定
path_img = sys.argv[2] + '/'

pkl_files = os.listdir(path_pkl)
pkl_files.sort()

url_blacklist = ['https://assets.cpcdn.com/assets/blank_logo_kondate_spweb.png?6f9d23b17b11c778db08604964160405d12a573e53eccf4bc888897a2d931956']
n = 0

url_error = []

# 途中から画像のスクレイピングを再開する場合は、再開を始めるのURLを指定して、次のFlagをFalseにする # 頭悪い…
# flag_start = True
# url_start = "https://img.cpcdn.com/recipes/257592/464x260/a3edc04c75ef451b465cc97cf95f7d88.jpg?u=66761&p=1214213085"


for pkl_file in pkl_files:
    print(pkl_file)
    with open(path_pkl + pkl_file, 'rb') as f:
        hoge = pickle.load(f)
    for i in range(len(hoge)):
        url = hoge[i]['image']
        '''
        if url==url_start:
            flag_start = True
            n = 0
            print("\n\nSTART\n")
        if not flag_start:
            n += 1
            print(n, end=" ")
            continue
        '''
        if url in url_blacklist:
            print("[I] No Image")
        else:
            try:
                f = io.BytesIO(urllib.request.urlopen(url).read())
            except urllib.error.HTTPError as e:
                print("[W] HTTP Error!")
                url_error.append(url)
                continue
            except:
                print("[W] Unknown Error!")
                url_error.append(url)
            try:
                img = Image.open(f)
                img.save(path_img + pkl_file[:20] + '-' + '{0:07d}'.format(i) + '.png')
                print('found: ', hoge[i]['name'], end="")
                n += 1
                print(",  n:", n)
            except:
                print("[W] Unknown Error!")
                url_error.append(url)

print("done")
print("url_error list")
print(url_error)
if len(url_error) > 0:
    print("################################################################")
    print("# Please delete these empty image file!")
    print("################################################################\n")
