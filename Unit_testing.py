def minimum_index(seq):
    if len(seq) == 0:
        raise ValueError("Cannot get the minimum value index from an empty sequence")
    min_idx = 0
    for i in range(1, len(seq)):
        if seq[i] < seq[min_idx]:
            min_idx = i
    return min_idx
 
class TestDataEmptyArray:
    def get_array():
        return []
         
class TestDataUniqueValues:
    def get_array(): #returns an array of size at least 2 with all unique elements
        arr = [2, 3, 4, 5, 1]
        return (arr)
    def get_expected_result(): #returns the expected minimum value index for this array
        expected_result = 4
        return (expected_result)
    
class TestDataExactlyTwoDifferentMinimums:
    def get_array(): #returns an array where the minimum value occurs at exactly 2 indices
        arr = [4, 6, 3, 7, 3]
        return(arr)
    def get_expected_result(): #returns the expected index
        expected_result = 2
        return (expected_result)
 

def TestWithEmptyArray():
    try:
        seq = TestDataEmptyArray.get_array()
        result = minimum_index(seq)
    except ValueError as e:
        pass
    else:
        assert False


def TestWithUniqueValues():
    seq = TestDataUniqueValues.get_array()
    assert len(seq) >= 2

    assert len(list(set(seq))) == len(seq)

    expected_result = TestDataUniqueValues.get_expected_result()
    result = minimum_index(seq)
    assert result == expected_result


def TestiWithExactyTwoDifferentMinimums():
    seq = TestDataExactlyTwoDifferentMinimums.get_array()
    assert len(seq) >= 2
    tmp = sorted(seq)
    assert tmp[0] == tmp[1] and (len(tmp) == 2 or tmp[1] < tmp[2])

    expected_result = TestDataExactlyTwoDifferentMinimums.get_expected_result()
    result = minimum_index(seq)
    assert result == expected_result

TestWithEmptyArray()
TestWithUniqueValues()
TestiWithExactyTwoDifferentMinimums()
print("OK")
