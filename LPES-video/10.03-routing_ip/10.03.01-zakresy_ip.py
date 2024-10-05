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
	{ 'title': [ "#10.3", "Adresacja i", "routing IP", "" ] },
	
	{ 'comment': 'zakreys IP' },
	{
		'console': [
			[0.071632, "o", eduMovie.prompt()],
			["sipcalc", "o", "sipcalc 2001:0db8:abcd:30::6543/59"],
			["sipcalc + 1.348619", "o", "\r\n"],
			["sipcalc + 1.351733", "o", "-[ipv6 : 2001:0db8:abcd:30::6543/59] - 0\r\n\r\n[IPV6 INFO]\r\nExpanded Address\t- 2001:0db8:abcd:0030:0000:0000:0000:6543\r\nCompressed address\t- 2001:db8:abcd:30::6543\r\nSubnet prefix (masked)\t- 2001:db8:abcd:20:0:0:0:0/59\r\nAddress ID (masked)\t- 0:0:0:10:0:0:0:6543/59\r\nPrefix address\t\t- ffff:ffff:ffff:ffe0:0:0:0:0\r\nPrefix length\t\t- 59\r\nAddress type\t\t- Aggregatable Global Unicast Addresses\r\nNetwork range\t\t- 2001:0db8:abcd:0020:0000:0000:0000:0000 -\r\n\t\t\t  2001:0db8:abcd:003f:ffff:ffff:ffff:ffff\r\n\r\n-\r\n"],
			["sipcalc + 1.352862", "o", eduMovie.prompt()],
			
			["Expanded", "o", eduMovie.editBegin(11) + "Expanded Address\t- " + eduMovie.markBegin + "2001:0db8:abcd:0030:0000:0000:0000:6543" + eduMovie.markEnd + eduMovie.editEnd(11)],
			["Compressed - 0.5", "o", eduMovie.editBegin(11) + "Expanded Address\t- 2001:0db8:abcd:0030:0000:0000:0000:6543" + eduMovie.editEnd(11)],
			["Compressed", "o", eduMovie.editBegin(10) + "Compressed address\t- " + eduMovie.markBegin + "2001:db8:abcd:30::6543" + eduMovie.markEnd + eduMovie.editEnd(10)],
			["Subnet", "o", eduMovie.editBegin(10) + "Compressed address\t- 2001:db8:abcd:30::6543" + eduMovie.editEnd(10)],
			["Subnet", "o", eduMovie.editBegin(9) + "Subnet prefix (masked)\t- " + eduMovie.markBegin + "2001:db8:abcd:20:0:0:0:0/59" + eduMovie.markEnd + eduMovie.editEnd(9)],
			["Host", "o", eduMovie.editBegin(9) + "Subnet prefix (masked)\t- 2001:db8:abcd:20:0:0:0:0/59" + eduMovie.editEnd(9)],
			["Host", "o", eduMovie.editBegin(8) + "Address ID (masked)\t- " + eduMovie.markBegin + "0:0:0:10:0:0:0:6543/59" + eduMovie.markEnd + eduMovie.editEnd(8)],
			["Prefix1 - 0.1", "o", eduMovie.editBegin(8) + "Address ID (masked)\t- 0:0:0:10:0:0:0:6543/59" + eduMovie.editEnd(8)],
			["Prefix1", "o", eduMovie.editBegin(7) + "Prefix address\t\t- " + eduMovie.markBegin + "ffff:ffff:ffff:ffe0:0:0:0:0" + eduMovie.markEnd + eduMovie.editEnd(7)],
			["Prefix2", "o", eduMovie.editBegin(7) + "Prefix address\t\t- ffff:ffff:ffff:ffe0:0:0:0:0" + eduMovie.editEnd(7)],
			["Prefix2", "o", eduMovie.editBegin(6) + "Prefix length\t\t- " + eduMovie.markBegin + "59" + eduMovie.markEnd + eduMovie.editEnd(6)],
			["Type", "o", eduMovie.editBegin(6) + "Prefix length\t\t- 59" + eduMovie.editEnd(6)],
			["Type", "o", eduMovie.editBegin(5) + "Address type\t\t- " + eduMovie.markBegin + "Aggregatable Global Unicast Addresses" + eduMovie.markEnd + eduMovie.editEnd(5)],
			["Range", "o", eduMovie.editBegin(5) + "Address type\t\t- Aggregatable Global Unicast Addresses" + eduMovie.editEnd(5)],
			["Range", "o", eduMovie.editBegin(4) + "Network range\t\t- " + eduMovie.markBegin + "2001:0db8:abcd:0020:0000:0000:0000:0000 -" + eduMovie.markEnd + eduMovie.editEnd(4)],
			["Range", "o", eduMovie.editBegin(3) + "\t\t\t- " + eduMovie.markBegin + " 2001:0db8:abcd:003f:ffff:ffff:ffff:ffff" + eduMovie.markEnd + eduMovie.editEnd(3)],
			["End", "o", eduMovie.editBegin(4) + "Network range\t\t- 2001:0db8:abcd:0020:0000:0000:0000:0000 -" + eduMovie.editEnd(4)],
			["End", "o", eduMovie.editBegin(3) + "\t\t\t-  2001:0db8:abcd:003f:ffff:ffff:ffff:ffff" + eduMovie.editEnd(3)],
			
			["Podzial + 0.546367", "o", "sipcalc 2001:0db8:abcd:20::/60"],
			["Podzial + 0.854209", "o", "\r\n"],
			["Podzial + 0.857166", "o", "-[ipv6 : 2001:0db8:abcd:20::/60] - 0\r\n\r\n[IPV6 INFO]\r\nExpanded Address\t- 2001:0db8:abcd:0020:0000:0000:0000:0000\r\nCompressed address\t- 2001:db8:abcd:20::\r\nSubnet prefix (masked)\t- 2001:db8:abcd:20:0:0:0:0/60\r\nAddress ID (masked)\t- 0:0:0:0:0:0:0:0/60\r\nPrefix address\t\t- ffff:ffff:ffff:fff0:0:0:0:0\r\nPrefix length\t\t- 60\r\nAddress type\t\t- Aggregatable Global Unicast Addresses\r\nNetwork range\t\t- 2001:0db8:abcd:0020:0000:0000:0000:0000 -\r\n\t\t\t  2001:0db8:abcd:002f:ffff:ffff:ffff:ffff\r\n\r\n-\r\n"],
			["Podzial + 0.858268", "o", eduMovie.prompt()],
			["Podzial2", "o", eduMovie.editBegin(3) + "\t\t\t  2001:0db8:abcd:" + eduMovie.markBegin + "002f" + eduMovie.markEnd + ":ffff:ffff:ffff:ffff" + eduMovie.editEnd(3)],
			["Podzial3", "o", eduMovie.editBegin(3) + "\t\t\t  2001:0db8:abcd:002f:ffff:ffff:ffff:ffff" + eduMovie.editEnd(3)],
			["Podzial3 + 0.451333", "o", "sipcalc 2001:0db8:abcd:30::/60"],
			["Podzial3 + 0.990583", "o", "\r\n"],
			["Podzial3 + 0.993681", "o", "-[ipv6 : 2001:0db8:abcd:30::/60] - 0\r\n\r\n[IPV6 INFO]\r\nExpanded Address\t- 2001:0db8:abcd:0030:0000:0000:0000:0000\r\nCompressed address\t- 2001:db8:abcd:30::\r\nSubnet prefix (masked)\t- 2001:db8:abcd:30:0:0:0:0/60\r\nAddress ID (masked)\t- 0:0:0:0:0:0:0:0/60\r\nPrefix address\t\t- ffff:ffff:ffff:fff0:0:0:0:0\r\nPrefix length\t\t- 60\r\nAddress type\t\t- Aggregatable Global Unicast Addresses\r\nNetwork range\t\t- 2001:0db8:abcd:0030:0000:0000:0000:0000 -\r\n\t\t\t  2001:0db8:abcd:003f:ffff:ffff:ffff:ffff\r\n\r\n-\r\n"],
			["Podzial3 + 0.994513", "o", eduMovie.prompt()],
			
			["adresIpv4", "o", "# czy 172.137.217.181  w 172.137.208.0/21 ?\r\n" + eduMovie.prompt()],
			["Ipv4", "o", "sipcalc 172.137.208.0/21"],
			["Ipv4 + 0.865341", "o", "\r\n"],
			["Ipv4 + 0.868309", "o", "-[ipv4 : 172.137.208.0/21] - 0\r\n\r\n[CIDR]\r\nHost address\t\t- 172.137.208.0\r\nHost address (decimal)\t- 2894712832\r\nHost address (hex)\t- AC89D000\r\nNetwork address\t\t- 172.137.208.0\r\nNetwork mask\t\t- 255.255.248.0\r\nNetwork mask (bits)\t- 21\r\nNetwork mask (hex)\t- FFFFF800\r\nBroadcast address\t- 172.137.215.255\r\nCisco wildcard\t\t- 0.0.7.255\r\nAddresses in network\t- 2048\r\nNetwork range\t\t- 172.137.208.0 - 172.137.215.255\r\nUsable range\t\t- 172.137.208.1 - 172.137.215.254\r\n\r\n-\r\n"],
			["Ipv4 + 0.868999", "o", eduMovie.prompt()],
		],
		'text' : [
			'Do przeliczania zakresów IP, <m> czyli uzyskania z adresu IP i długości prefixu różnych informacji <m> możemy skorzystać z narzędzi nazywanych kalkulatorami IP, <m>'
				'przykładem takiego narzędzia jest sipcalc. <mark name="sipcalc" />'
			
			'Polecenie to, uruchomione z adresem IPv6 oraz długością prefixu, wypisze <mark name="Expanded" />'
				'rozwiniętą postać adresu, czyli bez kompresji zer oraz postać <mark name="Compressed" /> skompresowaną, w której najdłuższy ciąg zer został zastąpiony dwoma dwukropkami.'
			'<mark name="Subnet" /> Wypisze także adres sieci oraz <mark name="Host" /> id hosta w ramach tej sieci. '
			'Następnie <mark name="Prefix1" /> prefix rozwinięty do postaci adresu, czyli maski <mark name="Prefix2" /> oraz długość prefixu. '
			'W kolejnej linii podana jest <mark name="Type" /> informacja o typie adresu a następnie podany <mark name="Range" /> zakres adresów wchodzących w skład sieci związanej z podanym adresem. <mark name="End" />'
			
			'Możemy też zobaczyć jak wyglądałby podział sieci <m> do której należy ten host na dwie mniejsze. <mark name="Podzial" />'
			'W tym celu możemy uruchomić sipcalc z adresem sieci uzyskanym <m> w poprzednim wywołaniu i zwiększoną o jeden długością prefixu. <mark name="Podzial2" />'
			'Widzimy że zakres naszej sieci kończy się teraz na 2 f, <m> czyli kolejną siecią będzie 3 0. <mark name="Podzial3" />'
			
			'W ten sposób uzyskaliśmy informacje o dwóch sieciach <m> agregujących się w naszą oryginalną sieć. <m>'
			'Łatwo, nawet bez użycia kalkulatora, możemy zauważyć, <m> że adres ip od którego zaczęliśmy leży w zakresie drugiej z tych sieci. <m>'
			
			'Adres sieci wraz z maską pozwala na sprawdzenie <m> czy dany host należy do sieci. <m>'
			'W niektórych przypadkach można to zauważyć <m> na tak zwany pierwszy rzut oka, w innych nie jest to takie oczywiste. <m>'
			'W takim przypadku możemy użyć narzędzia takiego jak właśnie sipcalc, <m> aby wyświetliło nam zakres adresów należących do danej sieci. <mark name="adresIpv4" />'
			'Spróbujmy ustalić czy adres <172.137.217.181>[sto siedemdziesiąt dwa kropka 137 kropka 217 kropka 181] <m> należy do sieci <172.137.208.0/21>[sto siedemdziesiąt dwa kropka 137 kropka 208 kropka 0 slash 21]. <mark name="Ipv4" />'
			'Widzimy że sieć ta kończy się na adresie <172.137.215.255>[sto siedemdziesiąt dwa kropka 137 kropka 215 kropka 255], <m> zatem podany adres nie należy do tej sieci. <m>',
			
			'Operację taką możemy też wykonać także w taki sposób jak robi to komputer. <m> Użyjemy do tego Pythona. <m>'
		]
	},
]

