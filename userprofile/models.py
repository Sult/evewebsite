# The extra information that is not included in User creation. Later I want to eddit the User class

#TODO: Function to send mail to admin/moderator for validation (build-in in user model already?)

from django.db import models
from django.contrib.auth.models import User
from static.models import Subscription


import datetime

# extra user informatie
class UserProfile(models.Model):
	"""
	Add a userprofile to a normal user, this profile contains the ingame information of the user.
	After creation after creation a mail needs to be send to a moderator/admin for validation
	
	# Create a userprofile
	Relations:
		user_id = "User" foreignkey
	Automated fields:
		creation_date = date of creation
	User input fields:
		ingame_name = ingame name
		corporation* = corporation the character works for
		description* = description about yourself or character
		
		* = optional field
	"""
	
	#Relations
	user_id = models.ForeignKey(
		User,
		verbose_name = 'User'
		)

	creation_date = models.DateTimeField(
		auto_now_add = True,
		editable = False,
		verbose_name = 'Creation date'
		)

	# User input
	# After creation send mail to admin/moderator for validation
	ingame_name = models.CharField(
		unique = True,
		max_length = 128,
		verbose_name ='Ingame name'
		)
		
	corporation = models.CharField(
		blank=True,
		max_length = 128,
		verbose_name = 'Corporation'
		)
		
	description = models.TextField(
		blank = True,
		max_length = 1024,
		verbose_name = 'Description'
		)

	def __unicode__(self):
		return self.ingame_name
		
		
class UserProfileDate(models.Model):
	"""
	UserProfile modification dates
	
	# Create a UserProfileDate
	Relations:
		userprofile_id = "UserProfile" foreignkey
	Automatic fields:
		date_modified = date and time of modifications to UserProfile
	"""
	
	userprofile_id = models.ForeignKey(
		UserProfile,
		verbose_name = 'userprofile_modfied_date'
		)
		
	date_modified = models.DateTimeField(
		auto_now_add = True,
		editable = False,
		verbose_name = 'Modification date'
		)
	
	def __unicode__(self):
		return self.userprofile__ingame_name

# keeping track of user permissions
class UserControl(models.Model):
	"""
	Admin options for a user like validating, banning and more
	
	#create AdminUserProfile
	Relations:
		userprofile_id = "UserProfile" foreignkey
	Admin Fields:
	(All defaults are False or empty)
		validated = True when userprofile has been validated
		validated_by = adds username that set validated to True
		clerk = True when user is aloud to set up shop
		banned = is the user banned?
		ban_reason = reason for ban
	"""
	
	# Relations:
	userprofile_id = models.OneToOneField(
		UserProfile,
		unique = True,
		verbose_name = 'User'
		)
	
	# Admin Fields
	validated = models.BooleanField(
		default = False,
		verbose_name ='Validated'
		)
		
	validated_by = models.ForeignKey(UserProfile,
		blank = True,
		related_name = 'validated_by',
		verbose_name = 'Validated By'
		)
		
	clerk = models.BooleanField(
		default = False,
		verbose_name = 'Clerk'
		)
	
	banned = models.BooleanField(
		default = False,
		verbose_name = 'Banned'
		)
	
	ban_reason = models.CharField(
		blank = True,
		max_length = 256,
		verbose_name = 'Ban reason'
		)
	
	def __unicode__(self):
		return self.userprofile__ingame_name
		
class UserControlDate(models.Model):
	"""
	UserControl modification dates and by who
	
	#Create UserControlDate
	Relations:
		usercontrol_id = "UserControl" foreignkey
		modified_by = person who changed something in "UserControl"
	Automated fields:
		date_modified = date and time of modifications to UserControl
		note = small reason why and what has been changed
	"""
	
	# Automated fields:	
	userprofile_id = models.ForeignKey(
		UserProfile,
		related_name = 'usercontrole_modified_date',
		verbose_name = 'User'
		)
		
	modified_by = models.ForeignKey(
		UserProfile,
		related_name = 'usercontrol_modified_by',
		verbose_name = 'Modified by'
		)
	
	date_modified = models.DateTimeField(
		auto_now_add = True,
		editable = False,
		verbose_name = 'Modification date'
		)
	
	# Admin input:
	note = models.TextField(
		verbose_name = 'Note'
		)
	
	def __unicode__(self):
		return self.modified_by__ingame_name
	
# User subscriptions and their dates		
class UserSubscription(models.Model):
	"""
	Manages the user subscriptionas, only for users who have the "UserControl.clerk" set on True
	
	# Create UserSubscription
	Relations: 
		userprofile_id = "UserProfile" foreignkey
		subscription_id = "Subscription" foreignkey from static model
	Automated field:
		starting_date = first date (ever) that user took a subscription
		started_by = user who added his subscription
	"""
	# Automated fields:
	userprofile_id = models.ForeignKey(
		UserControl,
		related_name = 'usersubscription_modified_date',
		verbose_name = 'User'
		)
		
	starting_date = models.DateTimeField(
		auto_now_add = True,
		editable = False,
		verbose_name = 'Starting date'
		)
	
	# Admin input:
	subscription_id = models.ForeignKey(
		Subscription,
		verbose_name = 'Subscription'
		)
	
	end_date = models.DateTimeField(
		auto_now_add = True,
		editable = False,
		verbose_name = 'End subscription'
		)
		
	def __unicode__(self):
		return self.UserSubscription__name
		

class UserSubscriptionDate(models.Model):
	"""
	UserSubsciptions modification dates and by who
	
	Relation:
		usersubscription_id = "UserSubscription" foreign key
	Automated fields:
		date_modified = date that UserSubscription has been modified
		modified_by = user that modified the UserSubscription
		note = note about what and why it has been modified
	"""
	
	
	usersubscription_id = models.ForeignKey(
		UserControl,
		verbose_name = 'User'
		)
	
	modified_by = models.ForeignKey(
		UserProfile,
		related_name = 'usersubscription_modified_by',
		verbose_name = 'Modified by'
		)
	
	date_modified = models.DateTimeField(
		auto_now_add = True,
		editable = False,
		verbose_name = 'Modification date'
		)
	
	# Admin input:
	note = models.TextField(
		verbose_name = 'Note'
		)

	def __unicode__(self):
		return self.modified_by__ingame_name
