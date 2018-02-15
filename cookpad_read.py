import json                                                                                          
import pickle
 
with open('menu-0-100.pkl', 'rb') as f:
    hoge = pickle.load(f)
 
for i in range(3):#(len(hoge)):
    print()
    print(i)
    print('name: ', hoge[i]['name'])
    print('datePublished', hoge[i]['datePublished'])
    print('image', hoge[i]['image'])
    print('recipeIngredient', hoge[i]['recipeIngredient']) # 半角空白文字で区切られてる
    print('recipeInstructions', hoge[i]['recipeInstructions']) # リストになってる
    #print(hoge[i])

