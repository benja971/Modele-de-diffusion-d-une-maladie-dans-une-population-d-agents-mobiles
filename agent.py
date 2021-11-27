from random import randint, random

class Agent():
	"""docstring for Agent."""
	def __init__(self,i, x, y, vx, vy, pdei):
		self.id = i
		self.x = x
		self.y = y
		self.vx = vx
		self.vy = vy
		self.radius = 10
		self.infected = False
		self.infection_time = 0
		self.infection_duration = randint(90, 150)
		self.infection_probability = pdei
		self.infection_radius = 100
		self.recovered = False
		self.dejaeu = False
		self.vaccinate = False
		self.last_infection_time = 0
		self.end_infection_time = 0
		self.end_immune_time = 0
		self.immune = False
		self.end_vaccination_time = 0
		self.dejaetevaccine = False

	def move(self, container):
		self.x += self.vx 
		self.y += self.vy 

		if self.x < 0:
			self.x = 0
			self.vx = -self.vx
		
		elif self.x > container.w:
			self.x = container.w
			self.vx = -self.vx
		
		elif self.y < 0:
			self.y = 0
			self.vy = -self.vy

		elif self.y > container.h:
			self.y = container.h
			self.vy = -self.vy

	
	def get_infected(self, time, container):
		self.infected = True
		self.infection_time = time
		self.last_infection_time = time
		self.end_infection_time = time + self.infection_duration

		container.healthys.remove(self)
		container.infecteds.append(self)


	def check_for_getting_healthy(self, time, container):
		if time - self.infection_time > self.infection_duration:
			self.infected = False	

			container.infecteds.remove(self)
			container.healthys.append(self)

			if not self.dejaeu:
				self.dejaeu = True
			
			self.infection_probability /= 0.9
			
			self.end_immune_time = self.end_infection_time + 200
			self.immune = True

			container.immunes.append(self)

			
	def distance(self, agent):
		return ((self.x - agent.x)**2 + (self.y - agent.y)**2)**0.5


	def infect_neighbours(self, container, time):
		suspects = list(filter(lambda a: a.id != self.id and not a.vaccinate and not a.immune and a.distance(self) < self.infection_radius, container.healthys))

		tours = 0
		for agent in suspects:
			tours += 1
			if random() < agent.infection_probability:
				agent.get_infected(time, container)

		return tours

	def get_vaccinated(self, vaccinateds, time):
		if not self.dejaetevaccine:
			self.vaccinate = True
			t =  randint(180, 240)
			self.end_vaccination_time = time + t
			self.dejaetevaccine = True
			vaccinateds.append(self)


	def remove_immunity(self, container, time):
		if self.immune and time > self.end_immune_time:
			self.immune = False
			container.immunes.remove(self)

	
	def remove_vaccination(self, container, time):
		if self.vaccinate and time > self.end_vaccination_time:
			self.vaccinate = False
			container.vaccinateds.remove(self)