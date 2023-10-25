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

def markedField(src, name):
	def convertTeX(inFile, outFile, name):
		os.system("sed " +
			r"-e 's#node\[\([^]]*\)\] *(\(" + name + r"\))#node[\1, fill=green]  (\2)#' " +
			"'" + inFile + "' > '" + outFile + "'"
		)
	return eduMovie.LaTex2Image(src, convertTeX, name, dpi=105, margins=8)

try: clipData
except NameError: clipData = []

code_nftlist="""
table inet filter {
	chain INPUT {
		type filter hook input priority 0; policy drop;
		iifname "lo" accept
		ct state { established, related } accept
		ct state invalid reject
		meta l4proto { icmp, igmp, ipv6-icmp } accept
		ip6 saddr fe80::/64 tcp dport ssh accept
		reject
	}
}
"""

clipData += [
	{ 'section': 'przekazywanie\n i filtrachja pakietów' },
	{
		'image': [
			[0.0, eduMovie.convertFile('proc_forwarding.svg')],
			["fireawall", ""],
		],
		'text' : [
			'Jeżeli chcemy żeby system mógł działać jako router, <m> czyli przekazywać pakiety, to należy zwrócić uwagę <m> na inny plik w tej strukturze katalogowej, czyli forwarding. <m>'
			'Występuje on osobno dla IPv4 i IPv6 i osobno dla każdego z interfejsów. <m>'
			'Ustawienie jedynki w wszystkich tych plikach spowoduje włączenie <m> przekazywania pakietów pomiędzy wszystkimi interfejsami w oparciu o <m> tablice routingu IPv4 i IPv6 oraz reguły filtrowania pakietów. <m>'
			
			'Oczywiście możemy włączyć przekazywanie tylko na wybranych interfejsach, <m> aczkolwiek na ogół w przypadku jeżeli nasz komputer jest routerem <m>'
			'to przekazywanie włączamy globalnie a dopuszczalne kierunki przekazywania <m> ustawiamy już na przykład w oparciu o wspomnianą filtrację pakietów. <mark name="fireawall" />'
			
			'Filtracja pakietów w Linuxie, jest realizowana przez jądro systemu <m> operacyjnego w oparciu o definiowany przez administratora zestaw reguł. <m>'
			'Reguły te dodawane są do jądra analogicznie jak ustawienia adresów <m> czy wpisy tablicy routingowej przy pomocy odpowiednich poleceń <m>'
			'i tak jak w tamtych przypadkach są konfiguracją typu <run-time>[rantajm], <m> czyli traconą po wyłączeniu systemu. <m>'
			'Mechanizm filtracji pakietów określany jest niekiedy jako systemowy firewall, <m>'
			'aczkolwiek jest to pojęcie węższe niż to do czego może być <m> i do czego jest wykorzystywany mechanizm filtracji pakietów. <m>'
			
			'Oprócz zwykłego decydowania czy pakiet ma być przepuszczony, zignorowany <m> czy odrzucony z błędem ICMP w oparciu o adresy źródłowe, docelowe, <m> numery portów, stan nawiązanych połączeń i tak dalej, <m>'
			'możemy także modyfikować adresy, numery portów i inne informacje <m> w takim pakiecie, kierować go do odpowiednich klas ruchu, <m> limitować ilość pakietów w czasie i tak dalej. <m>'
		]
	},
	{
		'console': [
			[0.0, eduMovie.clear + eduMovie.prompt()],
			["nftlist", "nft list ruleset"],
			["nftlist + 0.33", code_nftlist.replace('\n', '\n\r') + eduMovie.prompt()],
		],
		'text' : [
			'Do niedawna podstawowymi narzędziami konfiguryjącymi filtrację pakietów <m> były komendy <iptables>[IP tables] i <ip6tables>[IP 6 tables] (odpowiedzialne za filtrację ruchu IP) <m>'
			"oraz wspomagające <ebtables>[EB tables] i <arptables>[arp tables] (odpowiedzialne odpowiednio za <m> filtrację ruchu na bridge'ach i filtrację na poziomie L2, <m> przed spojrzeniem na warstwę L3). <m>"
			'Aktualnie są one nadal dostępne, lecz często stanowią jedynie ograniczoną <m> nakładkę na nowszy mechanizm, którym jest <nftables>[N F T tables], obsługiwany poleceniem <nft>[N F T]. <mark name="nftlist" /> <m>'
			
			'Komenda <nft>[N F T] pozwala na konfigurację wszystkich rodzajów filtrowania, <m> argumenty tego polecenia (podobnie jak w poleceniu ip) <m>'
			'podawane są w linii poleceń jako ciąg instrukcji, <m>  bez używania opcji rozpoczynających się od myślników, <itp>[i tym podobnych]. <m>'
			'Polecenie <nft>[N F T] list ruleset wypisze wszystkie reguły znajdujące się w jądrze. <m>'
		]
	},
	{
		'image': [
			[0.0, markedField("../../LPES-booklets/extra-tex-files/booklets-sections/network/ilustracje/51-nft.tex", "NO_MARK")],
			["nft_in", markedField("../../LPES-booklets/extra-tex-files/booklets-sections/network/ilustracje/51-nft.tex", "NETIN")],
			["nft_netdev", markedField("../../LPES-booklets/extra-tex-files/booklets-sections/network/ilustracje/51-nft.tex", "ingress")],
			["nft_preroute", markedField("../../LPES-booklets/extra-tex-files/booklets-sections/network/ilustracje/51-nft.tex", "prerouting")],
			["nft_route1 + 4", markedField("../../LPES-booklets/extra-tex-files/booklets-sections/network/ilustracje/51-nft.tex", "ROUTING1")],
			["nft_infwd", markedField("../../LPES-booklets/extra-tex-files/booklets-sections/network/ilustracje/51-nft.tex", "input\|forward")],
			["nft_input", markedField("../../LPES-booklets/extra-tex-files/booklets-sections/network/ilustracje/51-nft.tex", "input")],
			["nft_local", markedField("../../LPES-booklets/extra-tex-files/booklets-sections/network/ilustracje/51-nft.tex", "LOCAL")],
			["nft_route2", markedField("../../LPES-booklets/extra-tex-files/booklets-sections/network/ilustracje/51-nft.tex", "ROUTING2")],
			["nft_out", markedField("../../LPES-booklets/extra-tex-files/booklets-sections/network/ilustracje/51-nft.tex", "output")],
			["nft_postroute", markedField("../../LPES-booklets/extra-tex-files/booklets-sections/network/ilustracje/51-nft.tex", "postrouting")],
		],
		'text' : [
			'Na ekranie pokazany został schemat obrazujący drogę pakietu przez filtry <nft>[N F T]. <m>'
			'W pełnych (nie kropkowanych) prostokątach zostały podane punkty <m> w których możemy zaczepiać reguły <nft>[N F T]. <mark name="nft_in" />'
			
			'Zaraz po nadejściu pakietu <mark name="nft_netdev" /> mamy punkt zaczepienia netdev - ingress, który pozwala na <m>'
			'wykonywanie operacji mniej więcej na tym poziomie jak reguły komendy tc <m> i może stanowić dla nich alternatywę. <mark name="nft_preroute" />'
			'Następnie mamy punkt zaczepienia prerouting, <m> który jak sama nazwa wskazuje znajduje się przed <mark name="nft_route1" />'
			'poddaniem pakietu decyzjom routingowym (czy jest do lokalnego hosta, <m> czy ma być przekazany, na jakie urządzenie <itp.>[i te pe]). <m>'
			'W zależności od decyzji routingowej do pakietu zastosowanie będą miały <mark name="nft_infwd" /> punkty zaczepu input albo forward. <mark name="nft_input" />'
			'Pakiet który przeszedł przez input kończy swoją drogę <mark name="nft_local" /> jako dostarczony do jakiegoś procesu.  <m>'
			'Lokalne procesy mogą generować odpowiedzi na taki pakiet, <m> mogą także generować zupełnie nowe połączenia, <m>'
			'niezależnie od tego, pakiety takie <mark name="nft_route2" /> trafiają do mechanizmu routingowego a następnie <mark name="nft_out" /> na punkt zaczepienia filtrów output. <m>'
			'W przypadku akceptacji w specyficznej regule na tym poziomie <m> mogą zostać zwrócone do ponownego routingu. <mark name="nft_postroute" />'
			'Kolejnym punktem zaczepienia jest postrouting do którego pakiety trafiają <m> tuż przed opuszczeniem systemu (przed wysłaniem ich w sieć) <m>'
			'i przez punkt ten przechodzą zarówno pakiety przekazywane, <m> jak i utworzone lokalnie. <m>',
		]
	},
	{
		'image': [
			[0.0, eduMovie.convertFile('nft_tabele_lancuchy.svg', negate=True)],
			["rodzinytabel", eduMovie.convertFile('nft_rodziny_tabel.tex', negate=True)],
		],
		'text' : [
			'W ramach <nft>[N F T] mamy także tabele, łańcuchy i reguły. <m>'
			'Reguły grupowane są w łańcuchy, w ramach których przetwarzane są kolejno, <m> aż do napotkania reguły kończącej przetwarzanie danego pakietu, <m> czyli na przykład go odrzucającej albo akceptującej. <m>'
			
			'Łańcuchy grupowane są w tabele. <m> Służy to wyłącznie ułatwieniu zarządzania konfiguracją <m> i przetwarzane są wszystkie pasujące łańcuchy z wszystkich tabel. <m>'
			
			'Ruch do łańcucha kierowany może być jawnie przez regułę w innym łańcuchu <m> lub automatycznie w oparciu o parametry łańcucha, <m> takie jak punkt zaczepienia i priorytet. <m>'
			'Czyli jeżeli mamy na przykład dwa łańcuchy zaczepione w input <m> (bez względu na to czy znajdują się w jednej czy w różnych tabelach) <m> dla pakietu przechodzącego przez ten punkt przetworzone będą oba. <m>'
			'Kolejność przetwarzania zależeć będzie od priorytetów tych łańcuchów. <m>',
			
			'Łańcuchy posiadają także typy związane z akcjami które mogą wykonywać, <m> standardowym typem jest filter pozwalający na filtrowanie pakietów. <m>'
			'Istnieją także dwa specyficzne typy, które mogą być użyte tylko dla <m> rodzin związanych z protokołami IP i niektórych punktów zaczepienia <m>'
			'– nat, który odpowiada za zamianę adresów sieciowych, <m> w oparciu o śledzenie połączeń <m>'
			'oraz route, który umożliwia zawrócenie pakietów <m> z punktu zaczepienia output do ponownego przeroutowania. <mark name="rodzinytabel" />'
			
			'Każda, wspomniana wcześniej, tabela <m> przypisana jest do pewnej rodziny związanej <m> z poziomem stosu sieciowego na którym funkcjonuje <m> i z rodziną adresów na których operuje. <m>'
			'Są to ip, <ip6>[ip 6] i inet (działające w warstwie trzeciej <m> odpowiednio dla IPv4, IPv6 i obu tych protokołów) <m>'
			'oraz arp (działający w L2 przed procesowaniem L3), <m> bridge (działający dla pakietów przechodzących przez softwareowy switch) <m>'
			'i netdev (działający na samym wejściu pakietu na urządzenie sieciowe). <m>'
			
			'Tabele dla różnych rodzin mogą mieć taką samą nazwę, <m> w związku z czym w poleceniach operujących na tabeli <m> oprócz jej nazwy podaje się także jej rodzinę <m> (gdyż sama nazwa nie jest jednoznaczna). <m>'
			'Tabel dla danej rodziny może być wiele. <m>'
		]
	},
]
