import os
from flask import Flask, request, jsonify
from flask_cors import CORS

Base_file = "base.txt"
history = "History.txt"
Base = {}
absolute_address = 988
Error_text = "Ожидался иной ответ. Попробуйте использовать команду заново."


def create_the_Base(w1, w2, w3 = True):
	if w3:
		with open(Base_file, "a") as file:
			file.write(f"\n{w1} {w2}")
		
	with open(Base_file) as file:
		for line in file:
			arr = line.split()
			Base[int(arr[0])] = int(arr[1])

def change_the_Base(w1, w2):
	w = ''
	with open (Base_file,'r') as f:
		file= f.read().split('\n')
		for i in file:
			o = i.split()
			if o[0] == str(w1):
				w = w + f'{o[0]} {int(o[1]) + int(w2)}'
			elif o[0] != str(w1):
				w = w + f'{o[0]} {o[1]}'
			if file.index(i) != len(file)-1: 
				w = w + '\n'
	with open (Base_file,'w') as f:
		f.write(w)

def zashchecoins_of_user(w1):
	if check_user(w1):
		with open (Base_file, 'r') as f:
			file = f.read().split('\n')
			for i in file:
				o = i.split()
				if o[0] == str(w1):
					return int(o[1])
			raise Exception('Жопа, блять')

def check_user(w1):
	with open (Base_file, 'r') as f:
		file = f.read().split('\n')
		for i in file:
			o = i.split()
			if o[0] == str(w1):
				return True
		return False
		
app = Flask(__name__)
CORS(app)

@app.route('/send-data', methods=['POST'])
def receive_data():
	data = request.json  # Получаем JSON-данные из запроса
	print(f"Получены данные: {data}")
	if "data_get" in data:
		user_id = data.split("=")[1]
		return jsonify({"type": "coins", "coins": zashchecoins_of_user(user_id)})
	
	if "+coin" in data:
		w = ''
		user_id = data.split("=")[1]
		with open (Base_file,'r') as f:
			file= f.read().split('\n')
			for i in file:
				o = i.split()
				if o[0] == str(user_id):
					w = w + f'{o[0]} {int(o[1]) + int(1)}'
				elif o[0] != str(user_id):
					w = w + f'{o[0]} {o[1]}'
				if file.index(i) != len(file)-1: 
					w = w + '\n'
		with open (Base_file,'w') as f:
			f.write(w)
		return jsonify({"type": "coins", "coins": zashchecoins_of_user(user_id)})

# Запуск сервера
if __name__ == '__main__':
	app.run(debug=True, port=10000)
