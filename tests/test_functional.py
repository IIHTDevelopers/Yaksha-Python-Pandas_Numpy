#import sys, os
import unittest
import collections
import pandas as pd
#import pickle
import test_pandas as test_pd
import test_numpy as test_np
from tests.TestUtils import TestUtils
#file_path = os.path.dirname(os.path.realpath(__file__)) + '/../output_revised.txt'
#solutions = pd.read_csv("solutions_pandas.csv")["solution"].values
# with open('tests/H2f_Kkp5a4V.pickle', 'rb') as f:
#      solutions = pickle.load(f)

class FuctionalTests(unittest.TestCase):
    def test_create_df_from_dict(self):
        test_obj = TestUtils()
        try:
            ret_test = test_pd.create_df_from_dict()
            test_sol = solutions[0]
            passed = ret_test.equals(test_sol)
            if passed:
                test_obj.yakshaAssert("TestCreateDfFromDict", True, "functional")
                print("TestCreateDfFromDict = Passed")
            else:
                test_obj.yakshaAssert("TestCreateDfFromDict", False, "functional")
                print("TestCreateDfFromDict = Failed")
        except:
            test_obj.yakshaAssert("TestCreateDfFromDict", False, "functional")
            print("TestCreateDfFromDict = Failed")
        #assert passed

    def test_create_df_from_list(self):
        test_obj = TestUtils()
        try:
            ret_test = test_pd.create_df_from_list()
            test_sol = solutions[1]
            passed = ret_test.equals(test_sol)
            if passed:
                test_obj.yakshaAssert("TestCreateDfFromList", True, "functional")
                print("TestCreateDfFromList = Passed")
            else:
                test_obj.yakshaAssert("TestCreateDfFromList", False, "functional")
                print("TestCreateDfFromList = Failed")
        except:
            test_obj.yakshaAssert("TestCreateDfFromList", False, "functional")
            print("TestCreateDfFromList = Failed")
        #assert passed

    def test_get_df_stats(self):
        test_obj = TestUtils()
        try:
            ret_test = test_pd.get_df_stats()
            test_sol = solutions[2]
            passed = (ret_test[0] == test_sol[0]) & (ret_test[1] == test_sol[1]) & \
                    ret_test[2].equals(test_sol[2]) & (ret_test[4] == test_sol[4]).all() & \
                    (ret_test[5] == test_sol[5])
            if passed:
                test_obj.yakshaAssert("TestGetDfStats", True, "functional")
                print("TestGetDfStats = Passed")
            else:
                test_obj.yakshaAssert("TestGetDfStats", False, "functional")
                print("TestGetDfStats = Failed")
        except:
            test_obj.yakshaAssert("TestGetDfStats", False, "functional")
            print("TestGetDfStats = Failed")
        #assert passed

    def test_stack_series(self):
        test_obj = TestUtils()
        try:
            ret_test = test_pd.stack_series()
            test_sol = solutions[3]
            passed = ret_test[0].equals(test_sol[0]) & ret_test[1].equals(test_sol[1])
            if passed:
                test_obj.yakshaAssert("TestStackSeries", True, "functional")
                print("TestStackSeries = Passed")
            else:
                test_obj.yakshaAssert("TestStackSeries", False, "functional")
                print("TestStackSeries = Failed")
        except:
            test_obj.yakshaAssert("TestStackSeries", False, "functional")
            print("TestStackSeries= Failed")
        #assert passed

    def test_series_quantile(self):
        test_obj = TestUtils()
        try:
            ret_test = test_pd.series_quantile()
            test_sol = solutions[4]
            passed = ret_test[0].equals(test_sol[0]) & ret_test[1].equals(test_sol[1])
            if passed:
                test_obj.yakshaAssert("TestSeriesQuantile", True, "functional")
                print("TestSeriesQuantile = Passed")
                with open(file_path, "a") as f:
                    f.write("=True\n")
                    print("TestSeriesQuantile = Passed")
            else:
                test_obj.yakshaAssert("TestSeriesQuantile", False, "functional")
                print("TestSeriesQuantile = Failed")
        except:
            test_obj.yakshaAssert("TestSeriesQuantile", False, "functional")
            print("TestSeriesQuantile = Failed")
        #assert passed

    def test_handling_nans(self):
        test_obj = TestUtils()
        try:
            ret_test = test_pd.handling_nans()
            test_sol = solutions[5]
            passed = (ret_test[0]==ret_test[0]) & ret_test[1].equals(test_sol[1]) & \
                    (ret_test[2].equals(test_sol[2]))
            if passed:
                test_obj.yakshaAssert("TestHandlingNans", True, "functional")
                print("TestHandlingNans = Passed")
            else:
                test_obj.yakshaAssert("TestHandlingNans", False, "functional")
                print("TestHandlingNans = Failed")
        except:
            test_obj.yakshaAssert("TestHandlingNans", False, "functional")
            print("TestHandlingNans = Failed")
        #assert passed

    def test_handling_dates(self):
        test_obj = TestUtils()
        try:
            ret_test = test_pd.handling_dates()
            test_sol = solutions[6]
            passed = ret_test[0].equals(test_sol[0]) & ret_test[1].equals(test_sol[1])
            if passed:
                test_obj.yakshaAssert("TestHandlingDates", True, "functional")
                print("TestHandlingDates = Passed")
            else:
                test_obj.yakshaAssert("TestHandlingDates", False, "functional")
                print("TestHandlingDates = Failed")
        except:
            test_obj.yakshaAssert("TestHandlingDates", False, "functional")
            print("TestHandlingDates = Failed")
        #assert passed

    def test_string_manipulation_df(self):
        test_obj = TestUtils()
        try:
            ret_test = test_pd.string_manipulation_df()
            test_sol = solutions[7]

            passed = ret_test.equals(test_sol)
            if passed:
                test_obj.yakshaAssert("TestStringManipulationDf", True, "functional")
                print("TestStringManipulationDf = Passed")
            else:
                test_obj.yakshaAssert("TestStringManipulationDf", False, "functional")
                print("TestStringManipulationDf = Failed")
        except:
            test_obj.yakshaAssert("TestStringManipulationDf", False, "functional")
            print("TestStringManipulationDf = Failed")
        #assert ret_test.equals(test_sol)

    def test_sorting_df(self):
        test_obj = TestUtils()
        try:
            ret_test = test_pd.sorting_df()
            test_sol = solutions[8]

            passed = ret_test.equals(test_sol)
            if passed:
                test_obj.yakshaAssert("TestSortingDf", True, "functional")
                print("TestSortingDf = Passed")
            else:
                test_obj.yakshaAssert("TestSortingDf", False, "functional")
                print("TestSortingDf = Failed")
        except:
            test_obj.yakshaAssert("TestSortingDf", False, "functional")
            print("TestSortingDf = Failed")
        #assert ret_test.equals(test_sol)

    def test_groupby_df(self):
        test_obj = TestUtils()
        try:
            ret_test = test_pd.groupby_df()
            test_sol = solutions[9]
            passed = ret_test.equals(test_sol)
            if passed:
                test_obj.yakshaAssert("TestGroupbyDf", True, "functional")
                print("TestGroupbyDf = Passed")
            else:
                test_obj.yakshaAssert("TestGroupbyDf", False, "functional")
                print("TestGroupbyDf = Failed")
        except:
            test_obj.yakshaAssert("TestGroupbyDf", False, "functional")
            print("TestGroupbyDf = Failed")
        #assert ret_test.equals(test_sol)

    def test_stack_numpy(self):
        test_obj = TestUtils()
        try:
            ret_test = test_np.stack_numpy()
            test_sol = solutions[10]
            passed = (ret_test[0] == test_sol[0]).all() & (ret_test[1] == test_sol[1]).all()
            if passed:
                test_obj.yakshaAssert("TestStackNumpy", True, "functional")
                print("TestStackNumpy = Passed")
            else:
                test_obj.yakshaAssert("TestStackNumpy", False, "functional")
                print("TestStackNumpy = Failed")
        except:
           test_obj.yakshaAssert("TestStackNumpy", False, "functional")
           print("TestStackNumpy= Failed")
        #assert passed

    def test_reshape_numpy(self):
        test_obj = TestUtils()
        try:
            ret_test = test_np.reshape_numpy()
            test_sol = solutions[11]
            passed = (ret_test[0] == test_sol[0]).all() & (ret_test[1] == test_sol[1]).all()
            if passed:
                test_obj.yakshaAssert("TestReshapeNumpy", True, "functional")
                print("TestReshapeNumpy = Passed")
            else:
                test_obj.yakshaAssert("TestReshapeNumpy", False, "functional")
                print("TestReshapeNumpy= Failed")
        except:
            test_obj.yakshaAssert("TestReshapeNumpy", False, "functional")
            print("TestReshapeNumpy = Failed")

        #assert passed
    def test_compare_np_arrays(self):
        test_obj = TestUtils()
        try:
            ret_test = test_np.compare_np_arrays()
            test_sol = solutions[12]

            passed = (ret_test[0] == test_sol[0]).all()
            if passed:
                test_obj.yakshaAssert("TestCompareNpArrays", True, "functional")
                print("TestCompareNpArrays = Passed")
            else:
                test_obj.yakshaAssert("TestCompareNpArrays", False, "functional")
                print("TestCompareNpArrays = Failed")
        except:
            test_obj.yakshaAssert("TestCompareNpArrays", False, "functional")
            print("TestCompareNpArrays = Failed")
        #assert passed

    def test_stats_numpy(self):
        test_obj = TestUtils()
        try:
            ret_test = test_np.stats_numpy()
            test_sol = solutions[13]
            passed = (ret_test[0] == test_sol[0]).all()
            if passed:
                test_obj.yakshaAssert("TestStatsNumpy", True, "functional")
                print("TestStatsNumpy = Passed")
            else:
                test_obj.yakshaAssert("TestStatsNumpy", False, "functional")
                print("TestStatsNumpy = Failed")
        except:
            test_obj.yakshaAssert("TestStatsNumpy", False, "functional")
            print("TestStatsNumpy = Failed")
        #assert passed

    def test_twod_numpy(self):
        test_obj = TestUtils()
        try:
            ret_test = test_np.twod_numpy()
            test_sol = solutions[14]
            passed = (ret_test[0] == test_sol[0]).all() & (ret_test[1] == test_sol[1]).all() & \
                    (ret_test[2] == test_sol[2]).all() & (ret_test[3] == test_sol[3]).all()
            if passed:
                test_obj.yakshaAssert("TestTwodNumpy", True, "functional")
                print("TestTwodNumpy = Passed")
            else:
                test_obj.yakshaAssert("TestTwodNumpy", False, "functional")
                print("TestTwodNumpy = Failed")
        except:
            test_obj.yakshaAssert("TestTwodNumpy", False, "functional")
            print("TestTwodNumpy = Failed")
        #assert passed

    def test_handling_nans_1(self):
        test_obj = TestUtils()
        try:
            ret_test = test_np.handling_nans_1()
            test_sol = solutions[15]
            passed = (ret_test[0] == test_sol[0]).all() & (ret_test[1] == test_sol[1]).all() & \
                    (ret_test[2] == test_sol[2]).all()
            if passed:
                test_obj.yakshaAssert("TestHandlingNans1", True, "functional")
                print("TestHandlingNans1 = Passed")
            else:
                test_obj.yakshaAssert("TestHandlingNans1", False, "functional")
                print("TestHandlingNans1 = Failed")
        except:
            test_obj.yakshaAssert("TestHandlingNans1", False, "functional")
            print("TestHandlingNans1 = Failed")
        #assert passed

    def test_handling_nans_2(self):
        test_obj = TestUtils()
        try:
            ret_test = test_np.handling_nans_2()
            test_sol = solutions[16]
            passed = (ret_test[0][0] == test_sol[0][0]).all() & (ret_test[1] == test_sol[1]).all() & \
                    (ret_test[0][1] == test_sol[0][1]).all()
            if passed:
                test_obj.yakshaAssert("TestHandlingNans2", True, "functional")
                print("TestHandlingNans2 = Passed")
            else:
                test_obj.yakshaAssert("TestHandlingNans2", False, "functional")
                print("TestHandlingNans2 = Failed")
        except:
            test_obj.yakshaAssert("TestHandlingNans2", False, "functional")
            print("TestHandlingNans2 = Failed")
        #assert passed
