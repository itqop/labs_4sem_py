from heapq import heappop, heappush

def a_star(start_chain, goal_node):
    node_hash = {}
    chains_queue = []
    heappush(chains_queue, start_chain)
    while chains_queue:
        cur_chain = heappop(chains_queue)
        cur_node = cur_chain.last_node()
        if cur_node == goal_node:
            return cur_chain
        node_hash[cur_node] = cur_chain.g()
        for chain in cur_chain.get_neighbours():
            if chain.last_node() in node_hash:
                if chain.g() >= node_hash[chain.last_node()]:
                    continue
                node_hash[chain.last_node()] = chain.g()
            heappush(chains_queue, chain)

    raise Exception("Нет решения")