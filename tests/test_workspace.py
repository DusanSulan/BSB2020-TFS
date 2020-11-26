import unittest

class TestEnvironment(unittest.TestCase):

    def test_import_numpy(self):
        import numpy as np

    def test_import_pyplot(self):
        from matplotlib import pyplot as plt

    def test_import_cv2(self):
        import cv2

    def test_import_jupyter(self):
        import jupyter

    def test_get_files(self):
        import glob
        files = glob.glob('./data/cb/cb_*.png')
        self.assertEqual(len(files), 121)

    def test_datasets(self):
        import glob
        files = glob.glob('./data/ball-count/ball-count.png')
        self.assertEqual(len(files), 1)
        files = glob.glob('./data/cb/cb_*.png')
        self.assertEqual(len(files), 121)
        files = glob.glob('./data/focus/focus_*.png')
        self.assertEqual(len(files), 16)
        files = glob.glob('./data/stigmator/stigmator_*.png')
        self.assertEqual(len(files), 16)

    def test_load_image(self):
        import cv2
        image = cv2.imread('./data/cb/cb_000_0.57_0.30.png', 0)
        self.assertEqual(image.shape, (1024, 1536))

    def test_cv2_imshow(self):
        import glob
        import cv2
        files = glob.glob('./data/cb/cb_*.png')
        image = cv2.imread(files[0], 0)
        cv2.imshow('Image', image)
        cv2.waitKey(1)
        cv2.destroyAllWindows()

    def test_pyplot_imshow(self):
        import glob
        import cv2
        from matplotlib import pyplot as plt
        files = glob.glob('./data/cb/cb_*.png')
        image = cv2.imread(files[0], 0)
        plt.imshow(image, cmap='gray')
        plt.show(block=False)
        plt.close()

    def test_numpy_array(self):
        import numpy as np
        x = [[1, 2, 3], [4, 5, 6]]
        a = np.array(x)
        self.assertEqual(a.shape, (2, 3))
        self.assertEqual(np.max(a), 6)

    def test_numpy_nan(self):
        import numpy as np
        x = [[np.nan, 2, 3], [4, np.nan, 6], [7, 8, np.nan]]
        a = np.array(x)
        self.assertEqual(np.nanmax(a), 8)

    def test_plot(self):
        import numpy as np
        from matplotlib import pyplot as plt
        x = np.arange(0, 2*np.pi, 0.01)
        y = np.sin(x)
        plt.plot(x, y)
        plt.show(block=False)
        plt.close()


if __name__ == '__main__':
    unittest.main()
