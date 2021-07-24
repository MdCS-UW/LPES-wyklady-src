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
	{ 'title': [ "#11.1", "", "Ethernet", "" ] },
	
	{ 'comment': 'ethernet 1' },
	{
		'image': [
			[0.0, eduMovie.convertFile('ethernet1.svg', margins=0)],
			["ramka", eduMovie.convertFile('../../LPES-booklets/extra-tex-files/booklets-sections/network/ilustracje/40-ethernet.tex', margins=12, dpi=100)],
			["arp", eduMovie.convertFile('arp.svg', negate=True)],
		],
		'text' : [
			'Najpopularniejszym obecnie standardem warstwy dostępu do sieci jest Ethernet. <m>'
			'Standard ten określa dwie pierwsze warstwy w modelu <OSI>[O S I]. <m>'
			'Warstwa pierwsza związana jest z fizycznym przesyłem sygnału, <m> na przykład przy pomocy skrętki zakończonej złączem RJ45 <m> lub przy pomocy sygnału wifi 2.4 gigaherca albo 5 gigaherców. <mark name="ramka" />'
			'Przy czym są to dwie najpopularniejsze odmiany warstwy fizycznej Ethernetu <m> i każda z nich dzieli się na kilka lub kilkanaście standardów z których każdy opisuje różną prędkość. <m>'
			'Przykładowo Ethernet przesyłany po skrętce może być standardem <10BASE-T>[ten bejs ti], <100BASE-T>[handred bejs ti] lub <1000BASE-T>[tausend bejs ti], <m> zależnie czy jest to łącze 10, 100 czy 1000 <Mbps>[megabitów na sekundę]. <m>'
			'Dodatkowo istnieją też inne standardy o innych końcówkach w nazwie, <m> dotyczące na przykład przesyłania ramek Ethernetowych po światłowodach, <m> ścieżkach na płytkach drukowanych lub innych kablach. <m>'
			'Warstwa druga określa format ramki <ethernetowej>[eternetowej], adresy warstwy L2, <m> rozwiązywanie problemu kolizji w dostępie do medium transmisyjnego i tak dalej. <m>'
			
			'Adresy warstwy L2 w <ethernecie>[eternecie] nazywane są adresami sprzętowymi <m> lub adresami <MAC>[mak], gdyż standardowo taki unikalny adres dla danego <m> urządzenia sieciowego przydzielany jest przez producenta. <m>'
			'Są to adresy <48>[czterdziesto ośmio] bitowe zapisywane w notacji dwukropkowej, <m> gdzie każdy bajt zapisywany jest jako dwie cyfry szesnastkowe <m> i oddzielany od innych dwukropkiem. <m>'
			'W odróżnieniu od <IPv6>[IP v6] nie stosujemy tutaj kompresji zer do dwóch dwukropków. <m>'
			
			'Określony jest sposób ustalania adresu sprzętowego hosta o danym numerze IP. <mark name="arp" />'
			'Odbywa się to poprzez wysłanie na adres rozgłoszeniowy warstwy drugiej <m> (którym jest <48>[czterdziesto ośmio] bitowa liczba złożona z samych bitów o wartości jeden) <m>'
				'prośby aby host o podanym w takim pakiecie adresie IP podał swój adres <MAC>[mak]. <m>'
			'Taki pakiet odbierają wszystkie hosty w danej sieci fizycznej <m> (tak zwanej domenie rozgłoszeniowej) <m> i jeżeli któryś z nich stwierdza że to IP o które jest pytany należy do niego <m>'
			'to udziela odpowiedzi do nadawcy tego pakietu, informując pytającego <m> o tym że on jest posiadaczem takiego adresu IP. <m>'
			'Do wysłania odpowiedzi kożysta z adresu <MAC>[mak] i IP pytającego, <m> zawartego w pakiecie z pytaniem. <m>'
			'Dzięki temu pytający potrafi poprawnie zaadresować ramkę <ethernetową>[eternetową] <m> zawierającą pakiet IP mający trafić do danego hosta. <m>'
			'Aby uniknąć zbyt częstych zapytań informacja taka jest przechowywana <m> przez pewien czas w lokalnej tablicy mapowań IP na adresy sprzętowe. <m>'
			
			'Generalnie adres L2 zawarty w ramce nie zawsze musi zgadzać się <m> z adresem IP pakietu przesyłanego tą ramką. <m>'
			'Warto tutaj przypomnieć sobie to o czym mówiliśmy <m> przy omawianiu zasad routingu. <m>'
				'Jeżeli trasa routingu wskazuje bezpośrednio na dane urządzenie <m> to adres ramki L2 będzie <MAC>[mak] adresem hosta o numerze IP <m> zawartym w przesyłanym pakiecie. <m>'
				'Jeżeli jednak pakiet ma trafić do routera to adres w ramce L2 <m> będzie <MAC>[mak] adresem routera o IP wskazanym w danym wpisie tablicy routingu. <m>',
			
			'Opisane odpytywanie o adres L2 posiadacza danego adresu IP <m> w IPv4 realizuje protokół ARP, <m> który do przesyłania swojej struktury danych używa bezpośrednio ramek L2. <m>'
			'Natomiast w IPv6 jest to NDP, który korzysta z pakietów ICMP wersji 6, <m> czyli jest obudowywany całym pakietem IP <m> adresowanym na stosowny adres multicastowy. <m>'
			
			'Zapytania odwrotne, czyli o adres IP hosta o danym adresie L2, <m> są możliwe z użyciem protokołów revers ARP dla IPv4 i <IND>[i en de] dla IPv6. <m>'
			'<IND>[i en de] działa analogicznie do <NDP>[en de pe], <m> ale jest stosowny jedynie w specyficznych sieciach L2. <m>'
			'Natomiast reverse ARP wymaga obecności w sieci serwera tej usługi, <m> który posiada informacje o wszystkich adresach <MAC>[mak] <m> i przypisanych im adresach IP. <m>'
		]
	},
	{
		'image': [
			[0.0, eduMovie.convertFile('ethernet2.svg', margins=0)],
		],
		'text' : [
			'W dzisiejszych czasach sieci <ethernetowe>[eternetowe] posiadają typowo strukturę gwiazdy bądź drzewa, <m> czyli mamy tutaj pewnego rodzaju koncentratory, <m> do których dołączone są poszczególne hosty. <m>'
			'Koncentratory te są pudełkami z dużą liczbą złącz takich jak RJ45, <m> lub złącz światłowodowych i mogą być łączone także ze sobą <m> – wtedy zamiast zwykłej gwiazdy mamy gwiazdy wielokrotne lub drzewa. <m>'
			
			'Przykładem takiego koncentratora są <huby>[haby] bądź switche <ethernetowe>[eternetowe]. <m>'
			'<Huby>[haby] są obecnie już rzadkością i wykorzystywane są wyłącznie switche. <m>'
			
			'Rolą obu tych urządzeń jest zapewnienie przekazywania ramek <ethernetowych>[eternetowych] <m> pomiędzy podłączonymi hostami. <m>'
			'Prawdziwy <hub>[hab] <ethernetowy>[eternetowy] robił to po prostu łącząc elektrycznie <m> linie nadawczą każdego ze swoich portów z wszystkimi liniami odbiorczymi <m> i odpowiednio wzmacniając sygnał. <m>'
			'Powodowało to że nadawana treść trafiała zawsze do wszystkich <m> podłączonych hostów i tylko jeden z nich mógł w danej chwili nadawać, <m>'
			'gdyż inaczej doszłoby do wzajemnego zagłuszania się nadawanych informacji <m> – wszystkie komputery podłączone do takiego <huba>[haba] <m> znajdowały się w jednej domenie kolizji. <m>'
			
			'W przypadku switcha każdy z jego portów to niezależne łącze punkt - punkt <m> z osobnymi przewodami nadawania i odbioru, <m> do którego dołączany jest pojedynczy komputer lub inny switch. <m>'
			'Dzięki czemu kolizje nie mają racji bytu. <m>'
			'Switch ponadto na takie łącza stara się kierować ruch <m> w oparciu o adresy zawarte w ramkach <ethernetowych>[eternetowych]. <m>'
			'W tym celu zapamiętuje na którym z jego portów widoczne były <m> poszczególne <MAC>[mak] adresy jako źródłowe, w tak zwanej tablicy adresów <MAC>[mak]. <m>'
			
			'Jeżeli switch w swojej pamięci ma że dany <MAC>[mak] adres (jako źródłowy) <m> był widoczny na porcie x, to ramkę do niego adresowaną wysyła tylko na port x. <m>'
			'Jeżeli nie wie gdzie skierować daną ramkę <m> (albo jest ona adresowana na adres rozgłoszeniowy) <m> to kieruje ją na wszystkie swoje porty. <m>'
			'Gdy host do którego adresowany był taki pakiet na niego odpowie <m> to switch zauważy jego adres jako źródłowy <m> i będzie już wiedział do którego portu jest on podłączony, <m> czyli gdzie kierować kolejne ramki do niego. <m>'
			'Switch czyści także stare wpisy z tablicy MACów, <m> aby lepiej reagować na zmiany w układzie sieci. <m>'
			
			'Dzięki tym cechom na przykład każda z dwóch par komputerów <m> do niego podłączonych może komunikować się z pełną prędkością <m> nie zagłuszając swoich transmisji <m> i nie musząc słuchać transmisji drugiej pary hostów. <m>'
			'Dodatkowo takie działanie <switchy>[słiczy] powoduje pełną regenerację sygnału <m> przy wysyłaniu ramki na dany port<.>[ .] <m>'
			'W przypadku <huba>[haba] przesyłany był oryginalny sygnał elektryczny, <m> który ulegał jedynie wzmacnianiu, jednak jego zbocza traciły stromość <itd.>[i tak dalej], <m> przez co stawał się on mniej czytelny. <m>'
			'W przypadku switcha każda ramka jest dekodowana do postaci cyfrowej <m> (ciągu zer i jedynek) i ponownie generowana na odpowiednim porcie, <m> dzięki czemu nie tracimy na jej jakości przesyłając ją przez kolejne switche. <m>'
			'Dodatkowo możemy łączyć różne warstwy fizyczne w ramach jednej sieci (na przykład skrętkę oraz światłowody), <m> wystarczy tylko, że switche będą miały odpowiednie gniazda. <m>'
		]
	},
]
