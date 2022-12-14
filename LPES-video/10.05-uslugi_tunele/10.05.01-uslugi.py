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

services = open("/etc/services").read().split("\n")

url_txt = r"""
 https://user:passw@nazwa.domenowa.serw:8888/katalog/plik.php?arg1=valabc=123
 \___/    \__/ \__/ \_________________/ \__/\_______________/ \_____________/
   |       |     |           |            |           |                |
protokół  login hasło       host        port       ścieżka         argumenty
                       (adres serwera)

Przykłady:
  http://ciekawi.icm.edu.pl/materialy/edycja_XII/LPES.html
  http://213.135.60.13/
  http://[2001:6a0:0:21::60:13]:80/
  
  mailto:ciekawi@icm.edu.pl
  ssh://rrp@icm.edu.pl/home/rrp/plik.txt
"""

clipData += [
	{ 'title': [ "#10.5", "Usługi", "sieciowe", "i tunele" ] },
	
	{ 'comment': 'usługi w sieciach' },
	{
		'console': [
			[0.0, ""],
		],
		'text' : [
			'W ramach sieci mamy do czynienia z różnymi usługami realizowanymi <m> w oparciu o TCP przez protokoły warstw wyższych. <m>'
			'Przede wszystkim trzeba wspomnieć o protokole używanym do przesyłu <m> treści WWW czyli HTTP, protokole przesyłu poczty elektronicznej – SMTP, <m> protokołach dostępu do poczty elektronicznej POP3 i IMAP. <m>'
			'Należy też wspomnieć o protokołach związanych ze strumieniowaniem mediów <m> takich jak RTP i RTSP, protokołach Voice over IP – SIP i IAX <m> oraz komunikacji natychmiastowej – XMPP. <m>'
		]
	},
	{
		'console': [
			[0.0, "o", eduMovie.prompt()],
			[0.82227108433735, 'o', 'n'],
			[1.2750590361445786, 'o', 'c'],
			[1.405144578313253, 'o', ' '],
			[1.5786933734939759, 'o', '-'],
			[1.8485451807228916, 'o', 'C'],
			[2.1136234939759038, 'o', ' '],
			[2.4172457831325302, 'o', 'm'],
			[2.5328626506024094, 'o', 'a'],
			[2.629238554216868, 'o', 'i'],
			[2.7979481927710843, 'o', 'l'],
			[2.95205843373494, 'o', '.'],
			[3.125631325301205, 'o', 'o'],
			[3.236457831325301, 'o', 'p'],
			[3.3521481927710846, 'o', 'c'],
			[3.4677927710843375, 'o', 'o'],
			[3.602725903614458, 'o', 'd'],
			[3.752145180722892, 'o', 'e'],
			[3.9834975903614462, 'o', '.'],
			[4.190686144578313, 'o', 'e'],
			[4.364219879518073, 'o', 'u'],
			[4.571447590361446, 'o', '.'],
			[4.7641746987951805, 'o', 'o'],
			[5.0485614457831325, 'o', 'r'],
			[5.241342771084337, 'o', 'g'],
			[5.5063849397590365, 'o', ' '],
			[5.795556626506024, 'o', '2'],
			[6.041291566265061, 'o', '5'],
			[6.537725903614458, 'o', '\r\n'],
			[6.545798795180723, 'o', '220 dragon.icm.edu.pl ESMTP Exim 4.92 Fri, 12 Feb 2021 21:03:09 +0000\r\r\n'],
			[8.291926506024096, 'o', 'h'],
			[8.407519277108435, 'o', 'e'],
			[8.561780120481927, 'o', 'l'],
			[8.730474698795181, 'o', 'o'],
			[8.903930722891568, 'o', ' '],
			[9.01957891566265, 'o', 't'],
			[9.149709036144579, 'o', 'e'],
			[9.265364457831325, 'o', 's'],
			[9.381049397590361, 'o', 't'],
			[9.949780722891566, 'o', '\r\n'],
			[9.976630722891567, 'o', '250 dragon.icm.edu.pl Hello test [2a01:110f:345:900::1]\r\r\n'],
			[11.36182590361446, 'o', 'm'],
			[11.458175903614459, 'o', 'a'],
			[11.554535542168676, 'o', 'i'],
			[11.708766265060241, 'o', 'l'],
			[12.031642168674699, 'o', ' '],
			[12.147283132530122, 'o', 'f'],
			[12.27740903614458, 'o', 'r'],
			[12.412385542168675, 'o', 'o'],
			[12.566573493975904, 'o', 'm'],
			[12.831710843373495, 'o', ':'],
			[13.366628915662652, 'o', ' '],
			[13.536628915662652, 'o', '<'],
			[13.670239759036145, 'o', 'p'],
			[13.805124698795181, 'o', 'r'],
			[13.901541566265061, 'o', 'e'],
			[14.147336144578313, 'o', 'z'],
			[14.282248192771085, 'o', 'y'],
			[14.397942168674698, 'o', 'd'],
			[14.508788554216869, 'o', 'e'],
			[14.778678313253014, 'o', 'n'],
			[14.908775903614458, 'o', 't'],
			[15.236557831325301, 'o', '@'],
			[15.559331325301205, 'o', 'g'],
			[16.224494578313255, 'o', 'o'],
			[16.62929638554217, 'o', 'v'],
			[16.878648192771084, 'o', '.'],
			[17.275061445783134, 'o', 'p'],
			[17.467811445783134, 'o', 'l'],
			[17.578648192771084, 'o', '>'],
			[18.036520481927713, 'o', '\r\n'],
			[18.06417469879518, 'o', '250 OK\r\r\n'],
			[19.260668674698795, 'o', 'r'],
			[19.48712590361446, 'o', 'c'],
			[19.75702048192771, 'o', 'p'],
			[19.944963253012048, 'o', 't'],
			[20.460627710843372, 'o', ' '],
			[20.59556024096386, 'o', 't'],
			[20.706409036144578, 'o', 'o'],
			[21.053440963855422, 'o', ':'],
			[21.583560240963855, 'o', ' '],
			[21.673560240963855, 'o', '<'],
			[21.834110240963856, 'o', 'r'],
			[21.9304578313253, 'o', 'r'],
			[22.007647590361444, 'o', 'p'],
			[22.27266746987952, 'o', '@'],
			[23.51127891566265, 'o', 'o'],
			[23.64611265060241, 'o', 'p'],
			[23.80041807228916, 'o', 'c'],
			[23.949764457831325, 'o', 'o'],
			[24.200378313253015, 'o', 'd'],
			[24.311218072289158, 'o', 'e'],
			[24.426919277108432, 'o', '.'],
			[24.56182590361446, 'o', 'e'],
			[24.716057228915663, 'o', 'u'],
			[24.923262048192775, 'o', '.'],
			[25.077501807228916, 'o', 'o'],
			[25.226877108433737, 'o', 'r'],
			[25.38103313253012, 'o', 'g'],
			[25.58103313253012, 'o', '>'],
			[25.626939759036144, 'o', '\r\n'],
			[25.67932891566265, 'o', '250 Accepted\r\r\n'],
			[26.85108734939759, 'o', 'd'],
			[27.135369277108435, 'o', 'a'],
			[27.289556024096388, 'o', 't'],
			[27.438973493975904, 'o', 'a'],
			[27.76668373493976, 'o', '\r\n'],
			[27.794401204819277, 'o', '354 Enter message, ending with "." on a line by itself\r\r\n'],
			[28.793195180722893, 'o', 'F'],
			[28.928127710843373, 'o', 'r'],
			[29.140107228915664, 'o', 'o'],
			[29.289569879518073, 'o', 'm'],
			[29.55949578313253, 'o', ':'],
			[30.036584939759038, 'o', ' '],
			[30.417321084337352, 'o', 't'],
			[30.64376746987952, 'o', 'r'],
			[30.836543373493978, 'o', 'u'],
			[30.99074939759036, 'o', 'm'],
			[31.140159638554216, 'o', 'p'],
			[31.37149638554217, 'o', 'h'],
			[31.810145180722895, 'o', '@'],
			[32.51370361445783, 'o', 'w'],
			[32.72574096385542, 'o', 'h'],
			[33.02936024096386, 'o', '.'],
			[33.77153915662651, 'o', 'g'],
			[34.00286325301205, 'o', 'o'],
			[34.176339759036146, 'o', 'v'],
			[34.32579819277109, 'o', '.'],
			[34.51843373493976, 'o', 'u'],
			[34.68720843373494, 'o', 's'],
			[35.20288373493976, 'o', '\r\n'],
			[38.36920542168675, 'o', 'T'],
			[38.54262289156627, 'o', 'o'],
			[38.754730722891566, 'o', ':'],
			[39.23180903614458, 'o', ' '],
			[39.38117289156627, 'o', 'p'],
			[39.57393313253012, 'o', 'u'],
			[39.72333975903614, 'o', 't'],
			[40.031786746987954, 'o', 'i'],
			[40.1619343373494, 'o', 'n'],
			[40.48968253012048, 'o', '@'],
			[42.205345180722894, 'o', 'g'],
			[42.39804096385542, 'o', 'o'],
			[42.586044578313256, 'o', 'v'],
			[42.72096084337349, 'o', '.'],
			[42.94745602409639, 'o', 'r'],
			[43.10165662650603, 'o', 'u'],
			[43.54027228915663, 'o', '\r\n'],
			[44.629436144578314, 'o', 'S'],
			[44.79806265060241, 'o', 'u'],
			[44.913733132530126, 'o', 'b'],
			[45.04866987951808, 'o', 'j'],
			[45.159487349397594, 'o', 'e'],
			[45.31372409638554, 'o', 'c'],
			[45.42936746987952, 'o', 't'],
			[45.771667469879525, 'o', ':'],
			[46.22940783132531, 'o', ' '],
			[46.32576927710844, 'o', 'w'],
			[46.46073554216868, 'o', 'o'],
			[46.61011144578313, 'o', 'j'],
			[46.783643975903615, 'o', 'n'],
			[46.976375301204826, 'o', 'a'],
			[47.44872530120482, 'o', '\r\n'],
			[47.945121686746994, 'o', '\r\n'],
			[48.67281084337349, 'o', 'T'],
			[48.841486746987954, 'o', 'o'],
			[49.09205180722892, 'o', ' '],
			[49.24629277108434, 'o', 'k'],
			[49.33786566265061, 'o', 'i'],
			[49.45351746987952, 'o', 'e'],
			[49.56916385542169, 'o', 'd'],
			[49.66555301204819, 'o', 'y'],
			[49.79569036144579, 'o', ' '],
			[49.9691765060241, 'o', 'o'],
			[50.12339397590362, 'o', 'd'],
			[50.44631686746988, 'o', 'p'],
			[50.60049879518072, 'o', 'a'],
			[50.71134277108434, 'o', 'l'],
			[50.82700060240964, 'o', 'a'],
			[50.9232921686747, 'o', 'm'],
			[51.1113186746988, 'o', 'y'],
			[51.49692168674699, 'o', ' '],
			[52.465643373493975, 'o', 'a'],
			[52.773995783132534, 'o', 't'],
			[52.94269698795181, 'o', 'o'],
			[53.077653012048195, 'o', 'm'],
			[53.21256807228916, 'o', 'o'],
			[53.32344518072289, 'o', 'w'],
			[53.41981385542169, 'o', 'k'],
			[53.53545060240964, 'o', 'i'],
			[53.89703493975904, 'o', '?'],
			[54.75480120481928, 'o', ' '],
			[55.174065662650605, 'o', 'M'],
			[55.28968493975904, 'o', 'n'],
			[55.40534156626506, 'o', 'i'],
			[55.50173674698796, 'o', 'e'],
			[55.59323373493976, 'o', ' '],
			[55.80537951807229, 'o', 'p'],
			[55.920923493975906, 'o', 'a'],
			[56.070378313253016, 'o', 's'],
			[56.22460542168675, 'o', 'u'],
			[56.34030963855422, 'o', 'j'],
			[56.470433132530125, 'o', 'e'],
			[56.81740722891566, 'o', ' '],
			[56.96674939759036, 'o', 'w'],
			[57.14030602409639, 'o', ' '],
			[57.44392951807229, 'o', 'p'],
			[57.55952349397591, 'o', 'o'],
			[57.694462048192776, 'o', 'n'],
			[57.80535722891566, 'o', 'i'],
			[57.90173373493976, 'o', 'e'],
			[58.01739457831326, 'o', 'd'],
			[58.13304277108434, 'o', 'z'],
			[58.17149939759037, 'o', 'i'],
			[58.26320421686748, 'o', 'a'],
			[58.4752578313253, 'o', 'l'],
			[58.59089759036145, 'o', 'e'],
			[58.75956927710844, 'o', 'k'],
			[60.07533554216868, 'o', '.'],
			[60.21019638554217, 'o', ' '],
			[60.40296204819278, 'o', 'A'],
			[60.53307168674699, 'o', ' '],
			[60.66802771084338, 'o', 't'],
			[60.7643921686747, 'o', 'o'],
			[60.93308253012048, 'o', 'b'],
			[61.06800060240965, 'o', 'i'],
			[61.145107831325305, 'o', 'e'],
			[61.56450421686747, 'o', '?'],
			[62.06084819277108, 'o', '\r\n'],
			[62.46083855421686, 'o', '\r\n'],
			[62.91866506024097, 'o', 'P'],
			[63.015039156626514, 'o', 'o'],
			[63.12588132530121, 'o', 'z'],
			[63.260795180722894, 'o', 'd'],
			[63.37648975903615, 'o', 'r'],
			[63.58368493975904, 'o', 'o'],
			[63.892215060240964, 'o', '!'],
			[64.13784337349398, 'o', '\r\n'],
			[64.89934397590362, 'o', '.'],
			[65.18854879518072, 'o', '\r\n'],
			[66.91543855421688, 'o', '250 OK id=1lAfbM-0003Tu-S0\r\r\n'],
			[68.4849873493976, 'o', 'q'],
			[68.65840662650602, 'o', 'u'],
			[68.77411204819278, 'o', 'i'],
			[68.94275481927711, 'o', 't'],
			[69.1355686746988, 'o', '\r\n'],
			[69.16240060240965, 'o', '221 dragon.icm.edu.pl closing connection\r\r\n'],
			[69.73804638554218, 'o', '\r\n'],
			[69.74122771084338, 'o', eduMovie.prompt()],
		],  # timestamps rescale by:   for x in TA_LISTA:  print("[",x[0]/1.66,", 'o', ", x[-1].__repr__(),"],", sep="")
		'text' : [
			'Większość tych protokołów jest protokołami tekstowymi, <m> to znaczy pole danych TCP rozpoczyna się od tekstowego nagłówka <m> danego protokołu warstwy aplikacyjnej, <m>'
				'zarówno w przypadku żądania wysłanego przez klienta <m> jak i odpowiedzi wysłanej przez serwer. <m>'
			'Często całość komunikacji jest tekstowa, <m> jak na przykład w wypadku poczty elektronicznej. <m>'
			'Pozwala to na ręczne nawiązanie dialogu z serwerem takiej usługi <m> korzystając z klienta w postaci na przykład programu netcat lub telnet. <m>',
			
			'Na ekranie widzimy przykładową sesję SMTP, <m> czyli protokołu używanego do przesyłu poczty. <m>'
			'Po nawiązaniu połączenia z serwerem następuje przywitanie się komendą helo, <m> po czym podawane są adresy kopertowe korespondencji. <m>'
			'Warto zauważyć że często adres nadawcy już na tym etapie może być sfałszowany. <m>'
			'Adresu odbiorcy nie możemy sfałszować na tym etapie, <m> gdyż wyznacza on rzeczywistego odbiorcę do którego trafi wysyłany list. <m>'
			'Po komendzie data wysyłana jest treść listu, <m> w nagłówku którego ponownie określani są nadawca i odbiorca. <m>'
			'Tym razem możemy fałszować obu, <m> gdyż jest to tylko informacja wyświetlana w programach pocztowych. <m>'
			'Nagłówek kończymy pustą linią. A całość listu kropką w pustej linii. <m>',
			
			'Zasadniczo w poczcie elektronicznej, tak jak tej tradycyjnej, jedyną wiarygodną informacją jest adres odbiorcy podany na kopercie. <m>'
			'Aby zapewnić wiarygodność informacji o nadawcy i o treści należy stosować podpis elektroniczny. <m>'
			'W odróżnieniu jednak od tradycyjnej poczty, koperty w poczcie elektronicznej, <m> można powiedzieć że są przeźroczyste <m> - każdy po drodze może zobaczyć treść listu. <m>'
			'Aby zapewnić jego poufność należy stosować szyfrowanie end-to-end, <m> czyli takie gdzie dopiero odbiorca odszyfrowuje swoim tajnym kluczem <m> treść zaszyfrowaną przez nadawcę przed jej wysłaniem. <m>'
		]
	},
	{
		'console': [
			[0.0, eduMovie.prompt() + "less /etc/services"],
			*[  [4+i*0.077,  eduMovie.clear + "\n\r".join(services[i:i+23])] for i in range(0,len(services),23) ],
		],
		'text' : [
			'Z standardowymi usługami, takimi jak wcześniej wymienione, <m> a nawet dokładniej konkretnymi protokołami tych usług, <m> związane też są standardowe numery portów <m> na których nasłuchuje serwer danej usługi. <m>'
			'Na przykład serwer SMTP słucha m.in. na porcie <25>[dwadzieścia pięć], <m> serwer WWW na porcie <80>[osiemdziesiąt] i <443>[czterysta czterdzieści trzy] (dla połączeń szyfrowanych), <m> SSH na porcie <22>[dwadzieścia dwa]. <m>'
			"Pozwala to na nawiązywanie połączenia do danej usługi <m> w oparciu jedynie o adres (lub nazwę <domenową>[domen'ową]) hosta na której działa, <m> bez konieczności podawania takiego numeru portu. <m>"
			'Oczywiście usługa może działać na niestandardowym numerze portu <m> i wtedy musimy go jawnie podać w kliencie bądź adresie URL. <m>'
			'Listę standardowych portów wraz z nazwami powiązanych usług <m> znaleźć można w pliku </etc/services>[E T C services], który był wyświetlany na ekranie. <m>'
		]
	},
	{
		'console': [
			[0.0, eduMovie.clear + url_txt.replace("\n", "\n\r")],
		],
		'text' : [
			'Wspomnieliśmy tutaj o adresach URL. <m>'
			'Jest to zunifikowany sposób zapisu informacji o lokalizacji zasobu. <m>'
			'Może określać on używany protokół, <m> nazwę użytkownika i hasło potrzebne do dostępu, <m> nazwę lub adres serwera, numer portu, <m> ścieżkę na systemie zdalnym i dodatkowe argumenty. <m>'
			'Często wiele z tych elementów jest pomijanych, <m> gdyż nie jest wymaganych czy nawet sensownych w danym wypadku. <m>'
			'Jeżeli host określany jest adresem IPv6 adres ten zapisywany jest <m> w nawiasach kwadratowych, aby oddzielić go jednoznacznie od numeru portu. <m>'
		]
	},
	{
		'image': [
			[0.0, eduMovie.convertFile('adresy_ip.tex', margins=12)],
		],
		'text' : [
			'Nie tylko pewne wartości numerów portów mają powszechnie przyjęte znaczenie. <m>'
			'Podobnie jest z niektórymi numerami IP. <m>'
			'Wiemy już że adres złożony z samych zer <m> i o zerowej długości prefiksu oznacza cały internet. <m>'
			'Z koleji do adresowania hosta lokalnego w IPv4 zarezerwowano całą pulę <m> ponad 16 milionów adresów zaczynających się od 127, <m> prawie zawsze jednak jest to <127.0.0.1>[127 kropka 0 kropka 0 kropka jeden]. <m>'
			'W IPv6 jest to adres złożony z samych zer i najmłodszego bitu wartości jeden, <m> czyli po prostu dwukropek dwukropek jeden. <m>'
			
			'Kilka pul adrsów IPv4 zostało zarezerwowanych do użytku prywatnego, <m> czyli nie trzeba otrzymać ich przydziału aby z nich korzystać, <m> natomiast nie są one routowane do ogólnego Internetu. <m>'
			'Są to między innymi adresy zaczynające się od 10 i od 192 kropka 168. <m>'
			
			'W IPv6 warto wspomnieć o adresach link local zaczynających się od fe80, <m> pozwalających na nie wymagającą konfiguracji <m> komunikację w ramach jednej sieci fizycznej. <m>'
			'Oraz o adresach multicastowych zastępujących broadcasty <m> <–>[.] <ff0x::1>[ff0x dwukropek dwukropek jeden] adresujący wszystkie hosty w zakresie x <m> i <ff0x::2>[ff0x dwukropek dwukropek dwa] adresującym wszystkie routery w zakresie x, gdzie <m>'
				'x określa zasięg i np. wartość <2>[dwa] oznacza link local, <m> czyli całość danej sieci fizycznej. <m>'
		]
	},
	{
		'console': [
			[0.0, eduMovie.prompt() + "ip -6 r | grep fe80::"],
			[0.5, "\n\r"],
			[0.5, "fe80::/64 dev eth0 proto kernel metric 256 pref medium\n\r"],
			[0.5, "fe80::/64 dev eth1 proto kernel metric 256 pref medium\n\r"],
			[0.51, eduMovie.prompt()],
			
			[1.3, "ping fe80::c240:952:3b0c:6810"],
			[2.1, "\n\r"],
			[2.13, "PING fe80::c240:952:3b0c:6810(fe80::c240:952:3b0c:6810) 56 data bytes\n\r"],
			[4.33, "^C\n\r"],
			[4.38, "--- fe80::c240:952:3b0c:6810 ping statistics ---\n\r3 packets transmitted, 0 received, 100% packet loss, time 50ms\n\r"],
			[4.39, eduMovie.prompt()],
			
			[6.3, "ping fe80::c240:952:3b0c:6810%eth1"],
			[7.1, "\n\r"],
			[7.13, "PING fe80::c240:952:3b0c:6810(fe80::c240:952:3b0c:6810) 56 data bytes\n\r"],
			[7.23, "64 bytes from fe80::c240:952:3b0c:6810%eth1: icmp_seq=1 ttl=64 time=0.337 ms\n\r"],
			[8.23, "64 bytes from fe80::c240:952:3b0c:6810%eth1: icmp_seq=2 ttl=64 time=0.114 ms\n\r"],
			[8.73, "^C\n\r"],
			[8.74, "--- fe80::c240:952:3b0c:6810%eth1 ping statistics ---\n\r2 packets transmitted, 2 received, 0% packet loss, time 24ms\n\rrtt min/avg/max/mdev = 0.114/0.225/0.337/0.112 ms\n\r"],
			[8.75, eduMovie.prompt()],
		],
		'text' : [
			'Jako że sieć <fe80::/64>[fe osiemdziesiąt dwukropek dwukropek slash sześćdziesiąt cztery] będzie dostępna na każdym interfejsie, <m>'
				'to jeżeli mamy ich kilka, to mamy też kilka <m> tras routingowych do sieci link local. <m>'
			'W takim przypadku musimy wskazać jawnie interfejs który ma zostać użyty, <m> typowo możemy to zrobić z użyciem znaku procenta, <m> tak jak pokazano na ekranie. <m>'
		]
	},
]
