import pytest
def test_m1():
    a = 3
    b = 8
   # assert a == b, "test is failed if a is not eq to b"
    assert a+5 == b, "Test is pass"
def test_m2():
    num = 4
    assert num * num == 16
def test_m3():
    name = "ANITHA"
    assert name.lower()== "anitha"
def test_m4():
    assert True
def test_m5():
    assert False
def test_m6():
    assert 4 == 4
def test_login():
    assert "admin" == "admin"
