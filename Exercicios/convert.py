# -*- coding: utf-8 -*-
"""
Created on Sat May 30 17:52:47 2020

@author: leowc
"""
import unittest

x = hhmmss2ss(h = 5,m = 5,s = 30)

def hhmmss2ss(h: int = 0, m: int = 0, s: int = 0):
    """
    This function will convert a given hour, minute and second to seconds.
    Params: 
        1 - h - represeents Hour PM format (0-24)
        2 - m - represents Minutes (0-60)
        3 - s - represents Seconds (0)
    Return:
        int
    """
    assert h >= 0 and h <= 24, "Hours must be between 0 and 24"
    assert m >= 0 and m <= 60, "Minutes must be between 0 and 60"
    assert s >= 0 and s <= 60, "Seconds must be between 0 and 60"
    return h*3600+m*60+s


        
def should_return_assertion_error_when_hour_greater_than_24():
    try:
        hhmmss2ss(25)
        print('25 hour: Fail')
    except AssertionError:
        print('25 hour: Pass')
        pass
    
            
def should_return_3600_when_hour_is_1_and_has_no_minutes_and_seconds():
    try:
        s = hhmmss2ss(1)
        assert s == 3600
        print('24 hour: Pass')
    except AssertionError:
        print('24 hour: Fail')
        pass
    
should_return_3600_when_hour_is_1_and_has_no_minutes_and_seconds()

test()    
    

    
class Tests(unittest.TestCase):
    def should_return_assertion_error_when_hour_greater_than_24(self):
        
        with self.assertRaises(AssertionError):
            assert hhmmss2ss(25)
    #should_return_assertion_error_when_hour_greater_than_24(this)