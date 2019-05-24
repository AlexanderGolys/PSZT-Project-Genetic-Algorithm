import unittest
import sys
import os
sys.path.insert(0, sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)).replace('test', 'src')))
print(sys.path)
import adaptationFunction
import readFile


class Test(unittest.TestCase):
    def test1(self):
        matrix = readFile.getArray(os.path.dirname(os.path.abspath(__file__)) + '/arrays/data.txt')
        result = adaptationFunction.J(matrix, [3, 3, 3], [4, 4, 4], [0, 0, 0], 3)

        self.assertEqual(result, 0.1975, 'should fill up array correctly')

    def test2(self):
        matrix = readFile.getArray(os.path.dirname(os.path.abspath(__file__)) + '/arrays/data2.txt')
        result = adaptationFunction.J(matrix, [3], [4], [0], 3)

        self.assertEqual(result, 0.1852, 'should fill up array correctly')

    def test3(self):
        matrix = readFile.getArray(os.path.dirname(os.path.abspath(__file__)) + '/arrays/data3.txt')
        result = adaptationFunction.J(matrix, [3], [4], [0], 3)

        self.assertEqual(result, 0.1481, 'should fill up array correctly')

    def test4(self):
        matrix = readFile.getArray(os.path.dirname(os.path.abspath(__file__)) + '/arrays/data4.txt')
        result = adaptationFunction.J(matrix, [3], [4], [0], 3)

        self.assertEqual(result, 0.0864, 'should fill up array correctly')

    def test5(self):
        matrix = readFile.getArray(os.path.dirname(os.path.abspath(__file__)) + '/arrays/data5.txt')
        result = adaptationFunction.J(matrix, [3], [4], [0], 3)

        self.assertEqual(result, 0.0988, 'should fill up array correctly')

    def test6(self):
        matrix = readFile.getArray(os.path.dirname(os.path.abspath(__file__)) + '/arrays/data6.txt')
        result = adaptationFunction.J(matrix, [3], [4], [0], 3)

        self.assertEqual(result, 0.1481, 'should fill up array correctly')

    def test7(self):
        matrix = readFile.getArray(os.path.dirname(os.path.abspath(__file__)) + '/arrays/data7.txt')
        result = adaptationFunction.J(matrix, [0], [10], [0], 7)

        self.assertEqual(result, 0.5, 'should fill up array correctly')

    def test8(self):
        matrix = readFile.getArray(os.path.dirname(os.path.abspath(__file__)) + '/arrays/data7.txt')
        result = adaptationFunction.J(matrix, [0], [10], [0], 100)

        self.assertEqual(result, 0.7, 'should fill up array correctly')

    def test9(self):
        matrix = readFile.getArray(os.path.dirname(os.path.abspath(__file__)) + '/arrays/data9.txt')
        result = adaptationFunction.J(matrix, [2, 6, 2], [7, 6, 7], [0, 0, 0], 3)

        self.assertEqual(result, 0.3457, 'should fill up array correctly')

    def test10(self):
        matrix = readFile.getArray(os.path.dirname(os.path.abspath(__file__)) + '/arrays/data10.txt')
        result = adaptationFunction.Jx(matrix, [2, 6, 2], [7, 6, 7], [0, 0, 0], 3)

        self.assertEqual(result, 0.3086, 'should fill up array correctly')


if __name__ == '__main__':
    unittest.main()
