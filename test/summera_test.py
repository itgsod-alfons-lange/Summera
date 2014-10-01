#encoding: utf-8

from nose.tools import *
import sys
sys.path.append('../lib')

from summera import summera




@raises(TypeError)
def test_summera_takes_two_argument():
    summera()


def test_summera_3_5_should__give_12():

    assert_equal(summera(start=3,stop=5), 12)

def test_summera_2__negative_5_should_give_a_negative_12():

    assert_equal(summera(start=2,stop=-5), -12)

