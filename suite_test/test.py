from unittest import TestCase, main
import requests
import time
import uuid


class ConcurrencyTest(TestCase):
    def setUp(self):
        self.obj = Obj()
        print('setUp', self.obj.getTests())

    def tearDown(self):
        print('tearDown', self.obj.getTests())

    def test_sleep_1s_1(self):
        time.sleep(1)
        self.obj.addTest(1)

        self.assertEqual(True, True)

    def test_sleep_1s_2(self):
        time.sleep(1)
        self.obj.addTest(2)
        
        self.assertEqual(True, True)

    def test_sleep_1s_3(self):
        time.sleep(1)
        self.obj.addTest(3)
        
        self.assertEqual(True, True)

    def test_sleep_1s_4(self):
        time.sleep(1)
        self.obj.addTest(4)
        
        self.assertEqual(True, True)

if __name__ == '__main__':
    main()
