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
	{ 'comment': 'ethernet 2' },
	{
		'image': [
			[0.0, eduMovie.convertFile('vlan1.svg', negate=True)],
			["tagowane", eduMovie.convertFile('vlan2.svg', negate=True)],
		],
		'text' : [
			'Ethernet pozwala również na wirtualne podzielenie pojedynczej sieci fizycznej <m> na wiele niezależnych odseparowanych od siebie, <m> nie komunikujących się ze sobą w warstwie drugiej, <m> wirtualnych sieci nazywanych <VLANami>[vi lanami]. <m>'
			'<VLANy>[vi lany] identyfikowane są przy pomocy numerów, <m> które są <12>[dwunasto] bitowymi liczbami, czyli z zakresu od zera do 4098. <m>'
			'Jeżeli byłoby to za mało lub potrzebowalibyśmy mieć <VLANy>[vi lany] wewnątrz <m> sieci będącej <VLANem>[vi lanem] – są na to odpowiednie rozwiązania, <m> jednak nie będziemy ich tutaj omawiać. <m>'
			
			'Działanie mechanizmu wirtualnych sieci LAN opiera się o <m> wykorzystanie <switchy>[słiczy] zarządzalnych, <m> czyli takich które możemy konfigurować. <m>'
			'Najprostszy wariant działania <VLANów>[vi lanów] opiera się na tym, <m> że każdy port switcha jest przypisywany do jednego <m> z iluś skonfigurowanych na nim <VLANów>[vi lanów] <m>'
				'i switch pozwala na komunikację tylko pomiędzy portami <m> należącymi do tego samego <VLANu>[vi lanu] <m> a żadne pakiety nie są przekazywane pomiędzy portami różnych <VLANów>[vi lanów]. <m>'
			
			'Takie podejście działa dobrze dopóki mamy jeden switch <m> i nie mamy wielu hostów, które potrzebują być w dwóch <m> lub więcej takich wirtualnych sieciach. <m>'
			'Bo gdybyśmy mieli <np.>[na przykład] 10 <VLANów>[vi lanów] i jeden host który musi być w nich wszystkich <m> bo jest routerem dla wszystkich tych sieci <m>'
				'to host ten zajmowałby 10 portów w switchu i wymagał <10>[dziesięciu] kabli. <m>'
			'Podobnie gdybyśmy chcieli lub musieli rozpiąć taką <10 VLANową>[dziesięcio vi lanową] sieć <m> na kilku switchach – kolejne 10 kabli do każdego. <mark name="tagowane" />'
			
			"Rozwiązaniem tego problemu są <VLANy>[vi lany] <tagowane>[tago'wane], <m> czyli takie gdzie ten <12>[dwunasto] bitowy numeryczny identyfikator <VLANu>[vi lanu] <m>"
			'dodawany jest do każdej ramki związanej z danym <VLANem>[vi lanem], <m> dzięki czemu możemy kilka <VLANów>[vi lanów] przesyłać wspólnym kablem <m> bez obawy że się pomieszają. <m>'
			"Urządzenie sieciowe, takie jak switch czy komputer, rozumiejące <tagowane>[tago'wane] <VLANy>[vi lany] <m> będzie mogło w oparciu o ten identyfikator ruch nim oznaczony <m>"
			'skierować na odpowiednie swoje porty (należące do tego <VLANu>[vi lanu]) <m> lub powiązać z właściwym dla niego interfejsem sieciowym. <m>'
			
			'Oczywiście switch otrzymujący ramki z tagowanym <VLANem>[vi lanem] <m> może je przesłać zarówno w formie tagowanej <m> (na przykład na inny interfejs na którym dostępny jest inny zbiór <VLANów>[vi lanów]) <m>'
			'lub usunąć z nich ten tag i wysłać na interfejs <m> przypisany do tego <VLANu>[vi lanu] jako nietagowany. <m>'
			'Podobnie do ramek odbieranych z takiego nietagowanego interfejsu <m> switch doda odpowiedni tag przed wysłaniem ich interfejsem tagowanym. <m>'
		]
	},
	{
		'image': [
			[0.0, eduMovie.convertFile('bound.svg', negate=True)],
			["petle_stp", eduMovie.convertFile('pętle.svg', negate=True)],
		],
		'text' : [
			'Możliwe jest również zgrupowanie kilku portów <ethernetowych>[eternetowych] <m> w ramach jednego portu wirtualnego. <m>'
			'Może to służyć zwiększeniu niezawodności łącza <m> albo zwiększeniu przepustowości tego łącza. <m>'
			'Takie rozwiązanie nazywane jest port trunking lub bonding. <m>'
			
			'Dzięki takiemu zabiegowi mając dwie karty gigabitowe w komputerze <m> możemy utworzyć z nich trunk o przepustowości 2 gigabity. <m>'
			'Oczywiście pod warunkiem że switch do którego jesteśmy podłączeni <m> obsługuje takie rozwiązanie. <m>'
			
			'Może to służyć także zwiększeniu niezawodności sieci, <m> gdy takie łącza poprowadzimy różnymi rzeczywistymi trasami, lub do dwóch różnych <switchy>[słiczy] <m> komunikujących się ze sobą w odpowiedni sposób. <mark name="petle_stp" />'
			
			'Przy omawianiu IP mówiliśmy o polu TTL, <m> które służyło eliminacji zapętlonych pakietów. <m>'
			'Ethernet nie ma tego typu pola w ramach ramki <m> i jest podatny na problem pętli. <m>'
			'W związku z tym został opracowany protokół STP <m> (oraz jego kolejne wersje i warianty), który służy eliminacji pętli. <m>'
			'Protokół ten wymienia pomiędzy urządzeniami go obsługującymi <m> pakiety zawierające taki licznik w celu wykrycia pętli <m>'
			'i urządzenie na którym została wykryta pętla <m> zobowiązane jest wyłączyć jeden z interfejsów ją tworzących. <m>'
			
			'Z zastosowaniem STP niekiedy celowo konfiguruje się sieć <m> tak aby zawierała pętle, które są wyłączone przez ten protokół. <m>'
			'Służy to temu że jeżeli zostanie przerwany aktywny link <m> biorący udział w rozłączonej pętli, to protokół STP wykryje brak potencjalnej pętli <m> i włączy nieaktywny interfejs, co spowoduje włączenie zapasowego linku. <m>'
			'Mechanizm ten ma wady związane z czasem rekonfiguracji <m> i przypadkowością decyzji STP, który z linków jest wyłączany. <m>'
			'Jednak bywa stosowany, zwłaszcza gdy sprzęt nie pozwala na nic lepszego <m> (na przykład odpowiedni bonding interfejsów z użyciem LACP). <m>'
		]
	},
	{
		'image': [
			[0.0, "../../LPES-booklets/extra-tex-files/RJ-45_TIA-568A_Right.png"],
			["roznicowy", eduMovie.convertFile('skrętka.svg')],
		],
		'text' : [
			'W przypadku najczęściej spotykanego w warunkach domowych czy biurowych <m> <ethernetu>[eternetu] realizowanego po kablu, wykorzystuje się typowo <m> ośmio żyłowe kable złożone z czterech skręconych par<.>[ .] <m>'
			'Najpopularniejszym kablem jest kabel UTP kategorii piątej, <m> niekiedy określanej 5E. <m>'
			'UTP oznacza że jest to kabel nieekranowany, <m> możemy się spotkać również z kablami ekranowanymi, <m> na przykład FTP, SFTP i innymi tego typu kombinacjami nazw. <m>'
			'Wiążą się one ze sposobem ekranowania, <m> czyli mogą być ekranowane poszczególne pary, może być ekranowana jedynie <m> całość kabla, bądź też może być ekranowana całość i poszczególne pary. <mark name="roznicowy" />'
			
			'Skrętka wykorzystywana jest do transmisji różnicowej, czyli w obu <m> przewodach składających się na daną parę nadawany jest jakiś sygnał, <m>'
			'tyle że nie interesuje nas to czy mamy stan wysoki czy niski <m> na którymś z tych przewodów ale różnica pomiędzy tymi przewodami. <m>'
			'Na przykład jeżeli różnica ta jest mała to mamy zero, <m> a jeżeli jest duża to mamy jedynkę. <m>'
			'Zaletą tego typu transmisji jest to że jeżeli <m> wchodzi jakieś zakłócenie, czyli mamy do czynienia z wyindukowaniem <m> jakiegoś dodatkowego napięcia w tych przewodach, <m>'
			'to jako że są one skręcone i położone blisko siebie, <m> to zakłócenie wyindukuje podobną zmianę napięcia w obu przewodach. <m>'
			'W związku z tym różnica napięcia pomiędzy tymi przewodami <m> nie będzie na to wrażliwa – sygnał nie zostanie zniekształcony bądź zagłuszony. <m>'
			
			'Typowym ograniczeniem długości kabla pomiędzy <m> dwoma aktywnymi urządzeniami (na przykład pomiędzy dwoma switchami, <m> albo <switchem>[słiczem] i komputerem) jest 100 metrów. <m>'
		]
	},
	{
		'image': [
			[0.0, eduMovie.convertFile('światłowody.svg', margins=0)],
			["pryzmat", eduMovie.convertFile('wdm.svg')],
		],
		'text' : [
			'Ethernet to nie tylko kable i WIFI, <m> ale także transmisja optyczna z użyciem światłowodów. <m>'
			'Zapewnia ona duże dystanse pomiędzy urządzeniami <m> (liczone często w dziesiątkach kilometrów), <m> odporność na zakłócenia, separację galwaniczną i tak dalej. <m>'
			'Jeżeli sieć komputerową przesyłamy z użyciem takiego łącza optycznego, <m> to typowo w ramach jednego takiego światłowodu mamy jedno <m> połączenie pomiędzy jakimiś urządzeniami, <m>'
			'przesyłane przy pomocy światła o jakiejś ustalonej długości fali. <m>'
			
			'Mamy również urządzenia które umożliwiają zwielokrotnienie <m> takiego połączenia w taki sposób, że na pojedynczym światłowodzie możemy <m> uzyskać wiele kanałów transmisyjnych o pełnej przepustowości, <m>'
			'czyli takiej jaką mielibyśmy używając go klasycznie. <mark name="pryzmat" />'
			'Odbywa się to przy użyciu różnych długości fali <m> (czyli różnych kolorów światła) do transmisji różnych kanałów, <m> a urządzenia to realizujące to różnego rodzaju <WDMy>[wu de emy]. <m>'
			'Transmitery WDM na ogół używane są na duże odległości, <m> sięgające setek kilometrów. <m>'
		]
	},
]
