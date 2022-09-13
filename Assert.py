""" assert

    Pythonで本当に役立つ機能「アサーション」の使い方を解説！『Pythonトリック』から
    https://codezine.jp/article/detail/12179

    注意1: データチェックにアサーションを使用しない
           アサーションが無効化された時に、データチェックが無効化される。
             --> 通常のif文を使う。
    注意2: 決して失敗しないアサーション
           assert (条件, '文字列')
           これはタプルを評価しているので「常に正」
           AssertionErrorは起こらない

    デバッグの為にある機能だと思うこと
"""
def apply_discount(product, discount):
    price = int(product['price'] * (1.0 - discount))
    assert 0 <= price <= product['price'], 'ディスカウントエラー'
    
    return price

shoes = {'name': 'Fancy Shoes', 'price': 14900}
apply_discount(shoes, 1.25)