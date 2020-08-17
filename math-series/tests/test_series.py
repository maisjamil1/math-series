from math_series.series import sum_series,fibonacci,lucas

def test_one():
    expected = 13
    actual = sum_series(7)
    assert actual == expected

def test_two():
    expected = 29
    actual = sum_series(7,2,1)
    assert actual == expected



def test_three():
    expected = 0
    actual = sum_series(0)
    assert actual == expected

def test_four():
    expected = 1
    actual = sum_series(1)
    assert actual == expected

def test_five():
    expected = 1
    actual = sum_series(2)
    assert actual == expected


def test_six():
    expected = 18
    actual = sum_series(7,3,4)
    assert actual == expected

def test_seven():
    expected = 8
    actual = sum_series(5,2,3)
    assert actual == expected