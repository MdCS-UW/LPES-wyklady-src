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
	{ 'section': 'Standardowe interfejsy \n szeregowe' },
	{
		'image': [
			[0.0, ""],
			["spi", eduMovie.convertFile("../../LPES-booklets/images-src/elektronika/spi.sch", dpi=180, negate=True)],
		],
		'text' : [
			'Współcześnie zdecydowana większość interfejsów to interfejsy szeregowe. <m>'
			'Istnieje kilka powszechnie stosowanych standardów <m> prostych interfejsów szeregowych, z którymi warto się zapoznać. <mark name="spi" />'
			
			'Pierwszym przykładem będzie magistrala <SPI>[eS Pi aj], czyli Serial Peripheral Interface. <m>'
			'Magistrala ta składa się z osobnych linii odbioru i nadawania <m> określanych jako <MOSI>[mosi] i MISO, linii zegara SCK <m> oraz sygnału aktywującego dane urządzenie określanego jako chip select. <m>'
			
			'Linia <MOSI>[mosi] to linia używana do nadawania przez mastera <m> i odbioru przez urządzenia slave, <m> linia MISO to linia na której nadaje aktywny slave a odbiera master. <m>'
			'Zegar podawany jest przez mastera i jest wspólny dla transmisji w obu kierunkach. <m>'
			'Sygnał chip select oznacza że dany slave ma reagować na rzeczy transmitowane <m> przez mastera, w szczególności na nie odpowiadać używając linii MISO. <m>'
			'Slave który nie otrzymuje chip select zobowiązany jest <m> ignorować komunikację <SPI>[eS Pi aj] i nie nadawać. <m>'
			
			'Jeżeli na magistrali mamy wiele urządzeń slave, do ich adresowania <m> możemy użyć układu dekodera, który od mastera otrzyma numer układu, <m> który ma być zaadresowany i aktywuje odpowiedni układ. <m>'
			"W ten sposób mając na przykład 8 układów slave, <m> zamiast 8 linii do ich adresowania, master musi dysponować tylko trzema <m> liniami do wystawienia zakodowanego binarnie numeru danego slave'a."
		]
	},
	{
		'image': [
			[0.0, eduMovie.convertFile("../../LPES-booklets/images-src/elektronika/twi.sch", dpi=95, negate=True)],
			["onewire", eduMovie.convertFile("../../LPES-booklets/images-src/elektronika/onewire.sch", dpi=190, negate=True)],
		],
		'text' : [
			'Inną często stosowaną i bardzo użyteczną magistralą jest <I2C>[i kwadrat c], <m> która posiada tylko dwie linie – dwukierunkową linię danych i linię zegara. <m>'
			'Adresacja odbywa się z użyciem określonego protokołu wewnątrz danych. <m>'
			
			'Obie linie są typu open kolektor, co zapewnia duże równouprawnienie układów <m> do niej podłączonych – zasadniczo każdy z nich może pełnić rolę mastera. <m>'
			'W związku z stosowaniem linii open kolektor konieczne jest <m> użycie zewnętrznych rezystorów podciągających, <m> bo poszczególne układy zwierają daną linię jedynie do masy. <m>'
			'Możemy jednak dzięki temu bez obaw łączyć wiele układów w ramach tej magistrali <m> i każdy z nich mógłby nadawać co tylko chce i kiedy chce. <m>'
			
			'Oczywiście takie działanie prowadziłoby do konfliktów <m> i wzajemnego zagłuszania się poszczególnych układów, <m>'
				'dlatego w magistrali takiej wyróżnia się jeden lub kilka układów <m> pełniących funkcję mastera, czyli generujących zegar i inicjujących transmisję <m> z użyciem adresu odpowiedniego układu typu slave. <m>'
			
			'Magistrala i2c nazywana jest również TWI. <m>'
			'Wiąże się to z tym że <I2C>[i kwadrat c] jest zastrzeżonym znakiem towarowym <m> i pomimo tego że patenty co do standardu technicznego wygasły, <m>'
				'więc każdy może używać tej magistrali bez ponoszenia opłat licencyjnych, <m> ale nie każdy może ją nazywać <I2C>[i kwadrat c]. <m>'
			'Dlatego wielu producentów określają jako TWI, czyli Two Wire Interface, <m> od tego że używa ona dwóch przewodów. <m>'
			'Pod względem technicznym jest to dokładnie ta sama magistrala co <I2C>[i kwadrat c]. <mark name="onewire" />'
			
			'Kolejną magistralą o której warto powiedzieć jest <One>[łan] Wire, <m> w którym konstruktorzy poszli jeszcze dalej i zrezygnowali z linii zegarowej. <m>'
			'Jest to magistrala asynchroniczna, czyli układy mają własne zegary, <m> które są jedynie synchronizowane specjalnym stanem na linii danych <m> i w oparciu o które rozpoznają transmitowane dane. <m>'
			'Linia danych w tym wypadku jest także typu open kolektor <m> i dodatkowo może być użyta do zasilania układów. <m>'
		]
	},
	{
		'image': [
			[0.0, eduMovie.convertFile("../../LPES-booklets/images-src/elektronika/uart1.sch", dpi=170, negate=True)],
			["uart2", eduMovie.convertFile("../../LPES-booklets/images-src/elektronika/uart2.sch", dpi=120, negate=True)],
			["usbpci", ""], # TODO jakiś slajd z USB, PCI, SATA, ... (zdjęcia ?)
		],
		'text' : [
			'Innym bardzo istotnym standardem transmisji szeregowej jest <UART>[uart], <m> niekiedy nawet <USART>[usart], czyli uniwersalny asynchroniczny odbiornik nadajnik, <m> bądź uniwersalny synchroniczny asynchroniczny odbiornik nadajnik. <m>'
			'Generalnie <UART>[uart] określa sposób przesyłu grupy bitów <m> (na przykład jednego bajtu) asynchronicznym łączem, <m> czyli linią sygnałową bez związanej z nią linii zegarowej. <m>'
			
			'Może on występować w różnych odmianach elektrycznych. <m>'
			'Najprostszą z nich jest tak zwany <UART>[uart] TTL czyli interfejs działający <m> z poziomami logicznymi danego układu i złożony najczęściej z dwóch linii: <m> TX i RX służących odpowiednio do odbioru i nadawania. <m>'
			
			'Aby skomunikować dwa urządzenia z jego pomocą, przy założeniu że <m> operują na tych samych poziomach logicznych, należy TX jednego z nich <m> połączyć z RX drugiego oraz drugi RX z drugim TX. <m>'
			'Wyjątkiem jest sytuacja gdy w jednym z urządzeń nazwy te "dla wygody" <m> zostały zamienione, tak jak na przykład w modemach. <m>'
			'Należy też skonfigurować w taki sam sposób interfejsy w obu urządzeniach, <m> czyli ustawić tą samą prędkość, ilość bitów danych, <m> ilość bitów stopu i tak dalej. <mark name="uart2" />'
			
			'W bardziej rozbudowanej formie interfejs ten może zapewniać <m> sprzętowe sterowanie przepływem, czyli wymianę informacji o gotowości do <m> odbioru danych z użyciem dodatkowych sygnałów CTS i RTS. <m>'
			
			'Niektóre mikrokontrolery obsługują rozbudowany wariant <UART>[uart], <m> czyli <USART>[usart] pozwalający także na transmisję synchroniczną <m> i posiadający dodatkowo sygnał zegarowy. <m>'
			'Niekiedy wspierany jest też jednoprzewodowy <UART>[uart] <m> ze wspólną linią nadawania i odbioru typu open kolektor. <m>'
			
			'<UART>[uart] jest wykorzystywany razem z wieloma różnymi <m> standardami elektrycznymi dla takiej magistrali. <m>'
			'Może ona występować jako <RS232>[RS dwa trzy dwa], <m> czyli ten standard który występował kiedyś w komputerach PC jako porty COM, <m> używane między innymi do podłączenia modemu czy myszek. <m>'
			'Może być też w standardzie <RS422>[RS cztery dwa dwa] albo <485>[cztery osiem pięć], <m> które z kolei korzystają z transmisji różnicowej full duplex albo half duplex, <m> w zależności od użytego rozwiązania i ilości przewodów. <m>'
			
			'<RS232>[RS dwa trzy dwa] jest standardem dosyć starym, wywodzącym się z dalekopisów <m> i przyjmuje bardzo oryginalne poziomy logiczne: jedynka jest to napięcie <m> od minus 15 do minus 3 woltów, a zero od 3 do 15 woltów. <m>'
			'Pomiędzy minus 3 a plus 3 wolty mamy stan nieustalony <m> który nie powinien być interpretowany ani jako zero ani jako jedynka. <m>'
			'<RS232>[RS dwa trzy dwa] zapewnia też wiele dodatkowych sygnałów sterujących <m> pracą modemu, kontrolą przepływu i tak dalej, <m> ale najczęściej współcześnie wykorzystywane są tylko RX i TX. <mark name="usbpci" />'
			
			'Oczywiście mamy też takie interfejsy jak USB, PCI express, <SATA>[sata], <HDMI>[ha-de-em-i], Ethernet, <m> które także są interfejsami szeregowymi, <m> ale nie będziemy ich dokładniej omawiać. <m>'
			'Z wyjątkiem <ethernetu>[eternetu], o którym na trochę wyższej warstwie, <m> niż poziom elektrycznego sygnału, pomówimy przy sieciach komputerowych. <m>'
		]
	},
]
