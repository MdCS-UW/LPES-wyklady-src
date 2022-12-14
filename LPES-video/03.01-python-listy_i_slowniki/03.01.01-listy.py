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

code_listy_A = r"""
for x in [1,2,3]:
    print(x, x**2)
"""

code_listy_B = r"""
lista = ['a', 'b', 'c', 'd', 'e', 'f']
print( lista[1] )
print( lista[3:] )
print( lista[::2] )
print( lista[::-1] )
"""

code_listy_C = r"""
lista = ['a', 'b', 'c', 'd', 'e', 'f']

print( len(lista) );
for i in range(len(lista)):
    print( lista[i] )
"""

code_listy_D = r"""
lista = ['a', True, 13, 17.6, 'ebc', [1, 'x']]

for x in lista:
    print( x )
"""

code_listy_E = r"""
lista = ['a', True, 13, 17.6, 'ebc', [1, 'x']]

lista[1]='rty'
lista.append("xyz")

for x in lista:
    print( x )
"""

code_listy_F = r"""
lista = ['a', True, 13, 17.6, 'ebc', [1, 'x']]

del lista[1]

for x in lista:
    print( x )

del lista[1]

for x in lista:
    print( x )
"""


try: clipData
except NameError: clipData = []

clipData += [
	{ 'title': [ "#03.1", "Python:", "listy", "i słowniki" ] },
	
	{ 'comment': 'listy' },
	{
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_listy_A, "py")],
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(code_listy_A, [], cmd="python3")],
		],
		'text' : [
			"Przy omawianiu pętli for pojawiły nam się listy, <m> były one przykładem kolekcji elementów po których możemy iterować. <m>"
			"Zastosowanie list jest jednak znacznie szersze – stanowią one <m> dość uniwersalny kontener, pozwalający na przechowywanie różnych wartości. <m>"
			"Pythonowe listy charakteryzują się tym że zachowują kolejność elementów <m> oraz pozwalają na odwoływanie się do elementu poprzez jego numer. <m>"
			"Numeracja elementów jest ciągła i zaczyna się od zera. <m>"
			
			"Jak może już zauważyliśmy listy w wielu aspektach <m> przypominają napisy – ciągła numeracja od zera, identyczny sposób <m> iterowania w pętli for, dostęp do elementu o podanym indeksie, itd. <m>"
			"I tak jest w istocie – wiele operacji wygląda tak samo. <m>"
			"Jednak napisy i listy w Pythonie nie są ze sobą tożsame <m> (napis nie jest listą liter) <m> i istnieją między nimi istotne różnice. <m>"
		]
	},
	{
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_listy_B, "py")],
			["dlugosc", eduMovie.clear + eduMovie.code2console(code_listy_C, "py")],
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(code_listy_B, [], cmd="python3")],
			["dlugosc", eduMovie.runCode(code_listy_C, [], cmd="python3")],
		],
		'text' : [
			'Najpierw jednak trochę o podobieństwach. <m>'
			'Dostęp do elementów listy, a także jej fragmentów (pod-list) jest identyczny <m> jak w przypadku napisów i odbywa się z użyciem nawiasów kwadratowych. <m>'
			'Dla list możemy tak samo stosować zakresy podawane z użyciem dwukropka <m> oraz krok, także ujemny jeżeli chcemy odwrócić kolejność listy. <mark name="dlugosc" />'
			'Identycznie działa również funkcja len, która zwróci nam długość listy. <m>'
			'Co pozwala także na iterowanie po indeksach listy, a nie tylko jej elementach. <m>'
		]
	},
	{
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_listy_D, "py")],
			["modyfikowalnosc", eduMovie.clear + eduMovie.code2console(code_listy_E, "py")],
			["delelement", eduMovie.clear + eduMovie.code2console(code_listy_F, "py")],
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(code_listy_D, [], cmd="python3")],
			["modyfikowalnosc", eduMovie.runCode(code_listy_E, [], cmd="python3")],
			["delelement", eduMovie.runCode(code_listy_F, [], cmd="python3")],
		],
		'text' : [
			'Głównymi różnicami jest to że lista jest modyfikowalna <m> oraz że elementem listy mogą być obiekty dowolnego typu.'
			'Nawet w ramach pojedynczej listy <m> elementy mogą być różnych typów. <m> Elementami listy mogą być też inne listy. <m>'
			'Dla przypomnienia – napis był niemodyfikowalny <m> i składał się tylko ze znaków unicode. <mark name="modyfikowalnosc" />'
			
			'Modyfikowalność listy pozwala na zmianę <m> wartości (a nawet typu) wskazanego elementu. <m>'
			'Pozwala na dodawanie nowych elementów zarówno na końcu listy <m> (z użyciem metody append) <m>, jak i w dowolnym miejscu listy z użyciem metody insert. <mark name="delelement" />'
			
			'Możemy też usuwać elementy z listy korzystając <m> z instrukcji del do której przekazujemy element do usunięcia. <m>'
		]
	},
]

code_listy_G = r"""
napis="Ala ma kota"

l = list(napis)

del l[4]
l[4] = "miała"
l[9]='y'
napis = str.join("", l)

print(napis)
"""

code_listy_H = r"""
a=(1, [1,2]);

a[1][0]=2
print(a)

a[0]=2;
print(a)
"""

clipData += [
	{ #  
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_listy_G, "py")],
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(code_listy_G, [], cmd="python3")],
		],
		'text' : [
			'Podobieństwo list i napisów możemy wykorzystać <m> używając listę w roli modyfikowalnego napisu. <m>'
			'W tym celu możemy skonwertować dowolny napis na listę <m> wywołując po prostu konstruktor listy od podanego napisu. <m>'
			'Wykonać modyfikacje na otrzymanej liście, <m> a następnie skonwertować ją na napis. <m>'
			
			'Do konwersji na napis używamy funkcji join z klasy <str>[S T R] (obsługującej napisy) <m> do której podajemy napis używany do łączenia elementów listy <m> (w tym wypadku pusty) oraz tą listę. <m>'
			'Moglibyśmy zapisać to jako wywołanie metody join na pustym napisie, <m> ale taki zapis wydaje się dziwny. <m>'
			
			'Warto zauważyć że otrzymaną listę znaków możemy traktować <m> jako listę napisów i w ramach jej modyfikowania <m> w pojedynczą komórkę wstawiać całe napisy. <m>'
			'Oczywiście ten sposób na modyfikowanie napisów ma sens <m> tylko w niektórych przypadkach, często prościej jest utworzyć nowy napis, <m> korzystając z operatorów pobierajacych podnapisy oryginalnego napisu. <m>'
		]
	},
	{ #  
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_listy_H, "py")],
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(code_listy_H, [], cmd="python3")],
		],
		'text' : [
			'Warto wspomnieć iż mamy też niemodyfikowalny wariant list – krotki, <m> zapisujemy je podobnie jak listy, tyle że z użyciem <m> nawiasów okrągłych a nie kwadratowych. <m>'
			'Mogą okazać się one przydatne lub nawet niezbędne w pewnych sytuacjach, <m> ale mimo to nie będziemy im poświęcać zbyt wiele czasu. <m>'
			
			'Listy posiadają także metody umożliwiające ich sortowanie, odwracanie itd. <m>'
			'Warto zauważyć iż metody te na ogół modyfikują listę <m> a nie zwracają jej zmienioną kopię, <m> tak jak ma to miejsce w przypadku operatora nawiasu kwadratowego. <m>'
		]
	},
]

