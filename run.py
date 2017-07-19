from markov_python.cc_markov import MarkovChain
from get_data import get_data

def menu():
	print "Welcome to the ASOIAF Markov Chain Generator, what would you like to do?"
	print "1. Compile new Source Data"
	print "2. Produce new Markov Chain text"
	print "3. Exit"
	choice = int(raw_input("Please enter your choice: "))

	if choice == 1:
		get_data()
		menu()
	elif choice == 2:
		mc = MarkovChain()
		mc.add_file('text.txt')
		text = mc.generate_text(40)
		string = ''
		for i in text:
			string += i + ' '

		print string + '\n'
		menu()
	elif choice == 3:
		return
	else:
		print "That's not valid input, bro"
		menu()

menu()
