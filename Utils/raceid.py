from dataclasses import dataclass

@dataclass
class RaceId:
    
    year: str = ''
    month: str = ''
    day: str = ''
    venue: str = ''
    kaiji: str = ''
    nichiji: str = ''
    race_no: str = ''

    @property
    def race_id(self) -> str:
        """レースID[年・月・日・場所・回次・日次・レース番号]を作る

        Returns:
            str: レースID
        """
        #_race_id = f'{self.year:04s}{self.month:02s}{self.day:02s}{self.venue:02s}{self.kaiji:02s}{self.nichiji:02s}{self.race_no:02s}'
        _race_id = f'{self.year}{self.month}{self.day}{self.venue}{self.kaiji}{self.nichiji}{self.race_no}'
        
        return _race_id

    @race_id.setter
    def race_id(self, _race_id: str) -> None:
        """レースIDを年・月・日・場所・回次・日次に分解する"""
        if len(_race_id) != 16:
            raise Exception('invalid race_id error')
        print(_race_id)
        self.year    = _race_id[:4]
        self.month   = _race_id[4:6]
        self.day     = _race_id[6:8]
        self.venue   = _race_id[8:10]
        self.kaiji   = _race_id[10:12]
        self.nichiji = _race_id[12:14]
        self.race_no = _race_id[14:]
