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

code_ipr_output = r"""::1 dev lo proto kernel metric 256 pref medium
2001:0db8:1317::1d:0/112 dev eth0 proto kernel metric 256 pref medium
2001:0db8:1317::ff1d:0/112 dev eth1 proto kernel metric 256 pref medium
2001:0db8:6411::/64 via 2001:0db8:1317::1d:113 dev eth0 metric 1024 pref medium
fe80::/64 dev eth1 proto kernel metric 256 pref medium
fe80::/64 dev eth0 proto kernel metric 256 pref medium
default via 2001:0db8:1317::ff1d:1 dev eth1 metric 1024 pref medium
"""

clipData += [
	{ 'comment': 'routing IP' },
	{
		'console': [
			[0.0, "o", eduMovie.prompt()],
			["ipr", "o", "ip -6 r\n\r"],
			["ipr + 0.7", "o", eduMovie.markLines(code_ipr_output, edit=False)],
			["ipr + 0.73", "o", eduMovie.prompt()],
			
			["ipr_direct", "o", eduMovie.markLines(code_ipr_output, [0, 1, 2, 4, 5]) + eduMovie.prompt()],
			["ipr_via", "o", eduMovie.markLines(code_ipr_output, [3, 6]) + eduMovie.prompt()],
			["ipr_clear", "o", eduMovie.markLines(code_ipr_output) + eduMovie.prompt()],
			
			["ipr_via2", "o", eduMovie.editBegin(1) + "default " + eduMovie.markBegin + "via 2001:0db8:1317::ff1d:1" + eduMovie.markEnd + " dev eth1 metric 1024 pref medium" + eduMovie.editEnd(1)],
			["ipr_dev2", "o", eduMovie.editBegin(1) + "default via 2001:0db8:1317::ff1d:1 " + eduMovie.markBegin + "dev eth1" + eduMovie.markEnd + " metric 1024 pref medium" + eduMovie.editEnd(1)],
			["ipr_clear2", "o", eduMovie.editBegin(1) + "default via 2001:0db8:1317::ff1d:1 dev eth1 metric 1024 pref medium" + eduMovie.editEnd(1)],
		],
		'text' : [
			'Sprawdzanie czy host należy do danej sieci <m> jest podstawą działania routingu w ramach sieci komputerowej. <m>'
			'Routing związany jest z przekazywaniem pakietów pomiędzy hostami, <m> a nawet samym wysłaniem pakietu z hosta – każdy host wykonuje operację routingowe. <m>'
			
			'Routerem nazywamy urządzenie zajmujące się przekazywaniem ruchu IP <m> pomiędzy kilkoma różnymi podsieciami. <m>'
			'Może to być dedykowane fizyczne urządzenie, <m> jak również komputer działający na przykład pod kontrolą systemu Linux, <m>'
				'posiadający kilka interfejsów sieciowych (fizycznych lub wirtualnych) <m> i przekazujący pakiety IP pomiędzy nimi <m> w oparciu o zasady określone w tablicy routingu. <mark name="ipr" />'
			
			'W Linuxie informację o zawartości tablicy routingu <m> można wypisać używając polecenia <ip r>[IP R] lub <ip -6 r>[IP minus 6 R] dla IPv6. <m>'
			'Przykładowy wynik tej komendy pokazano na ekranie <m> – każda linia odpowiada jednemu wpisowi w tablicy routingu. <m>'
			
			'Pierwsza kolumna zawiera adres sieci której dotyczy wpis w tablicy routingu. <m>'
			'Wyróżnić możemy tutaj też dwa typy wpisów – <mark name="ipr_direct" /> kierujące ruch bezpośrednio na urządzenie włączone do danej sieci oraz <mark name="ipr_via" />'
				'takie które kierują ruch do kolejnego routera. <mark name="ipr_clear" />'
			'Fakt kierowania ruchu do kolejnego routera oznaczany jest <mark name="ipr_via2" /> umieszczeniem informacji via z numerem IP tego routera. <m>'
			'Urządzenie którym ma zostać wysłany dany pakiet oznaczane jest<mark name="ipr_dev2" /> przy pomocy dev i nazwy danego interfejsu sieciowego. <mark name="ipr_clear2" />'
			'Pozostałe informacje na razie nie będą nas interesować <m> – pozwalają one między innymi na wybór jednej z dwóch tak samo dobrych pod względem <m> długości prefixu tras, ustawienie odpowiedniego adresu źródłowego, itp. <m>'
			
			'W celu wysłania pakietu IP, system przeszukuje tablicę routingu <m> w poszukiwaniu sieci do której należy adres docelowy z tego pakietu. <m>'
			'Sprawdzanie to odbywa się na tablicy posortowanej wg długości prefixu, <m> w ten sposób że najpierw sprawdzamy najbardziej precyzyjne wpisy w tablicy, <m> czyli te o najdłuższym prefixie. <m>'
		]
	},
	{
		'console': [
			[0.0, "o", eduMovie.prompt()],
			[1.359482, "o", "#"],
			[1.927202, "o", " "],
			[2.183163, "o", "d"],
			[2.399272, "o", "e"],
			[2.623184, "o", "f"],
			[2.911193, "o", "a"],
			[3.191164, "o", "u"],
			[3.479249, "o", "l"],
			[3.767223, "o", "t"],
			[3.983171, "o", " "],
			[4.591212, "o", "="],
			[4.871202, "o", "="],
			[5.223164, "o", " "],
			[6.48742, "o", ":"],
			[6.647303, "o", ":"],
			[7.023184, "o", "/"],
			[7.599305, "o", "0"],
			[8.167188, "o", "\r\n"],
			[8.168266, "o", eduMovie.prompt()],
			[9.75435, "o", "#"],
			[9.8435, "o", " "],
			[9.935174, "o", "d"],
			[10.159172, "o", "e"],
			[10.415207, "o", "f"],
			[10.695207, "o", "a"],
			[10.951215, "o", "u"],
			[11.239198, "o", "l"],
			[11.519325, "o", "t"],
			[11.743231, "o", " "],
			[12.247163, "o", "="],
			[12.50333, "o", "="],
			[13.559293, "o", " "],
			[14.175316, "o", "0"],
			[14.527333, "o", "."],
			[14.935263, "o", "0"],
			[15.191199, "o", "."],
			[15.439335, "o", "0"],
			[15.791231, "o", "."],
			[16.079226, "o", "0"],
			[16.871316, "o", "/"],
			[17.279179, "o", "0"],
			[17.751306, "o", "\r\n"],
			[17.752225, "o", eduMovie.prompt()],
		],
		'text' : [
			'Default oznacza adres w postaci samych zer <m> z prefixem o długości zero, czyli cały internet. <m>'
			'Do wpisu takiego pasować będzie dowolny adres IP, <m> jednak dzięki najmniejszej możliwej długości prefixu, <m> będzie on sprawdzany jako ostatni. <m>'
			'Router określony w tym wpisie nazywany jest bramką domyślną. <m>'

			'Po odnalezieniu pasującego wpisu w tablicy routingu <m>'
				'(przypominam że gdy pasuje kilka wygrywa ten z najdłuższym prefiksem, <m> a gdy nawet takich jest kilka używane są inne kryteria, <m> takie jak metryka, celem ustalenia pojedynczego wpisu) <m>'
				'pakiet może zostać wysłany na związane z nim urządzenie. <m>'
			
			'Jeżeli wpis w tablicy routingu nie wskazuje następnego routera <m> (nie ma w nim via) to pakiet kierowany jest bezpośrednio do hosta docelowego <m> – jest on osiągalny w sieci w której znajduje się wskazane urządzenie. <m>'
			
			'Kierowanie ruchu do routera polega na zaadresowaniu pakietu <m> warstwy drugiej adresem tego routera, <m>'
				'podczas gdy w warstwie trzeciej, czyli w nagłówku IP <m> pozostaje niezmieniony adres odbiorcy <m> należący do sieci obsługiwanej przez ten router. <m>'
			'Konsekwencją tego jest że do adresu IP routera <m> musimy mieć trasę bezpośrednią (bez via), <m>'
				'czyli musi on być dostępny bezpośrednio w którejś z sieci <m> do których jesteśmy podpięci odpowiednim interfejsem. <m>',
			
			'Każdy router przekazując pakiet zmniejsza <m> wartość zapisaną w polu TTL bądź hop limit, <m>'
				'a gdy osiągnie ona zero to przestaje przetwarzać taki pakiet <m> i nie przesyła go dalej. <m>'
			'Za to zwraca do nadawcy odpowiedni komunikat ICMP o błędzie. <m>'
			'Mechanizm ten służy rozwiązaniu problemu zapętleń, <m> które mogłyby powstać w wyniku błędnej konfiguracji <m>'
				'i prowadzić do przekazywania tych samych pakietów <m> w kółko pomiędzy grupą jakiś routerów, <m>'
				'co wraz ze wzrostem ilości takich zagubionych pakietów <m> prowadziłoby do rosnącego obciążenia sieci śmieciowym ruchem. <m>',
			
			'To o czym do tej pory mówiliśmy dotyczy zasad routingu adresów typu unicast, <m> czyli adresów identyfikujących w sposób unikalny pojedynczego hosta. <m>'
			'Oprócz tego typu adresów mamy także wspomniane już adresy <m> typu broadcast, adresy multicast i anycast. <m>'
			
			'Adresy broadcast z punktu widzenia obsługi tablicy routingu <m> nie różnią się specjalnie od adresów unicast. <m>'
			'Natomiast typowo nie są poddawane przesyłaniu przez routery pośredniczące <m> a jedynie wysyłane do bezpośrednio dostępnej sieci. <m>'
			'Również samo przesyłanie L2 korzysta wtedy z innego mechanizmu adresacji <m> – taki pakiet musi dotrzeć do wszystkich hostów w danej sieci, <m> zatem na poziomie L2 też jest adresowany jako rozgłoszeniowy. <m>',
			
			'Adresy typu multicast służą do zaadresowania grupy hostów. <m>'
			'W tym wypadku adres docelowy identyfikuje pewien kanał nadawczy, <m> na odbiór którego zapisują się hosty docelowe. <m>'
			'Można też powiedzieć że identyfikuje dynamicznie zmieniającą się <m> grupę tych hostów docelowych. <m>'
				'Przy czym każdy z tych hostów może należeć do wielu takich grup. <m>'
			'Przekazywanie pakietów multicast między sieciami oparte jest o <m> informowaniu bramki o chęci odbioru danej grupy multicastowej <m>'
				"i wymianie informacji pomiędzy router'ami <m> na temat subskrybowanych grup multicastowych. <m>"
			'Stosowanie multicastu służy zmniejszeniu obciążenia sieci, <m> gdy przesyłane są nią te same dane (na przykład transmisja wideo), <m>'
				'które mają trafiać do wielu odbiorców, <m> dzięki temu że tak długo jak to możliwe są przesyłane wspólnie. <m>'
			'Na przykład jeżeli na jakimś routerze mamy zarejestrowanych <3>[trzech] odbiorców <m> danej transmisji multicastowej to pakiety z nią związane dotrą <m> do tego routera w jednym, a nie w trzech powielonych egzemplarzach. <m>'
			"W praktyce jednak multicast'y rzadko docierają aż do naszego komputera <m> – na ogół są stosowane w sieciach operatorskich, <m> na przykład do rozsyłu telewizji IP <m> i nie schodzą tak blisko końcowego użytkownika. <m>",
			
			'Ostatni wspomniany typ adresów, czyli anycast <m> opiera się na nadaniu tego samego adresu IP <m> różnym hostom w sieci, na ogół położonym w różnych lokalizacjach. <m>'
			'Wykorzystuje on odpowiednią konfiguracji routingu, <m> tak aby ruch był kierowany do najbliższego takiego hosta. <m>'
			'Jednym z bardziej znanych przykładów tego typu adresów jest 8.8.8.8 <m> czyli serwer rozwijający DNS oferowany przez Google. <m>',
			
			'Tablice routingu mogą zawierać wpisy statyczne, zarówno <m> dodawane jawnie przez administratora (takie jak np. bramka domyślna), <m> jak też wpisy pochodzenia automatycznego, takie jak <m>'
				'wpisy związane z obecnością danego adresu IP na urządzeniu. <m>'
				'Typowo sam fakt ustawienia adresu IP na jakimś urządzeniu powoduje, <m> że dodawana jest trasa routingowa do sieci <m> związanej z tym adresem na dane urządzenie. <m>'
			
			'Oprócz wpisów statycznych, wpisy w tablicach routingu <m> mogą też być umieszczane dynamicznie, <m> w wyniku działania protokołów wymiany informacji routingowej. <m>'
			
			'Duże routery w internecie, łączące sieci różnych operatorów, <m> wymieniają się ze sobą informacjami <m> o trasach dostępu do poszczególnych sieci. <m>'
			'Czyli taki router brzegowy danej sieci ogłasza informację,  <m> że jest ona dostępna poprzez takie i takie <m> adresy routerów (bramek do niej prowadzących). <m>'
			'Taka informacja jest propagowana dalej, <m> tak aby inne routery wiedziały jak kierować ruch do danej sieci. <m>'
			
			'Protokołów wykorzystywanych w tym celu nie będziemy omawiali <m> na tych zajęciach, natomiast warto o nich krótko wspomnieć. <m>'
			'Najpopularniejszym takim protokołem w Internecie jest BGP, <m> oprócz niego mamy też protokoły OSPF i tym podobne. <m>'
			'Różnią się one sposobem przekazywania informacji <m> i szczegółami technicznymi. <m>'
			'Natomiast wspólne dla tych protokołów jest to że wpływają one w dynamiczny <m> sposób na zasady routingu, na wpisy w tablicy routingu urządzeń <m> przekazujących pakiety pomiędzy sieciami. <m>'
			
			'Protokoły routingu dynamicznego mogą być wykorzystywane do <m> równoważenia obciążenia łącz, zapewnienia ich zastępowalności, <m>'
				'jak też zapewnienia zastępowalności serwisów – na przykład <m> przerzucenia ruchu sieciowego z serwerowni która uległa awarii do tej działającej. <m>'
			'Mogą także służyć blokowaniem ataków typu Denial of Service <m> poprzez usunięcie informacji na temat trasy routingowej <m> do atakowanego urządzenia z routerów zewnętrznych, <m>'
				'dzięki czemu ruch zostanie obcięty nie na naszym firewallu, <m> a po drugiej stronie łącza i nie będzie on zapychał naszego łącza. <m>'
		]
	},
]
