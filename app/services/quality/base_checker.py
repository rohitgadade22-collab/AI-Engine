class BaseChecker:

	def name(self):
		raise NotImplementedError("Checker must implement `name()`")

	def check(self, face_image, face_data):
		raise NotImplementedError("Checker must implement `check(face_image, face_data)`")
