import random


app_leituras = ['auth','admin','authtoken','contenttypes','site','django']
app_escritas = ['submissaoacad',]
auth_db = 'db_passo'
pltaforma_db = 'default'

class AuthRouter:
	"""
	A router to control all database operations on models in the
	auth and contenttypes applications.
	"""
	route_app_labels = app_leituras
	route_app_escrita = app_escritas

	def db_for_read(self, model, **hints):
		"""
		Attempts to read auth and contenttypes models go to auth_db.
		"""
		if model._meta.app_label in self.route_app_labels:
			return auth_db
		return None

	def db_for_write(self, model, **hints):
		"""
		Attempts to write auth and contenttypes models go to auth_db.
		"""
		if model._meta.app_label in self.route_app_labels:
			return auth_db
		return None

	def allow_relation(self, obj1, obj2, **hints):
		"""
		Allow relations if a model in the auth or contenttypes apps is
		involved.
		"""
		if (
			obj1._meta.app_label in self.route_app_labels or
			obj2._meta.app_label in self.route_app_labels
		):
		   return True
		return None

	def allow_migrate(self, db, app_label, model_name=None, **hints):
		"""
		Make sure the auth and contenttypes apps only appear in the
		'auth_db' database.
		"""
		# print("allow_migrate AuthRouter ", self, db, app_label, model_name)
		if app_label in self.route_app_labels:			
			# print("ENETROU  allow_migrate", self, db, app_label, model_name)
			return db == auth_db
		if app_label in self.route_app_escrita:			
			print("ENTROU  allow_migrate: ", self, db, pltaforma_db, app_label, model_name)
			return db == pltaforma_db
			print("aolá")
		return None

class ApplicationRouter:
	def db_for_read(self, model, **hints):
		return 'default'

	def db_for_write(self, model, **hints):
		return 'default'

	def allow_relation(self, obj1, obj2, **hints):
		if obj1._state.db == 'default' and obj2._state.db == 'default':
			return True
		return False

	def allow_migrate(self, db, app_label, model_name=None, **hints):
		return True
