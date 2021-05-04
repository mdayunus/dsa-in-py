class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]

        print(self.graph_dict)

    def yunus_find_path(self, start_from, end_at, travel=[], routes = []):
        travel = travel + [start_from]
        
        if start_from not in self.graph_dict:
            return []

        if start_from == end_at:
            return travel
        
        for city in self.graph_dict[start_from]:
            if city not in travel:
                if city == end_at:
                    travel = travel + [city]
                    routes.append(travel)
                else:
                    self.find_path(city, end_at, travel, routes)
        
        return routes

    
    def correct_fp(self, start_from, end_at, travel = [], all_routes = []):
        travel = travel + [start_from]
        if start_from == end_at:
            all_routes.append(travel)
            return 

        if start_from not in self.graph_dict:
            return []

        for city in self.graph_dict[start_from]:
            if city not in travel:
                self.fp(city, end_at, travel, all_routes)


        return all_routes



if __name__ == '__main__':
    es = (
        ('mumbai', 'paris'),
        ('mumbai', 'dubai'),
        ('paris', 'dubai'),
        ('paris', 'new york'),
        ('dubai', 'new york'),
        ('new york', 'toronto')
    )

    g = Graph(es)
    path = g.fp('mumbai', 'new york', ['ind'])
    print(path)
    # print(g)
