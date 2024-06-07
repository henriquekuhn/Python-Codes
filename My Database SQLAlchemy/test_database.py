import unittest
from main import DatabaseManagement

class TestDatabaseManagement(unittest.TestCase):

    def setUp(self):
        self.db_management = DatabaseManagement()
        self.db_management.create_db()
        self.db_management.initiate_db_session()

    def test_2_create_test(self):
        result = self.db_management.create_test("Test1", 25.0, 3.3, 0.9, 3.9, 2)
        self.assertEqual(result, "Test create success.")

    def test_3_query_db(self):
        self.size_1_test = self.db_management.query_test()
        self.db_management.create_test("Test2", 25.0, 3.3, 0.9, 3.9, 2)
        self.size_2_test = self.db_management.query_test()
        self.assertEqual(self.size_2_test, self.size_1_test+1)

    def test_4_queryfilter_db(self):
        column_search = "test_name"
        search_name = "Test2"
        self.result = self.db_management.query_by_filter(column_search, search_name)
        print(self.result)
        self.assertEqual(self.result, search_name)

    def test_5_update_db(self):
        self.search_name = "Test2"
        self.new_value = "TestEdited"
        self.column_search = "test_name"

        self.result = self.db_management.edit_register(self.column_search, self.search_name, self.new_value)
        self.assertEqual(self.result, self.new_value)

    def test_6_delete_db(self):
        self.search_name = "TestEdited"
        self.column_search = "test_name"
        self.result = self.db_management.delete_regiter(self.column_search, self.search_name)
        print(self.result)
        self.assertEqual(self.result, None)

        
if __name__ == '__main__':
    unittest.main()