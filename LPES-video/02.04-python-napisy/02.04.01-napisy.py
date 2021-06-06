# Copyright (c) 2020-2021 Matematyka dla Ciekawych Świata (http://ciekawi.icm.edu.pl/)
# Copyright (c) 2020-2021 Robert Ryszard Paciorek <rrp@opcode.eu.org>
# 
# MIT License
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

code_napisy_A = r"""
a = 'to jest napis'
b = "to także"
c = '''a ten
jest wieloliniowy'''
"""

code_napisy_B = code_napisy_A + r"""
napis = 'abcdefgh'

print(napis[0], napis[1])
print(napis[-1], napis[-2])
"""

code_napisy_C = r"""
napis = 'abcdefgh'

print (len(napis))
"""

code_napisy_D = r"""
napis = 'abcdefgh'

print (napis[1:4])
"""

code_napisy_E = r"""
napis = 'abcdefgh'

print (napis[1:4:2])
"""

code_napisy_F = r"""
napis = 'abcdefgh'

print (napis[3::2])
print (napis[3:])
print (napis[:3])
print (napis[::-1])
"""

code_napisy_G = r"""
napis = 'abcdef'
print (napis[::-1][::3], napis[::3][::-1], napis[::-3])

napis = 'abcdef'
print (napis[::-1][::3], napis[::3][::-1], napis[::-3])
"""

try: clipData
except NameError: clipData = []

clipData += [
	{ 'title': [ "#02.4", "Python:", "napisy", "(i liczby)" ] },
	
	{ 'comment': 'napisy' },
	{ #  print(napis[0], napis[-1], ...)   print (len(napis))
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_napisy_A, "py")],
			["znaki", eduMovie.clear + eduMovie.code2console(code_napisy_B, "py")],
			["len", eduMovie.clear + eduMovie.code2console(code_napisy_C, "py")],
		],
		'consoleDown': [
			[0.0, ""],
			["znaki", eduMovie.runCode(code_napisy_B, [], cmd="python3")],
			["len", eduMovie.runCode(code_napisy_C, [], cmd="python3")],
		],
		'text' : [
			'Wspomnieliśmy już bardzo krótko <m> o napisach, czyli ciągach znaków. <mark name="znaki" />'
			'Możemy odwoływać się do poszczególnych elementów <m> napisu z użyciem nawiasów kwadratowych. <m>'
			'Indeksowanie jest od zera, <m> czyli pierwszy znak w napisie ma indeks zero. <m>'
			'Możemy też podawać indeksy ujemne, <m> które adresują napis od tyłu. <m>'
			'Minus jeden oznacza ostatni znak,  <m>minus dwa przedostatni i tak dalej. <m>'
			'Jeżeli wyjdziemy poza zakres związany <m> z długością danego napisu Python zgłosi błąd. <mark name="len" />'
			'Długość napisu możemy uzyskać wywołując na napisie funkcję len. <m>'
		]
	},
	{ #  print (napis[1:4])
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_napisy_D, "py")],
			["trzy", eduMovie.clear + eduMovie.code2console(code_napisy_E, "py")]
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(code_napisy_D, [], cmd="python3")],
			["trzy", eduMovie.runCode(code_napisy_E, [], cmd="python3")],
		],
		'text' : [
			"Operator pobrania fragmentu napisu, <m> którym jest nawias kwadratowy <m> nie ogranicza się w Pythonie jedynie <m> do zwracania pojedynczych znaków z napisu. <m>"
			"Możemy w ramach niego podać z użyciem dwukropka <m> zakres znaków które mają zostać zwrócone. <m>"
			'I tutaj tak samo jak w przypadku instrukcji <m> range zakres jest lewostronnie domknięty <m> i prawostronnie otwarty <mark name="trzy" />'
			'Ponadto tak samo jak w instrukcji range <m> możemy podać trzeci argument określający krok.'
		]
	},
	{
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_napisy_F, "py")],
			["przemiennosc", eduMovie.clear + eduMovie.code2console(code_napisy_G, "py")]
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(code_napisy_F, [], cmd="python3")],
			["przemiennosc", eduMovie.runCode(code_napisy_G, [], cmd="python3")],
		],
		'text' : [
			"Jeżeli jakiegoś z argumentów nie chcemy podawać <m> możemy je pominąć i tak 3 dwukropek dwukropek 2, <m> będzie oznaczało napis od znaku o indeksie <3>[trzy] <m> co drugi znak do jego końca. <m>"
			"Trzeci argument może być też ujemny, <m> co będzie oznaczało branie znaków z napisu w odwrotnej kolejności. <m>"
			'W przykładzie pokazanym na ekranie widzimy też że użycie <m> dwukropek dwukropek minus jeden powoduje <m> wypisanie całego napisu od końca. <mark name="przemiennosc" />'
			'Warto zauważyć że operacje te nie zawsze są przemienne <m> – tak jak widać to w przykładzie pokazanym na ekranie. <m>'
			
			'Wszystkie operacje związane z operatorem nawiasu kwadratowego <m> stosowanego na napisie, zwracają nowy napis <m> utworzony z elementów oryginalnego napisu. <m>'
			'Także pobranie pojedynczego znaku zwraca napis. <m> W Pythonie nie ma osobnego typu używanego na pojedynczy znak. <m>'
			'Istotną konsekwencją tego że operator ten zwraca nowy napis, <m> a nie jakąś formę referencji do fragmentu oryginalnego napisu <m> jest fakt iż nie może on być użyty do modyfikowania napisu. <m>'
			'Nie ma też innej metody na modyfikowanie <m> (czyli zmianę fragmentu napisu, bez tworzenia nowego). <m> W Pythonie napisy są niemodyfikowalne <m> i każda operacja zmieniająca napis prowadzi <m> do utworzenia nowego napisu. <m>'
		]
	},
]

