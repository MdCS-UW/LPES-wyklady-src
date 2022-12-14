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
	{ 'title': [ "#10.1", "Podstawy", "sieci", "komputerowych" ] },
	
	{ 'comment': 'sieci - podstawy' },
	{
		'image': [
			[0.0, eduMovie.convertFile('network.svg', margins=0)],
			["chmurkiA", eduMovie.convertFile('sieci_chmurki_1.svg')],
			["chmurkiB", eduMovie.convertFile('sieci_chmurki_2.svg')],
		],
		'text' : [
			'Sieć komputerowa jest to zbiór hostów, komputerów, innych urządzeń <m> sieciowych, okablowania oraz protokołów określających zasady komunikacji. <m>'
			'Służy do zapewnienia komunikacji pomiędzy komputerami, przesyłu danych. <m>'
			'Sieci komputerowe działają na zasadzie przesyłania informacji <m> w ramach pewnych fragmentów z których każdy posiada przynajmniej informacje <m> o adresie odbiorcy do którego ma trafić. <m>'
			'Fragmenty takie nazywane są ramkami bądź pakietami <m> i zwykle oprócz adresu odbiorcy jest tam też adres nadawcy <m> i kilka innych informacji pomagających obsłużyć taki pakiet. <mark name="chmurkiA" /> <m>'
			
			'Umieszczanie w nagłówku każdego z pakietów adresów umożliwia kierowanie <m> ruchem takich pakietów bez wcześniejszego fizycznego zestawiania łącz. <m>'
			'W oparciu o ten adres host jest w stanie rozpoznać czy pakiet <m> jest przeznaczony dla niego czy nie, a przełączniki i routery mogą <m> kierować pakiety do odpowiednich fragmentów sieci. <m>'
			
			'Jeżeli w sieci komputerowej host A chce się komunikować z hostem B, <m> a host C z hostem D nie musimy zapewnić im osobnych łączy <m> do przeprowadzania takiej komunikacji, <m>'
				'tak jak to było na przykład w klasycznej telefonii analogowej, <m> gdzie dwie takie "rozmowy" wymagałyby zestawienia osobnych <m> fizycznych kabli od jednego abonenta do drugiego <m>'
				'(odbywało się to za pomocą przekaźników w centralach). <m>'
			'W sieci komputerowej hosty te będą wytwarzały odpowiednio zaadresowane <m> pakiety i reagowały tylko na pakiety zaadresowane do nich. <m>'
			'Dzięki temu pakiety, stanowiące osobne strumienie komunikacji, <m> mogą być z łatwością przesyłane tym samym fizycznym łączem. <m>'
			'Host C może słyszeć lub nie komunikację pomiędzy hostami A i B <m> (zależy to od różnych czynników, na przykład od wykorzystywanej sieci <m> i względnego położenia tych hostów), natomiast wie że to "nie do niego". <mark name="chmurkiB" /> '
			
			'Jeżeli w ramach sieci mamy jakieś urządzenie dzielące ją na <m> mniejsze kawałki, podział ten będzie się odbywał w oparciu o adresy pakietów <m>'
				'– urządzenie takie do danej sieci będzie przekazywało <m> tylko pakiety adresowane do hostów w tej sieci. <m>'
			'Mamy do czynienia z przełączaniem, czyli komutacją pakietów <m> – w odróżnieniu od (omówionej pokrótce na przykładzie telefonii) komutacji łączy, <m>'
				'która polegała na zestawianiu fizycznego łącza <m> pomiędzy komunikującymi się hostami. <m>'
		]
	},
	{
		'image': [
			[0.0, eduMovie.convertFile('../../LPES-booklets/extra-tex-files/booklets-sections/network/ilustracje/10-warstwy.tex', margins=12)],
		],
		'text' : [
			'Protokoły sieciowe na ogół tworzą tak zwane stosy protokołów, <m> gdzie dane opakowywane są kolejno w nagłówki kolejnych protokołów. <m>'
			'Każdy z protokołów w takim stosie pełni dedykowane mu funkcje <m> i na ogół nie ingeruje ani w protokoły warstwy niższej, <m> ani w przenoszoną przez niego zawartość, czyli protokoły warstwy wyższej z danymi. <m>'
			
			'Struktura warstwowa jest standardowo opisywana w ramach <m> tak zwanego modelu <OSI>[O S I] który wyróżnia 7 warstw. <m>'
		]
	},
	{
		'image': [
			[0.0, eduMovie.convertFile('warstwy-slajd.tex', margins=12)],
		],
		'text' : [
			'Najniższą warstwą jest warstwa fizyczna <m> – zajmuje się ona definiowaniem takich aspektów jak na przykład: <m>'
				'poziom sygnału elektrycznego w kablu tworzącym sieć, <m> częstotliwości radiowe w sieciach bezprzewodowych, <m> długości fali światła w sieciach optycznych i tak dalej. <m>'
			
			'Tutaj określane jest też to w jaki sposób przesyłane są kolejne bity <m> – w jaki sposób kodowana jest jedynka logiczna, a w jaki zero. <m>'
				'Ponieważ w przypadku takiej transmisji niekoniecznie jest tak że <m> napięcie wyższe odpowiada nam na przykład logicznej jedynce, a niższe zeru. <m>'
				'Niekiedy jest to kodowanie bardziej skomplikowane. <m>'
			'Warstwa ta określa też sposób kodowania kolejnych bajtów, <m> tak aby dało się identyfikować koniec i początek bajtu. <m>'
			'Przykładem protokołu tej warstwy o którym już mówiliśmy jest <UART>[uart] <m> i możliwe jest jego użycie w sieciach komputerowych. <m>',
			
			'Kolejną warstwą o numerze dwa w modelu <OSI>[O S I], <m> stąd często określaną jako L2, jest warstwa łącza danych. <m>'
			'Definiuje ona aspekty takie jak adresacja urządzeń fizycznych, <m> format ramki (w tym identyfikację jej początku i końca) <m> oraz protokoły dostępu do medium transmisyjnego określonego w L1, <m>'
				'czyli co zrobić jeżeli po tym samym kablu równocześnie <m> zaczną nadawać dwa urządzenia, jak takich sytuacji unikać, itd. <m>'
			
			'Często warstwy pierwsza i druga określone są <m> jednym standardem bądź rodziną standardów. <m>'
			'Bardzo często jest to Ethernet, <m> który używa takiego samego formatu ramki, tych samych rozwiązań L2 <m> dla różnych mediów transmisyjnych, różnych warstw L1 <m>'
				'– zarówno przewodowych miedzianych, optycznych jak i bezprzewodowych. <m>'
			'Mogą to być też protokoły związane z sieciami komórkowymi, <m> transmisją danych poprzez telewizję kablową i tak dalej. <m>'
			
			'Rolą trzeciej warstwy jest zapewnienie możliwości komunikacji <m> pomiędzy różnymi sieciami, różnymi standardami sieci L2. <m>'
			'Określa ona własną adresację, która powinna być unikalna <m> nie tylko w ramach jednej sieci L2, ale w ramach wszystkich łączonych nią sieci, <m> można powiedzieć że unikalna globalnie. <m>'
			'Najpopularniejszym protokołem tej warstwy jest IP. <m>',
			
			'Kolejna, czwarta warstwa nazywana jest transportową <m> i ma dwa główne zadania – zapewnienie adresacji wewnątrz hosta <m> oraz zapewnienie kontroli przepływu danych. <m>'
			'Warstwy druga i trzecia zajmują się jedynie <m> adresacją całych hostów, komputerów. <m>'
				'Jednak jak wiemy na pojedynczym komputerze może równocześnie funkcjonować <m> wiele różnych usług sieciowych, wiele różnych procesów, klientów, itd. <m>'
			'Konieczne jest zapewnienie możliwości wskazania do jakiej usługi <m> lub nawet do jakiego procesu ma być skierowana informacja zawarta w pakiecie. <m>'
			
			'Warstwa ta zajmuje się także kontrolą jakości przesyłanych danych, <m> ponieważ warstwa sieciowa (w szczególności na przykład protokół IP) <m> nie zapewnia pewności przesyłania danych< >[.] <m>'
				'– pakiet IP zawsze może zaginąć bez żadnych informacji o tym że zaginął <m> i protokoły warstwy wyższej powinny być tego co najmniej świadome <m> lub nawet radzić sobie jakoś z takimi problemami żądając jego retransmisji. <m>'
			
			'Najpopularniejszymi protokołami warstwy czwartej są UDP i <TCP>[ticipi]. <m> Oba zapewniają adresację usług i klientów. <m>'
			'<TCP>[ticipi] zapewnia także kontrolę otrzymywania kompletu pakietów <m> i mechanizmy retransmisji zagubionych pakietów. <m>',
			
			'Kolejne warstwy modelu <OSI>[O S I] - piąta, szósta i siódma określają <m> sposób rozmowy i interpretacji danych przez konkretne aplikacje. <m>'
			'Granice pomiędzy nimi są dość płynne <m> i nie będziemy ich na tych zajęciach traktować osobno. <m>'
			'Co zresztą jest dość często spotykane, <m> gdyż podział ten bywa problematyczny – na przykład część zadań warstwy piątej <m> realizuje <TCP>[ticipi], będący ewidentnie warstwą czwartą. <m>'
			
			'Spotkać się można także z innym modelem <m> związanym ze stosem protokołów z <TCP>[ticipi]/IP. <m>'
			'Model ten wyróżnia jedynie 4 warstwy – dostępu do sieci obejmującą L1 i L2, <m> internetową (obejmującą L3), transportową (obejmującą L4) <m> i aplikacji obejmującą właśnie te trzy wyższe warstwy modelu <OSI>[O S I]. <m>',
			
			'Nie każdy powszechnie stosowany protokół <m> daje się łatwo dopasować do konkretnej warstwy. <m>'
			'Przykładem może być SSL/TLS odpowiedzialny za szyfrowanie <m> przesyłanych danych (na przykład robienie HTTPS z HTTP). <m>'
			'Ewidentnie powinien on być powyżej warstwy transportowej bo zawarty jest <m> w jej pakietach, jednak nie jest on warstwą aplikacji z modelu <TCP>[ticipi]/IP, <m>'
				'gdyż jest wspólny dla wielu aplikacji, jest niezależny od przesyłanych nim danych <m> i ewidentnie jest poniżej protokołów warstwy aplikacji takich jak wspomniany HTTP. <m>'
			'Podobnie ciężko go wpasować w którąś z wyższych warstw <OSI>[O S I]. <m> Można by powiedzieć że stanowi warstwę <4>[cztery] i pół modelu <OSI>[O S I]. <m>'
		]
	},
]
