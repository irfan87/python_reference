# TODO: develop a simple greetings application where user can key in their first name and last name and print it with the greetings
print("Enter 'q' to exit")

while True:
	user_first_name_input = input("Please enter your first name: ")

	if user_first_name_input == 'q':
		print("Until we meet again")
		break

	user_first_name = str(user_first_name_input)

	user_last_name_input = input("Please enter your last name: ")

	if user_last_name_input == 'q':
		print("Until we meet again")
		break

	user_last_name = str(user_last_name_input)

	user_fullname = str.join(" ", (user_first_name, user_last_name))
	
	print(f"Hey, {user_fullname.title()}")

	prompt_message = input("Do you want to continue? (Y/n): ")

	prompt_message_array = ["no", "No", "n"]

	if prompt_message in prompt_message_array:
		print(f"Bye, {user_fullname.title()}. 'Till next time.")
		break