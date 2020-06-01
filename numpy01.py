import numpy as np


def main():
    a = np.array([1, 2, 3])
    print(a)
    print(a.shape)
    print(a.size)
    print(a.dtype)
    print(a.ndim)
    b = np.array([[4, 5, 6, 4]])
    print(b.ndim)
    print(b.shape)

    dt = np.dtype("f2")
    print(dt)
    # 自定義資料形態
    people = np.dtype([("name", "S20"), ("height", "i4"), ("weight", "f2")])
    b = np.array([("amy", 169, 60.), ("dsfdfsdfsfsdfsdfsdfsdfsdfsdf", 180, 66.3)], dtype=people)
    print(b)
    # 改變陣列形狀
    c = np.array([i for i in range(1, 13)])
    c2d = c.reshape(3, 4)
    print(c2d)
    c2dof = c.reshape(3, 4, order="F")
    print(c2dof)
    c3d = c.reshape(3, 2, 2)
    print(c3d)
    # 等差數列
    d = np.linspace(10, 19, 5)
    print(d)
    # 等比數列
    print("等比數列")
    e = np.logspace(2, 8, 7, dtype="i4")
    print(e)
    # 陣列填值
    print("陣列填值")
    f = np.zeros([3, 4])
    print(f)
    e = np.ones([2, 3])
    print(e)
    g = np.random.random((2, 3))
    print(g)
    print("對角線填值")
    h = np.eye(3, dtype="i4")
    print(h)
    i = np.eye(3, k=1)
    print(i)
    # 二維陣列取值
    print("二維陣列取值")
    j = np.arange(1, 37).reshape(6, 6)
    print(j)
    print(j[..., 3])  # 取第四行
    print(j[1:2])  # 取第2列
    print(j[0:3, 3:])  # 取3X3陣列
    print("跳躍取值")
    k = np.arange(1, 26).reshape(5, 5)
    print(k)
    print(k[[1, 2, 3], [1, 2, 3]])
    print("共用記憶體")
    l = np.arange(0, 7)
    print(l)
    m = l[1:5]
    print(m)
    m[0] = 100
    print(m)
    print(l)
    print(np.may_share_memory(l, m))
    n = l[1: 5].copy()
    print(n)
    print(np.may_share_memory(l, n))
    print("broadcast機制")
    aa = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8]])
    bb = np.array([1, 1, 1, 1])
    print(aa, "+", bb, "=", aa+bb)
    cc = np.array([[1], [2]])
    print(aa, "*", cc, end="")
    print("=", aa*cc)



if __name__ == "__main__":
    main()
