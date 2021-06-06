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
	{ 'section': 'tunelowanie' },
	{
		'image': [
			[0.0, ""],
			["tunele", eduMovie.convertFile('tunele.svg')]
		],
		'text' : [
			'Jak pamiętamy dane przesyłane wewnątrz pakietu IP, czy może raczej <m> TCP lub UDP (bo surowe IP jest rzadko używane) mogą być dowolne. <m>'
			'W szczególności może to być pakiet IP. <m>'
			'Przysyłanie pakietów IP wewnątrz innych pakietów IP pozwala na tworzenie <m> wirtualnych połączeń punkt-punkt dla naszych sieci poprzez sieć rozległą. <m>'
			'Takie tunelowanie pakietów IP jest właśnie podstawą <VPN>[Vi Pi eN], <m> czyli wirtualnych sieci prywatnych. <m>'
			
			'Jeżeli jest potrzeba to w ten sposób możemy <m> przesyłać nawet ramki warstwy drugiej. <m>'
			'Często przed włożeniem takiego pakietu bądź ramki do pola danych <m> pakietu w którym będzie przesyłany jest on szyfrowany, ale nie jest to wymogiem <m> – istnieją i są stosowane tunele nie szyfrowane. <m>'
			'Często także taki przesyłany w ten sposób pakiet jest obudowywany <m> jakąś dodatkową strukturą protokołu używanego do takiego przesyłania. <m>'
			
			'Dawno temu mówiliśmy o poleceniu SSH pozwalającym między innymi <m> na pracę zdalną, czyli wykonywanie poleceń, uruchamianie programów i tak dalej <m> na systemie do którego łączymy się poprzez sieć. <mark name="tunele" />'
			
			'Wspomnieliśmy wtedy o opcjach <-D>[minus d duże] i <-L>[minus l duże], służących do zestawiania tuneli. <m>'
			'Pierwsza z nich tworzy tunel dynamiczny, <m> udostępniając na kliencie interfejs zgodny z standardem SOCKS, <m> który przekazuje połączenia poprzez wskazany serwer SSH. <m>'
			'Druga pozwala na zestawienie tunelu umożliwiającego przekazywanie ruchu TCP <m> do wskazanego numeru portu na wskazanym hoście za pośrednictwem serwera SSH <m>'
				'oraz przesyłanych w drugą stronę odpowiedzi, <m> związanych z tak nawiązanym połączeniem TCP. <m>'
			'SSH oczywiście szyfruje tak przekazywany ruch. <m>',
			
			'Nie powiedzieliśmy wtedy jednak o dwóch kolejnych <m> opcjach związanych z tunelowaniem, czyli <-R>[minus r duże] i <-w>[minus wu małe]. <m>'
			'Pierwsza z nich jest trochę podobna do opcji <-L>[minus l duże], <m> tyle że klient i serwer SSH zamieniają się trochę rolami. <m>'
			'Wskazany numer portu zostanie otwarty po stronie serwera SSH, <m> a pakiety będą przekierowywane do odpowiedniego portu wskazanego hosta, <m> dostępnego po stronie klienta SSH. <m>'
			
			'Są to bardzo przydatne tunele, jednak mają swoje ograniczenia. <m>'
			'Tunele  <-L>[minus l duże] i <-R>[minus r duże] wymagają tworzenia <m> osobnego tunelu dla każdego portu, dla którego chcemy uzyskać takie połączenie <m> oraz tunelują jedynie TCP. <m>'
			'Tunel <-D>[minus d duże] wymaga wsparcia protokołu SOCKS <m> w aplikacji nawiązującej połączenie. <m>'
			
			'Innym rozwiązaniem, umożliwiającym pełne tunelowanie ruchu IP, <m> czy nawet ruchu L2 jest opcja <-w>[minus wu małe]. <m>'
			'SSH z taką opcją użyje wskazanych urządzeń sieciowych <m> do utworzenia tunelu pomiędzy klientem i serwerem. <m>'
			'Oczywiście użytkownik wywołujący SSH musi mieć <m> odpowiednie uprawnienia do tych urządzeń lub do ich tworzenia. <m>'
			
			'W przypadku tunelowania IP, co jest opcją domyślną będą to urządzenia tun <m> z numerami wskazanymi w argumentach opcji <-w>[minus wu]. <m>'
			'Jeżeli podamy dodatkowo opcję <-o Tunnel=ethernet>[minus o Tunnel równa się eternet] będą to urządzenia tap <m> z wskazanymi numerami, umożliwiające tunelowanie ramek <ethernetowych>[eternetowych]. <m>'
			
			'W ten sposób SSH pozwala nam na stworzenie pełnoprawnego połączenia <VPN>[Vi Pi eN]. <m>'
			'Innym popularnym oprogramowaniem do tego celu jest <OpenVPN>[Open Vi Pi eN]. <m>'
			'Działa on analogicznie do SSH z opcją <-w>[minus wu], <m> tyle że dodatkowo automatyzuje kwestię konfiguracji <m> tak tworzonych interfejsów, zarządzanie ich numerami <m>'
				'oraz samego procesu tworzenia, wymaganych uprawnień i tak dalej. <m>'
			
			'Rozwiązania tego typu są stosowane w celu dostępu do sieci prywatnych <m> oraz do wychodzenia na świat z innego adresu IP niż używany lokalnie <m>'
				'(np. udawania że jest się w innym kraju, celem ominięcia blokad geolokalizacyjnych). <m>'
		]
	},
]
