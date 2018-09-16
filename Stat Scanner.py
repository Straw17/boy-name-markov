#! usr/bin/python

numbers = '0123456789.'
letters = 'abcdefghijklmnopqrstuvwxyz'
page = open('C:\\Users\\Evan Conway\\Desktop\\Programming\\Python\\Algorithms\\Markov Chain\\Stats Raw.txt')
NamesAndValuesFile = open('C:\\Users\\Evan Conway\\Desktop\\Programming\\Python\\Algorithms\\Markov Chain\\Stats Raw.txt')
text = page.read().lower()
text = text.split('\n')
NamesAndValues = ''

for line in range(len(text)):
	if (line + 5) % 5 != 0:
		continue
	else:
		name = ''
		value = ''
		for character in range(len(text[line])):
			if text[line][character] in numbers:
				value += text[line][character]
			if text[line][character] in letters:
				name += text[line][character]
		#inefficient but speed doen't matter for this
		value = value[::-1]
		decimals = value[0:2]
		decimals = decimals[::-1]
		value = value[::-1]
		value = value[:-2] + '.' + decimals
		NamesAndValues += (name + ':' + str(int(round(float(value)))) + '\n')
print(NamesAndValues)