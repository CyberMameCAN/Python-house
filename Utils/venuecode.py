class VenueCode:
    def __init__(self) -> None:
        self.venue_map = {
            '札幌': '01',
            '函館': '02',
            '福島': '03',
            '新潟': '04',
            '東京': '05',
            '中山': '06',
            '中京': '07',
            '京都': '08',
            '阪神': '09',
            '小倉': '10',
        }

        self.code: str = ''

    def venue_name(self, _venue_code: str) -> str:
        """開催場所コードを開催場所名に変換する"""
        keys = [k for k, v in self.venue_map.items() if v == _venue_code]
        if len(keys) <= 0:
            return None
        return keys[0]  # 複数マッチしたら初めにヒットしたものを・・・というか１つしか無いはず

    def venue_code(self, _venue_name: str) -> str:
        """開催場所名を開催場所コードに変換する"""
        return self.venue_map.get(_venue_name)  # get()を使うとキー無しでもエラーにならない(Noneが返る)

