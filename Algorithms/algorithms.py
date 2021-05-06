import math

class Algorithms:

	def selection_sort(self, arrray):
		i = 0
		while i < len(arrray):
			smallest_value = i
			j = i
			while j < len(arrray):
				if arrray[j] < arrray[smallest_value]:
					smallest_value = j
				j += 1
			self.swap(arrray, i, smallest_value)
			i += 1

	def quick_sort(self, arrray, first = 0, last = 0):
		if arrray and not last: last = len(arrray) - 1
		pivot = arrray[last]
		biggerNumbers = []
		boundary = first
		counter = first
		while boundary < last:
			if arrray[boundary] < pivot:
				self.swap(arrray, counter, boundary)
				counter += 1
			boundary += 1
		self.swap(arrray, counter, last)
		
		if counter - first > 1:
			self.quick_sort(arrray, first, counter - 1)
		if last - counter > 1:
			self.quick_sort(arrray, counter + 1, last)
		
	def merge_sort(self, arrray, first = 0, last = 0):
		if not last: last = len(arrray)-1
		if len(arrray)-1 > 0:
			midpoint = math.floor((first + last) / 2)
		if midpoint - first == 1 and arrray[first] > arrray[first + 1]:
			self.swap(arrray,first,midpoint)
		if last - midpoint == 2 and arrray[last - 1] > arrray[last]:
			self.swap(arrray,last,last-1)
		
		
		if midpoint - first > 1:
			self.merge_sort(arrray, first, midpoint)
		if last - midpoint > 2:
			self.merge_sort(arrray, midpoint+1, last)
		a = first
		b = midpoint + 1
		holdArray = []

		while b <= last:
			while arrray[b] > arrray[a] and a <= midpoint:
				holdArray.append(arrray[a])				
				a += 1
			holdArray.append(arrray[b])
			b += 1
		while a <= midpoint:
			holdArray.append(arrray[a])
			a += 1
		
		c = 0
		while first <= last:
			arrray[first] = holdArray[c]
			c += 1
			first += 1
		
			
	def swap(self, theList, first, second):
		temp = theList[second]
		theList[second] = theList[first]
		theList[first] = temp

	def find(self, arrray, item, first = 0, last = 0):
		print(item)
		if not last: last = len(arrray)-1
		midpoint = math.floor((first + last) / 2)
		print(midpoint)
		if arrray[midpoint] == item:
			print("first")
			
		elif arrray[midpoint] > item:
			print("second")
			self.find(arrray,item,first, midpoint)
		elif arrray[midpoint] < item:
			print("third")
			self.find(arrray,item,midpoint+1, last)