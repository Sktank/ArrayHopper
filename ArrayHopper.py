import sys
__author__ = 'spencertank'


#Function that finds the minimum number of hops to traverse the given array
def findMinHops(input_file):
    try:
        f = open(input_file, 'r')
    except IOError:
        return "The input file specified could not be found!", -2

    s = f.read()
    input = s.split('\n')

    try:
        array = map(int, input)
    except ValueError:
        return "The specified input is not formatted correctly!", -3

    print "Input Array = " + str(array)
    indexes = []
    next_hop = 0
    next_stop = array[0]
    length = len(array)
    current_index = 0
    landing = 0
    indexes.append(0)

    while True:
        for i in range(current_index, next_stop + 1):
            landing = array[i] + i
            if landing > next_hop:
                next_hop = landing
                next_index = i
        if next_index == current_index:
            return "failure", -4
        indexes.append(next_index)
        if next_hop >= length:
            break
        next_stop = next_index + array[next_index]
        current_index = next_index
    return indexes, 0

if __name__ == "__main__":
    try:
        input_file = str(sys.argv[1])
    except IndexError:
           print "Please specify an input file!"
           quit()

    output, value = findMinHops(input_file)
    print output











