"""
UnitTestの雛形

テスト方法(-vは少し詳細な結果)
    poetry run python -m unittest -v
"""
import unittest
from unittest import TestCase, mock

from raceid import RaceId


class TestRaceId(TestCase):
    """RaceIdクラスのテストクラス"""
    
    @classmethod
    def setUpClass(cls):
        print('[全体-前-処理]')
        cls.race = RaceId()
 
    @classmethod
    def tearDownClass(cls):
        print('[全体-後-処理]')
 
    def setUp(self):
        print('[テスト-前-処理]')
        self.race.race_id = '2021061302010107'
 
    def tearDown(self):
        print('[テスト-後-処理]')

    def test_race_id(self):
        print("test_race_id開始")
        self.assertEqual(self.race.year, '2021')
        self.assertNotEqual(self.race.year, 2021)
        self.assertEqual(self.race.month, '06')
        self.assertEqual(self.race.day, '13')
        self.assertEqual(self.race.venue, '02')
        self.assertEqual(self.race.kaiji, '01')
        self.assertEqual(self.race.nichiji, '01')
        self.assertEqual(self.race.race_no, '07')
        print("test_race_id終了")

    def test_invalid_length(self):
        """16桁, 18桁以外では例外(ValueError)が発生すること"""
        with self.assertRaises(ValueError):
            self.race.race_id = '20210613020101077'

    @unittest.skip("メソッド修正中のためスキップ")
    def test_skip(self):
        pass

# def test_race_id():
#     race = raceid.RaceId()

#     org_id = '2021061302010102'
#     race.race_id = org_id
    
#     assert len(race.race_id) == 16

#     assert race.year == '2021'  # Trueになる条件
#     assert race.month == '06'
#     assert race.day   == '13'
#     assert race.venue == '02'
#     assert race.kaiji == '01'
#     assert race.nichiji == '01'
#     assert race.race_no == '02'
