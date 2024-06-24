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
	{ 'section': 'kod powrotu \n i łączenie poleceń' },
	{
		'console': [
			[0.0, eduMovie.clear + eduMovie.prompt()],
			[12.0, eduMovie.runCommandString(r"ls /etc/passwd; echo $?")],
			[16.0, eduMovie.runCommandString(r"ls /etc/BŁĘDNYPLIK; echo $?")],
		],
		'text' : [
			'Kolejnym tematem związanym z standardowym zachowaniem programów <m> jest pojęcie kodu powrotu polecenia, <m> czyli to czy komenda zakończyła się sukcesem czy porażką. <m>'
			'Typowo każdy program w systemach uniksowych <m> zwraca nam kod powrotu w postaci numerycznej. <m>'
			'Jeżeli ten kod wynosi 0 to oznacza to że komenda zakończyła się sukcesem, <m> jeżeli jest różny od zera oznacza to że komenda zakończyła się niepowodzeniem, <m> a wartość tego kodu może określać jakie to było niepowodzenie. <m>'
			'Kod ten możemy sobie wypisać przy pomocy dolar pytajnik. <m>'
			'W przykładzie prezentowanym na ekranie widzimy że dla <ls>[L S] <m> oraz istniejącego pliku kod ten był zero, czyli sukces, <m> a dla nie istniejącego pliku wynosił dwa <m> czyli informował o zakończeniu polecenia z błędem. <m>'
		]
	},
	{
		'console': [
			[0.0, ""],
			["_and", eduMovie.runCommandString(r"ls /etc/passwd && echo OK")],
			["_and + 1.0", eduMovie.runCommandString(r"ls /etc/BŁĘDNYPLIK && echo OK")],
			["_or", eduMovie.runCommandString(r"ls /etc/passwd || echo NOT OK")],
			["_or + 1.0", eduMovie.runCommandString(r"ls /etc/BŁĘDNYPLIK || echo NOT OK")],
		],
		'text' : [
			'Kod powrotu pozwala nam też na kilka sposobów łączenia poleceń <m> innych niż przekierowania strumieni pomiędzy poleceniami. <m>'
			'Łączenie to opiera się nie na przepływie danych <m> (jak było przy strumieniach), a na informacji <m> czy program zakończył się sukcesem czy porażką. <mark name="_and" />'
			
			'Rozdzielenie poleceń przy pomocy dwóch znaków ampersand <m> (pisanych bez spacji pomiędzy nimi) <m> spowoduje wykonanie polecenia znajdującego się po ich prawej stronie <m> wtedy i tylko wtedy gdy polecenie po lewej stronie zakończyło się sukcesem. <mark name="_or" />'
			
			'Rozdzielenie poleceń przy pomocy dwóch pionowych kresek <m> (pisanych bez spacji pomiędzy nimi) <m> spowoduje wykonanie polecenia znajdującego się po ich prawej stronie <m> wtedy i tylko wtedy gdy polecenie po lewej stronie zakończyło się porażką. <m>'
		]
	},
	{
		'console': [
			[0.0, ""],
			["srednik", eduMovie.runCommandString(r"echo ABC; echo 123")],
		],
		'text' : [
			'Innymi sposobami łączenia poleceń, <m> już nie związanymi z kodami powrotu, <m> jest średnik i pojedynczy ampersand. <m>'
			'Dokładniej mówiąc są to nie tyle metody łączenia poleceń co ich kończenia, <m> gdyż nie wymagają one aby po ich prawej stronie znajdowała się kolejne polecenie. <mark name="srednik" />'
			'Polecenia rozdzielane średnikami będą wykonywane kolejno <m> bez względu na ich efekt, <m> czyli tak jakbyśmy wpisywali je kolejno w terminalu po zakończeniu poprzedniego. <m>'
			'W przypadku zapisu poleceń w pliku <m> średnik jest zasadniczo równoważny znakowi nowej linii, <m> który oddziela polecenia w taki sam sposób. <m>'
		]
	},
	{
		'console': [
			[0.0, eduMovie.runCommandString(r"echo ABC & echo 123")],
		],
		'text' : [
			'Ampersand powoduje uruchomienie poprzedzającego go polecenia w tle <m> i oddanie przez niego terminala co pozwala na przykład na <m> uruchomienie kolejnego polecenia. <m>'
		]
	},
	{
		'image': [
			[0.0, "w_tle.mp4"],
		],
		'text' : [
			'W związku z tym polecenia oddzielane <m> ampersandami będą wykonywane równolegle. <m> Dokładniej mogą być wykonywane równolegle, <m> bo zależy to jeszcze od dostępności CPU. <m>'
			'Bash może wypisać także pewne dodatkowe informacje związane z <m> uruchomieniem komendy w tle, na razie nie będziemy się nimi zajmować. <m>',
			'Zauważ, że z poziomu linii poleceń basha <m> możemy uruchamiać nie tylko standardowe polecenia trybu tekstowego, <m> ale dowolne programy, także te działające w środowisku graficznym. <m>'
			'Te ostatnie często pozwalają na przekazanie w ten sposób argumentów, <m> np. pliku do otwarcia, lub dodatkowych opcji, <m> np. pozwalających na automatyzację ich działania. <m>',
			'Stosowanie spacji przed i po operatorach łączących polecenia jest opcjonalne. <m>'
			'Powszechnie stosowany jest zwyczaj zapisywania spacji po obu <m> stronach operatorów łączących polecenia w oparciu o kod powrotu <m> oraz przekierowujących strumień pomiędzy nimi, <m>'
			'a jedynie po prawej stronie pojedynczego średnika i ampersanda. <m>'
		]
	},
]
