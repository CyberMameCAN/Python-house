from Utils import raceid

def test_race_id():
    race = raceid.RaceId()

    org_id = '2021061302010102'
    race.race_id = org_id
    
    assert len(race.race_id) == 16

    assert race.year == '2021'  # Trueになる条件
    assert race.month == '06'
    assert race.day   == '13'
    assert race.venue == '02'
    assert race.kaiji == '01'
    assert race.nichiji == '01'
    assert race.race_no == '02'
