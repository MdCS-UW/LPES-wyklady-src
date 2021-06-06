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

code_zerodiv = r"""
a = 3 / 0
"""

code_sprawdz_kodu_powrotu = r"""
ret = funkcja1(a, b, c)
if ret<0:
  print("błąd w funkcja 1")
  exit(1)

ret = funkcja2(ret, c)
if ret<0:
  print("błąd w funkcja 2")
  exit(1)
"""

code_tryexcept = r"""
try:
  a = 3 / 0
except ZeroDivisionError:
  print("jakaś reakcja na błąd dzielenia przez zero")
except:
   print("inny błąd")
"""

code_raise = r"""
raise BaseException("ABC")
"""

code_wyjatki_wielopoziomowo = r"""
def f(x):
	if x<0:
		raise TypeError("A")
	elif x<5:
		raise ValueError("B")

def g(x):
	try:
		f(x)
	except TypeError:
		print("g: był błąd TypeError")

def h(x):
	try:
		g(x)
		print("h: OK")
	except:
		print("h: błąd w g")

h(-2)
h(2)
"""

try: clipData
except NameError: clipData = []

clipData += [
	{ 'title': [ "#03.2", "Python:", "operacje bitowe", "i wyjątki" ] },
	
	{ 'comment': 'wyjątki' },
	{
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_zerodiv, "py")],
			["kodpowrotu", eduMovie.clear + eduMovie.code2console(code_sprawdz_kodu_powrotu, "py")],
			["_try", eduMovie.clear + eduMovie.code2console(code_tryexcept, "py")],
			["_raise", eduMovie.clear + eduMovie.code2console(code_raise, "py")],
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(code_zerodiv, [], cmd="python3")],
			#["kodpowrotu", eduMovie.clear],
			["_try", eduMovie.runCode(code_tryexcept, [], cmd="python3")],
			["_raise", eduMovie.runCode(code_raise, [], cmd="python3")],
		],
		'text' : [
			'Mówiliśmy już trochę na temat komunikatów <m> o błędach i o tym że należy je czytać. <m>'
			'Warto się też przyjrzeć im od strony technicznej – w zdecydowanej <m> większości (pomijając czyste błędy składniowe) są one wyjątkami. <m>'
			'Wyjątki są mechanizmem pozwalającym na przerwanie <m> wykonywania programu z powodu błędu. <mark name="kodpowrotu" />'
			
			'Ich przewagą nad zwykłym ubiciem programu <m> w takiej sytuacji jest możliwość ich obsłużenia. <m>'
			'Wyjątek pozwala nam wyskoczyć z dowolnego poziomu zagnieżdżeń <m> funkcji bez pisania w nich specjalnego kodu, który się tym zajmuje. <m>'
			'Na przykład w postaci warunków sprawdzających kod powrotu wywoływanych funkcji <m> i powodujących przerywanie działanie funkcji, <m> która je wywołała oraz zwrócenie odpowiedniego kodu błędu. <m>'
			'Wyjątki pozwalają na programowanie bez konieczności sprawdzania dla <m> każdej funkcji, którą używamy, czy zakończyła się ona sukcesem czy porażką. <mark name="_try" />'
			
			'Dodatkowo w ramach kodu obsługującego wyjątek możemy <m> rozróżniać poszczególne błędy z użyciem obiektu używanego przez wyjątek <m> i odpowiednio na nie reagować. <m>'
			'W Pythonie do obsługi wyjątków służy konstrukcja <m> try / <except>[eksept], przypominająca trochę instrukcję if. <m>'
			'Pierwszy blok kodu (związany ze słowem kluczowym try) <m> wykonywany jest normalnie. <m>'
			'Jeżeli wystąpi w nim wyjątek (który nie był obsłużony wewnątrz <m> funkcji w nim użytych) to wykonywanie tego kodu jest w tym momencie przerwane <m> i program przechodzi do odpowiedniego bloku <except>[eksept]. <m>'
			'Bloków <except>[eksept] może być wiele, wybierany jest ten po którym <m> podana jest klasa zgodna z klasą użytą do "rzucenia wyjątku". <m>'
			'Jeżeli żadna z podanych klas nie pasuje <m> to wykonany będzie <m> domyślny wariant (czyli ten bez podanej klasy), <m>'
			'a jeżeli go nie ma to wyjątek pozostanie nie obsłużony <m> i będzie propagowany w górę stosu wywołań funkcji. <mark name="_raise" />'
			
			'Możemy rzucać własne wyjątki z użyciem słowa kluczowego raise <m> po którym wywołujemy konstruktor klasy pochodnej od <BaseException>[Base Eksepszyn] <m> lub podajemy obiekt takiej klasy. <m>'
		]
	},
	{
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_wyjatki_wielopoziomowo, "py", first=1, last=16)],
			*[  [17+i,  eduMovie.clear + eduMovie.code2console(code_wyjatki_wielopoziomowo, "py", first=1+i,  last=16+i)] for i in range(1,7)  ],
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(code_wyjatki_wielopoziomowo, [], cmd="python3")],
		],
		'text' : [
			'Na ekranie widzimy kod demonstrujący wielopoziomowość w obsłudze wyjątków. <m>'
			'Wyjątek <TypeError>[Type Error] generowany w funkcji f gdy x jest mniejsze od zera <m> obsługiwany jest w funkcji g, zatem nie jest zauważany w funkcji h. <m>'
			'Wyjątek <ValueError>[Value Error] generowany w funkcji f gdy x jest mniejsze od 5 <m> nie jest obsługiwany w funkcji g, zatem jest zauważany w funkcji h. <m>'
			
			'Widzimy też że rzucenie wyjątku przez jakąś funkcję w bloku try <m> skutkuje przerwaniem wykonywania tego bloku – <m> "h: OK" wypisało się tylko gdy g nie wypuściło wyjątku. <m>'
			
			'Obsługa wyjątków ma sens w sytuacji gdy spodziewamy się <m> że dany fragment kodu może zawieść i mamy pomysł jak na to zareagować. <m>'
			'Na przykład gdy otwieramy do odczytu plik <m> podany przez użytkownika, który może nie istnieć. <m>'
			'Przechwytywanie i ignorowanie wszystkich wyjątków <m> jest bardzo złą praktyką, która utrudnia szukanie błędów w programie. <m>'
			'Jeżeli zdecydujemy się na napisanie bloku try except, <m> to powinniśmy napisać kod który sensownie obsłuży taki wyjątek'
		]
	},
]
