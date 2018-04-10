
import random
from math import sqrt

def cities():
	n=10# number of cities
  	#cities=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]#city numbers
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

def samples(n,sample_no):
	samplelist = []
	cities = [0,1,2,3,4,5,6,7,8,9]
	for i in range(sample_no):
		random.shuffle(cities)
		samplelist.append(cities)
	return samplelist

def costFitness(samplelist, distance_matrix):

	fit = []
	for i in samplelist:
		fitness = tour_cost(i, distance_matrix)
		fit.append(fitness)
	return fit

def fitter(fit):
	chosen = []

	for i in range(3):
		g = random.sample(fit, 2)
		n1 = fit.index(min(g))
		g = random.sample(fit, 3)
		n2 = fit.index(min(g))

		chosen.append([n1, n2])

	return chosen


def local_genetic_search(n, distance_matrix):

	final_path = []
	final_cost = 0

	samplelist = samples(n, 6) 
	fit = costFitness(samplelist, distance_matrix)
	
	final_path = list(samplelist[fit.index(min(fit))])
	final_cost = tour_cost(final_path, distance_matrix)

	count = 0
	print("Evaluation Number:", count)
	print("Path under evaluation:",final_path)
	while count < 15 :
		print("Path under evaluation:",final_path)
		fit = costFitness(samplelist, distance_matrix)
		
		final_path1 = list(samplelist[fit.index(min(fit))])
		final_cost1 = tour_cost(final_path1, distance_matrix)
		
		print ("\n Distance Traveled :",str(int(final_cost*10)) +"miles")
		
		
		if final_cost1 < final_cost:
			final_cost = final_cost1

			final_path1 = list(final_path1)

		
		

		samplelist1 = crossover(n , fitter(fit) , samplelist)

		samplelist = mutator(n, samplelist1)

		count=count+1

	return (final_path, final_cost)


def crossover(n, chosen, samplelist):

	nextSamples = []

	for i in chosen:
		
		p1 = list(samplelist[i[0]])
		p2 = list(samplelist[i[1]])

		crossoverPoint = random.randint(2, n-2)

		c1 = list(p1)
		c2 = list(p2)

		c = list(c1)

		for i in range(crossoverPoint+1):
			swapIndex = c.index(c2[i])
			c[i] , c[swapIndex] = c[swapIndex] , c[i]

		for i in range(crossoverPoint+1):
			swapIndex = c2.index(c[i])
			c2[i] , c2[swapIndex] = c2[swapIndex] , c2[i]

		c1 = list(c)

		nextSamples.append(c1)
		nextSamples.append(c2)

	return nextSamples


def mutator(n, nextSamples):
	for item in nextSamples:
		index1, index2 = random.sample([i for i in range(n)], 2)
		item[index1] , item[index2] = item[index2] , item[index1]
	return nextSamples




def main():
	print("Travelling Salesman Problem Using Genetic Algorithm: ")
	n = 10								
	final_path= []
	final_cost = 0
	final_path, final_cost = local_genetic_search(n, cities())
	print ("The Path taken by Travelling Salesperson:", final_path)
	print ("\n Shortest Distance:",str(int(final_cost*10)) +"miles")

main()