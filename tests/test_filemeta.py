import pytest
from Utils import filemeta

def maked_day_mock(_filename) -> str:
    return '2022年07月18日'


def test_maked_day(monkeypatch):
    _meta_data = filemeta.FileMeta()
    # ファイルが指定されているかテスト
    with pytest.raises(ValueError) as e:  # throwする例外の型を指定
        _meta_data.maked_day(None)
    assert str(e.value) == 'ファイル名が指定されていません'

    # ファイルの更新日が取得できているかテスト
    monkeypatch.setattr(
        _meta_data, 'maked_day', maked_day_mock
    )
    
    result = _meta_data.maked_day('file.csv')
    assert result == '2022年07月18日'
