import csv
print('Ответьте на вопросы по английски для подбора игр')
gen = input('Какой жанр игры Вас интересует? ')
#print('На какой платформе предпочитаете играть?')
platform = input('На какой платформе предпочитаете играть? ')
#print('Одиночная или многопользоввтельска игра?')
types = input('Одиночная или многопользовательска игра? ')
status = True

if not gen and not platform  and not types:
	print('Перезапустите поиск и введите ответы')
	status = False
if not gen and not platform and not types:
	gen = platform
if gen  and not platform  and types :
	platform = gen
if gen and platform and not types :
	types = platform
if not gen and not platform and types :
	gen = types
	platform = types
if gen  and not platform and not types :
	platform = gen
	types = gen
if not gen == '' and platform and not types :
	gen = platform
	types = platform

def game_suggester (genre, platforms, ttypes):
	if status:
		with open ('steam.csv', encoding="utf-8", newline = '') as f:
			file = csv.reader(f)
			a = []
			for r in file:
				if (genre) and (platforms) and (ttypes) in r:
					a.append(r[1])
			a = list(dict.fromkeys(a))
		with open ('result.txt', 'w',) as res:
			for i in range (1,len(a)):
				res.write(str(a[i]) + '\n')

game_suggester(gen,platform,types)
