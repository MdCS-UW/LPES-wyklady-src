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

try: clipData
except NameError: clipData = []

clipData += [
	{ 'title': [ "#01.3", "Listowanie i", "wyszukiwanie", "plików" ] },
	
	{ 'comment': 'echo i znaki uogólniające' },
	{
		'console': [
			[0.0, ""],
			[10.0, eduMovie.runCommandString(r"echo *", cwd='demo')],
		],
		'text' : [
			'Wspomnieliśmy o poleceniu echo, które służy <m> do wypisywania jakiś informacji na ekran. <m>'
			'Polecenie to, gdy napiszemy echo gwiazdka, <m> może zostać użyte do wylistowania wszystkich <m> (nie ukrytych) plików w bieżącym katalogu. <m>'
			'Nie jest to jednak funkcjonalność samej komendy echo, <m> a powłoki ją wywołującej – to bash przed uruchomieniem polecenia echo <m> zastąpił w jego linii poleceń gwiazdkę listą wszystkich nie ukrytych plików. <m>'
			
			'Gwiazdka jest jednym z tak zwanych znaków uogólniających powłoki, <m> których użycie w jakimś (nie zabezpieczonym cudzysłowami) <m> napisie powoduje zastąpienie go poprzez listę pasujących plików, <m>'
			'w oparciu o rozwinięcie tych znaków. <m>'
			'Gwiazdka jest najbardziej ogólnym, a zarazem najczęściej stosowanym <m> tego typu znakiem i oznacza dopasowanie dowolnego, <m> także pustego ciągu znaków w jej miejscu. <m>'
		]
	},
	{
		'console': [
			[0.0, eduMovie.runCommandString(r"echo a*", cwd='demo')],
			[7.0, eduMovie.runCommandString(r"echo *l*", cwd='demo')],
			["ax", eduMovie.runCommandString(r"echo ax*", cwd='demo')],
		],
		'text' : [
			'Na przykład do a gwiazdka zostanie dopasowany plik o nazwie a <m> oraz wszystkie inne pliki, których nazwa zaczyna się od a. <m>'
			'Natomiast do gwiazdka <l>[el] gwiazdka <break time="150ms"/> dowolny plik mający literę <l>[el] w środku. <mark name="ax" />'
			'Należy mieć na uwadze, że gdy nie ma pasujących do wyrażenia <m> plików, bash uruchomi podane polecenie przekazując do niego <m> niezmodyfikowany ciąg zawierający znaki uogólniające. <m>'
		]
	},
	{
		'console': [
			[3.0, eduMovie.runCommandString(r"echo ?", cwd='demo')],
			[5.0, eduMovie.runCommandString(r"echo a?a", cwd='demo')],
			[16.0, eduMovie.runCommandString(r"echo \?*", cwd='demo')],
			["kwadratowe + 1.1", eduMovie.runCommandString(r"echo [Aa]?a", cwd='demo')],
			["kwadratowe + 3.5", eduMovie.runCommandString(r"echo [a-z]*", cwd='demo')],
			["kwadratowe + 7.0", eduMovie.runCommandString(r"echo [!Aa]*", cwd='demo')],
			["kwadratowe + 9.3", eduMovie.runCommandString(r"echo [-a!]*", cwd='demo')],
			["ukryte", eduMovie.runCommandString(r"echo .*", cwd='demo')],
		],
		'text' : [
			'Innymi znakami uogólniającymi powłoki jest pytajnik, <m> którym możemy zastąpić pojedynczy, dowolny znak. <m>'
			'Użycie samego pytajnika oznacza wszystkie jednoznakowe nazwy plików. <m>'
			'Jeżeli chcemy wylistować pliki których nazwy zaczynają się od pytajnika <m> powinniśmy poprzedzić ten znak odwrotnym ukośnikiem. <mark name="kwadratowe" />'
			'Natomiast korzystając z nawiasów kwadratowych możemy zastąpić <m> pojedynczy znak z podanego w nich zbioru znaków. <m>'
			'Zbiór ten może być określony poprzez wymienienie poszczególnych znaków, <m> podanie zakresu z użyciem myślnika lub zanegowanie zbioru <m> poprzez podanie po otwierającym nawiasie <m> kwadratowym wykrzyknika (lub dzióbka w górę). <m>'
			'Jeżeli wymieniając elementy zbioru chcemy uwzględnić <m> w nich myślnik, powinien być on podany jako pierwszy lub ostatni znak, <m> a wykrzyknik (lub dzióbek w górę) jako nie pierwszy znak. <mark name="ukryte" />'
			'Kropka gwiazdka pozwoli wypisać wszystkie ukryte pliki, <m> wliczając w to odwołanie do bieżącego i nadrzędnego katalogu, <m> w postaci kropki i dwóch kropek. <m>'
		]
	},
]

