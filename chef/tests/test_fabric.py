import mock

from chef.tests import TestChef


class FabricTestCase(TestChef):
    @mock.patch('chef.search.Search')
    def test_roledef(self, MockSearch):
        search_data = {
            ('role', '*:*'): {},
        }
        search_mock_memo = {}

        def search_mock(index, q='*:*', **kwargs):
            data = search_data[index, q]
            search_mock_inst = search_mock_memo.get((index, q))
            if search_mock_inst is None:
                search_mock_inst = search_mock_memo[index, q] = mock.Mock()
                search_mock_inst.data = data
            return search_mock_inst
        MockSearch.side_effect = search_mock
        # print(MockSearch('role').data)
