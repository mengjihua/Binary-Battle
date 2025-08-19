class UnionFind:
    def __init__(self, n: int) -> None:
        """初始化并查集"""
        self.parent = list(range(n))
        self.rank = [0] * n
        self.part = n

    def find(self, x):
        """查找根节点, 路径压缩"""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def merge(self, x, y):
        """合并两个节点所在的集合, 按秩合并"""
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return
        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
        elif self.rank[rx] > self.rank[ry]:
            self.parent[ry] = rx
        else:
            self.parent[ry] = rx
            self.rank[rx] += 1
        self.part -= 1