import redis
from time import strftime
import os
from retry import retry

class Stats:
	def __init__(self):
		self.config = {}
	
	def render(self, key):
		variables = dict(
			date = strftime('%Y-%m-%d'),
			hour = strftime('%H'),
		)
		variables.update(self.config)
		for k,v in variables.items():
			key = key.replace('['+k+']',v)
		return key
