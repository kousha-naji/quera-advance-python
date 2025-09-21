import unittest, time

from concurrency.threadizing.main import threadize


class ScoreListTest(unittest.TestCase):

    def test_time_len(self):
        dur = int(round(time.time() * 1000))

        threadize()
        print("hello\n")

        dur = int(round(time.time() * 1000)) - dur
        self.assertEqual(True, dur < 500, '\nابتدا باید تردهای مربوط به هر تابع را start و join کنید و سپس به سراغ تردهای مربوط به تابع بعدی بروید.')