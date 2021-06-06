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
	{ 'comment': 'procesy' },
	{
		'image': [
			[0.0, ""]
		],
		'text' : [
			"To tyle podstawowych informacji na temat samego startu systemu operacyjnego. <m>"
			"Należy powiedzieć także trochę na temat jego funkcji. <m>"
			
			"Mówiliśmy już o procesach – proces jest działającym, <m> bądź gotowym do działania, oczekującym kodem programu. <m>"
			"Wspomnieliśmy też o procesach typu Zombie, <m> czyli pozostałościach po procesach, których działanie zakończyło się, <m> ale czekają na odbiór kodu powrotu przez rodzica. <m>"
			"To właśnie system operacyjny odpowiedzialny jest za zarządzanie procesami. <m>"
			
			"Jedną z funkcji systemu operacyjnego jest szeregowanie zadań <m> czyli pilnowanie tego żeby procesy były uruchamiane naprzemiennie. <m>"
			"Zasadniczo polega to na decydowaniu które z gotowych <m> do działania procesów mają uzyskać dostęp do procesora. <m>"
			"Na przykład jeżeli mamy tylko 4 rdzenie, a 10 programów chce coś robić, <m> to system operacyjny musi zapewnić przełączanie tych programów <m> w taki sposób aby w miarę sprawiedliwie dostawały one czas procesora. <m>"
			"W tym celu stosowane są różne algorytmy szeregowania zadań, <m> natomiast w szczegóły raczej nie będziemy się na razie wdawać. <m>"
			"Należy jednak mieć świadomość że jest to jedno z istotniejszych zadań <m> systemu operacyjnego oraz że administrator systemu także ma jakiś wpływ <m> na to zarówno z jakimi priorytetami <szeregowane>[szerego'wane] są poszczególne procesy <m>"
			"(można to robić chociażby poprzez komendę nice albo ustawianie <m> priorytetów czasu rzeczywistego dla danych procesów) <m> jak również na to jakie algorytmy są używane przez nasz system operacyjny. <m>"
			
			"Dodatkowo system musi uwzględniać fakt że proces może czekać <m> na jakieś wydarzenie (np. odczyt danych z pliku, lub odebranie ich <m> poprzez interfejs sieciowy) i odpowiednio to czekanie obsługiwać. <m>"
			"Proces taki staje się gotowym do działania <m> dopiero po tym zdarzeniu lub ustawionym timeoucie. <m>"
			
			"System operacyjny zapewnia także obsługę plików, dostępu do nich <m> oraz obsługę różnych urządzeń wejścia-wyjścia (np. sieci komputerowych). <m>"
			"W Linuxie zasadniczo wszystko jest plikiem – przekonamy się o tym <m> także przy programowaniu sieciowym, gdzie połączenia sieciowe <m> będziemy obsługiwali tak jak pliki, <m>"
				"w szczególności będziemy używali poznanej już funkcji select, <m> zapewniającej takie czekanie na dane w jednym z kilku otwartych plików. <m>"
		]
	},
	{ 'section': 'kończenie i wstrzymywanie\nprocesu' },
	{
		'image': [
			[0.0, ""]
		],
		'text' : [
			"Wspominaliśmy już o takich skrótach klawiaturowych jak <m> Control C i Control D. <m>"
			"Pierwszy z nich wysyła sygnał do procesu proszący go <m> o zakończenie się (sygnał ten może być zignorowany). <m>"
			"Drugi nie wysyła sygnału, ale (wprowadzony w pustej linii) <m> informuje proces czytający jakieś dane, oczekujący na te dane <m> że nastąpił ich koniec <m>"
				"(tak jakby przy czytaniu danych z pliku osiągnięto koniec tego pliku). <m>"
			"Warto rozróżniać te skróty, gdyż informacja o zakończeniu <m> danych wejściowych pozwala programowi na przetworzenie <m> wczytanych danych i wypisanie wyników. <m>"
			
			"Mamy również Control <Z>[zet], który także wysyła sygnał do procesu, <m> ale nie proszący go o zakończenie się, tylko zawieszający jego wykonywanie. <m>"
			"Proces zawieszony nadal zajmuje przydzielone mu zasoby <m> (w szczególności pamięć), więc Control <Z>[zet] nie jest dobrą metodą kończenia programów. <m>"
			"Za to mamy możliwość wznowienia tak przerwanego programu <m> odpowiednim sygnałem, bądź poleceniami <fg>[FG] lub <bg>[BG]. <m>"
			"Pierwsze z nich wznawia proces w taki sposób że zajmuje <m> on ponownie terminal, a drugie w taki sposób że zostaje on przeniesiony w tło, <m>"
				"a w terminalu możemy wykonywać inne operacje <m> (czyli tak jak byśmy przy uruchamianiu tamtego programu dodali ampersand). <m>"
		]
	},
]
