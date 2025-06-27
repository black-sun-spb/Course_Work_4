from src.models.vacancy import Vacancy

def test_comparison():
    v1 = Vacancy("Dev", "url1", {"from": 100000}, "desc")
    v2 = Vacancy("Dev", "url2", {"from": 150000}, "desc")
    assert v1 < v2
