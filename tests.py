#!/usr/bin/env python

import unittest
import os
import uuid

from daab import DAAB, Store
from dotenv import load_dotenv

class TestDAAB(unittest.TestCase):

    def setUp(self):
        load_dotenv()
        self.daab = DAAB(os.getenv('DO_TOKEN'), os.getenv('DOMAIN'))

    def test_daab(self):
        # Test creating stores
        key = f'test_scenario:{uuid.uuid4().hex}'
        self.daab.set(key, 'I\'m doing a hecking test')

        # Test scanning stores
        stores = self.daab.scan('test_scenario:*')
        self.assertGreater(len(stores), 0)

        # Test getting stores
        store = self.daab.get(key)
        self.assertIsInstance(store, Store)

        # Test update store
        store = self.daab.set(key, 'A new value')
        self.assertEqual(store.value, 'A new value')

        # Test delete store
        self.daab.delete(store.key)


if __name__ == '__main__':
    unittest.main()
