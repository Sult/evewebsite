# All static tables for eve site
# TODO make it importable from eve-ap instead of .csv 

from django.db import models
import datetime

#Basic blueprint infomartion
class Blueprint(models.Model):
	"""
	Basic information about blueprints. This will be automaticly imported by .csv or eve-api 
	
	#Create a Blueprint
	Automated fields:
		eve_blueprint_id = the eve-api id of the blueprint
		name = Blueprint name without blueprnt at end
		group = blueprint group (without blueprint at the end)
		production_time* = standard time to manufacture in seconds
		* = optional field (for now)
	"""

	#Automated input:
	eve_blueprint_id = models.IntegerField(
		verbose_name = 'Blueprint ID'
		)
	
	name = models.CharField(
		max_length = 128,
		verbose_name = 'Name'
		)
		
	group = models.CharField(
		max_length = 128,
		verbose_name = 'Group'
		)
	
	# imported from eve api
	production_time = models.IntegerField(
		blank = True,
		verbose_name = 'Production Time'
		)										#blank is true will be removed after api works

	def __unicode__(self):
		return self.name

# the different subscriptiontypes
class Subscription(models.Model):
	"""
	the different subscriptiontypes and their price, custom subscriptions can always be added
	
	# Create Subscription 
	Admin fields:
		name = name of the subscription (handy for special offers)
		max_blueprints = maximum quantity of blueprints in shop
		months = length of subscription
		price = Isk cost of the subscription
		description = desription of the subscription
	"""
	name = models.CharField(
		max_length = 64,
		verbose_name = 'Subscription name'
		)
		
	max_blueprints = models.IntegerField(
		verbose_name = 'Maximum blueprints'
		)
		
	months = models.IntegerField(
		default = 1,
		verbose_name = 'Months'
		)
	
	price = models.IntegerField(
		verbose_name = 'Price'
		)
	
	description = models.TextField(
		max_length = 1024,
		verbose_name = 'Description'
		)
	
	def __unicode__(self):
		return self.name
