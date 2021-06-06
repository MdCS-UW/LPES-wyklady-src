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
	{ 'title': [ "#01.4", "Kopiowanie,", "przenoszenie,", "usuwanie plików" ] },
	
	{ 'comment': 'cp mv rm' },
	{
		'console': [
			[0.0, ""],
			["cpA", eduMovie.runCommandString(r"# cp /skąd/kopiujemy /dokąd/kopiujemy")],
			["cpA + 1.0", eduMovie.runCommandString(r"cp /etc/passwd /tmp/")],
			["cpA + 2.0", eduMovie.runCommandString(r"ls -l /etc/passwd /tmp/passwd")],
			
			["cpB", eduMovie.runCommandString(r"cp /etc/passwd /etc/group  /tmp/")],
			["cpC", eduMovie.runCommandString(r"cp -r /etc/vim  /tmp/")],
			["cpC + 1.0", eduMovie.runCommandString(r"ls -ld /etc/vim /tmp/vim")],
		],
		'text' : [
			'Samo oglądanie zawartości file systemu – listowanie plików <m> czy też ich wyszukiwanie to nie wszystko co chcemy robić z plikami. <m>'
			'Chcemy też móc wykonywać takie operacje jak kopiowanie, przenoszenie <m> czy usuwanie plików i do tego również mamy odpowiednie komendy. <mark name="cpA" />'
			
			'Kopiowanie umożliwia nam komenda <cp>[CP] która przyjmuje <m> co najmniej dwa argumenty – ścieżkę lub nazwę pliku źródłowego oraz ścieżkę <m> lub nazwę pliku, bądź katalogu docelowego. <mark name="cpB" />'
			
			'Możemy też podać kilka plików źródłowych pod warunkiem że <m> celem będzie katalog, wtedy zostaną przekopiowane wszystkie te pliki <m> z zachowaniem swojej oryginalnej nazwy do wskazanego katalogu. <mark name="cpC" />'
			
			'Jeżeli chcemy przy pomocy <cp>[CP] kopiować katalogi musimy podać <m> opcję <-r>[minus R] czyli rekursywne kopiowanie katalogów <m> wraz z podkatalogami, kolejnymi podkatalogami i tak dalej. <m>'
			'Podobnie działa opcja <-a>[minus A], <m> przy czym zachowuje ona <m> atrybuty plików takie jak na przykład data modyfikacji, <m>'
			'a jeżeli wywołujemy ją z odpowiednimi uprawnieniami to również skopiowane zostaną <m> uprawnienia, właściciel, grupa właścicielska i tym podobne. <m>'
			
			'Standardowo <cp>[CP] nadpisze bez pytania pliki docelowe <m> (jeżeli takowe istnieją), z wyjątkiem plików tylko do odczytu <m> – w ich wypadku zapyta się o nadpisanie. <m>'
			
			'Zachowanie to można zmienić opcjami <-i>[minus I], <m> która spowoduje <m> że <cp>[CP] zawsze będzie pytał o nadpisywanie plików oraz <-f>[minus f], <m> która spowoduje że <cp>[CP] nigdy nie będzie pytał o nadpisywanie plików. <m>'
			'Stosowana jest opcja która wystąpiła jako ostatnia w linii poleceń. <m>'
		]
	},
	{
		'console': [
			[0.0, ""],
			[3.0, eduMovie.runCommandString(r"# mv /skąd/przenosimy /dokąd/przenosimy")],
			[4.0, eduMovie.runCommandString(r"mv /tmp/passwd /tmp/vim/PASS")],
			[5.0, eduMovie.runCommandString(r"ls -l /tmp/passwd /tmp/vim/PASS")],
			[13.0, eduMovie.runCommandString(r"cd /tmp;  mv group GG")],
			[14.0, eduMovie.runCommandString(r"ls /tmp/group /tmp/GG")],
		],
		'text' : [
			'Podobnie do <cp>[CP] działa komenda <mv>[MV], z tym że zamiast tworzyć kopię, <m> przenosi ona plik do innego katalogu, pod tą samą lub inną nazwą.<m>'
			'jeżeli przenoszenie jest w obrębie jednego katalogu <m> to <mv>[MV] jedynie zmienia nazwę . <m>'
			
			'Tutaj tak samo w pierwszym argumencie podajemy źródło, <m> a w drugim cel <m> którym może być nowa nazwa pliku, <m> nowa ścieżka pliku lub ścieżka do katalogu w którym plik ma zostać umieszczony. <m>'
			'Podobnie jak w <cp>[CP] gdy ostatnim argumentem jest katalog <m> to możemy podać wiele plików źródłowych, <m> które zostaną przeniesione do tego katalogu. <m>'
			
			'Przenoszenie katalogów nie wymaga stosowania żadnych dodatkowych opcji. <m>'
			'Natomiast pytanie o nadpisywanie działa tak jak w przypadku <cp>[CP]. <m>'
		]
	},
	{
		'console': [
			[0.0, eduMovie.runCommandString(r"rm /tmp/GG")],
			["rmB", eduMovie.runCommandString(r"rm /tmp/vim")],
			["rmB+1.0", eduMovie.runCommandString(r"rm -fr /tmp/vim")],
		],
		'text' : [
			'Do usuwania plików służy komenda <rm>[RM], <m> która usunie wszystkie pliki określone w jej argumentach. <m>'
			'Podobnie jak <cp>[CP] <m> to polecenie posiada opcję <-r>[minus r] służącą do <m> rekursywnego kasowania katalogu wraz z zawartością. <mark name="rmB" />'
			'Bez tej opcji <rm>[RM] odmówi kasowania katalogów. <m>'
			'Posiada także opcje <-i>[minus i] i <-f>[minus f], <m> działające analogicznie jak w przypadku <cp>[CP] i <mv>[MV]. <m>'
		]
	},
	{
		'console': [
			[0.0, eduMovie.runCommandString(r"mkdir ABCD")],
			[1.0, eduMovie.runCommandString(r"ls -ld ABCD")],
			[2.0, eduMovie.runCommandString(r"echo > ABCD/x")],
			[3.0, eduMovie.runCommandString(r"rmdir ABCD")],
			[4.0, eduMovie.runCommandString(r"rm ABCD/x")],
			[5.0, eduMovie.runCommandString(r"rmdir ABCD")],
		],
		'text' : [
			'Jeżeli chcemy utworzyć katalog możemy się posłużyć komendą <mkdir>[MK dir]. <m>'
			'Katalog możemy usunąć komendą <rmdir>[RM dir], <m> przy czym komenda ta usuwa tylko i wyłącznie katalogi puste. <m>'
		]
	},
]
