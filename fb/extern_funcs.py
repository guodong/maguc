import networkx as nx
import magellan as mg


def shortest_path(src, dst):
    G = nx.Graph(mg.topo)
    path = G.shortest(src, dst)
    return mg.path.normalize(path)


def ecmp_paths(src, dst):
    G = nx.Graph(mg.topo)
    paths = G.paths(src, dst).sort(lambda p: len(p))
    min_num_hops = len(paths[0])
    paths = paths.filter(lambda p: len(p) == min_num_hops)
    return mg.path.normalize(paths)


def frr(path):
    G = nx.Graph(mg.topo)
    paths = G.paths(path[0], path[-1]).filter(lambda p: p != path).sort(lambda p: len(p))
    return mg.path.normalize(paths[0])


mg.export(shortest_path)
mg.export(ecmp_paths)
mg.export(frr)
