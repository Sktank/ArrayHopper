
from ArrayHopper import findMinHops

# Unit Tests for ArrayHopper

def UnitTests():
    numTests = 6
    count = 0
    correct1 = [0,1,2,3,4,5]
    correct2 = [0, 1, 4, 7, 8, 14, 15]
    correct3 = [0, 1, 2, 10]
    correct4 = -4
    correct5 = -3
    correct6 = -2

    print "Testing ArrayHopper on " + str(numTests) + " arrays"

    count += arrayTest("array", correct1, 1)
    count += arrayTest("array2", correct2, 2)
    count += arrayTest("array3", correct3, 3)
    count += arrayTest("array4", correct4, 4)
    count += arrayTest("array5", correct5, 5)
    count += arrayTest("idontexist", correct6, 6)

    print"==================================="
    print
    print"Tests passed: " + str(count) + "/" + str(numTests)
    print


def arrayTest(array_name, correct_output, number):
    print"==================================="
    print"Test " + str(number)
    output, value = findMinHops(array_name)
    correct = str(correct_output)
    print "correct output = " + correct
    print "AHopper output = " + str(output)
    if str(output) == correct or str(value) == correct:
        print "Test Passed"
        return 1
    else:
        print "Test Failed"
        return 0


if __name__ == "__main__":
    UnitTests()