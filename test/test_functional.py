import unittest
from test.TestUtils import TestUtils
from numpy_ex import *
from pandas_ex import *
class FuctionalTest(unittest.TestCase):
    def test_array_type(self):
        b = np.array([])
        t=check_type()
        test_obj = TestUtils()   
        if type(b)==t:
                test_obj.yakshaAssert("TestArrayType", True, "functional")
                print("TestArrayType = Passed")            
        else:
            test_obj.yakshaAssert("TestArrayType", False, "functional")
            print("TestArrayType = Failed")
    def test_square(self):
        sq=find_square()
        test_obj = TestUtils()
        if sq[0][0]==1 and sq[0][1]==4 and sq[1][0]==9 and sq[1][1]==16:
                test_obj.yakshaAssert("TestSquare", True, "functional")
                print("TestSquare = Passed")            
        else:
            test_obj.yakshaAssert("TestSquare", False, "functional")
            print("TestSquare = Failed")

    def test_sum(self):
        sm=find_sum()
        test_obj = TestUtils()
        if sm==10:
            test_obj.yakshaAssert("TestSum", True, "functional")
            print("TestSum = Passed")
        else:
            test_obj.yakshaAssert("TestSum", False, "functional")
            print("TestSum = Failed")

    def test_dimension(self):
        dim=find_dimension()
        test_obj = TestUtils()
        if dim==2:
            test_obj.yakshaAssert("TestDimension", True, "functional")
            print("TestDimension = Passed")
        else:
            test_obj.yakshaAssert("TestDimension", False, "functional")
            print("TestDimension = Failed")

    def test_size(self):
        s=find_size()
        test_obj = TestUtils() 
        if s==4:
            test_obj.yakshaAssert("TestSize", True, "functional")
            print("TestSize = Passed")
        else:
            test_obj.yakshaAssert("TestSize", False, "functional")
            print("TestSize = Failed")

    def test_shape(self):
        shp=find_shape()
        test_obj = TestUtils()
        if shp!=None:
            if shp[0]==2 and shp[1]==2:
                test_obj.yakshaAssert("TestShape", True, "functional")
                print("TestShape = Passed")
            else:
                test_obj.yakshaAssert("TestShape", False, "functional")
                print("TestShape = Failed")
        else:
            test_obj.yakshaAssert("TestShape", False, "functional")
            print("TestShape = Failed")

    def test_biggest(self):
        big=find_biggest()
        test_obj = TestUtils()
        if big==4:
            test_obj.yakshaAssert("TestBiggest", True, "functional")
            print("TestBiggest = Passed")
        else:
            test_obj.yakshaAssert("TestBiggest", False, "functional")
            print("TestBiggest = Failed")

    def test_list_series(self):
        e=define_series_with_list()
        test_obj = TestUtils()
        if e==30:
            test_obj.yakshaAssert("TestListSeries", True, "functional")
            print("TestListSeries = Passed")
        else:
            test_obj.yakshaAssert("TestListSeries", False, "functional")
            print("TestListSeries = Failed")

    def test_dict_series(self):
        e=define_series_with_dict()
        test_obj = TestUtils()
        if e==35:
            test_obj.yakshaAssert("TestDictSeries", True, "functional")
            print("TestDictSeries = Passed")
        else:
            test_obj.yakshaAssert("TestDictSeries", False, "functional")
            print("TestDictSeries = Failed")

    def test_series_size(self):
        s=check_size()
        test_obj = TestUtils()
        if s==7:
            test_obj.yakshaAssert("TestSeriesSize", True, "functional")
            print("TestSeriesSize = Passed")
        else:
            test_obj.yakshaAssert("TestSeriesSize", False, "functional")
            print("TestSeriesSize = Failed")

    def test_is_series_unique(self):
        b=check_unique()
        test_obj = TestUtils()
        if b==False:
            test_obj.yakshaAssert("TestIsSeriesUnique", True, "functional")
            print("TestIsSeriesUnique = Passed")
        else:
            test_obj.yakshaAssert("TestIsSeriesUnique", False, "functional")
            print("TestIsSeriesUnique = Failed")

    def test_lowest_element_index(self):
        ind=check_lowest() 
        test_obj = TestUtils()
        if ind==3:
            test_obj.yakshaAssert("TestLowestElementIndex", True, "functional")
            print("TestLowestElementIndex = Passed")
        else:
            test_obj.yakshaAssert("TestLowestElementIndex", False, "functional")
            print("TestLowestElementIndex = Failed")        

       