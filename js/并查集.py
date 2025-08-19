class UnionFind:
    def __init__(self, n: int) -> None:
        self.root_or_size = [-1] * n  # 负数表示根节点且绝对值为集合大小，正数表示父节点索引
        self.part = n  # 连通分量数量
        self.n = n     # 总节点数
    
    def initialize(self):
        """重置并查集到初始状态"""
        self.root_or_size = [-1] * self.n
        self.part = self.n
    
    def find(self, x: int) -> int:
        """查找x的根节点，带路径压缩"""
        if self.root_or_size[x] < 0:
            return x
        
        # 路径压缩：直接将x的父节点指向根节点
        self.root_or_size[x] = self.find(self.root_or_size[x])
        return self.root_or_size[x]
    
    def union(self, x: int, y: int) -> bool:
        """合并x和y所在的集合，返回是否成功合并"""
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False  # 已在同一集合，无需合并
        
        # 确保root_x是更大的集合（负数的值更小表示大小更大）
        if self.root_or_size[root_x] > self.root_or_size[root_y]:
            root_x, root_y = root_y, root_x
        
        # 合并：小集合(root_y)合并到大集合(root_x)
        self.root_or_size[root_x] += self.root_or_size[root_y]  # 更新大小
        self.root_or_size[root_y] = root_x                     # 将小集合的根指向大集合的根
        self.part -= 1  # 连通分量减少
        return True
    
    def is_connected(self, x: int, y: int) -> bool:
        """检查x和y是否连通"""
        return self.find(x) == self.find(y)
    
    def get_size(self, x: int) -> int:
        """获取x所在集合的大小"""
        root = self.find(x)
        return -self.root_or_size[root]