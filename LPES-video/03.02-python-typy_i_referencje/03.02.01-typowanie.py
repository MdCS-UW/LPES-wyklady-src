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

code_type_A = r"""
a = 3
b = [13.0, 3]

print(type(a), type(b))

a = 'abc'
b = 13.0

print(type(a), type(b))
"""

code_type_B = r"""
def a():
  print("x")

x = a()
print(x, type(x))
"""

code_type_C = r"""
y = None

if y == None:
    print("A")

if not y:
    print("B")
"""

code_size_A = r"""
a=17;
print(a.__sizeof__());

a=17**100
print(a.__sizeof__());
"""

code_size_B = r"""
a = [1, 2]
b = ["abcd", a]
c = [1, 2, 3]

print(a.__sizeof__(), b.__sizeof__(), c.__sizeof__())
"""

code_size_C = r"""
a = [1, 2]
print(a.__sizeof__())

a.append(3)
print(a.__sizeof__())

a.append(4)
print(a.__sizeof__())
"""

try: clipData
except NameError: clipData = []

clipData += [
	{ 'title': [ "#03.2", "Python:", "typy", "i referencje" ] },
	
	{ 'comment': 'typowanie' },
	{ #  
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_type_A, "py")],
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(code_type_A, [], cmd="python3")],
		],
		'text' : [
			'W pythonie typ zmiennej możemy sprawdzić przy pomocy funkcji type. <m> Jak widzimy każda zmienna ma określony typ, <m> jednak na skutek przypisania do niej innej wartości może ona go zmienić. <m>'
			
			'Python ma typowanie dynamiczne, <m> czyli(w odróżnieniu na przykład od C) <m> programista nie martwi się określaniem typu zmiennej, <m>'
			'tylko pisze <m> że a równa się zero i to Python <m> martwi się o to żeby ustalić typ a jako zmienną całkowitą. <m>'
			
			'Python z każdą zmienną wiąże pewien typ <m> i robi to w oparciu o przypisywaną do niej wartość, <m> dzięki czemu programista nie musi go jawnie deklarować. <m>'
			'Przypomina to działanie typu (czy raczej słowa kluczowego) <m> auto z współczesnego <C++>[c plus plus]. <m>'
			'Pozwala ono na automatyczne określenie typu deklarowanej <m> zmiennej w oparciu o przypisywaną do niej wartość. <m>'
		]
	},
	{ #  
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_type_B, "py")],
			["nonetype", eduMovie.clear + eduMovie.code2console(code_type_C, "py")],
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(code_type_B, [], cmd="python3")],
			["nonetype", eduMovie.runCode(code_type_C, [], cmd="python3")],
		],
		'text' : [
			'Kiedy python nie wie jaką wartość przypisać do zmiennej, <m> bo np. przypisujemy do niej wynik funkcji <m> która nic nie zwraca to używa typu <None>[nan]. <m>'
			'W pewnym stopniu jest on takim Pythonowym odpowiednikiem <NULL>[nul] <m> znanego z C <m> i informuje o tym że zmienna nie ma wartości ani typu. <mark name="nonetype" />'
			
			'Możemy też celowo inicjalizować zmienne (np. argumenty funkcji) <m> taką wartością aby wykryć fakt ich ustawienia lub nie. <m>'
			'W przypadku użycia w warunkach, <None>[nan] konwertowany jest na False <m> (więc <None>[nan] może być użyty jako wartość False – tak jak <m> miało to miejsce w funkcji search z modułu re). <m>'
			'Możemy też porównywać zmienną z <None>[nan] aby sprawdzić czy została <m> ona ustawiona na coś innego (więc możemy odróżnić False od <None>[nan]). <m>'
		]
	},
	{ #  
		'consoleTop': [
			[0.0, eduMovie.clear],
		],
		'consoleDown': [
			[0.0, "o", eduMovie.prompt()],
			[0.3, "o", r"""php -n -r ' echo 1+"11"+$a . "\n"; '"""],
			[2.0, "o", "\n\r"],
			[2.2, "o", "12\n\r" + eduMovie.prompt()],
		],
		'text' : [
			'Są jednak języki z luźniejszym typowaniem niż Python, <m> w których kontrola typu zmiennej odbywa się <m> w momencie jej użycia (a nie inicjalizacji jak w Pythonie). <m>'
			'W językach takich to czy zmienna zachowa się jak liczba czy tekst <m> może zależeć od operacji którą na niej wykonujemy. <m>'
			'Często języki takie też pozwalają na odwoływanie się <m> do niezaincjalizowanej zmiennej, <m> traktując ją w takich odwołaniach jako napis pusty, zero, itd. <m>'
			'Na ekranie widzimy przykład takiego liberalnego podejścia do zmiennych w PHP, <m> w którym sumujemy liczbę <1>[jeden] z napisem <11>[jedenaście] i niezaincjalizowaną zmienną a, <m> po czym dopisujemy do tego znak nowej linii. <m>'
			'W Pythonie, jak wiemy, odwołanie do niezainicjalizowanej zmiennej jest błędem, <m> a napisy na liczby i liczby na napisy należy konwertować jawnie. <m>'
		]
	},
	{ #  
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_size_A, "py")],
			["size2", eduMovie.clear + eduMovie.code2console(code_size_B, "py")],
			["size3", eduMovie.clear + eduMovie.code2console(code_size_C, "py")],
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(code_size_A, [], cmd="python3")],
			["size2", eduMovie.runCode(code_size_B, [], cmd="python3")],
			["size3", eduMovie.runCode(code_size_C, [], cmd="python3")],
		],
		'text' : [
			'Rozmiar zmiennej w Pythonie można sprawdzić korzystając <m> z metody <sizeof>[size of], tak jak widzimy na ekranie. <m>'
			'Możemy zauważyć także że rozmiar nawet prostej zmiennej jak liczba <m> całkowita jest spory i rośnie wraz ze wzrostem jej wartości. <m>'
			'Związane jest to z tym iż nawet takie proste typy są obiektami, <m>'
			'a zaletą tego jest że Python nie posiada ograniczenia na wielkość <m> którą może wyrażać liczba całkowita <m> (takiego jak na przykład dwa do sześćdziesiątej czwartej). <mark name="size2" />'
			
			'Rozmiar listy nie zależy od typów czy też rozmiarów elementów w niej zawartych. <m>'
			'Zależy natomiast od ilości elementów <m> i w systemach <64>[sześćdziesięcio cztero] bitowych rośnie o 8 bajtów z każdym elementem. <m>'
			'Wynika to z faktu, iż <sizeof>[size of] podaje rozmiar samego obiektu listy, <m> natomiast jej elementy żyją poza nią, <m> a lista stanowi jedynie tablicę wskaźników na te elementy. <mark name="size3" />'
			
			'Niektóre wywołania append zwiększają rozmiar listy o więcej <m> niż odpowiadający jednemu elementowi, <m> rezerwując pamięć pod kolejne powiększenie listy z jej użyciem. <m>'
			'Za to kolejne nie wpływają na rozmiar listy. <m>'
		]
	},
]

