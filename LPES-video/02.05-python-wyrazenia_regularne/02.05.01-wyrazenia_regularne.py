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

code_re_A = r"""
import re

napis="abcdef"

if re.search("[dz][ex]", napis):
  print("y zawiera de, dx, ze lub zx")

print(re.search("[dz][ex]", napis))

wynik = re.search("[dz][ex]", napis)
print(wynik.span(), wynik.group())
"""

code_re_B = r"""
import re

napis1="de123de"
napis2="de123zx"

print( re.search("([dz][ex])[0-9]+\\1", napis1) )
print( re.search("([dz][ex])[0-9]+\\1", napis2) )
"""

code_re_C = r"""
import re

x="AdzB"
y="AdzqB"

# zasięg alternatywy jest ograniczony do podwyrażenia
print( re.search("A(dz|qw)B", x) )
print( re.search("A(dz|qw)B", y) )

# zasięg alternatywy nie jest ograniczony
print( re.search("A(dz)|(qw)B", x) )
print( re.search("A(dz)|(qw)B", y) )
"""

try: clipData
except NameError: clipData = []

clipData += [
	{ 'title': [ "#02.5", "Python:", "wyrażenia", "regularne" ] },
	
	{ 'comment': 'wyrażenia regularne' },
	{
		'image': [
			[0.0, eduMovie.convertFile("wyr_uogolniajace.tex", negate=True)],
			["regularne", eduMovie.convertFile("wyr_regularne.tex", negate=True)]
		],
		'text' : [
			'Na jednych z poprzednich zajęć poznawaliśmy <m> wyrażenia uogólniające powłoki, <m> w których np. do a gwiazdka <m> dopasowywane były wszystkie pliki <m> których nazwa zaczynała się na literę a. <m>'
			
			'Bardziej rozbudowaną formą tego typu <m> wyrażeń są wyrażenia regularne. <mark name="regularne" />'
			'Pełnią one taką samą funkcję, <m> czyli opisują jakiś wzorzec do którego możemy dopasowywać napis. <m> Oferują jednak większe możliwości. <m>'
			'Wyrażenia regularne występują w różnych narzędziach <m> i językach programowania i mają zbliżoną do siebie składnie, <m> aczkolwiek można mówić o różnych dialektach, <m> do czego wrócimy na jednych z kolejnych zajęć. <m>'
			'Składnia wyrażeń regularnych, <m> jest jednak dość odmienna od wyrażeń uogólniających powłoki <m> i mechanizmów tych nie należy mylić. <m>'
			
			'W wyrażeniach regularnych jeden dowolny znak to jest kropka, <m> dowolny ciąg znaków to jest kropka gwiazdka, <m> bo gwiazdka oznacza dowolną (także zerową) <m> ilość powtórzeń tego co występuje przed nią. <m>'
			'Na przykład <ab*>[a b gwiazdka] będzie oznaczało: <m> a, <ab>[A B], <abb>[A B B], <abbb>[A B B B] i tak dalej. <m>'
			
			'Zakresy znaków działają tak samo <m> jak w przypadku basha – jeżeli podamy w nawiasach <m> kwadratowych <a-z>[a myślnik zet] – to będą wszystkie <m> małe litery alfabetu łacińskiego od a do <z>[zet]. <m>'
			'W nawiasach kwadratowych możemy też jawnie wymienić cały <m> zbiór znaków, który ma być dopasowywany. <m>'
			'Jeżeli chcemy zanegować zbiór możemy to zrobić <m> tylko przy pomocy daszka w górę umieszczanego <m> zaraz po otwierającym nawiasie kwadratowym. <m>'
			
			'Pytajnik oznacza tutaj zero lub jedno powtórzenie <m> tego co przed nim, plus natomiast oznacza jedno lub więcej, <m> czyli mają one funkcje podobne do gwiazdki. <m>'
			'Dokładną ilość powtórzeń możemy określić przy pomocy <m> nawiasów klamrowych, tak jak widać to na ekranie. <m>'
			
			'Operatory dzióbka w górę i dolara dopasowują <m> odpowiednio początek i koniec napisu.'
			
			'Fragmenty wyrażeń możemy grupować w nawiasach okrągłych celem <m> zastosowania do nich jako całości operatorów określających powtórzenia <m>'
			'lub możliwości odwołania się do takiego podwyrażenia w przyszłości <m> podając jego numer poprzedzony odwrotnym ukośnikiem. <m>'
			
			'Możemy także zapisać alternatywę, <m> czyli dopasowanie do jednego z dwóch wyrażeń. <m> W tym celu rozdzielamy je pionową kreską. <m>'
			
			'Były to jedynie najważniejsze elementy składni wyrażeń regularnych, więcej można znaleźć w odpowiedniej dokumentacji. <m>'
		]
	},
	{ #  
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_re_A, "py")],
			["przyklad2", eduMovie.clear + eduMovie.code2console(code_re_B, "py")],
			["przyklad3", eduMovie.clear + eduMovie.code2console(code_re_C, "py")],
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(code_re_A, [], cmd="python3")],
			["przyklad2", eduMovie.runCode(code_re_B, [], cmd="python3")],
			["przyklad3", eduMovie.runCode(code_re_C, [], cmd="python3")],
		],
		'text' : [
			'Żeby korzystać z wyrażeń regularnych należy <m> zaimportować moduł re, który dostarcza między innymi funkcje <m> pozwalające na sprawdzanie czy napis pasuje do wyrażenia <m>'
			'oraz na wykonywanie operacji wyszukaj i zastąp <m> z użyciem wyrażeń regularnych. <m>'
			
			'Aby sprawdzić czy napis pasuje do wyrażenia regularnego <m> możemy skorzystać z funkcji search z modułu re. <m>'
			'Funkcja ta przyjmuje dwa argumenty <m> – wyrażenie regularne i dopasowywany napis. <m>'
			'W pokazanym na ekranie przykładzie sprawdzamy <m> czy napis zawarty w zmiennej, zawiera ciąg złożony z litery <m> d albo <z>[zet], po której następuje litera e albo x. <m>'
			'Oczywiście funkcja search w zwracanym wyniku zawiera więcej <m> informacji niż tylko fakt znalezienia – mamy tam między innymi <m> pozycję na której nastąpiło dopasowanie i dopasowany ciąg. <m>'
			'Wszystkie te informacje możemy pobrać odwołując się <m> do odpowiednich pól i metod zwróconego obiektu. <mark name="przyklad2" />'
			
			'W kolejnym przykładzie widzimy zastosowanie nawiasów okrągłych <m> do wyznaczenia pod-wyrażenia oraz odwołania się do takiego <m> pod-wyrażenia z użyciem dwóch odwrotnych ukośników i jego numeru. <m>'
			'Warto tutaj zwrócić uwagę iż takie odwołanie powoduje <m> dopasowywanie do tego co zostało dopasowane do pod-wyrażenia <m> a nie ponowne dopasowanie do samego pod-wyrażenia. <m>'
			'W przykładzie do pod-wyrażenia pasuje zarówno <de>[D E] jak i <zx>[Zet X], <m> ale dopasowane zostało <de>[D E], bo taki był napis, <m> więc w miejscu backslash backslash 1 oczekujemy <de>[D E]. <mark name="przyklad3" />'
			
			'Nawiasy okrągłe przydatne są też w połączeniu <m> z alternatywą wprowadzaną pionową krechą. <m>'
			'Standardowo alternatywa ta działa w taki sposób że wszystko co po lewej <m> (od początku wyrażenia), albo wszystko co po prawej (do końca wyrażenia). <m>'
			'Umieszczenie jej wewnątrz pod-wyrażenia ogranicza jej działanie <m> do tego podwyrażenia, tak jak pokazano na przykładzie. <m>'
			
			'Przykładami praktycznych zastosowań dla takich dopasowań <m> może być sprawdzanie czy napis jest poprawnym numerem telefonu, <m>'
			'poprawnym numerem IP, czy jest słowem i tego typu rzeczy <m> związane z walidacją wprowadzanych danych. <m>'
		]
	},
]

