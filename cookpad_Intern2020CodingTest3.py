"""
ソース：https://gist.github.com/sankichi92/4e77203d7cd022f03bb1b95138c8b3f2
dragon、griffin、medusa、troll、vampireの5匹のモンスターがいます。
APIサーバーにそのうちの2匹を指定すると、対戦をさせた結果を得ることができます。
モンスターの強さは決まっていて、同じモンスター同士であれば、対戦の結果は常に変わりません。このAPIサーバーをつかって、5匹のモンスターを強い順に並べてください。
API アクセス例
$ curl https://ob6la3c120.execute-api.ap-northeast-1.amazonaws.com/Prod/battle/dragon+griffin
{"winner":"dragon","loser":"grifin"}
実行例
$ ruby solve.rb
dragon, griffin, medusa, troll, vampire
"""
import requests

monsters = ['dragon', 'griffin', 'medusa', 'troll', 'vampire']
# monsters = ['troll', 'dragon', 'medusa', 'griffin', 'vampire'] #ソート結果　これで実行すると入れ替えが起きない

def compare_strength(monster1, monster2):
    url = 'https://ob6la3c120.execute-api.ap-northeast-1.amazonaws.com/Prod/battle/' + monster1 + '+' + monster2
    response = requests.get(url)
    txt = response.text
    #文字列の整形
    unnecessary_strings = ['{', '}','"']
    for s in unnecessary_strings:
        txt = txt.replace(s,'')
    # 勝敗結果を配列resultに格納
    result = [None] * 2
    for i, s in enumerate(txt.split(',')):
        result[i] = s[s.index(':')+1 :]
    return result # => ['勝者', '敗者']

# バブルソートで並べる
for _ in range(len(monsters) - 1):
    for i in range(len(monsters) - 1):
        print('-----------------------------------------')
        print(f'{monsters}')
        compare_result = compare_strength(monster1=monsters[i], monster2=monsters[i+1])
        print(f'比較結果:　{compare_result}')
        # monster2がmonster1より強いとき
        if compare_result.index(monsters[i]) > compare_result.index(monsters[i+1]):
            monsters[i], monsters[i+1] = monsters[i+1], monsters[i]
            print(f'{monsters}：入れ替えた！')
print(monsters)




