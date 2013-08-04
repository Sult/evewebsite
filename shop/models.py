# Inforation about a shop, its produtcs prices and more

#TODO ClerkShop - description: bb or html code should be useable
#TODO ClerkShop - location: Should be autocomplete of eve online systems (use apior static table)

from django.db import models
from userprofile.models import UserProfile
from static.models import Blueprint

import datetime


# Top table that contians all subs
class Shop(models.Model):
	"""
	Basic shop information such as a name and description.
	
	#Create a shop
	Automated fields:
		creation_date = date of creation
		modified = date of last modification
	
	User input fields:
		clerk = the shop owner
		shop_name = name of the shop
		location  = system of operation
		description* = shop description
		api_id* = eve online api-id (only for 1 character)
		api_key* = eve online api-key (only for 1 character)
		
		* = optional field
	"""
	
	# Relations
	userprofile_id = models.ForeignKey(
		UserProfile,
		verbose_name = 'User Profile'
		)
	
	# User input:
	shop_name = models.CharField(
		max_length = 128,
		verbose_name = 'Shop name'
		)
	
	location = models.CharField(
		max_length = 256,
		verbose_name = 'Location'
		)									# Gets linked to a system from the eve database	
	
	description = models.TextField(
		blank = True,
		max_length = 1024, 
		verbose_name = 'Shop description'
		)
	
	production_lines = models.IntegerField(
		default = 1,
		verbose_name = 'Production lines'
		)									# auto fill in from eve-api 
		
	research_lines = models.IntegerField(
		default = 1,
		verbose_name = 'Research lines'
		)									# auto fill in from eve-api 
		
	api_id = models.IntegerField(
		blank = True,
		verbose_name = 'Api ID'
		)
	
	api_key = models.CharField(
		blank=True,
		max_length = 64,
		verbose_name = 'Api key'
		)									# Minimum lenght is also 64 characters
		
		
		
	def __unicode__(self):
		return self.clerk__ingame_name
			



# Product information about shop items
class Product(models.Model):
	"""
	personal information about blueprint and price
	
	#Blueprint information
	User input:
		material_efficiency = researched material level on blueprint
		production_efficiency = researched production level on blueprint
		bp_type = Original(True) or Copy (False)
		runs = remaining runs (leave Null if bp_type = True
		
	"""
	
	# Relations
	shop_id = models.ForeignKey(
		Shop,
		verbose_name = 'Shop'
		)
		
	blueprint_id = models.ForeignKey(
		Blueprint,
		verbose_name = 'Blueprint'
		)
	
	# User input:
	material_efficiency = models.IntegerField(
		default = 0,
		verbose_name = 'Material efficiency'
		)
		
	production_efficiency = models.IntegerField(
		default = 0,
		verbose_name = 'Material efficiency'
		)

	bp_type = models.BooleanField(
		verbose_name = 'Blueprint type'
		)
	
	
