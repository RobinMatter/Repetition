from DataStore import DataStore


def test_DataStore():
    post_data = DataStore()
    #test self.add
    post_data.add("robin", 5)
    post_data.add("robin", 3)
    post_data.add("tim" , 2)
    assert post_data.get_value("robin") == (8, True)

    #test self.min
    post_data.min("robin",2)
    assert post_data.get_value("robin") == (6, True)
    post_data.min("robin", 7)
    assert post_data.get_value("robin") == (-1, True)

    # test self.sum
    post_data.sum("robin", 3, 7)
    assert post_data.get_value("robin") == (9, True)
    post_data.sum("björn", 3, 3)
    assert post_data.get_value("björn") == (6, True)

    # test self.dif
    post_data.dif("robin", 3, 7)
    assert post_data.get_value("robin") == (5, True)
    post_data.dif("julian", 3, 3)
    assert post_data.get_value("julian") == (0, True)

    # test self.quo
    post_data.quo("robin", 4, 2)
    assert post_data.get_value("robin") == (7, True)
    post_data.quo("paul", 6, 3)
    assert post_data.get_value("paul") == (2, True)
    #assert post_data.quo("paul", 8, 0) == None

    # test self.mul
    post_data.mul("robin", 4, 2)
    assert post_data.get_value("robin") == (15, True)
    post_data.mul("james", 6, 3)
    assert post_data.get_value("james") == (18, True)


