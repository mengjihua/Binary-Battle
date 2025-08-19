import networkx as nx
import matplotlib.pyplot as plt
# https://csacademy.com/app/graph_editor/


class TreeNode:
    def __init__(self):
        self.children = []
        self.val = None

    def generate_and_draw_graph(self, n, label, edges):
        # 创建无向图
        G = nx.Graph()

        # 验证标签长度与节点数是否匹配
        if len(label) != n:
            raise ValueError("节点标签长度必须与节点数相同!")

        # 添加边
        G.add_edges_from(edges)

        # 定义节点标签：格式为 "0\na" 表示节点 0 的 label 是 a
        labels = {k: f"{k}\n{v}" for k, v in zip(range(n), label)}

        # 设置绘图参数为深色主题
        plt.style.use('default')  # 可以换成 'dark_background' 等风格

        # 绘制图形
        plt.figure(figsize=(9, 7))  # 设置图像大小

        # 自动布局算法之一：spring_layout
        pos = nx.spring_layout(G, seed=42)  # 固定 seed 保证每次布局一致

        # 绘制节点、边
        nx.draw_networkx_nodes(
            G, pos, node_color='lightgreen', node_size=800)  # 节点颜色
        nx.draw_networkx_edges(G, pos, edge_color='gray')  # 边颜色

        # 设置中文字体支持
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

        # 显示节点标签（节点编号 + label 字符）
        nx.draw_networkx_labels(
            G, pos, labels, font_size=12, font_color='black', font_weight='bold')

        # 设置标题
        plt.title("图结构可视化 (含节点编号和字符)", fontsize=16)
        plt.axis('off')  # 关闭坐标轴
        plt.tight_layout()  # 自动调整防止裁剪
        plt.show()


# 使用示例
tree_node = TreeNode()
tree_node.generate_and_draw_graph(n=7, edges=[[0, 1], [1, 2], [1, 3], [3, 4], [0, 5], [5, 6]], label="aabbcbc")
# tree_node.generate_and_draw_graph(n = 3, edges = [[0,1],[0,2]], label = "abc")