code_adresy_A = r"""
from ipaddress import *
adres = ip_interface("172.137.217.181")
siec  = ip_interface("172.137.208.0/21")

adres = int(adres.ip)
maska = int(siec.netmask)
siec  = int(siec.ip)

print(hex(adres), hex(siec), hex(maska))
"""

code_adresy_B = code_adresy_A + r"""
x = siec & maska
y = adres & maska
"""

code_adresy_C = code_adresy_B + r"""
print(x==y)
"""

clipData += [
	{
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_adresy_A, "py")],
			["codeB", eduMovie.clear + eduMovie.code2console(code_adresy_B, "py")],
			["codeC", eduMovie.clear + eduMovie.code2console(code_adresy_C, "py")],
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(code_adresy_A, [], cmd="python3")],
			["codeB", eduMovie.runCode(code_adresy_B, [], cmd="python3")],
			["codeC", eduMovie.runCode(code_adresy_C, [], cmd="python3")],
		],
		'text' : [
			'W tym celu użyjemy modułu <ipaddress>[ip address], <m> który zapewni nam konwersję adresów na ich wartości liczbowe. <mark name="codeB" />'
			
			'Na uzyskanych liczbach wykonamy operacje bitowe <m> mające na celu wyzerowanie części adresu identyfikującej hosta w obu adresach <m>'
                'i pozostawienie nie wyzerowanej <m> jedynie części związanej z adresem sieci. <m>'
            'Jeżeli adres sieci podajemy w typowej postaci to <m> te bity są już wyzerowane, ale mimo to zróbmy te operacje. <mark name="codeC" />'
			
			'Następnie wystarczy porównać uzyskane w ten sposób adresy sieci, <m> aby wiedzieć czy host należy do danej sieci. <m>'
			'Oczywiście w Pythonie można to zrobić prościej <m> operując bezpośrednio na obiektach zwróconych przez funkcję ip_interface, <m>'
				'ale ten sposób pokazuje wnętrzności mechanizmu <m> sprawdzania przynależności do sieci. <m>',
			
			'Zakładamy tutaj milcząco, że host używa takiej samej <m> długości prefixu jak sprawdzana sieć. <m>'
			'Daje nam to odpowiedź na pytanie o to czy host <m> jest w zakresie adresacji danej sieci, <m>'
				'ale nie mówi nam o tym czy host ma bezpośredni dostęp <m> do wszystkich innych hostów w tej sieci. <m>'
			
			'Tak będzie jeżeli długość prefixu używanego przez hosta jest <m> równa lub mniejsza od długości prefixu sprawdzanej sieci. <m>'
			'Wtedy host uważa że jest fragmentem całej tej sieci. <m>'
			
			'Jeżeli jednak długość prefiksu używana przez hosta byłaby <m> większa niż długość prefiksu sprawdzanej sieci to <m>'
				'host uważa że należy tylko do fragmentu takiej sieci <m> i nie widzi bezpośrednio wszystkich innych hostów w tej sieci. <m>'
		]
	},
	{
		'image': [
			[0.0, eduMovie.convertFile('nierówne_maski.svg', negate=True)],
		],
		'text' : [
			'Na przykład host o adresie <10.20.30.40>[dziesięć kropka 20 kropka 30 kropka czterdziści] i długości prefixu <16>[szesnaście] <m> należy do sieci <10.20.30.0>[10 kropka 20 kropka 30 kropka zero] z długością prefixu <24>[dwadzieścia cztery] <m>'
				'i należy też do sieci <10.0.0.0>[10 kropka 0 kropka 0 kropka 0] z długością prefixu <8>[osiem]. <m>'
			'W pierwszym przypadku <16>[szesnaście] jest mniejsze od 24 <m> zatem host ten widzi całość sieci <10.20.30.0>[10 kropka 20 kropka 30 kropka zero]. <m>'
			'W drugim wypadku host ten widzi bezpośrednio <m> tylko fragment sieci <10.0.0.0>[10 kropka 0 kropka 0 kropka 0], ale nie widzi na przykład hosta <10.100.1.1>[10 kropka 100 kropka jeden kropka jeden], <m>'
				'należącego także do tej sieci. <m>'
			
			'Jest to normalna sytuacja, dopóki zachodzi wzajemność, <m> czyli host <10.100.1.1>[10 kropka 100 kropka jeden kropka jeden] też ma odpowiednio większą długość prefixu niż 8 <m>'
				'i uważa że nie widzi bezpośrednio hosta <10.20.30.40>[10 kropka 20 kropka 30 kropka czterdziści]. <m>'
		]
	},
]
