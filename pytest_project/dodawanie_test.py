import pytest

@pytest.mark.parametrize("skladnik,suma",[(5,10),(2,4)])
def test_dodawania(skladnik,suma):
    assert skladnik + skladnik == suma, "Suma dwoch takich samych skladnikow powinna byc rowna " + str(skladnik+skladnik)