import datetime
from pathlib import Path

class FileMeta:
    def __init__(self) -> None:
        pass

    def maked_day(self, _filename: str) -> str:
        if _filename is None:
            raise ValueError('ファイル名が指定されていません')
            
        """更新日の取得"""
        _p = Path(_filename)
        _update_time = datetime.datetime.fromtimestamp(_p.stat().st_mtime) # 更新日

        return _update_time
