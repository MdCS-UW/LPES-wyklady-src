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

code_ipa_output=r"""1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether f4:13:04:4e:17:e8 brd ff:ff:ff:ff:ff:ff
    inet 192.168.6.3/24 brd 192.168.6.255 scope global dynamic eth0
       valid_lft 63549sec preferred_lft 63549sec
    inet6 2001:0db8::6411:f613:4ff:fe4e:17e8/64 scope global dynamic mngtmpaddr
       valid_lft 1775sec preferred_lft 575sec
    inet6 fe80::f613:4ff:fe4e:17e8/64 scope link
       valid_lft forever preferred_lft forever
"""

code_ipa_output2=r"""1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether f4:13:04:4e:17:e8 brd ff:ff:ff:ff:ff:ff
    inet 192.168.6.3/24 brd 192.168.6.255 scope global dynamic eth0
       valid_lft 63549sec preferred_lft 63549sec
    inet 10.0.71.113/20 scope global enp1s0
       valid_lft forever preferred_lft forever
    inet6 2001:0db8::6411:f613:4ff:fe4e:17e8/64 scope global dynamic mngtmpaddr
       valid_lft 1775sec preferred_lft 575sec
    inet6 fe80::f613:4ff:fe4e:17e8/64 scope link
       valid_lft forever preferred_lft forever
"""

code_ipr_output2=r"""default via 192.168.6.1 dev eth0
10.0.64.0/20 dev eth0 proto kernel scope link src 10.0.1.0
192.168.6.0/24 dev eth0 proto kernel scope link src 192.168.6.3
"""

