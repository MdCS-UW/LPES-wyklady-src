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
	{ 'section': 'polecenie find' },
	{
		'console': [
			[0.0, ""],
			[11.0, eduMovie.runCommandString(r"find", cwd='demo')],
		],
		'text' : [
			'Oprócz listowania plików w znanej lokalizacji przydatna jest też <m> możliwość wyszukiwania plików w oparciu o ich parametry, <m> takie jak nazwa pliku, data modyfikacji, rozmiar, itp. <m>'
			'Pozwala na to polecenie find. <m> Przeszukuje ono rekurencyjnie wskazany katalog <m> (lub katalog bieżący jeżeli w linii poleceń nie został wskazany inny) <m> w poszukiwaniu plików spełniających podane warunki. <m>'
			'Warunki standardowo łączone są spójnikiem AND <m> czyli muszą być spełnione wszystkie. <m> Find bez podanych warunków wylistuje rekurencyjnie wszystkie pliki <m> z podanego katalogu.'
		]
	},
	{
		'console': [
			[0.0, ""],
			["find_e0", eduMovie.runCommandString(r"find -name cc*", cwd='demo')],
			["find_e1", eduMovie.runCommandString(r"find -name ab*", cwd='demo')],
			["find_e2", eduMovie.runCommandString(r"find -name bb*", cwd='demo')],
			["find_ok", eduMovie.runCommandString(r"find -name 'cc*'", cwd='demo')],
			["find_ok+1", eduMovie.runCommandString(r"find -name 'ab*'", cwd='demo')],
			["find_ok+2", eduMovie.runCommandString(r"find -name 'bb*'", cwd='demo')],
		],
		'text' : [
			'Warunek <-name>[minus name] służy do określenia nazwy pliku, <m> czyli zostaną wypisane tylko pliki o pasującej nazwie. <m> Nazwę możemy określić bezpośrednio lub z użyciem znaków uogólniających powłoki. <m>'
			'Należy tutaj pamiętać iż musimy przekazać to wyrażenie <m> do polecenia find w postaci nie rozwiniętej przez powłokę. <m>'
			'W przykładzie na ekranie widać, że jeżeli argument warunku name <mark name="find_e0"/> jest nie zabezpieczony przed interpretacją przez powłokę to możemy <m>'
			'otrzymać poprawne wyniki, jeżeli w bieżącym katalogu nie ma nazw pasujących do wyrażenia, <mark name="find_e1"/>'
			'dostać komunikat o błędzie, jeżeli do wyrażenia pasuje wiele nazw w bieżącym katalogu, <mark name="find_e2"/>'
			'lub dostać niepoprawne wyniki jeżeli do wyrażenia dopasowana została jedna nazwa. <mark name="find_ok"/>'
			
			'Jeżeli zabezpieczymy argument przed interpretacją przez powłokę, <m> to jak widać w prezentowanym przykładzie, <m> w każdym z tych przypadków dostaniemy poprawne wyniki. <m>'
		]
	},
	{
		'console': [
			[0.0, eduMovie.runCommandString(r"find -iname 'al*'", cwd='demo')],
			["path", eduMovie.runCommandString(r"find -path '*xx*'", cwd='demo')],
			["path2", eduMovie.runCommandString(r"find -path '*/xx*/*'", cwd='demo')],
		],
		'text' : [
			'Mamy również warunek <-iname>[minus iname] który działa analogicznie <m> jak name ale ignoruje wielkość liter, <m> czyli traktuje wielkie i małe litery jako równoważne. <mark name="path"/>'
			
			'Jeżeli chcemy szukać nie według nazwy pliku, <m> a według tego że ścieżka do danego pliku coś zawiera mamy warunek <-path>[minus path]. <m>'
			'Analogicznie jak w przypadku warunku name dopasowanie <m> było robione do pełnej nazwy pliku, tak w przypadku path <m> dopasowanie jest robione do pełnej ścieżki, a nie do elementu tej ścieżki. <mark name="path2"/>'
			'Zatem jeżeli chcemy wyszukać pliki w katalogach których nazwa <m> zaczyna się na przykład na <xx>[iks iks] to w argumencie warunku musimy <m> pozwolić na dopasowanie dowolnego początku ścieżki przy pomocy gwiazdki, <m>'
			'następnie dać ukośnik oznaczający początek kolejnego elementu ścieżki, <m> <xx>[iks iks] oznaczający początek nazwy katalogu, gwiazdkę dopasowującą resztę tej nazwy, <m>'
			'ukośnik kończący nazwę katalogu i gwiazdkę dopasowującą resztę ścieżki. <m>'
			
			'Analogicznie do path działa warunek <-ipath>[minus ipath], który nie rozróżnia wielkości liter. <m>'
		]
	},
	{
		'console': [
			[0.0, ""],
			["type + 3", eduMovie.runCommandString(r"find -type d", cwd='demo')],
			["size", eduMovie.runCommandString(r"find -type f -size +15c -size -2k", cwd='demo')],
		],
		'text' : [
			'Polecenie find oferuje także warunki do wyszukiwania w oparciu o <m> dopasowanie ścieżki do wyrażenia regularnego oraz wymagania określonego typu pliku. <mark name="type"/>'
			'Typ pliku możemy określić przy pomocy warunku <-type>[minus type], <m> gdzie jako argument podajemy jednoliterowe określenie typu pliku. <m>'
			'Przez typ pliku rozumiemy tutaj to czy jest to <m> zwykły plik (oznaczany literą f), katalog (oznaczany d), link symboliczny <m> (o których będziemy mówić w dalszej części zajęć), czy jeszcze inny obiekt. <mark name="size"/>'
			
			'Dostępne są także warunki do wyszukiwania po <m> czasie modyfikacji lub utworzenia pliku oraz jego rozmiarze. <m>'
			'Na przykład <find -size  +15c -size -2k>[find minus size plus 15 c minus size minus 2 k] <m> wyszuka pliki większe od 15 bajtów, ale równocześnie mniejsze niż 2 kilobajty. <m>'
			
			'Ogólnie w argumentach opcji związanych z rozmiarem, czasem, itp. <m> plus będzie oznaczał większe niż a minus mniejsze niż. <m>'
		]
	},
	{
		'console': [
			[0.0, eduMovie.runCommandString(r"find -type f -size +15c -size -2k -exec ls -ldh \{\} \;", cwd='demo')],
			["zabezp", eduMovie.runCommandString(r"find -type f -size +15c -size -2k -exec ls -ldh '{} ;'", cwd='demo')],
			["zabezp + 1", eduMovie.runCommandString(r"find -type f -size +15c -size -2k -exec ls -ldh '{}' ';'", cwd='demo')],
			["execdir", eduMovie.runCommandString(r"find -type f -size +15c -size -2k -execdir ls -ldh \{\} \;", cwd='demo')],
		],
		'text' : [
			'Bardzo użytecznym warunkiem polecenia find jest <-exec>[minus exec], <m> który pozwala na uruchomienie dowolnego polecenia <m> i przekazanie do niego ścieżki do wyszukanego pliku. <m>'
			'Warunek ten jako swój argument przyjmuje polecenie, <m> które ma zostać uruchomione, polecenie to musi być zakończone średnikiem <m>'
			"(zabezpieczonym przed zinterpretowaniem go przez powłokę uruchamiającą finda), <m> natomiast pod klamerki (także zabezpieczone odwrotnymi ukośnikami) <m> zostanie podstawiona ścieżka do wyszukanego pliku. <m>"
			'Na ekranie widzimy przykład wykorzystania tego warunku <m> do wyświetlenia szczegółów na temat wyszukanych plików. <mark name="zabezp"/>'
			
			'Do zabezpieczenia klamerek i średnika można oczywiście użyć także cudzysłowów, <m> należy jednak pamiętać że klamerki i średnik muszą się znaleźć w osobnych napisach. <m>'
			'Zabezpieczenie klamerek nie zawsze jest wymagane. <mark name="execdir"/>'
			
			'Podobnie do warunku exec działa warunek <-execdir>[minus exec dir], <m> jednak w odróżnieniu od exec wchodzi on najpierw do katalogu zawierającego wyszukany plik <m>'
			'i dopiero w nim uruchamia wskazaną komendę przekazując do niej ścieżkę <m> względem tamtego katalogu postaci kropka ukośnik nazwa wyszukanego pliku. <m>'
		]
	},
	{
		'console': [
			[0.0, eduMovie.runCommandString(r"find -exec false \; -execdir ls -ldh \{\} \;", cwd='demo')],
			[1.7, eduMovie.runCommandString(r"find -exec true \; -execdir ls -ldh \{\} \;", cwd='demo')],
			["print", eduMovie.runCommandString(r"find -print -exec false \; -exec echo PLIK 2 \{\} \;", cwd='demo')],
		],
		'text' : [
			'Warto zauważyć że zarówno exec jak i <execdir>[exec dir] są warunkami, <m> czyli możemy je wykorzystać do testowania właściwości plików <m> nie obsługiwanych bezpośrednio przez komendę find <m>'
				'(na przykład długości pliku audio lub video, rozmiaru obrazka w pikselach). <m>'
			'Działają one w oparciu o kod powrotu uruchamianego polecenia <m> – jeżeli uruchomione polecenie zwróciło kod zero, warunek jest spełniony. <m>'
			'Na ekranie widzimy wywołania find gdzie w ramach exec zostały użyte <m> polecenia false i true, zwracające odpowiednio zawsze fałsz i prawdę. <m>'
			
			'Używając warunków exec i <execdir>[exec dir] należy pamiętać że wyłączają one <m> domyślne zachowanie find polegające na wypisywaniu znalezionych plików. <m>'
			'Możemy je wypisać używając na przykład warunku <-print>[minus print] <mark name="print"/>'
			
			'Należy też zauważyć że find sprawdza warunki po kolei <m> – od lewej do prawej do napotkania pierwszego który nie został spełniony. <m>'
			'Dlatego w pokazanym na ekranie przykładzie warunek print <m> wykonany został dla wszystkich plików, natomiast exec echo dla żadnego <m> bo poprzedni exec zawsze zwracał false i przerywał dalsze sprawdzanie warunków. <m>'
		]
	},
]
