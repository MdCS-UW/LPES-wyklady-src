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

code_range = r"""
for i in range(1,5,2):
  print(i)
"""

code_generator = r"""
def fib(x):
  a, b = 0, 1
  while a < x:
    yield a
    a, b = b, a + b

for x in fib(40):
  print(x)
"""

code_iterator = r"""
l = [6, 7, 8]
i = iter(l)  # zmienna i jest tutaj iteratorem

print( next(i) )
print( next(i) )
print( next(i) )
print( next(i) )
"""

try: clipData
except NameError: clipData = []

clipData += [
	{ 'section': 'generatory i iteratory' },
	{ #  
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_range, "py")],
			["generator", eduMovie.clear + eduMovie.code2console(code_generator, "py")],
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(code_range, [], cmd="python3")],
			["generator", eduMovie.runCode(code_generator, [], cmd="python3")],
		],
		'text' : [
			'Pamiętamy funkcję range używaną do uzyskiwania kolejnych <m> liczb całkowitych w ramach pętli for. <m>'
			'Pamiętamy też jej ograniczenia, takie jak możliwość pracy <m> wyłącznie z liczbami całkowitymi, stały krok iteracji, itp. <mark name="generator" />'
			
			'Python pozwala na samodzielne tworzenie obiektów które <m> będą podawały nam kolejne wartości na przykład w ramach iteracji pętlą for. <m>'
 			'Obiekty takie nazywamy generatorami i definiujemy tak samo jak <m> każdą normalną funkcje, rozpoczynając od słowa kluczowego def. <m>'
			'Różnica polega na użyciu zamiast return słowa kluczowego yield. <m>'
			'Powoduje ono zwrócenie podanej do niego wartości, <m> jednak nie przerywa działania generatora, <m> a jedynie zawiesza je do próby pobrania kolejnej wartości. <m>'
			'W przypadku takiej próby kod generatora wykonywany będzie <m> od instrukcji następnej po yield <m> (tak jakby właśnie zakończyło się wykonanie yield) <m>'
			'lub (jedynie gdy jest to pierwsze uruchomienie generatora) od początku. <m>'
			
			'Warto zauważyć że funkcja związana z generatorem odpalana jest raz <m> i jedynie zawieszana przy kolejnych wykonaniach yield. <m>'
			'Jeżeli funkcja ta zakończy się na przykład poprzez dojście do końca <m> swojego kodu lub jawne wykonanie return to generator przestanie działać, <m>'
			'a jego ponowne uruchomienie możliwe będzie na przykład w kolejnym <m> wywołaniu pętli i odbędzie się od początku (pierwszej zwracanej wartości). <m>'
			
			'Zaletami generatora w stosunku co do funkcji <m> zwracającej listę wszystkich elementów jest mniejsze zapotrzebowanie <m> na pamięć w przypadku sporych list lub list dużych obiektów <m>'
			'oraz brak generowania elementów które mogą okazać się nie potrzebne <m> na przykład gdy pętla, która z niego korzysta zostanie <m> wcześniej przerwana przez break. <m>'
		]
	},
	{ #  
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_iterator, "py")],
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(code_iterator, [], cmd="python3")],
		],
		'text' : [
			'Dotychczas do iterowania po elementach różnych kolekcji, <m> czy też kolejnych wartościach zwracanych przez generatory <m> korzystaliśmy z pętli for. <m>'
			'Możemy to zrobić także w inny sposób korzystając z iteratorów. <m>'
			'W tym celu należy utworzyć obiekt iteratora poprzez wywołanie <m> funkcji iter od kolekcji lub generatora po którym chcemy iterować. <m>'
			'Kolejne elementy możemy pobierać używając funkcji next <m> wywoływanej od tego iteratora, <m> tak jak jest to pokazane w przykładzie widocznym na ekranie. <m>'
			
			'Jeżeli nie ma elementów które możemy pobrać <m> (bo na przykład pobraliśmy już wszystkie elementy listy) <m> to funkcja next rzuci wyjątek <StopIteration>[stop iteration], <m> który oczywiście możemy stosownie obsłużyć. <m>'
			
			'Iteratory pozwalają nam na łatwe pobieranie kolejnych wartości <m> kolekcji bez użycia pętli lub w wielu pętlach. <m>'
			'Jest to użyteczne na przykład jeżeli kod operujący na kolekcji <m> musi być jakoś porozrzucany po różnych miejscach w programie. <m>'
			'Iterator przydaje się niekiedy także do sprawdzenia <m> czy coś po czym iterujemy nie jest puste <m> (gdyż potrafi rzucać wyjątek związany z końcem iteracji) <m>'
			'lub do pobrania jedynie pierwszego elementu kolekcji. <m>'
		]
	},
]
