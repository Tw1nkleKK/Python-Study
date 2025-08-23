__all__ = ['test_a']

def test(a, b):
    print(a + b)

def test_a():
    print("正常导入")
def test_b():
    print("正常2")

if __name__ == '__main__':
    test(100, 100)