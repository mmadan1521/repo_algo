
def find_followers(key: str, graph_edges: dict, visited_vertex_list: dict) -> int:
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
   

def find_max_influencer(graph_edges: dict) -> str:
   max_follwers = 0
   max_influencer = ""
   for key in graph_edges.keys():
      follwers = find_followers(key, graph_edges, {})
      print(f"number of followers for {key} is {follwers}")
      if max_follwers < follwers:
         max_follwers = follwers
         max_influencer = key
   return max_influencer

def create_graph(tw_f: list) -> dict:
   graph_edges = {} 
   for tup in tw_f:
      # using tup[1] as key instead of tup[0]
      # so, instead of storing "stuart follows marty"
      # the graph_edges indicates "marty is followed by stuart"
      # this helps in recursively finding followers of stuart and their followers
      if tup[1] in graph_edges:
         graph_edges[tup[1]].append(tup[0])
      else:
         graph_edges[tup[1]] = [tup[0]]
   return graph_edges

if __name__ == "__main__":
   # list of tuples
   twitter_followers = [
                        ('Stuart',  'Marty'),   # stuart follows marty
                        ('Helene',  'Elmer'),   # helene follows elmer
                        ('Donald',  'Marty'),
                        ('Bruce',   'Elmer'),
                        ('Donald',  'Elmer'),
                        ('Donald',  'Stuart'),
                        ('Stuart',  'Mehran'),
                        ('Mehran',  'Donald'),
                        ('Reid',    'Elmer'),
                        ('Marty',   'Mehran'),
                        ]
    
   graph_edges = create_graph(twitter_followers)
   print(f"Graph of twitter followers {graph_edges}")

   max_influencer = find_max_influencer(graph_edges)
   print(f"\nMAX Influencer is {max_influencer}\n")
