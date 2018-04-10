#TSP considering 10 cities and predefined distances
from math import sqrt
def cities():
  n=10# number of cities
  cities=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]#city numbers
  city_coords=[(2,3),(4,5),(8,9),(6,5),(4,1),(6,7),(3,4),(8,9),(4,2),(6,1)]# x and y coordinates of each city on a plain
  distance_matrix=[[0 for x in range(n)] for y in range(n)] 
  for i in range (n):
    for j in range (n):
      x_comp=city_coords[j][0]-city_coords[i][0]
      y_comp=city_coords[j][1]-city_coords[i][1]
      distance_matrix[i][j]=distance_matrix[j][i]=sqrt(x_comp**2+y_comp**2)
  return distance_matrix
 

def tour_cost(tour,distance_matrix):

  dist_matrix=distance_matrix
  tour=list(tour)
  tour_cost=0
  n=len(tour)


  for i in range (n-1):
    tour_cost+= dist_matrix[tour[i]][tour[i+1]]
  tour_cost+= dist_matrix[tour[n-1]][tour[0]]
  return tour_cost


def local_hillclimb_search(cities,distance_matrix):
  final_path=[]
  final_cost=0
  n=10

  curr_path=list(cities)

 
  dm=distance_matrix
  curr_cost=tour_cost(curr_path,dm)

  tour1= list(curr_path)
  cost1=curr_cost

  b=0
  c=0

  while b==0:
    print("Evaluation Number:",c)

    print("Path: ", str(curr_path) +" Distance Covered: ", str(int(curr_cost*10)) +"miles")

    b=1

    for i in range(0,n-1):
      for j in range(i+1,n):
        next_path=list(curr_path)
        next_path[i], next_path[j] = next_path[j],next_path[i]

        next_cost=tour_cost(next_path, dm)

        if next_cost<cost1:
          b=0
          tour1=list(next_path)
          cost1=next_cost
    
    curr_path = list(tour1)
    curr_cost = cost1

    c=c+1

  final_path=list(curr_path)
  final_cost=curr_cost
  return(final_path, final_cost)



def main():

  curr_tour=[0,1,2,3,4,9,6,7,8,5]
  final_path, final_cost=hillclimibing(curr_tour,cities())

  print("========================================================================")

  print("\n Shortest Path taken by Travelling Salesman: ",str(final_path)+" \n \
  Shortest Distance Covered:", str(int(final_cost*10))+"miles")
main()



