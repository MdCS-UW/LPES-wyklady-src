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

eduMovie.runCommandString(r"rm -fr /tmp/linki; mkdir /tmp/linki")

try: clipData
except NameError: clipData = []

clipData += [
	{ 'section': 'linki twarde i symboliczne' },
	{
		'console': [
			[0.0, ""]
		],
		'text' : [
			'Ostatnią rzeczą związaną z tego typu operacjami na plikach jest <m> tworzenie linków, czyli odniesień do jakiś plików z użyciem innej ścieżki. <m>'
			
			'Do tworzenia linków służy komenda <ln>[LN] <m> która ma składnie analogiczną do <cp>[CP] <m> czyli również podajemy pliki źródłowe a później podajemy cel. <m>'
			'Plików źródłowych również może być kilka <m> pod warunkiem że cel jest katalogiem. <m>'
			
			'Do ważniejszych opcji <ln>[LN] należy zaliczyć <-s>[minus s], <m> która tworzy linki symboliczne zamiast domyślnych linków twardych <m>'
			'oraz <-r>[minus r], która powoduje użycie ścieżki względnej <m> w tworzonych linkach symbolicznych. <m>'
			
			'Warto zauważyć iż w odróżnieniu od <cp>[CP], polecenie <ln>[LN] <m> nie ma opcji do działania rekurencyjnego – jeżeli chcemy utworzyć kopie katalogu, <m>'
			'w której zamiast kopiowania plików tworzone byłyby linki do nich <m> to możemy wywołać <cp>[CP] z odpowiednimi opcjami. <m>'
		]
	},
	{
		'image': [
			[0.0, eduMovie.convertFile("../../LPES-booklets/images-src/linux/link_twardy_i_symboliczny.svg", dpi=160)],
		],
		'text' : [
			'Należy powiedzieć kilka słów o tym jak działają linki, <m> oraz czym się różnią linki twarde od linków symbolicznych. <m>'
			
			'Link twardy <m> jest innym dowiązaniem na te same dane na dysku twardym. <m>'
			'Mamy tutaj kilka poziomów dostępu do danych znajdujących się na dysku twardym <m> – fizyczną lokalizację tych danych gdzieś na dysku, <m>'
			'coś co można by w uproszczeniu nazwać uchwytem do takich danych <m>(nazywany <i-node>[aj nołd]), <m>'
			"oraz wpis w katalogu, który określa nazwę pliku <m> i odnośnik go odpowiedniego uchwytu (<i-node'a>[aj nołda]). <m>"
			
			'Link twardy, który widzimy na ilustracji zaznaczony kolorem czerwonym, <m> utworzony komendą <ln plik2.txt link1.txt>[L N plik dwa TXT link jeden TXT], <m>'
			'stanowi po prostu kolejne dowiązanie <m> do tych samych danych do których dowiązaniem był <plik2.txt>[plik dwa TXT]. <m>'
			
			'Ze względu na taką naturę linków twardych ograniczają się one <m> do pojedynczego systemu plików (urządzenia) na którym znajdują się dane. <m>'
			'Typowo nie jest również dopuszczalne tworzenie linków twardych do katalogów.'
		]
	},
	{
		'console': [
			[0.0, eduMovie.runCommandString(r"echo 'ABC 123' > plik2.txt", cwd="/tmp/linki")],
			[0.5, eduMovie.runCommandString(r"ls -l", cwd="/tmp/linki")],
			["link1", eduMovie.runCommandString(r"ln plik2.txt link1.txt", cwd="/tmp/linki")],
			["link1ls", eduMovie.runCommandString(r"ls -l", cwd="/tmp/linki")],
			["link1cat", eduMovie.runCommandString(r"cat link1.txt", cwd="/tmp/linki")],
			["link1mod", eduMovie.runCommandString(r"echo 'XYZ' >> plik2.txt", cwd="/tmp/linki")],
			["link1mod + 1.3", eduMovie.runCommandString(r"cat link1.txt", cwd="/tmp/linki")],
			["link1rm", eduMovie.runCommandString(r"rm plik2.txt", cwd="/tmp/linki")],
			["link1rm + 2", eduMovie.runCommandString(r"cat link1.txt", cwd="/tmp/linki")],
			["link1rm + 3.7", eduMovie.runCommandString(r"ls -l", cwd="/tmp/linki")],
			["lsla", eduMovie.runCommandString(r"ls -la", cwd="/tmp/linki")],
		],
		'text' : [
			'Spróbujmy utworzyć link twardy. <mark name="link1" />'
			'Należy pamiętać że najpierw podajemy plik do którego tworzymy link, <m> a później podajemy nazwę lub ścieżkę do tworzonego linku <m> – analogicznie jak w komendzie <cp>[CP] czy <mv>[MV]. <mark name="link1ls" />'
			
			'W wyniku polecenia <ls>[LS] widzimy że powstał plik <link1.txt>[link jeden TXT], <m> ale również zmieniła się pewna informacja <m> dotycząca oryginalnego pliku <plik2.txt>[plik dwa TXT]. <m>'
			'Poprzednio pomiędzy uprawnieniami a nazwą właściciela mieliśmy jedynkę, <m> a teraz mamy dwójkę. <m> Ta liczba wskazuje nam ilość <m> dowiązań do danych związanych z danym plikiem. <m>'
			'Warto zauważyć iż rozmiar oraz uprawnienia obu plików są takie same. <mark name="link1cat" />'
			
			'Jeżeli wypiszemy dane z <link1.txt>[link jeden TXT] dostaniemy <m> dokładnie to co mamy w oryginalnym pliku. <mark name="link1mod" />'
			'Jeżeli do pliku coś dopiszemy w <link1.txt>[link jeden TXT] także się to pojawia. <mark name="link1rm" />'
			
			'Nawet jeżeli skasujemy oryginalny plik to z użyciem <m> linku twardego nadal mamy dostęp do danych. <m> Zmieniła się natomiast ilość dowiązań <m> i wynosi ona teraz jeden. <m>'
			'Dane zostaną usunięte (a dokładniej oznaczone jako do nadpisania) <m> w momencie gdy ten licznik odwołań spadnie do zera. <m>'
			'Jak widać, link twardy jest równoważny oryginalnemu plikowi, <m> ale dane na dysku twardym trzymane są tylko w jednym miejscu. <mark name="lsla" />'
			
			'Warto także zwrócić uwagę na wpisy związane z kropką i dwiema kropkami <m> – są to automatycznie tworzone dowiązania typu link twardy <m> odpowiednio do katalogu bieżącego i nadrzędnego. <m>'
			'Liczba dowiązań do kropki to 2 plus liczba podkatalogów, <m> a liczba dowiązań do dwóch kropek równa jest <m> liczbie dowiązań do kropki w katalogu nadrzędnym. <m>'
		]
	},
	{
		'image': [
			[0.0, eduMovie.convertFile("../../LPES-booklets/images-src/linux/link_twardy_i_symboliczny.svg", dpi=160)],
		],
		'text' : [
			'Link symboliczny, który widzimy na ilustracji zaznaczony kolorem niebieskim, <m> stanowi wpis w strukturze katalogu informujący że pod daną nazwą <m> (w naszym przykładzie <link2.txt>[link dwa kropka TXT]) jest odniesienie do innej ścieżki <m> (w naszym przykładzie <./plik1.txt>[kropka ukośnik plik jeden kropka TXT]). <m> Jest on w istocie odniesieniem do innej ścieżki, a nie danych na dysku jako takich. <m>'
			
			'Dzięki takim cechom linki te mogą wskazywać <m> na pliki położone na innych urządzeniach, systemach plików. <m>'
			'Linki symboliczne możemy tworzyć do dowolnych <m> obiektów w systemie plików – także katalogów. <m>'
		]
	},
	{
		'console': [
			[0.0, eduMovie.runCommandString(r"echo 'abc 123' > plik1.txt", cwd="/tmp/linki")],
			[1.0, eduMovie.runCommandString(r"ln -s ./plik1.txt link2.txt", cwd="/tmp/linki")],
			[1.5, eduMovie.runCommandString(r"ls -l", cwd="/tmp/linki")],
			
			["linksymmod", eduMovie.runCommandString(r"cat link2.txt", cwd="/tmp/linki")],
			["linksymmod + 1", eduMovie.runCommandString(r"echo '000' > link2.txt", cwd="/tmp/linki")],
			["linksymmod + 2", eduMovie.runCommandString(r"cat plik1.txt", cwd="/tmp/linki")],
			
			["linksymdu", eduMovie.runCommandString(r"du -h link2.txt", cwd="/tmp/linki")],
			
			["linksymrm", eduMovie.runCommandString(r"rm plik1.txt", cwd="/tmp/linki")],
			["linksymrm + 2.0", eduMovie.runCommandString(r"cat link2.txt", cwd="/tmp/linki")],
			["linksymrm + 3.0", eduMovie.runCommandString(r"ls -l", cwd="/tmp/linki")],
		],
		'text' : [
			'Link symboliczny tworzymy podobnie jak link twardy, <m> tyle że dodajemy opcję <-s>[minus s]. <m>'
			
			'Jak widzimy, <m> link symboliczny jest pokazywany inaczej przez <ls>[LS] <m>'
			'– ma inny rozmiar niż nasz plik źródłowy, a dodatkowo <ls>[LS] wskazuje że jest to <m> link symboliczny poprzez oznaczenie typu pliku jako l <m> i podanie ścieżki na którą wskazuje. <mark name="linksymmod" />'
			'Link symboliczny funkcjonuje podobnie do linku twardego, <m> zapewniając dostęp do tych samych danych przez dwie różne ścieżki. <mark name="linksymdu" />'
			
			'Podawany rozmiar linku symbolicznego wynika z długości przechowywanej ścieżki <m> – tyle danych zawiera sam link symboliczny, natomiast rozmiar pokazywany przez <du>[D U] <m> dla linku symbolicznego będzie wynosił zero, <m>'
			'gdyż sam link nie zajmuje osobnego miejsca na dysku, <m> a jedynie zwiększa rozmiar zajmowany przez strukturę opisującą katalog. <m>'
			
			'Należy mieć świadomość, iż w przypadku linków symbolicznych nie mamy <m> takiego podobieństwa linku do obiektu na który wskazuje ten link, <m> jak w przypadku linków twardych. <mark name="linksymrm" />'
			'W przypadku linków symbolicznych, usunięcie pliku na który wskazywał link, <m> czy też nawet zmiana lokalizacji bądź nazwy takiego pliku, <m>'
			'prowadzi do tego że link symboliczny staje się linkiem zerwanym <m> i tracimy dostęp do danych z wykorzystaniem tego linku. <m>'
			'Jeżeli plik na który wskazywał link zostanie skutecznie usunięty, <m> czyli nie będzie ani tego pliku ani linków twardych do niego to dane też zostaną usunięte, <m>'
			'bez względu na to czy już wskazywały na nie jakieś linki symboliczne, czy nie. <m>'
		]
	},
	{
		'console': [
			["symlinkproblem + 0.0", eduMovie.runCommandString(r"mkdir abc", cwd="/tmp/linki")],
			["symlinkproblem + 1.0", eduMovie.runCommandString(r"ln ./plik2.txt podkatalog/link.txt", cwd="/tmp/linki")],
			["symlinkproblem + 2.0", eduMovie.runCommandString(r"cat podkatalog/link.txt", cwd="/tmp/linki")],
			["symlinkproblem + 3.0", eduMovie.runCommandString(r"ls -l podkatalog", cwd="/tmp/linki")],
		],
		'text' : [
			'Polecenie <ln>[LN] standardowo zapisze do tworzonego linku <m> literalnie podaną w linii poleceń ścieżkę. <m>'
			'Oznacza to że możemy tworzyć linki symboliczne do nieistniejących plików, <m> ale też przez pomyłkę możemy utworzyć błędne dowiązania. <mark name="symlinkproblem" />'
			
			'Należy mieć świadomość iż ścieżki względne zapisane w linku <m> nie są interpretowane względem bieżącego katalogu roboczego, <m> czy nawet katalogu użytego w ścieżce dostępu do linku <m>'
			'a względem katalogu w którym znajduje się link. <m>'
		]
		# INNY przykład:
		#   mkdir -p aa/xx; echo "A"> aa/p; ln -s ../p aa/xx/l; cat aa/xx/l
		#   mkdir -p bb; echo "B"> bb/p; ln -s ../aa/xx bb/xx; cat bb/xx/l
		# odniesienie do bb/xx/l ( l wskazuje na ../p) nie wskazuje na bb/p, ale na aa/p bo xx jest linkiem do aa, więc l jest fizycznie w aa/xx
	},
]

