from unittest import TestCase, main
import requests
import time
import uuid


class ConcurrencyTest(TestCase):
    def setUp(self):
        self.key = str(uuid.uuid4())[:6]
        self.value = str(uuid.uuid4())[:6]
        print('setUp', self.key, self.value)

    def tearDown(self):
        print('tearDown', self.key, self.value)

    def test_sleep_1s_1(self):
        time.sleep(1)
        print(self.key, self.value)

        self.assertEqual(True, True)

    def test_sleep_1s_2(self):
        time.sleep(1)
        print(self.key, self.value)
        
        self.assertEqual(True, True)

    def test_sleep_1s_3(self):
        time.sleep(1)
        print(self.key, self.value)
        
        self.assertEqual(True, True)

    def test_sleep_1s_4(self):
        time.sleep(1)
        print(self.key, self.value)
        
        self.assertEqual(True, True)

if __name__ == '__main__':
    main()
