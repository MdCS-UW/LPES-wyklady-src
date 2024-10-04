# Copyright (c) 2020-2021 Matematyka dla Ciekawych Świata (http://ciekawi.icm.edu.pl/)
# Copyright (c) 2020-2024 Robert Ryszard Paciorek <rrp@opcode.eu.org>
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

prompt_txt  = eduMovie.prompt(clear=False)
userhostdir = eduMovie.prompt(prompt="", color=False)

try: clipData
except NameError: clipData = []

clipData += [
	{ 'title': [ "#01.1", "Podstawy pracy", "w terminalu", "" ] },
	
	{ 'comment': 'terminal' },
	{
		'image': [
			[0, eduMovie.convertFile('komputer.svg', margins=0)]
		],
		'text' : [
			"Komputer jest urządzeniem służącym do wykonywania <m> ciągów instrukcji składających się na program komputerowy. <m>"
			"Z punktu widzenia procesora je wykonującego, <m> mają one zawsze postać kodu maszynowego, <m> czyli numeru instrukcji do wykonania i jej argumentów. <m>"
			"Z punktu widzenia programisty, mogą być one reprezentowane <m> przez złożone instrukcje języków wyższego poziomu <m> lub wywołania funkcji bibliotecznych. <m>"
			"Natomiast z punktu widzenia użytkownika, często są nimi całe gotowe programy, czy też jakieś konkretne funkcje w ramach danego programu. <m>",
			
			"Zawsze jednak potrzebna jest metoda wprowadzenia takiego ciągu instrukcji <m> oraz odebrania wyników działania programu. <m>"
			"Dawno temu polegało to na przygotowaniu całości programu na jakimś nośniku (np. kartach perforowanych), <m>"
				"uruchomieniu komputera, a następnie odebraniu wygenerowanych wyników <m> na jakimś nośniku (np. w postaci wydruku). <m>"
			"Interakcja z komputerem ograniczała się do możliwości <m> niskopoziomowego podglądania stanu jego działania <m>"
				"i ewentualnie możliwości wpłynięcia na działanie programu, <m> z poziomu pulpitu technicznego. <m>"
			
			"Pracę interaktywną umożliwiła dopiero komunikacja tekstowa, <m> pozwalająca na prowadzenie swego rodzaju dialogu z komputerem, <m> w trakcie jego pracy. <m>"
			"Dialogu polegającego na przesyłaniu do komputera poleceń i danych <m> oraz odbieraniu wyników jego działania. <m>"
			"Urządzenie umożliwiające taką tekstową komunikację z komputerem nazywamy terminalem. <m>"
		]
	},
	{
		'image': [
			[0, eduMovie.convertFile('terminal_szeregowy_diagram.svg')]
		],
		'text' : [
			"Terminal może pracować zarówno w środowisku graficznym <m> – jako tak zwany emulator terminala, <m> działający pod kontrolą X serwera. <m>"
			"Może on także działać w ramach linuxowej wirtualnej konsoli <m> – czyli w trybie tekstowym lub pseudo tekstowym nie wymagającym środowiska graficznego <m>"
			"lub być uruchomiony na prawdziwym połączeniu czysto tekstowym, <m> takim jak na przykład port szeregowy. <m>"
			"Terminal zapewnia obsługę wejścia-wyjścia <m> czyli wprowadzania znaków (przyjmowanych typowo z klawiatury) <m> oraz wyświetlania znaków, typowo na ekranie. <m>"
			"Szczegóły tego działania zależne są od konkretnej implementacji <m> terminala i sprzętu na którym funkcjonuje. <m>"
			"Inaczej będzie realizowane działanie terminala na porcie szeregowym, <m> a inaczej w środowisku X serwera. <m>"
			"Terminal zapewnia też obsługę sekwencji sterujących <m> związanych z ruchem kursora, ustalaniem miejsca wypisywania informacji, <m> przełączania kolorów i innego formatowania tekstu. <m>"
		]
	},
	{
		'image': [
			[0, eduMovie.convertFile('terminal_szeregowy.svg', margins=0)]
		],
		'text' : [
			"W ramach terminala działają różnego rodzaju programy. <m> Podstawowym takim programem jest na ogół jakiś interpreter poleceń, nazywany również powłoką. <m>"
			"Pozwala on na uruchamianie kolejnych programów, <m> którymi mogą być też kolejne interpretery poleceń <m> zarówno tego samego jak i innego rodzaju. <m>"
			"Różne interpretery często korzystają z różnych składni <m> i różnią się tak zwanym znakiem zachęty. <m>"
		]
	},
	{
		'console': [
			[0.0, "o", prompt_txt]
		],
		'text' : [
			"Znakiem zachęty nazywamy to co jest wypisane na początku linii przed migającym kursorem, <m> który oznacza oczekiwanie na wprowadzanie tekstu. <m>"
			"Na ekranie widzimy aktualnie basha, <m> czyli chyba najpopularniejszą powłokę systemową <m> stosowaną w systemach linuksowych. <m>"
			"Bash jest zgodny ze składnią <sh>[SH] <m> i oprócz zwykłego uruchamiania innych programów <m> zapewnia między innymi także obsługę zmiennych i znaków uogólniających. <m>"
			"Standardowy znak zachęty w bashu ma postać znaku dolara (dla zwykłego użytkownika) <m> lub znaku krzyżyka (hasza) dla <root'a>[ruta]. <m>"
			"Przed znakiem zachęty w zależności od konfiguracji basha <m> mogą występować dodatkowe informacje, <m>"
				'takie jak: nazwa użytkownika na prawach którego funkcjonujemy, <m> nazwa hosta i ścieżka do katalogu w którym się znajdujemy. <m>'
			"W widocznym przykładzie nazwą użytkownika jest <rrp>[RRP], <m> nazwą hosta dragon, a bieżącym katalogiem jest <tmp>[TMP]. <m>"
			"Do rozdzielenia nazwy hosta od ścieżki użyty został dwukropek, <m> co jak się przekonamy w przyszłości, jest dość typowe. <m>"
			"Innym przykładem interpretera poleceń może być na przykład Python. <m>"
		]
	},
	{
		'console': [
			[0.386726, "o", "p"],
			[1.082962, "o", "y"],
			[1.274729, "o", "t"],
			[1.522928, "o", "h"],
			[1.779238, "o", "o"],
			[2.002661, "o", "n"],
			[3.266715, "o", "3"],
			[4.090717, "o", "\r\n"],
			[4.116192, "o", "Python 3.7.3 (default, Jul 25 2020, 13:03:44) \r\n[GCC 8.3.0] on linux\r\nType \"help\", \"copyright\", \"credits\" or \"license\" for more information.\r\n"],
			[4.145747, "o", ">>> "]
		],
		'text' : [
			"Po uruchomieniu Pythona widzimy że zmienił się znak zachęty <m> – przyjął on postać trzech znaków większości. <m>"
			"Jeżeli zakończymy działanie Pythona <m> (na przykład przy pomocy Control D, oznaczającego koniec wprowadzanych danych tekstowych) <m> to wrócimy do wcześniej używanego interpretera poleceń <m> – w tym wypadku basha. <m>"
		]
	},
	{
		'console': [
			[0.0, "o", "\r\n"],
			[0.0, "o", prompt_txt] # TODO pokazanie wciskanych klawiszy jako grafiki, polecenia z historii, ruch kursora
		],
		'text' : [
			"Jest to również sygnalizowane zmianą znaku zachęty. <m>"
			"Bash pozwala na edycję linii poleceń oraz korzystanie z historii, <m> dzięki czemu przy pomocy strzałek góra-dół <m> możemy przeglądać historię wprowadzonych poleceń, <m> a za pomocą skrótu Control R możemy ją przeszukiwać. <m>"
		]
	},
	{
		'console': [
			[0.0, eduMovie.prompt()], # TODO pokazanie wciskanych klawiszy jako grafiki
			["tab1 + 0.871946", "o", "p"],
			["tab1 + 1.191943", "o", "y"],
			["tab1 + 1.407962", "o", "t"],
			["tab1 + 2.586316", "o", "\u0007hon"],
			["tab2 + 2.3", "o", "\r\npython      python2.7   python3.7   python3m    pythontex   \r\npython2     python3     python3.7m  pythoncad   pythontex3  \r\n"],
			["tab2 + 2.3", "o", prompt_txt + "python"],
			["tab2 + 5.216088", "o", "c"],
			["tab2 + 6.33088", "o", "ad "],
		],
		'text' : [
			"Wprowadzane lub wybrane z historii polecenia możemy także edytować <m> poruszając się po nich strzałkami prawo-lewo <m> i uruchomić naciskając Enter. <m>"
			'Istotnym ułatwieniem przy wprowadzaniu poleceń <m> jest funkcja auto uzupełniania obejmująca zarówno same nazwy poleceń, <m> jak również ścieżki, a nierzadko także inne argumenty poleceń. <mark name="tab1" />'
			"Pojedyncze naciśnięcie klawisza Tab powoduje dopełnienie <m> wpisywanego tekstu, jeżeli jest ono jednoznaczne. <m>"
			'Jeżeli jest kilka możliwości, <m> dopełniony zostanie najdłuższy jednoznaczny fragment, <m> w widocznym przykładzie jest to python. <mark name="tab2" />'
			"Dwukrotne naciśnięcie klawisza Tab spowoduje wyświetlenie dostępnych możliwości. <m>"
			"Po ujednoznacznieniu możemy ponownie użyć klawisza Tab, <m> aby nastąpiło dopełnienie, i tak dalej. <m>",
			
			"Warto zauważyć że taka obsługa linii poleceń i jej historii nie jest cechą terminala, tylko samej powłoki. <m>"
			"A jako że jest to funkcjonalnośc dostarczana przez dedykowaną biblioteką można ją spotkać nie tylko w bashu ale także wielu innych programach (np. wspomnianym już Pythonie). <m>",
			
			"Oprócz samej powłoki i terminala możemy mieć także do czynienia <m> z programami określanymi jako multipleksery terminala. <m> Są one niejako pomiędzy terminalem a powłoką. <m>"
		]
	},
	{
		'console': [
			[0.05532, "o", " ^C\n\r" + eduMovie.prompt()],
			[0.917739, "o", "t"],
			[1.173472, "o", "m"],
			[1.517678, "o", "u"],
			[1.741687, "o", "x"],
			[2.534316, "o", "\r\n"],
			[2.541397, "o", "\u001b[?1049h\u001b[22;0;0t\u001b[?1h\u001b=\u001b[H\u001b[2J\u001b[?12l\u001b[?25h\u001b[?1000l\u001b[?1002l\u001b[?1006l\u001b[?1005l\u001b[c\u001b(B\u001b[m\u001b[?12;25h\u001b[?12l\u001b[?25h\u001b[?1003l\u001b[?1006l\u001b[?2004l\u001b[1;1H\u001b[1;24r\u001b]112\u0007\u001b[1;1H"],
			[2.546538, "o", "\u001b[?25l\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[37m\u001b[100m                                                                                \u001b(B\u001b[m\u001b[1;1H\u001b[?12l\u001b[?25h"],
			[2.547046, "o", "\u001b[?69h\u001b(B\u001b[m\u001b[?12;25h\u001b[?12l\u001b[?25h\u001b[?1003l\u001b[?1006l\u001b[?2004l\u001b[1;1H\u001b[1;24r\u001b[1;24r\u001b[s\u001b[1;1H"],
			[2.551242, "o", "\u001b[?25l\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[37m\u001b[100m                                                                                \u001b(B\u001b[m\u001b[1;1H\u001b[?12l\u001b[?25h"],
			[2.612277, "o", prompt_txt],
			[2.615792, "o", "\u001b[?25l\u001b[24;1H\u001b[33m\u001b[40m\u001b[1m7:0.0 \u001b(B\u001b[m\u001b[33m\u001b[40m" + userhostdir + " \u001b[37m\u001b[100m             0:bash*              \u001b[31m\u001b[40m 2021-01-13 20:20:44 UTC\u001b(B\u001b[m\u001b[1;18H\u001b[?12l\u001b[?25h"],
			[3.544789, "o", "\u001b[?25l\u001b[24;1H\u001b[33m\u001b[40m\u001b[1m7:0.0 \u001b(B\u001b[m\u001b[33m\u001b[40m" + userhostdir + " \u001b[37m\u001b[100m             0:bash*              \u001b[31m\u001b[40m 2021-01-13 20:20:45 UTC\u001b(B\u001b[m\u001b[1;18H\u001b[?12l\u001b[?25h"],
			[4.544372, "o", "\u001b[?25l\u001b[24;1H\u001b[33m\u001b[40m\u001b[1m7:0.0 \u001b(B\u001b[m\u001b[33m\u001b[40m" + userhostdir + " \u001b[37m\u001b[100m             0:bash*              \u001b[31m\u001b[40m 2021-01-13 20:20:46 UTC\u001b(B\u001b[m\u001b[1;18H\u001b[?12l\u001b[?25h"],
			[5.545748, "o", "\u001b[?25l\u001b[24;1H\u001b[33m\u001b[40m\u001b[1m7:0.0 \u001b(B\u001b[m\u001b[33m\u001b[40m" + userhostdir + " \u001b[37m\u001b[100m             0:bash*              \u001b[31m\u001b[40m 2021-01-13 20:20:47 UTC\u001b(B\u001b[m\u001b[1;18H\u001b[?12l\u001b[?25h"],
			[6.245631, "o", "\u001b[?25l\u001b[12;1H─────────────────────────────────────────\u001b[32m───────────────────────────────────────\u001b[1;1H\u001b(B\u001b[m" + prompt_txt + "\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\u001b[2B\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[33m\u001b[40m\u001b[1m7:0.1 \u001b(B\u001b[m\u001b[33m\u001b[40m" + userhostdir + " \u001b[37m\u001b[100m             0:bash*              \u001b[31m\u001b[40m 2021-01-13 20:20:47 UTC\u001b(B\u001b[m\u001b[13;1H\u001b[?12l\u001b[?25h\u001b[H\u001b[K" + prompt_txt + "\u001b[13;1H"],
			[6.316847, "o", prompt_txt],
			[6.320672, "o", "\u001b[?25l\u001b[24;1H\u001b[33m\u001b[40m\u001b[1m7:0.1 \u001b(B\u001b[m\u001b[33m\u001b[40m" + userhostdir + " \u001b[37m\u001b[100m             0:bash*              \u001b[31m\u001b[40m 2021-01-13 20:20:47 UTC\u001b(B\u001b[m\u001b[13;18H\u001b[?12l\u001b[?25h"],
			[6.545798, "o", "\u001b[?25l\u001b[24;1H\u001b[33m\u001b[40m\u001b[1m7:0.1 \u001b(B\u001b[m\u001b[33m\u001b[40m" + userhostdir + " \u001b[37m\u001b[100m             0:bash*              \u001b[31m\u001b[40m 2021-01-13 20:20:48 UTC\u001b(B\u001b[m\u001b[13;18H\u001b[?12l\u001b[?25h"],
			[7.189859, "o", "e"],
			[7.545419, "o", "\u001b[?25l\u001b[24;1H\u001b[33m\u001b[40m\u001b[1m7:0.1 \u001b(B\u001b[m\u001b[33m\u001b[40m" + userhostdir + " \u001b[37m\u001b[100m             0:bash*              \u001b[31m\u001b[40m 2021-01-13 20:20:49 UTC\u001b(B\u001b[m\u001b[13;19H\u001b[?12l\u001b[?25h"],
			[8.165949, "o", "c"],
			[8.486011, "o", "h"],
			[8.546478, "o", "\u001b[?25l\u001b[24;1H\u001b[33m\u001b[40m\u001b[1m7:0.1 \u001b(B\u001b[m\u001b[33m\u001b[40m" + userhostdir + " \u001b[37m\u001b[100m             0:bash*              \u001b[31m\u001b[40m 2021-01-13 20:20:50 UTC\u001b(B\u001b[m\u001b[13;21H\u001b[?12l\u001b[?25h"],
			[8.830487, "o", "o"],
			[9.181813, "o", " "],
			[9.543918, "o", "\u001b[?25l\u001b[24;1H\u001b[33m\u001b[40m\u001b[1m7:0.1 \u001b(B\u001b[m\u001b[33m\u001b[40m" + userhostdir + " \u001b[37m\u001b[100m             0:bash*              \u001b[31m\u001b[40m 2021-01-13 20:20:51 UTC\u001b(B\u001b[m\u001b[13;23H\u001b[?12l\u001b[?25h"],
			[9.621989, "o", "A"],
			[9.941761, "o", "\r\n"],
			[9.942614, "o", "A\r\n" + prompt_txt + ""],
			[10.546714, "o", "\u001b[?25l\u001b[24;1H\u001b[33m\u001b[40m\u001b[1m7:0.1 \u001b(B\u001b[m\u001b[33m\u001b[40m" + userhostdir + " \u001b[37m\u001b[100m             0:bash*              \u001b[31m\u001b[40m 2021-01-13 20:20:52 UTC\u001b(B\u001b[m\u001b[15;18H\u001b[?12l\u001b[?25h"],
			[10.702881, "o", "\u001b[?25l\u001b[32m\u001b[12;1H─────────────────────────────────────────\u001b[39m───────────────────────────────────────\u001b[24;1H\u001b(B\u001b[m\u001b[33m\u001b[40m\u001b[1m7:0.0 \u001b(B\u001b[m\u001b[33m\u001b[40m" + userhostdir + " \u001b[37m\u001b[100m             0:bash*              \u001b[31m\u001b[40m 2021-01-13 20:20:52 UTC\u001b(B\u001b[m\u001b[1;18H\u001b[?12l\u001b[?25h"],
			[11.463979, "o", "e"],
			[11.544199, "o", "\u001b[?25l\u001b[24;1H\u001b[33m\u001b[40m\u001b[1m7:0.0 \u001b(B\u001b[m\u001b[33m\u001b[40m" + userhostdir + " \u001b[37m\u001b[100m             0:bash*              \u001b[31m\u001b[40m 2021-01-13 20:20:53 UTC\u001b(B\u001b[m\u001b[1;19H\u001b[?12l\u001b[?25h"],
			[11.741887, "o", "c"],
			[11.933859, "o", "h"],
			[12.189882, "o", "o"],
			[12.445885, "o", " "],
			[12.546813, "o", "\u001b[?25l\u001b[24;1H\u001b[33m\u001b[40m\u001b[1m7:0.0 \u001b(B\u001b[m\u001b[33m\u001b[40m" + userhostdir + " \u001b[37m\u001b[100m             0:bash*              \u001b[31m\u001b[40m 2021-01-13 20:20:54 UTC\u001b(B\u001b[m\u001b[1;23H\u001b[?12l\u001b[?25h"],
			[12.853846, "o", "B"],
			[13.517799, "o", "\r\n"],
			[13.51809, "o", "B\r\n"],
			[13.521417, "o", "\u001b[?25l\u001b[24d\u001b[33m\u001b[40m\u001b[1m7:0.0 \u001b(B\u001b[m\u001b[33m\u001b[40m" + userhostdir + " \u001b[37m\u001b[100m             0:bash*              \u001b[31m\u001b[40m 2021-01-13 20:20:55 UTC\u001b(B\u001b[m\u001b[3;1H\u001b[?12l\u001b[?25h" + prompt_txt + ""],
			[14.246374, "o", "\u001b[?25l\u001b[12;1H─────────────────────────────────────────\u001b[32m───────────────────────────────────────\u001b[24;1H\u001b(B\u001b[m\u001b[33m\u001b[40m\u001b[1m7:0.1 \u001b(B\u001b[m\u001b[33m\u001b[40m" + userhostdir + " \u001b[37m\u001b[100m             0:bash*              \u001b[31m\u001b[40m 2021-01-13 20:20:55 UTC\u001b(B\u001b[m\u001b[15;18H\u001b[?12l\u001b[?25h"],
			[14.544826, "o", "\u001b[?25l\u001b[24;1H\u001b[33m\u001b[40m\u001b[1m7:0.1 \u001b(B\u001b[m\u001b[33m\u001b[40m" + userhostdir + " \u001b[37m\u001b[100m             0:bash*              \u001b[31m\u001b[40m 2021-01-13 20:20:56 UTC\u001b(B\u001b[m\u001b[15;18H\u001b[?12l\u001b[?25h"],
			[15.366213, "o", "\u001b[?25l\u001b[12;1H────────────────────────────────────────\u001b[32m┬───────────────────────────────────────\u001b[13;41H│\u001b[14;41H│\u001b[15;41H│\u001b[16;41H│\u001b[17;41H│\u001b[18;41H│\u001b[19;41H│\u001b[20;41H│\u001b[21;41H│\u001b[22;41H│\u001b[23;41H│\u001b[H\u001b(B\u001b[m" + prompt_txt + "echo B\u001b[K\r\nB\u001b[K\r\n" + prompt_txt + "\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\u001b[2B" + prompt_txt + "echo A                \u001b[1X\n\u001b[1K\rA\u001b[15;40H\u001b[1K\r" + prompt_txt + "\u001b[16;40H\u001b[1K\n\u001b[1K\n\u001b[1K\n\u001b[1K\n\u001b[1K\n\u001b[1K\n\u001b[1K\n\u001b[1K\u001b[13;42H\u001b[K\n\u001b[K\n\u001b[K\n\u001b[K\n\u001b[K\n\u001b[K\n\u001b[K\n\u001b[K\n\u001b[K\n\u001b[K\n\u001b[K\r\n\u001b[33m\u001b[40m\u001b[1m7:0.2 \u001b(B\u001b[m\u001b[33m\u001b[40m" + userhostdir + " \u001b[37m\u001b[100m             0:bash*              \u001b[31m\u001b[40m 2021-01-13 20:20:56 UTC\u001b(B\u001b[m\u001b[13;42H\u001b[?12l\u001b[?25h"],
			[15.366426, "o", "\u001b[15;40H\u001b[1K\r" + prompt_txt + "\u001b[13;42H"],
			[15.430381, "o", prompt_txt],
			[15.434236, "o", "\u001b[?25l\u001b[24;1H\u001b[33m\u001b[40m\u001b[1m7:0.2 \u001b(B\u001b[m\u001b[33m\u001b[40m" + userhostdir + " \u001b[37m\u001b[100m             0:bash*              \u001b[31m\u001b[40m 2021-01-13 20:20:56 UTC\u001b(B\u001b[m\u001b[13;59H\u001b[?12l\u001b[?25h"],
			[15.544961, "o", "\u001b[?25l\u001b[24;1H\u001b[33m\u001b[40m\u001b[1m7:0.2 \u001b(B\u001b[m\u001b[33m\u001b[40m" + userhostdir + " \u001b[37m\u001b[100m             0:bash*              \u001b[31m\u001b[40m 2021-01-13 20:20:57 UTC\u001b(B\u001b[m\u001b[13;59H\u001b[?12l\u001b[?25h"],
			[16.237942, "o", "e"],
			[16.544769, "o", "\u001b[?25l\u001b[24;1H\u001b[33m\u001b[40m\u001b[1m7:0.2 \u001b(B\u001b[m\u001b[33m\u001b[40m" + userhostdir + " \u001b[37m\u001b[100m             0:bash*              \u001b[31m\u001b[40m 2021-01-13 20:20:58 UTC\u001b(B\u001b[m\u001b[13;60H\u001b[?12l\u001b[?25h"],
			[16.557783, "o", "c"],
			[16.753421, "o", "h"],
			[17.061897, "o", "o"],
			[17.31793, "o", " "],
			[17.54472, "o", "\u001b[?25l\u001b[24;1H\u001b[33m\u001b[40m\u001b[1m7:0.2 \u001b(B\u001b[m\u001b[33m\u001b[40m" + userhostdir + " \u001b[37m\u001b[100m             0:bash*              \u001b[31m\u001b[40m 2021-01-13 20:20:59 UTC\u001b(B\u001b[m\u001b[13;64H\u001b[?12l\u001b[?25h"],
			[17.693923, "o", "C"],
			[18.013811, "o", "\u001b[14;42H"],
			[18.014111, "o", "C\u001b[15;42H"],
			[18.014709, "o", prompt_txt],
			[18.545791, "o", "\u001b[?25l\u001b[24;1H\u001b[33m\u001b[40m\u001b[1m7:0.2 \u001b(B\u001b[m\u001b[33m\u001b[40m" + userhostdir + " \u001b[37m\u001b[100m             0:bash*              \u001b[31m\u001b[40m 2021-01-13 20:21:00 UTC\u001b(B\u001b[m\u001b[15;59H\u001b[?12l\u001b[?25h"],
			[18.87006, "o", "logout\u001b[16;42H"],
			[18.890323, "o", "\u001b[?25l\u001b[12;1H─────────────────────────────────────────\u001b[32m───────────────────────────────────────\u001b[1;1H\u001b(B\u001b[m" + prompt_txt + "echo B\u001b[K\r\nB\u001b[K\r\n" + prompt_txt + "\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\u001b[2B" + prompt_txt + "echo A\u001b[K\r\nA\u001b[K\r\n" + prompt_txt + "\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[33m\u001b[40m\u001b[1m7:0.1 \u001b(B\u001b[m\u001b[33m\u001b[40m" + userhostdir + " \u001b[37m\u001b[100m            0:mkdir*              \u001b[31m\u001b[40m 2021-01-13 20:21:00 UTC\u001b(B\u001b[m\u001b[15;18H\u001b[?12l\u001b[?25h"],
			[18.890623, "o", "\r\u001b[K" + prompt_txt],
			[19.463375, "o", "\u001b[?25l\u001b[24;1H\u001b[33m\u001b[40m\u001b[1m7:0.1 \u001b(B\u001b[m\u001b[33m\u001b[40m" + userhostdir + " \u001b[37m\u001b[100m             0:bash*              \u001b[31m\u001b[40m 2021-01-13 20:21:00 UTC\u001b(B\u001b[m\u001b[15;18H\u001b[?12l\u001b[?25h"],
			[19.546472, "o", "\u001b[?25l\u001b[24;1H\u001b[33m\u001b[40m\u001b[1m7:0.1 \u001b(B\u001b[m\u001b[33m\u001b[40m" + userhostdir + " \u001b[37m\u001b[100m             0:bash*              \u001b[31m\u001b[40m 2021-01-13 20:21:01 UTC\u001b(B\u001b[m\u001b[15;18H\u001b[?12l\u001b[?25h"],
			[20.206293, "o", "\u001b[?25l\u001b[H\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[33m\u001b[40m\u001b[1m7:1.0 \u001b(B\u001b[m\u001b[33m\u001b[40m" + userhostdir + " \u001b[37m\u001b[100m         0:bash- 1:bash*          \u001b[31m\u001b[40m 2021-01-13 20:21:01 UTC\u001b(B\u001b[m\u001b[1;1H\u001b[?12l\u001b[?25h"],
			[20.272377, "o", prompt_txt],
			[20.276055, "o", "\u001b[?25l\u001b[24;1H\u001b[33m\u001b[40m\u001b[1m7:1.0 \u001b(B\u001b[m\u001b[33m\u001b[40m" + userhostdir + " \u001b[37m\u001b[100m         0:bash- 1:bash*          \u001b[31m\u001b[40m 2021-01-13 20:21:01 UTC\u001b(B\u001b[m\u001b[1;18H\u001b[?12l\u001b[?25h"],
			[20.542163, "o", "\u001b[?25l\u001b[24;1H\u001b[33m\u001b[40m\u001b[1m7:1.0 \u001b(B\u001b[m\u001b[33m\u001b[40m" + userhostdir + " \u001b[37m\u001b[100m         0:bash- 1:bash*          \u001b[31m\u001b[40m 2021-01-13 20:21:02 UTC\u001b(B\u001b[m\u001b[1;18H\u001b[?12l\u001b[?25h"],
			[20.894014, "o", "e"],
			[21.149792, "o", "c"],
			[21.398092, "o", "h"],
			[21.544245, "o", "\u001b[?25l\u001b[24;1H\u001b[33m\u001b[40m\u001b[1m7:1.0 \u001b(B\u001b[m\u001b[33m\u001b[40m" + userhostdir + " \u001b[37m\u001b[100m         0:bash- 1:bash*          \u001b[31m\u001b[40m 2021-01-13 20:21:03 UTC\u001b(B\u001b[m\u001b[1;21H\u001b[?12l\u001b[?25h"],
			[21.68591, "o", "o"],
			[21.941769, "o", " "],
			[22.253813, "o", "D"],
			[22.543833, "o", "\u001b[?25l\u001b[24;1H\u001b[33m\u001b[40m\u001b[1m7:1.0 \u001b(B\u001b[m\u001b[33m\u001b[40m" + userhostdir + " \u001b[37m\u001b[100m         0:bash- 1:bash*          \u001b[31m\u001b[40m 2021-01-13 20:21:04 UTC\u001b(B\u001b[m\u001b[1;24H\u001b[?12l\u001b[?25h"],
			[23.14197, "o", "\r\nD\r\n"],
			[23.142765, "o", prompt_txt],
			[23.545517, "o", "\u001b[?25l\u001b[24;1H\u001b[33m\u001b[40m\u001b[1m7:1.0 \u001b(B\u001b[m\u001b[33m\u001b[40m" + userhostdir + " \u001b[37m\u001b[100m         0:bash- 1:bash*          \u001b[31m\u001b[40m 2021-01-13 20:21:05 UTC\u001b(B\u001b[m\u001b[3;18H\u001b[?12l\u001b[?25h"],
			[23.74233, "o", "\u001b[?25l\u001b[12;1H─────────────────────────────────────────\u001b[32m───────────────────────────────────────\u001b[1;1H\u001b(B\u001b[m" + prompt_txt + "echo B\u001b[K\r\nB\u001b[K\r\n" + prompt_txt + "\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\u001b[2B" + prompt_txt + "echo A\u001b[K\r\nA\u001b[K\r\n" + prompt_txt + "\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[33m\u001b[40m\u001b[1m7:0.1 \u001b(B\u001b[m\u001b[33m\u001b[40m" + userhostdir + " \u001b[37m\u001b[100m         0:bash* 1:bash-          \u001b[31m\u001b[40m 2021-01-13 20:21:05 UTC\u001b(B\u001b[m\u001b[15;18H\u001b[?12l\u001b[?25h"],
			[24.545329, "o", "\u001b[?25l\u001b[24;1H\u001b[33m\u001b[40m\u001b[1m7:0.1 \u001b(B\u001b[m\u001b[33m\u001b[40m" + userhostdir + " \u001b[37m\u001b[100m         0:bash* 1:bash-          \u001b[31m\u001b[40m 2021-01-13 20:21:06 UTC\u001b(B\u001b[m\u001b[15;18H\u001b[?12l\u001b[?25h"],
			[25.198647, "o", "\u001b[1;24r\u001b(B\u001b[m\u001b[?1l\u001b>\u001b[H\u001b[2J\u001b]112\u0007\u001b[?12l\u001b[?25h\u001b[?1000l\u001b[?1002l\u001b[?1006l\u001b[?1005l\u001b[?69l\u001b[?1049l\u001b[23;0;0t"],
			[25.198896, "o", "[detached (from session 7)]\r\n"],
			[25.199588, "o", "\u001b]0;" + userhostdir + "\u0007"],
			[25.199747, "o", prompt_txt],
			[25.82964, "o", "tmux"],
			[26.373588, "o", " "],
			[26.653629, "o", "a"],
			[26.973813, "o", "t"],
			[27.157602, "o", "t"],
			[27.31768, "o", "a"],
			[27.637728, "o", "c"],
			[27.797586, "o", "h"],
			[28.461715, "o", "\r\n"],
			[28.465893, "o", "\u001b[?1049h\u001b[22;0;0t\u001b[?1h\u001b=\u001b[H\u001b[2J\u001b[?12l\u001b[?25h\u001b[?1000l\u001b[?1002l\u001b[?1006l\u001b[?1005l\u001b[c\u001b(B\u001b[m\u001b[?12;25h\u001b[?12l\u001b[?25h\u001b[?1003l\u001b[?1006l\u001b[?2004l\u001b[1;1H\u001b[1;24r\u001b]112\u0007\u001b[15;18H"],
			[28.469667, "o", "\u001b[?25l\u001b[12;1H─────────────────────────────────────────\u001b[32m───────────────────────────────────────\u001b[1;1H\u001b(B\u001b[m" + prompt_txt + "echo B\u001b[K\r\nB\u001b[K\r\n" + prompt_txt + "\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\u001b[2B" + prompt_txt + "echo A\u001b[K\r\nA\u001b[K\r\n" + prompt_txt + "\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[37m\u001b[100m                                                                                \u001b(B\u001b[m\u001b[15;18H\u001b[?12l\u001b[?25h"],
			[28.46989, "o", "\u001b[?69h\u001b(B\u001b[m\u001b[?12;25h\u001b[?12l\u001b[?25h\u001b[?1003l\u001b[?1006l\u001b[?2004l\u001b[1;1H\u001b[1;24r\u001b[1;24r\u001b[s\u001b[15;18H"],
			[28.470422, "o", "\u001b[?25l\u001b[12;1H─────────────────────────────────────────\u001b[32m───────────────────────────────────────\u001b[1;1H\u001b(B\u001b[m" + prompt_txt + "echo B\u001b[K\r\nB\u001b[K\r\n" + prompt_txt + "\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\u001b[2B" + prompt_txt + "echo A\u001b[K\r\nA\u001b[K\r\n" + prompt_txt + "\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[37m\u001b[100m                                                                                \u001b(B\u001b[m\u001b[15;18H\u001b[?12l\u001b[?25h"],
			[28.473317, "o", "\u001b[?25l\u001b[24;1H\u001b[33m\u001b[40m\u001b[1m7:0.1 \u001b(B\u001b[m\u001b[33m\u001b[40m" + userhostdir + " \u001b[37m\u001b[100m         0:bash* 1:bash-          \u001b[31m\u001b[40m 2021-01-13 20:21:09 UTC\u001b(B\u001b[m\u001b[15;18H\u001b[?12l\u001b[?25h"],
			[29.469481, "o", "\u001b[?25l\u001b[24;1H\u001b[33m\u001b[40m\u001b[1m7:0.1 \u001b(B\u001b[m\u001b[33m\u001b[40m" + userhostdir + " \u001b[37m\u001b[100m         0:bash* 1:bash-          \u001b[31m\u001b[40m 2021-01-13 20:21:10 UTC\u001b(B\u001b[m\u001b[15;18H\u001b[?12l\u001b[?25h"],
			[29.922399, "o", "\u001b[?25l\u001b[24;1H\u001b[33m\u001b[40m\u001b[1m7:0.1 \u001b(B\u001b[m\u001b[33m\u001b[40m" + userhostdir + " \u001b[37m\u001b[100m         0:bash* 1:bash-          \u001b[31m\u001b[40m 2021-01-13 20:21:11 UTC\u001b(B\u001b[m\u001b[15;18H\u001b[?12l\u001b[?25h"],
		],
		'text' : [
			"Pozwalają one na uzyskanie wielu okien konsoli (terminali) na pojedynczym terminalu. <m> Mogą one być wyświetlane jedno po drugim albo obok siebie zarówno w pionie jak i poziomie. <m>"
			"Innym zastosowaniem multiplekserów terminala jest możliwość <m> odłączenia się od aktywnej sesji terminala, <m> wylogowanie się z systemu (na przykład zdalnego) <m> i powrót po pewnym czasie do takiej sesji, <m> w ramach której ciągle mogły działać uruchomione w niej programy. <m>"
			"Multiplexery terminala oferują także dostęp do historii <m> tego co było wypisywane na terminalu, <m> co pozwala między innymi na zapoznanie się z wynikiem działania <m> programów z okresu kiedy byliśmy odłączeni od sesji. <m>"
			"W zależności od używanego multipleksera terminala <m> mamy różne możliwości konfiguracji tych programów. <m> Najpopularniejszymi przykładami jest screen i <tmux>[te mux]. <m> W tym wypadku prezentowany jest <tmux>[te mux]. <m>"
		]
	}
]
