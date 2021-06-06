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
	{ 'title': [ "#04.1", "Operacje", "na plikach", "(tekstowych)" ] },
	
	{ 'comment': 'grep' },
	{
		'console': [
			[0.0, ""],
			["grep", eduMovie.runCommandString(r"grep '^s[sf]' /etc/passwd", hiddenargs="--color=always")],
		],
		'text' : [
			'Poznane wcześniej polecenie find pozwala wyszukiwać pliki <m> w oparciu o ich zewnętrzne atrybuty, takie jak nazwa, rozmiar, itp. <m>'
			'Nie pozwala ono jednak na przeszukiwanie zawartości plików, <m> czy też wyszukiwanie ich w oparciu o zawartość. <mark name="grep" />'
			
			'Funkcjonalność taką oferuje polecenie grep, <m> umożliwia ono przeszukiwanie plików w oparciu o wyrażenia regularne. <m>'
			'Wyrażenia regularne już poznaliśmy w ramach zajęć <m> poświęconych programowaniu w Pythonie. <m>'
			'I dobrą wiadomością jest to że grep używa bardzo podobnych <m> a z odpowiednim przełącznikiem nawet takich samych wyrażeń regularnych. <m>'
			
			'Tak samo jak w Pythonie kropka oznacza dowolny znak, <m> gwiazdka dowolną także zerową ilość powtórzeń, itd. <m>'
			"Jako że przynajmniej niektóre ze znaków używanych w wyrażeniach <m> regularnych są znakami specjalnymi dla powłoki, <m> wyrażenia przekazywane do grep'a warto ujmować w apostrofy. <m>"
			
			"Na ekranie widzimy wywołanie grep'a, które wypisuje z pliku </etc/passwd>[e te ce pass wu de] <m> linie pasujące do podanego wyrażenia regularnego. <m>"
			'Wyrażenie to wymaga aby na początku dopasowywanego napisu <m> (czyli w przypadku grepa na początku linii) <m> znajdowała się litera <s>[es] a po niej kolejne <s>[es] lub <f>[ef]. <m>'
		]
	},
	{
		'console': [
			[0.0, eduMovie.runCommandString(r"grep -v '^[a-s]' /etc/passwd", hiddenargs="--color=always")],
			["minusi - 1.3", eduMovie.runCommandString(r"grep 'mail' /etc/passwd", hiddenargs="--color=always")],
			["minusi", eduMovie.runCommandString(r"grep -i 'mail' /etc/passwd", hiddenargs="--color=always")],
			["greprekursywny", eduMovie.runCommandString(r"grep -r 'messagebus' /etc/  2>/dev/null", hiddenargs="--color=always")],
			["greprekursywny2", eduMovie.runCommandString(r"grep -rl 'messagebus' /etc/  2>/dev/null", hiddenargs="--color=always")],
		],
		'text' : [
			"Z ważniejszych opcji grep'a należy wspomnieć o <m>"
				'<-v>[minus V], które powoduje wypisywanie linii niepasujących do podanego wyrażenia regularnego (zamiast linii pasujących) oraz <mark name="minusi" />'
				'<-i>[minus I], które spowoduje ignorowanie wielkości liter. <m>'
			
			"Możemy również wymusić przeszukiwanie przez grep'a <m> plików binarnych, tak jakby były plikami tekstowymi, "
				"czyli jeżeli grep'owi wydaje się że plik jest plikiem binarnym <m> to możemy nakazać mu potraktować ten plik jak plik tekstowy. <m>"
			'Służy do tego opcja <-a>[minus A]. <mark name="greprekursywny" />'
			
			'Opcja <-r>[minus R] pozwala na rekursywne przeszukiwanie podanych katalogów, <mark name="greprekursywny2" />'
				'opcja <-l>[minus L małe] pozwala na wypisanie <m> jedynie ścieżek do plików w których było dopasowanie, <m>'
				'a opcja <-L>[minus L duże] tych w których dopasowania nie było. <m>'
			'Warto zauważyć iż małe l wraz z v nie równoważy dużego L, <m> gdyż opcja <-v>[minus V] działa per linia, a opcje <-l, -L>[minus L] per plik. <m>'
			
			'W pokazanym przykładzie zignorowane <m> (poprzez przekierowanie do </dev/null>[dev null]) <m> zostały błędy związane z brakiem dostępu do pewnych plików w <etc>[e te ce]. <m>'
			'Zwykły użytkownik nie może czytać niektórych <m> podkatalogów <etc>[e te ce] i jest to normalne. <m>'
		]
	},
	{
		'console': [
			["minusP", eduMovie.runCommandString(r"grep 'ro.*t' /etc/passwd", hiddenargs="--color=always")],
			["minusP2", eduMovie.runCommandString(r"grep -P 'ro.*?t' /etc/passwd", hiddenargs="--color=always")],
			
			["minusE", eduMovie.runCommandString(r"grep -E '(r..t).*\1' /etc/passwd", hiddenargs="--color=always")],
			["minusE + 1", eduMovie.runCommandString(r"grep '\(r..t\).*\1' /etc/passwd", hiddenargs="--color=always")],
			
			["minusE + 4", eduMovie.runCommandString(r"grep -E '\(ad.*\)' /etc/passwd", hiddenargs="--color=always")],
			["minusE + 5", eduMovie.runCommandString(r"grep '(ad.*)' /etc/passwd", hiddenargs="--color=always")],
		],
		'text' : [
			"Grep potrafi korzystać z trzech dialektów wyrażeń regularnych <m> - podstawowych, rozszerzonych i perl'owskich. <m>"
			"Domyślnie grep korzysta z wyrażeń podstawowych, <m> wyrażenia rozszerzone możemy włączyć opcją <-E>[minus E duże], a perl'owskie <-P>[minus P duże]. <m>"
			
			'''Najbardziej podobne do tego czego uczyliśmy się na zajęciach <m> związanych z pythonem są wyrażenia perl'owskie <mark name="minusP" /> - zadziałają w nich podwyrażenia grupowane nawiasami okrągłymi, <m>'''
				'krotności powtórzeń wyrażane w nawiasach klamrowych, <mark name="minusP2" /> a także nie zachłanne dopasowania z użyciem gwiazdka pytajnik. <m>'
			
			"Wyrażenia rozszerzone są niejako pomiędzy perl'owskimi a podstawowymi <m> - nie obsługują dopasowań nie zachłannych, <m> natomiast reszta będzie działała w taki sposób <m> w jaki używaliśmy wyrażeń regularnych w Pythonie. <m>"
			
			'Z kolei wyrażenia podstawowe pozwalają w zasadzie na to samo <m> co rozszerzone, różnią się jednak zapisem. <mark name="minusE" />'
			'Niektóre ze znaków sterujących używanych w wyrażeniach rozszerzonych <m> (na przykład nawiasy okrągłe, klamrowe, pytajnik) <m>'
				'aby pozostały znakami sterującymi w wyrażeniach podstawowych muszą <m> zostać poprzedzone odwrotnym ukośnikiem. <m>'
			'Inaczej będą traktowane jak zwykłe znaki. <m> Z kolei jeżeli chcemy je traktować jak zwykłe znaki w wyrażeniach <m> rozszerzonych to muszą w nich być poprzedzane odwrotnym ukośnikiem. <m>'

			'Wynika to oczywiście z tak zwanej kompatybilności wstecznej. <m>'
			'Grep pierwotnie traktował pytajnik jako pytajnik, <m> zatem później kiedy wymyślono dla niego znaczenie specjalne, <m> nie mógł zacząć traktować go jako znaku specjalnego. <m>'
			'Gdyż wszystkie programy używające grepa, w których pytajnik <m> był traktowany jako zwykły znak, mogły przestać działać. <m>'
			'W związku z tym zostały wprowadzone wyrażenia rozszerzone <m> w których pytajnik stał się znakiem specjalnym, <m>'
				'a w podstawowych jako znak sterujący postanowiono traktować eskejpowany pytajnik, <m> czyli ciąg odwrotny ukośnik pytajnik. <m>'

			'Jak zwykle szczegóły można przeczytać w dokumentacji systemowej man. <m>'
		]
	},
	{
		'console': [
			[0.0, eduMovie.runCommandString(r"echo abcdef | grep --color cd | grep a")],
			[1.0, eduMovie.runCommandString(r"echo abcdef | grep --color=always cd | grep a")],
			[2.0, eduMovie.runCommandString(r"echo abcdef | grep --color=always cd | grep de")],
		],
		'text' : [
			'To czy grep domyślnie koloruje swoje wyjście, czy nie, <m> zależy od ustawień na danym systemie. <m> Kolorowanie można włączyć lub wyłączyć opcją <--color>[minus minus kolor]. <m>'
			'Standardowo kolorowanie jest wyłączane jeżeli wyjście grepa <m> jest przekierowywane do innych poleceń. <m> Dodając argument always opcji <color>[kolor] możemy wymusić <m> aby działało także w takiej sytuacji. <m>'
			
			'Jednak należy pamiętać że kolorowanie odbywa się poprzez <m> dodanie do napisu specjalnych sekwencji sterujących. <m>'
			'W związku z tym przekierowanie kolorowego wyjścia <m> na przykład do kolejnego grepa, tak jak pokazano na ekranie, <m> może spowodować niewłaściwe funkcjonowanie. <m>'
			'W widocznym przykładzie ciąg <de>[D E] nie został znaleziony, <m> gdyż pomiędzy <d>[de] a <e>[E] jest sekwencja kończąca kolorowanie. <m>'
		]
	},
]
