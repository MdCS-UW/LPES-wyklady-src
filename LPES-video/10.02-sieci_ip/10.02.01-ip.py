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
			r"-e 's#packetsPutField\[\([^]]*\)\]{\([0-9]*}{" + name + r"\)#packetsPutField[\1, fill=green]{\2#' " +
			r"-e 's#packetsPutField{\([0-9]*}{" + name + r"\)#packetsPutField[protocolsField, fill=green]{\1#' " +
			"'" + inFile + "' > '" + outFile + "'"
		)
	return eduMovie.LaTex2Image(src, convertTeX, name, dpi=150, margins=8)

try: clipData
except NameError: clipData = []

clipData += [
	{ 'title': [ "#10.2", "Internet", "Protocol", "" ] },
	
	{ 'comment': 'IP' },
	{
		'image': [
			[0.0, ""], # TODO jakaś ilustracja ?
		],
		'text' : [
			'Protokół IP jest najpopularniejszym protokołem warstwy trzeciej <m> i na jego działaniu opiera się cały Internet. <m>'
			'Występuje on w 2 wersjach – czwartej i szóstej różniących się przede wszystkim <m> długością adresów, czyli tym ile hostów może być zaadresowanych. <m>'
			
			'Oprócz samej adresacji protokół IP określa zasady kierowania pakietów <m> pomiędzy hostami oraz pomiędzy całymi podsieciami, czyli routingu. <m>'
			'Jako że IP stworzony jest do łączenia różnych fizycznych sieci <m> w jedną sieć logiczną (internet), to pozwala on na wydzielanie <m>'
				'w oparciu o zasady adresacji mniejszych fragmentów sieci, <m> nazywanych niekiedy podsieciami. <m>'
			'Oczywiście zapewnia też mechanizmy przekazywania pakietów <m> pomiędzy takimi podsieciami. <m>'
			
			'Protokół IP wspomagany jest przez protokół, <m> który ciężko zaliczyć do którejś z warstw modelu <OSI>[O S I] <m>'
				'Najbardziej pasuje on do warstwy trzeciej, jednak umieszczany jest w pakietach IP, <m> czyli jest powyżej protokołu IP. <m>'
				'Można by powiedzieć że leży w warstwie <3>[trzy] i pół. <m>'
			'Jest nim ICMP (Internet Control Message Protocol), który służy do przesyłu <m> informacji kontrolnych związanych z działaniem protokołu IP <m> oraz protokołów warstwy czwartej stowarzyszonych z IP. <m>'
			'Przykładami takich informacji może być informacja o tym że host <m> do którego próbowaliśmy wysłać pakiet jest nieosiągalny <m>'
				'– na przykład host o podanym adresie IP został wyłączony <m> albo z innych powodów nie mamy do niego trasy dostępowej. <m>'
			'Innym przykładem może być komunikat o zniszczeniu pakietu IP <m> w związku z przekroczeniem jego czasu życia. <m>'
			'Pozwala też na odpytywanie hostów o ich istnienie, na zasadzie pytań "żyjesz?" <m> i odpowiedzi "żyję" lub braku odpowiedzi. <m>'
			'Ogólnie jest to protokół sygnalizacyjny wspomagający działanie IP <m> i zapewniający tego typu pomocniczą komunikację. <m>'
		]
	},
	{
		'image': [
			[0.0, markedField("../../LPES-booklets/extra-tex-files/booklets-sections/network/ilustracje/10-ipv4.tex", "NO_MARK")],
			["ip4_wersja", markedField("../../LPES-booklets/extra-tex-files/booklets-sections/network/ilustracje/10-ipv4.tex", "Wersja")],
			["ip4_ihl", markedField("../../LPES-booklets/extra-tex-files/booklets-sections/network/ilustracje/10-ipv4.tex", "IHL")],
			["ip4_qos", markedField("../../LPES-booklets/extra-tex-files/booklets-sections/network/ilustracje/10-ipv4.tex", "QoS")],
			["ip4_len", markedField("../../LPES-booklets/extra-tex-files/booklets-sections/network/ilustracje/10-ipv4.tex", "Długość")],
			["ip4_ttl", markedField("../../LPES-booklets/extra-tex-files/booklets-sections/network/ilustracje/10-ipv4.tex", "Time")],
			["ip4_proto", markedField("../../LPES-booklets/extra-tex-files/booklets-sections/network/ilustracje/10-ipv4.tex", "Protokół")],
			["ip4_adresy", markedField("../../LPES-booklets/extra-tex-files/booklets-sections/network/ilustracje/10-ipv4.tex", "Adres")],
		],
		'text' : [
			'Na ekranie widoczna jest struktura pakietu IP w wersji czwartej. <m>'
			'Pakiet składa się z części nagłówkowej, <m> mającej dobrze zdefiniowaną strukturę zaprezentowaną na tych ilustracjach, <m> oraz przesyłanych danych, których struktury ten protokół nie określa. <m>'
			'Mogą to być dowolne dane, aczkolwiek na ogół też posiadają jakąś strukturę <m> – są pakietem protokołu wyższej warstwy. <m>'
			'W nagłówku mamy przede wszystkim adresy nadawcy i odbiorcy. <m>'
			'Adres nadawcy jest potrzebny aby wiedzieć do kogo skierować odpowiedź <m> lub ewentualny komunikat o błędzie związanym z dostarczaniem pakietu. <mark name="ip4_wersja" />'
			
			'Pierwsze pole określa wersję protokołu, <mark name="ip4_ihl" /> kolejne określa wielkość nagłówka, <m> przy czym nie jest on tutaj wyrażony bezpośrednio w bajtach, <m> tylko w wielokrotnościach <4>[czterech] bajtów. <m>'
			'Minimalna wartość tego pola to 5, <m> gdyż minimalna długość nagłówka to 20 bajtów czyli 5 razy 4 bajty. <mark name="ip4_qos" />'
			
			'Kolejne 8 bitów to pole typ / klasa usługi, ale go nie będziemy omawiać. <mark name="ip4_len" />'
			'Po nim na kolejnych 16 bitach zapisana jest długość całego pakietu <m> (czyli nagłówka wraz z danymi) wyrażona w bajtach. <m>'
			
			'W efekcie czego wiemy że długość opcji wynosi IHL minus pięć razy cztery, <m> a długość danych wynosi długość całkowita minus IHL razy cztery. <mark name="ip4_ttl" />'
			
			'Kolejnymi istotnymi polami są Time To Live oraz Protocol, <m> określające czas życia pakietu. <m>'
			'Trochę więcej o znaczeniu pola TTL powiemy sobie później. <mark name="ip4_proto" />'
			'Natomiast pole protocol informuje nas jak należy interpretować zawartość pakietu, <m> czyli przesyłane w nim dane. <m>'
			'Określa ono protokół warstwy wyższej, który został użyty do opisu przenoszonych danych. <m>'
			
			'Oczywiście w nagłówku znajdują się  <mark name="ip4_adresy" /> <32>[trzydziesto dwu] bitowe adresy nadawcy i odbiorcy pakietu. <m>'
		]
	},
	{
		'image': [
			[0.0, markedField("../../LPES-booklets/extra-tex-files/booklets-sections/network/ilustracje/10-ipv6.tex", "NO_MARK")],
			["ip6_wersja", markedField("../../LPES-booklets/extra-tex-files/booklets-sections/network/ilustracje/10-ipv6.tex", "Wersja")],
			["ip6_class", markedField("../../LPES-booklets/extra-tex-files/booklets-sections/network/ilustracje/10-ipv6.tex", "Klasa")],
			["ip6_flow", markedField("../../LPES-booklets/extra-tex-files/booklets-sections/network/ilustracje/10-ipv6.tex", "Losowy")],
			["ip6_dlen", markedField("../../LPES-booklets/extra-tex-files/booklets-sections/network/ilustracje/10-ipv6.tex", "Długość")],
			["ip6_next", markedField("../../LPES-booklets/extra-tex-files/booklets-sections/network/ilustracje/10-ipv6.tex", "Next")],
			["ip6_hop", markedField("../../LPES-booklets/extra-tex-files/booklets-sections/network/ilustracje/10-ipv6.tex", "Hop")],
			["ip6_adresy", markedField("../../LPES-booklets/extra-tex-files/booklets-sections/network/ilustracje/10-ipv6.tex", "Adres")],
		],
		'text' : [
			'Podobnie w wersji szóstej – również <mark name="ip6_wersja" /> na początku mamy pole określające wersję protokołu. <mark name="ip6_class" />'
			'Po nim występuje traffic class o znaczeniu podobnym do <m> type of service z wersji czwartej. <mark name="ip6_flow" />'
			'Pole Flow Label określa etykietę strumienia danych, <m> ale nie będziemy się nim zajmować. <mark name="ip6_dlen" />'
			
			'Następnie mamy długość danych, <m> czyli długość całkowitą pomniejszoną o 40 bajtów, które liczy nagłówek IPv6. <mark name="ip6_next" />'
			'NextHeader pełni funkcję analogiczną do pola Protocol, <m> przy czym może też określać opcjonalny nagłówek IPv6, <m>'
				'w którym to dopiero zostanie podany właściwy protokół <m> enkapsulujący dane (albo kolejny nagłówek opcjonalny i tak dalej). <mark name="ip6_hop" />'
			'Hop Limit pełni funkcję taką samą jak TTL w wersji czwartej. <mark name="ip6_adresy" />'
			'Następnie mamy dwa <128>[stu dwudziesto ośmio] bitowe adresy - nadawcy i odbiorcy. <m>'
		]
	},
	{
		'image': [
			[0.0, eduMovie.convertFile('adresy_IP_1.svg', negate=True)],
			["ipbin", eduMovie.convertFile('adresy_IP_2.svg', negate=True)],
		],
		'text' : [
			'Adres IP jest liczbą, którą zapisywać możemy w różny sposób. <m>'
			'Natomiast taka czy inna forma zapisu służy wyłącznie naszej wygodzie <m> i nie wpływa na interpretację tej liczby przez komputery i urządzenia sieciowe. <m>'
			'Najczęściej stosowaną formą zapisu w przypadku adresów IPv4 <m> jest postać kropkowo dziesiętna, <m>'
				'czyli kolejne bajty zapisywane są jako liczba dziesiętna <m> z zakresu 0 - 255 i oddzielane od kolejnego bajtu adresu kropką. <m>'
			'Jest to dosyć wygodna postać zapisu adresu IP w wersji czwartej, <m>'
				'które mają tylko cztery bajty, więc uzyskujemy cztery człony <m> adresu rozdzielane od siebie kropkami. <m>'
			
			'W przypadku adresu wersji 6 często stosowana jest notacja dwukropkowa, <m>'
				'w której kolejne dwubajtowe fragmenty adresu zapisywane są szesnastkowo <m> i oddzielone od siebie dwukropkami. <m>'
			'Jeżeli w jakimś miejscu występują dwa dwukropki zaraz po sobie <m> oznacza to że w tym miejscu występuje tyle pól o szerokości 16 bitów <m> z wartością zero żeby cały adres miał 8 takich pól. <mark name="ipbin" />'
			
			'Jak już powiedzieliśmy adres jest liczbą, <m> która w postaci binarnej może być reprezentowana jako ciąg zer i jedynek. <m>'
			'To właśnie na takich liczbach operują systemy przetwarzające pakiety IP. <m>'
			
			'Liczbę taką możemy podzielić na dwie części – bardziej znaczącą <m> czyli złożoną z bitów wchodzących z większymi potęgami dwójki <m> o długości n bitów i mniej znaczącą, <m>'
				'czyli złożoną z bitów wchodzących z mniejszymi potęgami dwójki, <m> o długości <32>[trzydziści dwa] minus n dla wersji czwartej lub 128 minus n dla wersji szóstej. <m>'
			'Ta bardziej znacząca część o długości n określana jest mianem prefixu. <m>'
		]
	},
	{
		'image': [
			[0.0, eduMovie.convertFile('agregacja.svg', negate=True)],
			["ipbinmask1", eduMovie.convertFile('adresy_IP_3.svg', negate=True)],
			["ipmask", eduMovie.convertFile('adresy_IP_4.svg', negate=True)],
			["ipbinmask2", eduMovie.convertFile('adresy_IP_3.svg', negate=True)], # celowy powrót do poprzedniego slajdu
		],
		'text' : [
			'Na takim podziale oparte jest grupowanie hostów w podsieci <m> – wszystkie hosty mające wspólny prefix należą do jednej podsieci. <m>'
			'Taka podsieć może być podzielona na kolejne podsieci, <m> których prefix jest po prostu dłuższy. <m>'
			'Każdą sieć mającą dostateczną ilość adresów, możemy podzielić <m> na dwie sieci o wielkości będącej połową tej pierwotnej, <m> 4 o wielkości jednej czwartej i tak dalej. <m>'
			
			'Z tego względu prefix często określany jest jako adres podsieci, <m> a mniej znacząca część adresu jako adres hosta w ramach danej sieci. <m>'
			
			'Na tej samej zasadzie sieci mające wspólny początkowy fragment prefixu <m> możemy zgrupować w większą sieć, oczywiście pamiętając że <m>'
				'będzie ona obejmować wszystkie sieci z tym prefixem. <m>'
			'Łączenie takich mniejszych sieci w sieć większą <m>'
				'jest bardzo pożyteczne z punktu widzenia określania zasad routingu <m> i nazywa się agregacją sieci. <mark name="ipbinmask1" />'
			
			'Do wydzielenia prefixu stosowana jest maska podsieci, <m> czyli liczba mająca w zapisie binarnym ciąg samych jedynek o długości n, <m> a następnie ciąg samych zer o długości <32>[trzydziści dwa] lub 128 minus n, <m>'
				'gdzie n jest długością prefixu. <mark name="ipmask" />'
			
			'W IPv4 maska zapisywana jest często jawnie, tak jak adres, <m> czyli w notacji kropkowo-dziesiętnej <m> lub bardziej skrótowo jako długość prefixu podawana po ukośniku. <m>'
			'W przypadku IPv6 stosuje się praktycznie jedynie <m> zapis w postaci długości prefixu podawanej po ukośniku. <mark name="ipbinmask2" />',
			
			'Skoro ilość bitów w adresie jest stała, a wspólny prefiks <m> oznacza przynależność do jednej sieci, to w oczywisty sposób długość <m> tego prefixu wyznacza dostępną ilość adresów w danej sieci. <m>'
			
			'Liczba adresów nie jest równa liczbie hostów, które możemy zaadresować. <m>'
			'Wynika to z faktu iż w wersji czwartej protokołu IP, <m> dwa adresy mają znaczenie specjalne – adres z samymi zerami <m> w części hosta jest adresem sieci (o którym już wspomnieliśmy), <m>'
				'a adres z samymi jedynkami w tej części jest adresem rozgłoszeniowym. <m>'
			'Adresów tych nie przydziela się hostom w danej sieci, <m> wyjątkiem są tu sieci zawierające tylko jeden adres, <m> określający jeden konkretny host <m>'
				'(mają one zerowej długości część adresu hosta, <m> więc ciężko mówić o adresie sieci, czy też adresie rozgłoszeniowym). <m>'
			
			'Adres rozgłoszeniowy jest adresem, <m> na który powinny reagować wszystkie hosty w danej sieci. <m>'
			'W IPv6 adresy rozgłoszeniowe nie występują, zatem adres <m> z samymi jedynkami w części hosta może być przydzielany jako zwykły adres, <m> ale nie jest to raczej praktykowane. <m>'
		]
	},
]
