
def find_followers(key: str, graph_edges: {}, visited_vertex_list: {}) -> int:
   if key in graph_edges:
      if key not in visited_vertex_list:
         visited_vertex_list[key] = 1
         for item in graph_edges[key]:
            visited_vertex_list[key] += find_followers(item, graph_edges, visited_vertex_list)
         return visited_vertex_list[key]
      else:
         return 0
   elif key not in graph_edges:
      return 1
   

def find_max_influencer(graph_edges: {}) -> None:
   for key in graph_edges.keys():
      max_influence = find_followers(key, graph_edges, {})
      print(f"max influence of {key} is {max_influence}")

def create_graph(tw_f: []) -> {}:
   graph_edges = {} 
   for tup in tw_f:
      # using tup[1] as key instead of tup[0]
      # so, instead of "stuart follows marty"
      # the graph_edges edge indicates "marty is followed by stuart"
      # this helps in finding followers of stuart and recursively followers of follwer
      if tup[1] in graph_edges:
         graph_edges[tup[1]].append(tup[0])
      else:
         graph_edges[tup[1]] = [tup[0]]
   return graph_edges

if __name__ == "__main__":
   # list of tuples
   twitter_followers = [
                        ('stuart',  'marty'),   # stuart follows marty
                        ('helene',  'elmer'),   # helene follows elmer
                        ('donald',  'marty'),
                        ('bruce',   'elmer'),
                        ('donald',  'elmer'),
                        ('donald',  'stuart'),
                        ('stuart',  'mehran'),
                        ('mehran',  'donald'),
                        ('reid',    'elmer'),
                        ('marty',   'mehran'),
                        ]
    
   graph_edges = create_graph(twitter_followers)
   print(f"Graph of twitter followers {graph_edges}")

   find_max_influencer(graph_edges)
