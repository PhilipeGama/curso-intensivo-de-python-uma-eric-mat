def descrive_pet(animal_type, pet_name):
	"""Exibe informações sobre um animal de estimação."""
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

descrive_pet(animal_type="hamster",pet_name="harry")
descrive_pet(pet_name="harry",animal_type="hamster")
