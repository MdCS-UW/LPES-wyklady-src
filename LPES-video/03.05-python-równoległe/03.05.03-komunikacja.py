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

code_lock_idea = r"""
if not blokada:
	blokada = True
	# działania na pamięci współdzielonej
	blokada = False
"""

try: clipData
except NameError: clipData = []

clipData += [
	{ 'comment': 'komunikacja' },
	{
		'consoleTop': [
			[0.0, eduMovie.clear],
		],
		'consoleDown': [
			[0.0, ""],
		],
		'text' : [
			'Warto powiedzieć także kilka słów o komunikacji między procesowej. <m> Istnieje kilka mechanizmów z nią związanych. <m>'
			'Jednym z nich, o którym mówiliśmy już na pierwszych zajęciach, <m> a przed chwilą przypomnieliśmy go sobie <m> jest przekierowanie standardowego wejścia wyjścia. <m>'
			'Może ono przekazywać zarówno dane tekstowe jak i binarne <m> i pozwala na komunikację kilku procesów pracujących w strumieniu. <m>'
			'– Dane z pierwszego przekazywane są do kolejnego, <m> po przetworzeniu przez niego do następnego i tak dalej. <m>'
			
			'Podobnie można korzystać z łącz nazwanych, czyli tak naprawdę plików <m> pełniących rolę takiego strumienia wtedy jedna ze stron otwiera  <m>'
			'konkretny plik przy pomocy open do pisania, <m> druga robi to do odczytu i mogą się w ten sposób komunikować. <m>'
			'Innymi metodami są sygnały (o których będziemy mówić na kolejnych zajęciach), <m> kolejki komunikatów (o których raczej dużo nie będziemy mówili) i pamięć współdzielona. <m>'
			
			'Pamięć współdzielona, czyli dostęp do tych samych zmiennych <m> przez różne procesy, wymaga stosowania zabezpieczenia przed jednoczesną <m> modyfikacją jej przez kilka procesów, czy też odczytem w trakcie modyfikacji. <m>'
		]
	},
	{
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_lock_idea, "py")],
		],
		'consoleDown': [
			[0.0, ""],
		],
		'text' : [
			'Ideę tego zabezpieczenia może wyrazić kod widoczny na ekranie. <m>'
			'Jeżeli dostęp do pamięci współdzielonej nie jest zablokowany, <m> to go blokujemy, wykonujemy działania i zdejmujemy blokadę. <m>'
			
			'Taka blokada jest konieczna, gdyż jeżeli na przykład jeden proces <m> modyfikuje jakiś większy obszar pamięci a inny go chce przeczytać <m> to chcemy aby przeczytał go w spójnym stanie <m>'
			'– czyli albo przed rozpoczęciem modyfikacji, <m> albo po jej zakończeniu, ale nie w jej trakcie. <m>'
			
			'Niestety przedstawiony kod nie realizuje tego zadania poprawnie, <m> z tego względu iż nie mamy żadnej gwarancji, <m> że taki kod nie będzie się wykonywał całkowicie równolegle, <m>'
			'czyli oba procesy nie sprawdzą dokładnie w tym samym momencie warunku <m> i w tym samym momencie nie wejdą w kod nim objęty. <m>'
			'Tak samo nie mamy gwarancji że jeden proces nie zostanie wstrzymany <m> pomiędzy sprawdzeniem warunku a ustawieniem blokady, <m>'
			'a drugi w tym momencie nie wejdzie do kodu w środku blokady, czyli tak zwanej sekcji krytycznej <m> (do której ten pierwszy też już wszedł, tylko nie zdążył jej zablokować). <m>'
			
			'Dlatego tak nie robimy, a stosujemy w tym celu rozwiązania <m> systemowe takie jak locki i semafory, czy też <m> inne mechanizmy oferowane przez używany język programowania. <m>'
		]
	},
	{
		'consoleTop': [
			[0.0, eduMovie.clear],
		],
		'consoleDown': [
			[0.0, ""],
		],
		'text' : [
			'Oprócz tworzenia pełnych kopii procesów przy pomocy fork, <m> możemy tworzyć też wątki. <m>'
			'Wątek różni się od procesu tym że w przypadku wątku mamy <m> z automatu współdzieloną całą pamięć rodzica i potomków, <m>'
			'czyli potomkowie mogą wtedy modyfikować zmienne rodzica. <m>'
			'W związku z tym powinniśmy stosować mechanizmy ochrony <m> obszarów pamięci które współdzielimy. <m>'
			'Oczywiście wątek ma też swoje zmienne prywatne, natomiast one <m> tak naprawdę są i tak przechowywane w pamięci wspólnej, <m> w związku z tym są dostępne dla innych wątków i dla rodzica <m>'
			'(tyle że rodzic oraz inne wątki nie znają ich adresów <m> – wiedzą tylko że ten fragment jest używany przez inny wątek). <m>'
			
			'W przypadku Pythona najważniejszą informacją o wątkach jest <m> taka że najpopularniejszy interpreter Pythona <m> ze swojej konstrukcji jest jednowątkowy. <m>'
			'W związku z tym jeżeli utworzymy tutaj kilka wątków, to operacje <m> używające CPU (np. zwykłe dodawanie) wykonywać w danej chwili może tylko jeden z nich. <m>'
			'Nawet jeżeli mamy odpowiednią ilość nieużywanych rdzeni procesora. <m>'
			'Efektem tego jest to iż wątki pythonowe nadają się do czekania <m> (na przykład na poznanej już funkcji select), <m> ale nie do aktywnego wykonywania równoległych obliczeń. <m>'
			'Dlatego w przypadku programowania równoległego w Pythonie <m> korzysta się z osobnych procesów a nie z wątków. <m>'
			'W praktyce oznacza to, że aby wymieniać dane trzeba <m> korzystać z tych samych mechanizmów jak przy oddzielnych procesach, <m> mimo tego że te procesy tworzą logicznie jeden program.'
		]
	},
]

