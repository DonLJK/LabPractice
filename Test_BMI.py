import BMIcal as bmical


def test_bmi_normal_weight():
    result = bmical.calculate(1.76, 60)
    expected = 0
    assert(result == expected)

def test_bmi_overweight():
    result = bmical.calculate(1.76, 120)
    expected = 1
    assert(result == expected)

def test_bmi_underweight():
    result = bmical.calculate(1.76, 10)
    expected = -1
    assert(result == expected)