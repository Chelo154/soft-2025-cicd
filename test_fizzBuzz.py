from fizzBuzz import Solution



def test_fizzBuzz():
    expected = ["1","2","Fizz","4","Buzz"]

    result = Solution().fizzBuzz(5)

    assert expected == result