code_re_D = r"""
import re

napis="abcdbdefda"

print (re.sub('kota', 'unixa', "Ala ma kota"))

print (re.sub('[bd]+', "X", napis))
print (re.sub('[bd]+', "X", napis, 2))
"""

code_re_E = r"""
import re

napis="12 f13r p17u x11"

print (re.sub('[a-z]+([0-9]+)[a-z]+', "_\\1_", napis))
"""

code_re_F = r"""
import re

napis="po < abc > xyz < 123 > qw"

print (re.sub('< (.*) >', "[ \\1 ]", napis))
print (re.sub('< (.*?) >', "[ \\1 ]", napis))
"""

clipData += [
	{ #  
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_re_D, "py")],
			["przyklad5", eduMovie.clear + eduMovie.code2console(code_re_E, "py")],
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(code_re_D, [], cmd="python3")],
			["przyklad5", eduMovie.runCode(code_re_E, [], cmd="python3")],
		],
		'text' : [
			'Oprócz sprawdzania tego czy napis spełnia jakieś wymyślne kryteria <m> wyrażenia regularne mogą służyć również do zastępowania. <m>'
			'W tym celu możemy użyć funkcji sub z modułu re. <m>'
			'Przyjmuje ona trzy argumenty – pierwszym jest wyrażenie regularne <m> opisujące wyszukiwany, zastępowany fragment, drugim jest tekst <m> którego chcemy użyć do zastępowania, a trzecim jest <m> napis na którym chcemy wykonać całą operację. <m>'
			'Opcjonalnie możemy podać czwarty argument <m> określający ile maksymalnie zastąpień ma wykonać ta funkcja. <m>',
			
			'W pierwszym z pokazanych przykładów napis "kota" został zastąpiony napisem "unixa". <m>'
			'Taki zwykły tekst jest również wyrażeniem regularnym <m> i do jego zastępowania można użyć funkcji z nimi związanych. <m>'
			'Należy jednak mieć na uwadze, że znaki o specjalnym znaczeniu <m> dla wyrażeń regularnych zostaną w nim potraktowane specjalnie, <m> więc może to być podchwytliwe <m> i lepiej do tego celu użyć metody replace typu napisowego. <m>'
			'W drugim przykładzie pojedynczą literą x, <m> zastępowany jest każdy ciąg złożony z liter b oraz d. <m>'
			'Najpierw dla wszystkich wystąpień, <m> a w kolejnym wywołaniu tylko dla dwóch pierwszych. <mark name="przyklad5" />'
			
			'Jeżeli w wyrażeniu regularnym wydzielimy jakieś <m> podwyrażenia przy pomocy nawiasów to w drugim argumencie <m> funkcji możemy odwołać się do tego co zostało dopasowane <m> do takiego podwyrażenia i użyć tego w zastępującym ciągu znaków. <m>'
			
			'Ogólnie działanie tej funkcji powinno kojarzyć się <m> z działaniem polecenia wyszukaj i zastąp w edytorze vi, <m> o którym była mowa na pierwszych zajęciach, <m>'
			'w ramach tamtego polecenia także możemy używać wyrażeń regularnych <m> i na dodatek bardzo podobnych do tych poznanych przed chwilą. <m>'
		]
	},
	{ #  
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_re_F, "py")],
			["help", eduMovie.clear + eduMovie.code2console("help(re)", "py")],
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(code_re_F, [], cmd="python3")],
			["help", ""],
		],
		'text' : [
			"Wyrażenia regularne są zachłanne, <m> czyli dopasowują maksymalnej długości ciąg który pasuje do wyrażenia. <m>"
			'Jeżeli chcielibyśmy aby dopasowanie nie działało zachłannie, <m> a obejmowało najmniejszy możliwy ciąg to możemy skorzystać z operatorów <+?>[plus pytajnik] i <*?>[gwiazdka pytajnik]. <mark name="help" />'
			'Z pełnym opisem składni wyrażeń regularnych obsługiwanych <m> przez Pythona można się zapoznać w dokumentacji modułu re. <m>'
		]
	},
]

