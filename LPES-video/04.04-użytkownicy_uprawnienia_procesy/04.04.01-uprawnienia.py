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
	{ 'title': [ "#04.4", "Użytkownicy", "uprawnienia", "i procesy" ] },
	
	{ 'comment': 'uprawnienia' },
	{
		'console': [
			[0.0, eduMovie.runCommandString(r"mkdir /tmp/dd")],
			[0.0, eduMovie.runCommandString(r"echo ABC > /tmp/dd/abc")],
			[0.7, eduMovie.runCommandString(r"ls -l /tmp/dd/abc")],
			
			["chmod1", eduMovie.runCommandString(r"chmod g+w,o-r /tmp/dd/abc")],
			["chmod1 + 1.0", eduMovie.runCommandString(r"ls -l /tmp/dd/abc")],
			
			["chmod2", eduMovie.runCommandString(r"chmod -R a+Xr /tmp/dd")],
			["chmod2 + 1.0", eduMovie.runCommandString(r"ls -la /tmp/dd")],
			
			["chmod3", eduMovie.runCommandString(r"chmod g=,o=w /tmp/dd/abc")],
			["chmod3 + 1.0", eduMovie.runCommandString(r"ls -l /tmp/dd/abc")],
			
			["chmod4", eduMovie.runCommandString(r"chmod 0754 /tmp/dd/abc")],
			["chmod4 + 1.0", eduMovie.runCommandString(r"ls -l /tmp/dd/abc")],
		],
		'text' : [
			'Jak pamiętamy komenda <ls>[LS] z opcją <-l>[minus l] wypisuje <m> różne informacje na temat plików, w szczególności <m> uprawnienia do pliku, jego właściciela i grupę właścicielską. <m>'
			'Uprawnienia można zmieniać przy pomocy komendy <chmod>[ceha mod]. <mark name="chmod1" />'
			'Operację którą ta komenda ma wykonać możemy wyrazić na przykład jako <m> dodanie lub zabranie jakiegoś uprawnienia danej klasie użytkowników <m>'
			'(to jest właścicielowi, grupie, lub wszystkim pozostałym) <m> przy pomocy operacji plus lub minus. <m>'
			'W prezentowanym przykładzie widzimy dodanie prawa zapisu dla grupy <m> oraz usunięcie prawa odczytu dla pozostałych. <mark name="chmod2" />'
			
			'Oznaczenia literowe są zasadniczo zgodne z tymi podawanymi przez <ls>[LS]. <m>'
			'Dodając opcję <-R>[minus R duże] możemy użyć <chmod>[ceha mod] rekurencyjnie <m> na wszystkich plikach i katalogach w podanych katalogach. <m>'
			'Wtedy wygodne może być korzystanie z oznaczenia <X>[X duże], <m> które oznacza prawo wykonywalności tylko jeżeli obiekt jest katalogiem <m> lub plikiem je posiadającym. <mark name="chmod3" />'
			
			'Możemy także użyć tej komendy do ustawienia pożądanych uprawnień <m> wyrażonych symbolicznie z użyciem znaku równości i oznaczeń literowych <mark name="chmod4" />'
				'lub numerycznie - poprzez podanie ich wartości zapisanej w systemie ósemkowym. <m>'
			'Pierwsza od lewej cyfra jest opcjonalna i wyraża dodatkowe flagi <m> związane z uprawnieniami, kolejna oznacza uprawnienia właściciela, <m> następna grupy, a ostatnia wszystkich pozostałych. <m>'
			'Każda z trzech ostatnich cyfr jest sumą wartości: <m> <1>[jeden] dla prawa wykonywalności, <2>[dwa] dla prawa zapisu i <4>[cztery] dla prawa odczytu. <m>'
			
			'Prawo zapisu do katalogu oznacza prawo tworzenia w nim plików <m> oraz kasowania plików się w nim znajdujących, <m> typowo także takich do których nie mamy praw. <m>'
			'Zatem domyślnie prawo zapisu w katalogu pozwala nam <m> na nadpisanie pliku dla którego nie mamy prawa zapisu. <m>'
			'Zachowanie to może być zmienione dodaniem <m> odpowiedniej flagi w uprawnieniach katalogu. <m>'
		]
	},
	{
		'console': [
			[0.0, eduMovie.runCommandString(r"cd /tmp")],
			[0.7, eduMovie.runCommandString(r"echo 'echo Hello' > xyz", cwd="/tmp")],
			[1.9, eduMovie.runCommandString(r"chmod +x xyz", cwd="/tmp")],
			
			[3.0, eduMovie.runCommandString(r"/tmp/xyz", cwd="/tmp")],
			[3.9, eduMovie.runCommandString(r"xyz", cwd="/tmp")],
			[4.5, eduMovie.runCommandString(r"./xyz", cwd="/tmp")],
			
			["path", eduMovie.runCommandString(r"echo $PATH", cwd="/tmp")],
			
			["python1", eduMovie.runCommandString(r"""echo 'print("Hello")' > xyz""", cwd="/tmp")],
			["python1a", eduMovie.runCommandString(r"./xyz", cwd="/tmp")],
			
			["python2", eduMovie.runCommandString(r"""echo '#!/usr/bin/python3' > xyz""", cwd="/tmp")],
			["python2 + 0.5", eduMovie.runCommandString(r"""echo 'print("Hello")' >> xyz""", cwd="/tmp")],
			["python2 + 1.7", eduMovie.runCommandString(r"cat xyz", cwd="/tmp")],
			["python2 + 3.3", eduMovie.runCommandString(r"./xyz", cwd="/tmp")],
			
			["python3", eduMovie.runCommandString(r"""echo '#!/usr/bin/env python3' > xyz""", cwd="/tmp")],
			["python3 + 0.5", eduMovie.runCommandString(r"""echo 'print("Hello")' >> xyz""", cwd="/tmp")],
			["python3 + 1.7", eduMovie.runCommandString(r"cat xyz", cwd="/tmp")],
			["python3 + 3.3", eduMovie.runCommandString(r"./xyz", cwd="/tmp")],
			
			["bezx1", eduMovie.runCommandString(r"chmod -x xyz; ls -l xyz", cwd="/tmp")],
			["bezx1 + 1.5", eduMovie.runCommandString(r"python3 xyz", cwd="/tmp")],
			
			["bezx2", eduMovie.runCommandString(r"cp /bin/ls abc; chmod a-x abc; ls -l abc", cwd="/tmp")],
			["bezx2 + 1.5", eduMovie.runCommandString(r"./abc", cwd="/tmp")],
			["bezx2 + 3.3", eduMovie.runCommandString(r"/lib64/ld-linux-x86-64.so.2 ./abc  | head", cwd="/tmp")],
		],
		'text' : [
			'Jeżeli plik ma prawo wykonywalności, to możemy go uruchomić <m> poprzez podanie ścieżki do tego pliku, ale nie poprzez jego nazwę. <m>'
			'Jeżeli plik jest w bieżącym katalogu to i tak musimy określić go <m> poprzez ścieżkę, ponieważ bash nie traktuje jako ścieżek <m> nazw poleceń nie zawierających ukośnika. <m>'
			'Bash zakłada w takim przypadku że są to nazwy poleceń wbudowanych, funkcji <m> lub programów znajdujących się w ścieżce wyszukiwania, <m> określonej zmienną PATH. <mark name="path" />'
			'Natomiast katalog bieżący zazwyczaj nie znajduje się w ścieżce wyszukiwania. <m>'
			'Oczywiście można by dodać kropkę do zmiennej PATH, <m> jednak nie jest to zalecane i typowo pliki z katalogu bieżącego <m> uruchamiamy podając do nich ścieżkę względną postaci <./nazwa_pliku>[kropka ukośnik nazwa pliku]. <mark name="python1" />'
			
			'Jeżeli nasz skrypt nie będzie skryptem zgodnym z <sh>[es ha], <m> tylko na przykład, tak jak widzimy na ekranie, skryptem pythonowym <mark name="python1a" />'
				'to próba jego uruchomienia zakończy się błędem <m> związanym z tym iż bash nie rozumie tej składni. <mark name="python2" />'
			
			'Problem ten rozwiązuje się poprzez umieszczenie w pierwszej linii pliku <m> komentarza sterującego w postaci <#!ścieżka>[hash wykrzyknik ścieżka] do interpretera, <m> który ma być użyty do wykonania danego pliku. <m>'
			'W linii tej możemy też dodać wymagane przez ten interpreter opcje. <m>'
			'Komentarz taki spowoduje że system uruchomi podaną w tej linii komendę <m> wraz z podanymi opcjami i doda argument będący ścieżką do uruchamianego pliku. <mark name="python3" />'
			
			'Jeżeli chcemy żeby nasz skrypt był uruchamiany domyślną wersją pythona <m> ustaloną w oparciu o zmienną PATH zamiast podawać wprost ścieżkę do niego <m> możemy wykorzystać program <env>[enw] w sposób widoczny na ekranie. <m>'
			
			'Warto mieć świadomość że interpretacja tego komentarza <m> sterującego odbywa się na poziomie systemowym. <m>'
			'Czyli jak do funkcji <os.execv>[os kropka exec v] w Pythonie <m> podamy ścieżkę do skryptu bashowego z takim komentarzem, <m>'
			'to zostanie on poprawnie zinterpretowany i Python zostanie <m> zastąpiony bashem który wykona treść takiego skryptu. <mark name="bezx1" />'
			
			'Warto zaznaczyć iż brak prawa wykonywalności <m> nie oznacza braku możliwości wykonania pliku. <m>'
			'W przypadku skryptów wystarczy jawne uruchomienie <m> interpretera i wskazanie mu takiego pliku. <mark name="bezx2" />'
			
			'Pliki binarne bez prawa wykonywalności również daje się wykonywać <m> – służy do tego odpowiedni plik biblioteki linkera, <m> który możemy znaleźć w katalogu z bibliotekami systemowymi. <m>'
		]
	},
	{
		'console': [
			[0.0, eduMovie.runCommandString(r"ls -l /tmp/xyz")],
			[1.0, eduMovie.runCommandString(r"chown root /tmp/xyz")],
			["grp + 3", eduMovie.runCommandString(r"chgrp sudo /tmp/xyz")],
			["grp + 4.7", eduMovie.runCommandString(r"ls -l /tmp/xyz")],
			["acl", eduMovie.runCommandString(r"getfacl /tmp/xyz")],
		],
		'text' : [
			'Właściciela pliku możemy zmienić poleceniem <chown>[czeha own], <m> ale w praktyce może tego dokonać jedynie root. <mark name="grp" />'
			'Grupę możemy zmienić poleceniem <chgrp>[czeha GRP], aby móc zmienić <m> grupę właścicielską należy być właścicielem pliku <m> i należeć do grupy którą się ustawia. <m>'
			
			'Oprócz podstawowych praw do plików mamy też <m> uprawnienia rozszerzone, czyli listy kontroli dostępu do pliku. <m>'
			'Pozwalają one na ustawienie indywidualnych uprawnień <m> dla każdego użytkownika w systemie, a także między innymi <m> na wymuszenie uprawnień domyślnych. <mark name="acl" />'
			'Do ich obsługi służą polecenia <getfacl>[get f ACL] i <setfacl>[set f ACL]. <m>'
			'Na uprawnienia do pliku wpływ mogą też mieć inne mechanizmy, <m> takie jak selinux, apparmor, atrybuty systemu plików <m> i atrybuty związane z właściwościami jądra. <m>'
		]
	},
]
