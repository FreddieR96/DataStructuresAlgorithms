import random

class Developer:


	def __init__(self, name, years_experience, frontend_skill, backend_skill):
		self.name = name
		self.years_experience = years_experience
		self.frontend_skill = frontend_skill
		self.backend_skill = backend_skill

	def __lt__(self, other):
		if other.years_experience > self.years_experience:
			return True
		elif other.years_experience < self.years_experience:
			return False
		elif other.backend_skill > self.backend_skill:
			return True
		elif other.backend_skill < self.backend_skill:
			return False
		elif other.frontend_skill > self.frontend_skill:
			return True
		elif other.frontend_skill < self.frontend_skill:
			return False
		elif self.name > other.name:
			return True
		elif self.name < other.name:
			return False
		else:
			return False

	def __gt__(self, other):
		if self.years_experience > other.years_experience:
			return True
		elif self.years_experience < other.years_experience:
			return False
		elif self.backend_skill > other.backend_skill:
			return True
		elif self.backend_skill < other.backend_skill:
			return False
		elif self.frontend_skill > other.frontend_skill:
			return True
		elif self.frontend_skill < other.frontend_skill:
			return False
		elif self.name < other.name:
			return True
		elif self.name > other.name:
			return False
		else:
			return False


	def __str__(self):
		years = str(self.years_experience)
		return self.name + " has "  + years + " years of experience"
            
	@classmethod
	def createDevs(cls, number):
		if number > 50:
			print("Number can't be higher than 50")
			return
		a = open("developers_list.txt", 'r')
		b = a.read()
		names = b.split(",")
		devs = []
		c = 0
		while c < number:
			name = names[c].capitalize()
			d = random.uniform(0.0, 20.0)
			years_experience = float(format(d, '.1f'))
			e = random.uniform(0.0, 20.0)
			frontend_skill = float(format(e, '.1f'))
			f = random.uniform(0.0, 20.0)
			backend_skill = float(format(f, '.1f'))
			dev = Developer(name, years_experience, frontend_skill, backend_skill)
			devs.append(dev)
			c += 1
		return devs
			
