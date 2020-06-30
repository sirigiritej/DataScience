# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 19:35:27 2020

@author: Teja
"""

class BoardPosition:
	def __init__(self):
		self.sequence = None
		self.score = None
		self.survival = None
	def setSequence(self, val):
		self.sequence = val
	def setScore(self, score):
		self.score = score
	def setSurvival(self, val):
		self.survival = val