

# https://stackoverflow.com/questions/58866132/django-multiple-databases-connections
#if model._meta.app_label in ['auth', 'django', 'sessions', 'admin']:
import random


app_leituras = ['auth','admin','contenttypes','site','django', 'cadastrorh', 'academicocad','permissoes']
app_escritas = ['eventos',]
auth_db = 'db_passo'
pltaforma_db = 'db_plataforma'

class AuthRouter:
	"""
	A router to control all database operations on models in the
	auth and contenttypes applications.
	"""
	route_app_labels = app_leituras

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
		print("allow_migrate AuthRouter ", self, db, app_label, model_name)
		if app_label in self.route_app_labels:			
			print("ENETROU  allow_migrate AuthRouter", self, db, app_label, model_name)
			return db == auth_db
		return None

class PrimaryReplicaRouter:
	def db_for_read(self, model, **hints):
		"""
		Reads go to a randomly-chosen replica.
		"""
		return pltaforma_db

	def db_for_write(self, model, **hints):
		"""
		Writes always go to primary.
		"""
		return pltaforma_db

	def allow_relation(self, obj1, obj2, **hints):
		"""
		Relations between objects are allowed if both objects are
		in the primary/replica pool.
		"""
		raise Exception("1")
		db_set = {'db_plataforma'}
		if obj1._state.db in db_set and obj2._state.db in db_set:
			return True
		return None

	def allow_migrate(self, db, app_label, model_name=None, **hints):
		"""
		All non-auth models end up in this pool.
		"""
		print("allow_migrate PrimaryReplicaRouter ", self, db, app_label, model_name)
		return True


'''
class AuthRouter:
	def db_for_read(self, model, **hints):
		if model._meta.app_label in app_leituras:
			return 'db_passo'
		return None

	def db_for_write(self, model, **hints):
		if model._meta.app_label in app_leituras:
			return 'db_passo'
		return None

	def allow_relation(self, obj1, obj2, **hints):
		return True

	def allow_migrate(self, db, app_label, model_name=None, **hints):
		if app_label in app_leituras:
			return False
		return True
'''
class ApplicationRouter:
	def db_for_read(self, model, **hints):
		return 'db_plataforma'

	def db_for_write(self, model, **hints):
		return 'db_plataforma'

	def allow_relation(self, obj1, obj2, **hints):
		if obj1._state.db == 'db_plataforma' and obj2._state.db == 'db_plataforma':
			return True
		return False

	def allow_migrate(self, db, app_label, model_name=None, **hints):
		return True