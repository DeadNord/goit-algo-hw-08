import networkx as nx
import heapq
import matplotlib.pyplot as plt


class CableCombiner:
    def __init__(self, cable_lengths):
        self.cable_lengths = cable_lengths
        heapq.heapify(self.cable_lengths)
        self.total_cost = 0

    def combine_cables(self):
        while len(self.cable_lengths) > 1:
            first = heapq.heappop(self.cable_lengths)
            second = heapq.heappop(self.cable_lengths)
            cost = first + second
            self.total_cost += cost
            heapq.heappush(self.cable_lengths, cost)

        return self.total_cost

    def get_heap(self):
        return self.cable_lengths


def plot_heap(heap, ax):
    if not heap:
        return

    G = nx.Graph()
    labels = {}
    for i, value in enumerate(heap):
        G.add_node(i)
        labels[i] = str(value)
        if i != 0:  # уникнення кореня
            G.add_edge(i, (i - 1) // 2)

    pos = nx.drawing.nx_agraph.graphviz_layout(G, prog="dot")
    nx.draw(G, pos, ax=ax, with_labels=False, arrows=False)
    nx.draw_networkx_labels(G, pos, labels, ax=ax)


def visualize_combining_process(cable_lengths):
    combiner = CableCombiner(cable_lengths)
    fig, ax = plt.subplots(figsize=(8, 6))

    while len(combiner.get_heap()) > 1:
        ax.clear()
        plot_heap(combiner.get_heap(), ax)
        combiner.combine_cables()
        ax.set_title(f"Total Cost: {combiner.total_cost}")
        plt.pause(1)

    plt.show()


def main():
    cable_lengths = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    visualize_combining_process(cable_lengths)


if __name__ == "__main__":
    main()
