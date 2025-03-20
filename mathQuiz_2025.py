# mathQuiz_ version 2.0
import random
import operator #  operator module for using various operations in our quiz
from decimal import *
ops={'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}  #define operators dictionary with key:value


def main():
	print ("Mad Minutes Quiz. Bienvenue.")
	print ("***** \nAnswer non-integer answers to 1 decimal place. \nTo end the quiz, type 'end'.\n*****\n")
	name=input('Our examinee today is: ')
	min, max=quiz_range()
	score, total_q=quiz(min, max, name)
	print ("End of Quiz.")
	print (f"{name}'s Grade: {score}/{total_q}")


def quiz_range():
	print("Input the range of numbers you would like to be quizzed on.")
	while True: #   'while True' loop allows a block of code to be repeated indefinitely--> if exception, run loop again
		try:
			min=int(input('Smallest number: '))
			max=int(input("Largest number: "))
			assert((min+1)<max) # if assert() ==False, throws error --> except block
			# min+1 bc quiz uses range min:max-1
			print ("Let's begin.")
			# else:
			# 	print("Please enter your range values in the order they appear.")
			# 	continue #run loop again
		except: #if you dont specify error type, will run except no matter what error 
			print ("Please try again. Enter your range as whole numbers that are at least 2 digits apart.")
			continue #return to start of loop
		else:
			break # once try block runs without error, can exit the loop
	return min, max


def quiz(min, max, name):
	score = 0 
	total_q=0
	while True: #   infinite loop
		try:
			r1=random.randint(min+1, max)
			r2=random.randint(min, (r1-1)) #r2 always smaller bc dont want zeroerror in division 
		except: #in case any issues with r2 selection due to r1 being too  
			continue
		opr=random.choice(list(ops.keys())) 
		#    ops.keys() alone includes output 'dict_keys' which causes errors, therefore must use list()
		ans=Decimal(ops[opr](r1, r2))
		ans= float(ans.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP))
		# we are NOT going to use round() bc it rounds unpredictably bc of how floats are stored; @ https://stackoverflow.com/questions/34620633/how-does-rounding-in-python-work
		# instead try Decimal(), instruct it to round up
		# but this also sometimes doesnt compare correctly to ans ?? amybe another storage artefact
		# so we'll convert it to float again
		quest=input(f'{r1}{opr}{r2}= ') #use f-string to embed {variables} into a string #was going to use int() directly in quest but will cause error if not a numerical input...
		#  making list for wrong answer responses to be randomly chosen from random.choice(list)
		try: #lines that could produce error are anything checking the input value
			if quest=='end':
				break
			total_q += 1 #dont want to count 'end' question, so this after 
			if ans==float(quest): #cant put int() inside quest= in case they want to 'end' quiz.
				print("...correct.")
				score += 1
			else:
				wrong = ["Uh oh. Try again.", "Not according to this dimension's mathematics.", f"Hmm, that's not {ans}.", f"Um, it's actually {ans}...", "Would you like to phone a friend?", "Monkey see, monkey cannot do.", f"Time for {name}'s nap."]
				print(random.choice(wrong))
		except ValueError:#non numerical answer input will cause ValeuError
			print("This is not imaginary math. Numbers only, please.")
			continue
	return score, total_q


main()