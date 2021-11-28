from agent import Agent
from container import Container
from random import randint, choice, sample
import numpy as np
import matplotlib.pyplot as plt
from time import time

def main(name, conf, gestesB, nbr_vacc):
	# Initialisation

	w, h = 5000, 5000
	container = Container(w, h)

	confinement = conf
	gestesBarrieres = gestesB
	container.agents = [Agent(i, randint(10, w-10), randint(10, h-10), randint(-20, 20) // confinement, randint(-20, 20) // confinement, 0.035/gestesBarrieres) for i in range(1000)]

	patient0 = choice(container.agents)

	container.healthys = [*container.agents]

	patient0.get_infected(0, container)
	i = 0

	# t = int(input("Nombre de tours : "))
	t = 1825

	infected_history = [None] * t
	healthy_history = [None] * t
	vaccinated_history = [None] * t
	immune_history = [None] * t


	while i < t:
		nbr_v = nbr_vacc
		tours = 0
		# print("{}/{}".format(i, t), end="    \r")

		infected_history[i] = len(container.infecteds)/5
		healthy_history[i] = len(container.healthys)/5
		vaccinated_history[i] = len(container.vaccinateds)/5
		immune_history[i] = len(container.immunes)/5

		for agent in container.agents:	
			tours += 1
			agent.move(container)

			if agent.infected:
				tours += agent.infect_neighbours(container, i)
				agent.check_for_getting_healthy(i, container)

			if agent.immune:
				agent.remove_immunity(container, i)

			if agent.vaccinate:
				agent.remove_vaccination(container, i)
		
		
		l = list(filter(lambda a: not a.vaccinate and not a.dejaetevaccine , container.healthys))

		if len(l) < nbr_v:
			nbr_v = len(l)

		container.vaccine_people(sample(l, nbr_v), i)

		i += 1

		# print("time: {}, infecteds: {}, healthys: {}, len(l): {} nbr_v/j: {}, vaccinates: {}, tours: {}".format(i, len(container.infecteds), len(container.healthys), len(l), nbr_v, len(container.vaccinateds),tours), end="                                              \r")

	sainsmoinsimmunes = []


	for i in range(len(healthy_history)):
		sainsmoinsimmunes.append(healthy_history[i] - immune_history[i])

	# print(sum(infected_history))

	temps = np.arange(0, t, 1)
	plt.plot(temps, infected_history, label="infected", color="red", linewidth=2, markerfacecolor="red", markeredgecolor="red")
	plt.plot(temps, vaccinated_history, label="vaccinated", color="green", linewidth=2, markerfacecolor="green", markeredgecolor="green")
	plt.plot(temps, sainsmoinsimmunes, label="healthy - immunes", color="blue", linewidth=2, markerfacecolor="blue", markeredgecolor="blue")
	plt.plot(temps, immune_history, label="immune", color="yellow", linewidth=2, markerfacecolor="yellow", markeredgecolor="yellow")
	plt.title(name)
	plt.legend()
	plt.xlabel("Time")
	plt.ylabel("Number of agents")
	# plt.show()
	plt.savefig("./Courbes/1000_agents_1_contaminé_5_ans/{}.png".format(name))
	plt.close()

if __name__ == "__main__":
	
	names = ["Natural_immunity_only", "Light_confinement", "Partial_confinement", "Strict_confinement", "Basics_barrier_gestures", "Mediums_barrier_gestures", "Heavys_barrier_gestures", "Vaccin01", "Vaccin03", "Vaccin04", "Vaccin05"]
	# names = ["Vaccin01_repeat", "Vaccin03_repeat", "Vaccin04_repeat", "Vaccin05_repeat"]
	# names = ["Vaccin01", "Vaccin03", "Vaccin04", "Vaccin05"]
	# names = ["Light_confinement", "Partial_confinement", "Strict_confinement"]

	confinement = 1
	gestesBarrieres = 1
	nbr_vacc = 0

	# start time count
	start = time()

	for name in names:
		print(name)

		if name == "Light_confinement":
			confinement = 2
			gestesBarrieres = 1
			nbr_vacc = 0

		elif name == "Partial_confinement":
			confinement = 3
			gestesBarrieres = 1
			nbr_vacc = 0

		elif name == "Strict_confinement":
			confinement = 5
			gestesBarrieres = 1
			nbr_vacc = 0

		elif name == "Basics_barrier_gestures":
			confinement = 1
			gestesBarrieres = 2
			nbr_vacc = 0

		elif name == "Mediums_barrier_gestures":
			confinement = 1
			gestesBarrieres = 3
			nbr_vacc = 0
		
		elif name == "Heavys_barrier_gestures":
			confinement = 1
			gestesBarrieres = 5
			nbr_vacc = 0
		
		elif name == "Vaccin01":
			confinement = 1
			gestesBarrieres = 1
			nbr_vacc = 1
		
		elif name == "Vaccin03":
			confinement = 1
			gestesBarrieres = 1
			nbr_vacc = 3

		elif name == "Vaccin04":
			confinement = 1
			gestesBarrieres = 1
			nbr_vacc = 4

		elif name == "Vaccin05":
			confinement = 1
			gestesBarrieres = 1
			nbr_vacc = 5

		elif name == "Vaccin01_repeat":
			confinement = 1
			gestesBarrieres = 1
			nbr_vacc = 1
		
		elif name == "Vaccin03_repeat":
			confinement = 1
			gestesBarrieres = 1
			nbr_vacc = 3
		
		elif name == "Vaccin04_repeat":
			confinement = 1
			gestesBarrieres = 1
			nbr_vacc = 4
		
		elif name == "Vaccin05_repeat":
			confinement = 1
			gestesBarrieres = 1
			nbr_vacc = 5

		for j in range(5):
			main(name, confinement, gestesBarrieres, nbr_vacc)

	# end time count
	end = time()
	print("\nExecution time: {}".format(end - start))