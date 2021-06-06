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
	{ 'section': 'konfiguracja automatyczna' },
	{
		'console': [
			[0.0, eduMovie.prompt()],
			["dhclient", "o", "sudo dhclient -v eth0"],
			["dhclient + 1.780706", "o", "\r\n"],
			["dhclient + 1.795227", "o", "Internet Systems Consortium DHCP Client 4.4.1\r\nCopyright 2004-2018 Internet Systems Consortium.\r\nAll rights reserved.\r\nFor info, please visit https://www.isc.org/software/dhcp/\r\n\r\n"],
			["dhclient + 1.844821", "o", "Listening on LPF/eth0/f4:13:04:4e:17:e8\r\nSending on   LPF/eth0/f4:13:04:4e:17:e8\r\n"],
			["dhclient + 1.845223", "o", "Sending on   Socket/fallback\r\nDHCPDISCOVER on eth0 to 255.255.255.255 port 67 interval 3\r\n"],
			["dhclient + 1.85138", "o", "DHCPOFFER of 192.168.6.3 from 192.168.6.1\r\nDHCPREQUEST for 192.168.6.3 on eth0 to 255.255.255.255 port 67\r\n"],
			["dhclient + 1.861168", "o", "DHCPACK of 192.168.6.3 from 192.168.6.1\r\n"],
			["dhclient + 1.868623", "o", "RTNETLINK answers: File exists\r\n"],
			["dhclient + 1.894979", "o", "bound to 192.168.6.3 -- renewal in 32714 seconds.\r\n" + eduMovie.prompt()],
		],
		'text' : [
			'Gdy rozmawialiśmy o protokołach służących zamianie adresu IP <m> na adres warstwy drugiej urządzenia mającego ten IP, <m> czyli ARP i NDP wspomnieliśmy także o reverse ARP. <m>'
			
			'Revers ARP (ze względu na wymaganie serwera tej usługi) <m> nie był protokołem służącym głównie odpytaniu się <m> o to jaki adres bądź jakie adresy IP ma host o danym adresie <MAC>[mak], <m>'
			'tylko był prostym i obecnie praktycznie nie stosowanym protokołem <m> pozwalającym na autokonfigurację – czyli uzyskanie przez host o danym <m> adresie <MAC>[mak] informacji jaki adres IP powinien używać. <mark name="dhclient" />'
			
			'Współcześnie dużo częściej w celu automatycznego uzyskania danych <m> konfiguracyjnych wykorzystywany jest protokół DHCP i DHCPv6. <m>'
			'Protokoły te działają na zasadzie klient-serwer, <m> czyli klient tego protokołu (na przykład polecenie <dhclient>[DH klient]) <m> rozsyła zapytanie rozgłoszeniowe do wszystkich hostów w sieci <m>'
			'o to czy ktoś jest serwerem DHCP i może mu zaoferować dane konfiguracyjne. <m>'
			'Jeżeli w danej sieci taki serwer istnieje to <m> odpowiada on na takie zapytanie przesyłając ofertę takich danych. <m>'
		]
	},
	{
		'image': [
			[0.0, eduMovie.convertFile('link_local.svg', negate=True)],
			["proc", eduMovie.convertFile('proc_ipv6_ra.svg', negate=True)],
		],
		'text' : [
			'Protokół IPv6 posiada również własny mechanizm automatycznej konfiguracji <m> oparty o ICMPv6 a dokładniej NDP, <m> czyli znany nam już protokół odkrywania sąsiadów. <m>'
			'Nie wchodząc zbytnio w szczegóły host może wysłać zapytanie <m> z prośbą o zgłoszenie się routerów znajdujących się w sieci <m>'
			'i dostać od nich odpowiedź, <m> ponadto routery taką informację co pewien czas wysyłają same z siebie. <m>'
			'W oparciu o uzyskane na tej drodze informacje host może <m> skonfigurować domyślną trasę routingową na dany router <m> oraz przekształcić swój adres link-local na adres globalny. <m>'
			'Adres link lokal typowo generowany jest automatycznie <m> w oparciu o adres L2 danego interfejsu sieciowego. <m>'
			'Zamiana adresu link local na adres globalny odbywa się poprzez <m> zastąpienie prefixu fe80::/<64>[sześćdziesiąt cztery] otrzymanym od routera prefixem długości 64 bitów. <m>'
			'Aby zapewnić działanie tego mechanizmu typowo przydzielaną <m> najmniejszą siecią IPv6 jest sieć o prefixie długości 64 bitów. <m>'
			
			'Istnieje propozycja rozsyłania w ten sposób konfiguracji resolvera DNS, <m> nie jest ona jednak powszechnie implementowana, <m>'
			'stąd częste użycie DHCPv6 pozwalającego na bardziej zaawansowane <m> przesyłanie konfiguracji - np. prostszych, manualnie ustawianych adresów, <m> dodatkowych ścieżek routingowych i tak dalej. <m>'
			
			'O włączeniu bądź nie DHCP decydują opcje podawane w konfiguracji interfejsu <m> lub jawne odpalenie klienta DHCP. <mark name="proc" />'
			'O korzystaniu z autokonfiguracji IPv6 decydują wpisy w omawianym już <m> wcześniej wirtualnym systemie plików proc. <m>'
			'Dla każdego interfejsu są to osobne pliki, <m> a przykładowe ścieżki widoczne są na ekranie. <m>'
			
			'Jeżeli w pliku autoconf mamy jedynkę, <m> to mechanizm automatycznego ustawiania adresu globalnego <m> w oparciu o otrzymany prefix jest włączony. <m>'
			'Jeżeli zapisali byśmy do takiego pliku <0>[zero] <m> (najlepiej przed uruchomieniem interfejsu sieciowego, <m> czyli przed zrobieniem link up na tym interfejsie) <m>'
			'to wtedy automatyczna konfiguracja nie będzie pobierana <m> i ustawiana dla danego interfejsu sieciowego. <m>'
			'Może to być przydatne jeżeli nadajemy adresy IP w sposób manualny <m> i nie chcemy korzystać z adresów nadawanych automatycznie. <m>'
			
			'Ustawienia w pliku <accept_ra>[accept R A] są silniejsze i wyłączają całkowicie <m> obsługę informacji wysyłanych przez router w pakietach Router Advertisements. <m>'
		]
	},
]