code_napisy_H = r"""
napis = 'abcdef'
napis2 = '123'

print(napis+napis2, 3*napis2)
"""

code_napisy_I = r"""
napis = 'abcd'

for x in napis:
  print(x)
  x = 'qq'

print(napis)
"""

code_napisy_J = r"""
napis = 'abcd'

for i in range(len(napis)):
  print(i, "→", napis[i])
"""

clipData += [
	{
		'consoleTop': [
			[0.0,    eduMovie.clear + eduMovie.code2console(code_napisy_H, "py")],
			["for1", eduMovie.clear + eduMovie.code2console(code_napisy_I, "py")],
			["for2", eduMovie.clear + eduMovie.code2console(code_napisy_J, "py")],
		],
		'consoleDown': [
			[0.0,    eduMovie.runCode(code_napisy_H, [], cmd="python3")],
			["for1", eduMovie.runCode(code_napisy_I, [], cmd="python3")],
			["for2", eduMovie.runCode(code_napisy_J, [], cmd="python3")],
		],
		'text' : [
			"Python pozwala na dodawanie napisów i mnożenie ich przez liczbę. <m>"
			'Efektem dodawania jest napis złożony z dodawanych napisów <m> (jest to metoda łączenia napisów) <m>.'
			'A rezultatem mnożenia przez n jest napis n-krotnie złączony sam ze sobą. <mark name="for1" />'
			'Po elementach napisu możemy przechodzić <m> także przy pomocy pętli for, <m> tak jak po elementach listy. <m>'
			'W ramach każdego obiegu takiej pętli pod zmienną iteracyjną, <m> podstawiana będzie kopia kolejnego znaku z napisu. <mark name="for2" />'
			'Możemy także iterować po numerach znaków w napisie <m> i odwoływać się do nich z użyciem nawiasów kwadratowych <m> i indeksu danego znaku. <m>'
			'Metoda ta może być wygodna <m> jeżeli z jakiś innych powodów potrzebny nam jest numer znaku <m> lub na przykład mamy potrzebę podejrzenia następnego znaku. <m>'
		]
	},
]
