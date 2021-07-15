class DuplicateOid(Exception):
	
	def __init__(self, oid, message="Object ID already exists"): 
		self.oid = oid
		self.message = message
		super().__init__(self.message)


class DuplicateEmail(Exception):

	def __init__(self, email, message="Email is already tied to a member"):
		self.email = email
		self.message = message
		super().__init__(self.message)
