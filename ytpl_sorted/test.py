import unittest
from youtubeservice import playlistIDToVideos
from sortservice import sortByFunctions

class TestSort(unittest.TestCase):
    def test_sort(self):
        """
            TEST
        """
        data = [1,2,3]
        self.assertEqual(1,2)

if __name__ == '__main__':
    unittest.main()