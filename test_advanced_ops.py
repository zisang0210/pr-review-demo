from advanced_ops import AdvancedOps


def test_power():
    ops = AdvancedOps()
    assert ops.power(2, 3) == 8


def test_sqrt():
    ops = AdvancedOps()
    assert ops.sqrt(16) == 4