clipData += [
	{ 'title': [ "#11.3", "Konfiguracja", "sieci", "" ] },
	
	{ 'comment': 'konfiguracja - ip ifconfig ...' },
	{
		'image': [
			[0.0, eduMovie.convertFile('polecenie_ip_1.tex', negate=True)],
		],
		'text' : [
			'Obecnie podstawową komendą służącą do konfiguracji interfejsów sieciowych <m> w systemach Linux, ale niekoniecznie w innych Unix’ach jest polecenie ip. <m>'
			'Komenda ta przyjmuje w linii poleceń ciągi argumentów określające <m> jakie akcje ma wykonać i na jakim zbiorze ustawień ma je wykonać. <m>'
			'Pierwszy argument określa właśnie ten zbiór i mogą to być ustawienia <m> takie jak adresy, trasy routingowe, interfejsy L2, interfejsy tunelowe, <itd>[i te de]. <m>'
			'Domyślnym działaniem, jeżeli ciąg argumentów zakończymy na określeniu <m> tego zbioru, jest wypisanie informacji na temat wskazanego zbioru. <m>'
		]
	},
	{
		'console': [
			[0.0, eduMovie.prompt()],
			[0.058368, "o", "i"],
			[0.314328, "o", "p"],
			[0.690461, "o", " "],
			[0.978361, "o", "a"],
			[1.298309, "o", "d"],
			[1.45029, "o", "d"],
			[1.738358, "o", "r"],
			[2.12497, "o", "\n\r" + eduMovie.markLines(code_ipa_output, edit=False)],
			[2.126245, "o", eduMovie.prompt()],
			
			["ipa_eth1", "o",  eduMovie.editBegin(7) + "    link/ether " + eduMovie.markBegin + "f4:6d:04:4e:ad:e8" + eduMovie.markEnd + " brd ff:ff:ff:ff:ff:ff" + eduMovie.editEnd(7)],
			["ipa_eth2", "o",  eduMovie.editBegin(7) + "    link/ether f4:6d:04:4e:ad:e8 brd " + eduMovie.markBegin + "ff:ff:ff:ff:ff:ff" + eduMovie.markEnd + eduMovie.editEnd(7)],
			["ipa_inet1", "o", eduMovie.editBegin(7) + "    link/ether f4:6d:04:4e:ad:e8 brd ff:ff:ff:ff:ff:ff" + eduMovie.editEnd(7)],
			
			["ipa_inet1", "o", eduMovie.editBegin(6) + "    " + eduMovie.markBegin + "inet" + eduMovie.markEnd + " 192.168.6.3/24 brd 192.168.6.255 scope global dynamic eth0" + eduMovie.editEnd(6)],
			["ipa_inet2", "o", eduMovie.editBegin(6) + "    inet " + eduMovie.markBegin + "192.168.6.3/24" + eduMovie.markEnd + " brd 192.168.6.255 scope global dynamic eth0" + eduMovie.editEnd(6)],
			["ipa_inet3", "o", eduMovie.editBegin(6) + "    inet 192.168.6.3/24 brd " + eduMovie.markBegin + "192.168.6.255" + eduMovie.markEnd + " scope global dynamic eth0" + eduMovie.editEnd(6)],
			["ipa_inet4", "o", eduMovie.editBegin(6) + "    inet 192.168.6.3/24 brd 192.168.6.255 scope global dynamic eth0" + eduMovie.editEnd(6)],
			
			["ipa_inet6", "o", eduMovie.editBegin(4) + "    " + eduMovie.markBegin + "inet6" + eduMovie.markEnd + " 2001:0db8::6411:f66d:4ff:fe4e:ade8/64 scope global dynamic mngtmpaddr" + eduMovie.editEnd(4)],
			["ipa_inet7", "o", eduMovie.editBegin(4) + "    inet6 " + eduMovie.markBegin + "2001:0db8::6411:f66d:4ff:fe4e:ade8/64" + eduMovie.markEnd + " scope global dynamic mngtmpaddr" + eduMovie.editEnd(4)],
			["ipa_inet8", "o", eduMovie.editBegin(4) + "    inet6 2001:0db8::6411:f66d:4ff:fe4e:ade8/64 scope global dynamic mngtmpaddr" + eduMovie.editEnd(4)],
			
			["ipa_inet8", "o",   eduMovie.clear + eduMovie.prompt() + "ip addr\n\r" + eduMovie.markLines(code_ipa_output, [10, 12], edit=False) + eduMovie.prompt()],
			["ipa_local", "o",   eduMovie.clear + eduMovie.prompt() + "ip addr\n\r" + eduMovie.markLines(code_ipa_output, [12], edit=False) + eduMovie.prompt()],
			["ipa_global", "o",  eduMovie.clear + eduMovie.prompt() + "ip addr\n\r" + eduMovie.markLines(code_ipa_output, [10], edit=False) + eduMovie.prompt()],
			["ipa_updown1", "o", eduMovie.clear + eduMovie.prompt() + "ip addr\n\r" + eduMovie.markLines(code_ipa_output, [6], edit=False) + eduMovie.prompt()],
			["ipa_updown2", "o", eduMovie.clear + eduMovie.prompt() + "ip addr\n\r" + eduMovie.markLines(code_ipa_output, edit=False) + eduMovie.prompt()],
			
			["ipa_updown2", "o", eduMovie.editBegin(9) + "2: eth0: <BROADCAST,MULTICAST," + eduMovie.markBegin + "UP,LOWER_UP" + eduMovie.markEnd + "> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000" + eduMovie.editEnd(8)],
			["ipa_updown3", "o", eduMovie.editBegin(9) + "2: eth0: <BROADCAST,MULTICAST," + eduMovie.markBegin + "UP" + eduMovie.markEnd + ",LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000" + eduMovie.editEnd(8)],
			["ipa_updown4", "o", eduMovie.editBegin(9) + "2: eth0: <BROADCAST,MULTICAST,UP," + eduMovie.markBegin + "LOWER_UP" + eduMovie.markEnd + "> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000" + eduMovie.editEnd(8)],
			["ipa_add", "o", eduMovie.editBegin(9) + "2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000" + eduMovie.editEnd(8)],
			
			["ipa_add", "o", eduMovie.prompt() + "sudo ip addr add 10.0.71.113/20 dev eth0"],
			["ipa_add + 2.3", "o", "\n\r" + eduMovie.prompt()],
			["ipa_add + 2.5", "o", "\n\r" + eduMovie.prompt()],
			["ipa_add + 3.3", "o", "ip addr"],
			["ipa_add + 3.9", "o", "\n\r" + eduMovie.markLines(code_ipa_output2 + eduMovie.prompt(), edit=False)],
			
			["ipa_del", "o",  eduMovie.prompt() + "sudo ip addr del 10.0.71.113/20 dev eth0"],
			["ipa_delX", "o", "^C\n\r" + eduMovie.prompt()],
			
			["ipr", "o", "ip route"],
			["ipr + 1.82497", "o", "\n\r" + eduMovie.markLines(code_ipr_output2 + eduMovie.prompt(), edit=False)],
			["automatycznatrasa", "o", eduMovie.markLines(code_ipr_output2 + eduMovie.prompt(), [1])],
			#["automatycznatrasa2", "o", eduMovie.markLines(eduMovie.runCommandString(r"sipcalc 10.0.71.113/20"), [11], edit=False)]
		],
		'text' : [
			'Polecenie ip address, ip addr lub jeszcze krócej ip a wypisze informację <m> na temat adresów na poszczególnych interfejsach. <m>'
			
			'Warto wspomnieć o tym jakie informacje podało nam takie wywołanie polecenia ip. <m>'
			'Widzimy <mark name="ipa_eth1" /> adres <ethernetowy>[eternetowy] wraz z <mark name="ipa_eth2" /> <ethernetowym>[eternetowym] adresem rozgłoszeniowym. <m>'
			'<mark name="ipa_inet1" />Jako inet podawany <mark name="ipa_inet2" /> jest adres IPv4 wraz z długością prefixu <mark name="ipa_inet3" />'
				'oraz adresem rozgłoszeniowym <mark name="ipa_inet4" /> oraz dodatkowymi informacjami o tym adresie. <m>'
			'<mark name="ipa_inet6" /> Jako <inet6>[inet sześć] podawany <mark name="ipa_inet7" /> jest adres IPv6 wraz z długością prefixu. <mark name="ipa_inet8" />'
			
			'Widzimy że mamy dwa adresy IPv6 – jeden z nich rozpoczyna się <mark name="ipa_local" /> od prefiksu fe80 i jest adresem link-local, <m>'
			'co zresztą sama komenda ip nam zaznacza pisząc <"scope link">[skołp link], <mark name="ipa_global" /> drugi jest już standardowym routowalnym adresem IPv6 o zasięgu globalnym, czyli <"scope global">[skołp global]. <mark name="ipa_updown1" />'
			
			'Wynik komendy również podaje także pewne informacje <m> na temat interfejsu warstwy niższej, najbardziej użytecznymi są informacje <mark name="ipa_updown2" /> up / down, lower up / lower down. <mark name="ipa_updown3" />'
			'Pierwsze z nich odnoszą się do konfiguracyjnego <m> włączenia / wyłączenia interfejsu sieciowego. <mark name="ipa_updown4" />'
			'Lower up lub down informuje nas o tym czy dostępne jest medium transmisyjne <m> na którym warstwa niższa funkcjonuje, czy też nie jest dostępne. <m>'
			'Na przykład jeżeli w przypadku interfejsu przewodowego wyjmiemy kabel <m> <ethernetowy>[eternetowy] to pojawi się tutaj lower down. <mark name="ipa_add" />'
			
			'Jeżeli polecenie to rozbudujemy do postaci ip address add <m> lub krócej ip <break time="80ms"/> a <break time="100ms"/> a, to będziemy mogli użyć go do dodania <m> wskazanego adresu na wskazany po nim interfejs. <m>'
			'Oczywiście działania inne niż wyświetlanie jakiś informacji, <m> będą wymagały stosownych uprawnień, najczęściej uprawnień <root’a>[ruta]. <m>'
			'Na pojedynczym interfejsie może być skonfigurowanych wiele różnych adresów. <mark name="ipa_del" />'
			
			'W podobny sposób, pisząc ip address del, możemy usuwać adresy z interfejsu, <mark name="ipa_delX" /> ale nie róbmy tego jeszcze w tej chwili. <mark name="ipr" />'
			
			'Output polecenia ip route znany nam jest już <m> z omawiania zagadnień związanych z tablicą routingu, <m> bo właśnie informacje na jej temat wypisuje to polecenie. <m>'
			'Domyślnie wypisuje tablicę dla IPv4, <m> aby uzyskać tablicę dla IPv6 należy dodać opcję -6. <m>'
			'Tutaj także, podobnie jak w ip a, możemy skrócić route do litery r <m> i możemy także dodawać i usuwać trasy routingowe. <m>'
			
			'Dzięki temu że nie usunęliśmy jeszcze dodanego niedawno adresu, <mark name="automatycznatrasa" />'
				'widzimy iż z każdym adresem ustawionym na interfejsie <m> wiąże się trasa routingowa do sieci w której znajduje się ten adres. <mark name="automatycznatrasa2" />'
			'Sieć ta jest zdefiniowana przez prefix określony w tym adresie, <m> o długości podanej przy jego ustawianiu na danym interfejsie. <m>       '
		]
	},
	{
		'image': [
			[0.0, eduMovie.convertFile('polecenie_ip_2.tex', negate=True)],
			["slajd2", eduMovie.convertFile('polecenie_ip_3.tex', negate=True)],
		],
		'text' : [
			'Polecenie ip link wypisze nam informacje o interfejsach L2, <m> z odpowiednimi wywołaniami umożliwia włączanie i wyłączanie takich interfejsów, <m> zmienianie adresów L2, konfiguracje <VLANów>[vi lanów] tagowanych. <m>'
			
			'Włączenie, wyłączenie interfejsu odbywa się za pomocą poleceń <m> up i down wykonanych na wskazanym interfejsie. <m>'
			'Konfiguracja <VLANów>[vi lanów] polega na utworzeniu interfejsu typu <VLAN>[vi lan] <m> z określonym id (czyli tym <12>[dwunasto] bitowym numerem <VLANu>[vi lanu]) <m> na danym interfejsie sieciowym. <m>'
			'Typowo interfejsy związane z <VLANami>[vi lanami] nazywa się od nazwy interfejsu bazowego <m> dodając do niej po kropce numer wskazanego <VLANu>[vi lanu], ale jest to jedynie konwencja. <mark name="slajd2" />'
			
			'Ponadto polecenie to pozwala utworzyć programowy <m> (czyli realizowany na poziomie systemu operacyjnego) <m> switch złożony z kilku interfejsów sieciowych. <m>'
			'W tym celu należy utworzyć interfejs typu bridge <m> i następnie dodać do niego interfejsy wchodzące w skład takiego switcha, <m> tak jak pokazano na ekranie. <m>'
			"Do zarządzania switch'ami programowymi przydatne może być też polecenie bridge. <m>"
			
			'Polecenie ip umożliwia też konfigurowanie, wspomnianych przy omawianiu sieci ethernet, <m> <trunków>[tranków] złożonych z kilku interfejsów sieciowych. <m>'
			"Podobnie jak przy bridge'ach należy tutaj utworzyć interfejs typu bond <m> i dodać do niego odpowiednie interfejsy składowe. <m>"
		]
	},
	{
		'image': [
			[0.0, eduMovie.convertFile('polecenie_ip_old_new.tex', negate=True)],
		],
		'text' : [
			'Na wielu systemach nadal są dostępne klasyczne komendy <m> służące konfiguracji sieci takie jak: ifconfig <m> (który odpowiada za funkcjonalność ip address <m> oraz włączanie i wyłączanie interfejsów), <m>'
				'route (który odpowiada za obsługę tablic routingu), <m> <vconfig>[V config] (do konfiguracji <VLANów>[vi lanów]), <m> <brctrl>[BR ctrl] (do konfiguracji bridge) i ifenslave (do konfiguracji bondów). <m>'
			
			'Warto jednak mieć świadomość istnienia komend ifconfig oraz route, <m> ponieważ na wielu innych systemach uniksowych w ten sposób konfiguruje się sieć, <m> jednak składnia tych komend jest różna na różnych systemach. <m>'
			'Natomiast w Linuxach całość funkcjonalności tych poleceń przejęta została <m> przez komendę ip i również coraz częściej polecenia te nie są <m> standardowo instalowane na nowych systemach. <m>'
			
			'Innym poleceniem związanym z konfiguracją sieci, <m> którego szczegółowo nie będziemy omawiać, <m> jest tc od Traffic Control. <m>'
			'Umożliwia ono konfigurację ustawień kontroli przepływu <m> - na przykład kolejkowania, związanych z tym prędkości ruchu i tak dalej <m> na poszczególnych interfejsach sieciowych. <m>'
			'Przydatny jest jeżeli nasz Linux ma pełnić funkcje routingowe <m> i mamy potrzebę na przykład regulacji bądź ograniczenia <m> przepustowości na konkretnych interfejsach. <m>'
			
			'Konfiguracja interfejsów dokonywana poleceniami ip, <m> jego klasycznymi odpowiednikami, poleceniem tc i innymi tego typu komendami <m> jest konfiguracją typu <run-time>[rantajm], czyli jest tracona po wyłączeniu systemu. <m>'
			'W związku z tym polecenia te często zapisywane są w postaci plików, <m> będących skryptami powłoki uruchamianymi w trakcie startu systemu operacyjnego. <m>'
			'A jeszcze częściej wykorzystywane są pliki konfiguracyjne <m> (specyficzne dla danej rodziny dystrybucji Linuxa), <m>'
				"które są <parsowane>[pars'owane] przez skrypty uruchomieniowe celem wykonania <m> w oparciu o ich treść odpowiedniej konfiguracji interfejsów. <m>",
			
			"Należy wspomnieć także o narzędziach używanych do konfiguracji sieci bezprzewodowych takich jak <m>"
				"<iwconfig>[I W config] obsługujący podstawowe operacje na interfejsie bezprzewodowym, <m>"
				"<iwlist>[I W list] służący do listowania widocznych sieci i informacji o nich <m>"
				"oraz <wpa_supplicant>[W P A supplicant] służący do łączenia się z sieciami zabezpieczonymi WPA. <m>"
			"Możliwe jest też uczynienie z komputera z linuxem i kartą wi-fi <m> access <pointa>[pojta] przy pomocy programu <hostapd>[host A P D]. <m>"
			"Jeżeli chcemy oferować DHCP i DNS przyda się także <dnsmasq>[DNS mask]. <m>"
		]
	},
]
