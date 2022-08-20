import requests

import unittest
import  json
from flask import jsonify


class TestStringMethods(unittest.TestCase):

    def test_algorithms(self):
        dictionary={"Bert":"","SedTwik":"","Twemeddings":""}
        test_res =list(dictionary.keys())
        x = requests.get('https://rps.ise.bgu.ac.il/njsw28/algorithm/all')
        print(type(x.text))
        self.assertEqual(test_res,list(x.text.split("\n"))[1:-2])

    def test_algorithms(self):
        dictionary={"Bert":"","SedTwik":"","Twemeddings":""}
        test_res =list(dictionary.keys())
        x = requests.get('https://rps.ise.bgu.ac.il/njsw28/algorithm/all')
        print(type(x.text))
        self.assertEqual(test_res,list(x.text.split("\n"))[1:-2])



if __name__ == '__main__':
    unittest.main()
