from app import add

def test_add(): # test_add() function
    assert add(2, 3) == 5
    assert add(-1, 1) == 0