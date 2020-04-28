#!/usr/bin/python3
import requests
import re
def send_text(numbers, api_key):
	person = input('The person you want to text: ')
	message = input('The message you want to send: ')
	resp = requests.post('https://textbelt.com/text', {
		'phone': numbers[person].lower(),
		'message': message,
		'key': api_key,
		})
	print(resp.json())	
	return

def add_person(numbers_db, numbers_dict):
	person = input('The name of the person: ')
	number = input('The person\'s number: ')
	numbers_dict[re.sub('[\n]', '', person).lower()] = re.sub('[\n]', '', number)
	
	with open(numbers_db, 'a') as db:
		db.write('++++++++++++++++++++\n')
		db.write(person + '\n')
		db.write(number + '\n')
	
	return 

def main():
	api_key = ''
	api_site = 'https://textbelt.com/text/'
	numbers_db = 'fone_nums'
	numbers_dict = {}
	
	with open(numbers_db, 'r') as f:
		while f.readline():
			person = f.readline()
			number = f.readline()
			numbers_dict[re.sub('[\n]', '', person).lower()] = re.sub('[\n]', '', number)
	
	print(numbers_dict)
	loop = True	
	while loop == True:
		command = input('TEXT: ').lower()
		
		if command == 'text':
			send_text(numbers_dict, api_key)
			
		elif command == 'add':
			add_person(numbers_db, numbers_dict)
		
		elif command == 'print':
			print(numbers_dict)
		
		elif command == 'quit' or command == 'q':
			loop = False
		
		else:
			print("the only valid commands are text and add or quiti etc, just look at the source code")

if __name__ == '__main__':
	main()
