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

prompt_txt  = eduMovie.prompt(clear=False)
prompt_len_str = str( len( eduMovie.prompt(color=False) ) + 1 )

clipData += [
	{ 'section': 'ICMP' },
	{
		'console': [
			[0.065789, "o", eduMovie.prompt()],
			[0.816091, "o", "p"],
			[1.136099, "o", "i"],
			[1.416121, "o", "n"],
			[1.704, "o", "g"],
			[1.960003, "o", " "],
			[2.176013, "o", "c"],
			[2.368842, "o", "i"],
			[2.56007, "o", "e"],
			[2.904012, "o", "k"],
			[3.096001, "o", "a"],
			[3.319927, "o", "w"],
			[3.512179, "o", "i"],
			[3.824075, "o", "."],
			[4.208022, "o", "i"],
			[4.456127, "o", "c"],
			[4.648026, "o", "m"],
			[4.936057, "o", "."],
			[5.096119, "o", "e"],
			[5.312037, "o", "d"],
			[5.440042, "o", "u"],
			[5.792052, "o", "."],
			[6.040038, "o", "p"],
			[6.264016, "o", "l"],
			[6.70409, "o", "\r\n"],
			[6.720903, "o", "PING www2.icm.edu.pl (213.135.59.55) 56(84) bytes of data.\r\n"],
			[6.86536, "o", "64 bytes from www2.icm.edu.pl (213.135.59.55): icmp_seq=1 ttl=60 time=4.04 ms\r\n"],
			[7.726534, "o", "64 bytes from www2.icm.edu.pl (213.135.59.55): icmp_seq=2 ttl=60 time=4.05 ms\r\n"],
			[8.727749, "o", "64 bytes from www2.icm.edu.pl (213.135.59.55): icmp_seq=3 ttl=60 time=3.99 ms\r\n"],
			[9.729038, "o", "64 bytes from www2.icm.edu.pl (213.135.59.55): icmp_seq=4 ttl=60 time=4.08 ms\r\n"],
			[10.256049, "o", "^C\r\n--- www2.icm.edu.pl ping statistics ---\r\n"],
			[10.256433, "o", "4 packets transmitted, 4 received, 0% packet loss, time 7ms\r\nrtt min/avg/max/mdev = 3.988/4.039/4.081/0.071 ms\r\n"],
			[10.257591, "o", eduMovie.prompt()],
			
			["ping2 + 0.983585", "o", "ping -c3 google.pl"],
			["ping2 + 1.771201", "o", "\r\n"],
			["ping2 + 1.787012", "o", "PING google.pl(fra16s08-in-x03.1e100.net (2a00:1450:4001:817::2003)) 56 data bytes\r\n"],
			["ping2 + 1.835732", "o", "64 bytes from fra16s08-in-x03.1e100.net (2a00:1450:4001:817::2003): icmp_seq=1 ttl=114 time=26.8 ms\r\n"],
			["ping2 + 2.812934", "o", "64 bytes from fra16s08-in-x03.1e100.net (2a00:1450:4001:817::2003): icmp_seq=2 ttl=114 time=24.3 ms\r\n"],
			["ping2 + 3.814275", "o", "64 bytes from fra16s08-in-x03.1e100.net (2a00:1450:4001:817::2003): icmp_seq=3 ttl=114 time=24.1 ms\r\n\r\n--- google.pl ping statistics ---\r\n3 packets transmitted, 3 received, 0% packet loss, time 5ms\r\nrtt min/avg/max/mdev = 24.116/25.061/26.767/1.215 ms\r\n"],
			["ping2 + 3.815487", "o", eduMovie.prompt()],
			
			["ping3", eduMovie.runCommandString(r"ping -c3 -4 -n google.pl")],
		],
		'text' : [
			'Kolejnym takim pomocniczym protokołem będącym trochę z boku jest wspomniany już ICMP. <m>'
			'Jest on podstawą działania poleceń takich jak ping, <m> które pozwalają nam na sprawdzenie czy mamy dostęp do wskazanego hosta. <m>'
			'Polecenie to wysyła do wskazanego hosta pakiet ICMP echo request <m> i odbiera pakiety echo reply. <m>'
			'Służą one właśnie do testowania połączenia, <m> sprawdzania działania zdalnego systemu, itp. <m>'
			"Host możemy określić zarówno nazwą <domenową>[domen'ową], <m> jak też bezpośrednio adresem IP. <m>"
			'Jak widzimy na ekranie ping poinformuje nas o adresie IP i nazwie <m> hosta do którego wysyła żądanie echo (co może być istotne jeżeli podana nazwa rozija się na kilka adresów) <m> oraz o adresach IP i nazwach hostów z których dostał odpowiedzi. <m>'
			'Nazwy hostów pozyskiwane są w oparciu o zapytania odwrotnego DNS. <mark name="ping2" />'
			
			'Uruchomione polecenie ping będzie działało dopóki nie zostanie przerwane <m> np. przy pomocy Control C, chyba że określimy przy pomocy <m> opcji <-c>[minus c] ilość pakietów które ma wysłać. <m>'
			'Jak widzimy jeżeli jest dostępny adres IPv6 i mamy routing IPv6 <m> to ping będzie domyślnie korzystać z tej wersji protokołu. <m>'
			'Wersję możemy wymuszać opcjami <-4>[minus 4] bądź <-6>[minus 6]. <m>'
			'Dotyczy to nowszych systemów <–>[.] na starszych polecenie ping <m> działało tylko dla wersji czwartej IP, <m> a dla wersji szóstej funkcjonowało osobne polecenie <ping6>[ping sześć]. <mark name="ping3" />'
			
			'Z przydatnych opcji polecenia ping warto zwrócić uwagę na opcję <-n>[minus n], <m> która wyłącza zamianę numerów IP na nazwy w oparciu o rev DNS. <m>'
			'Jest to szczególnie pomocne gdy sieć nam nie działa, <m> w związku z czym nie działa nam DNS, <m> a polecenia ping używamy aby ustalić dlaczego nie działa. <m>'
			'Bez tej opcji ping może długo czekać z wypisaniem odpowiedzi <m> (aż nastąpi timeout zapytania DNS), co może prowadzić do wrażenia, <m> że pytany host nie odpowiada na pingi. <m>'
		]
	},
	{
		'console': [
			[0.0, "o", eduMovie.prompt()],
			[0.417027, "o", "traceroute ciekawi.icm.edu.pl"],
			[1.021683, "o", "\r\n"],
			[1.026886, "o", "traceroute to ciekawi.icm.edu.pl (213.135.59.55), 30 hops max, 60 byte packets"],
			[1.027515, "o", "\r\n"],
			[1.0389, "o", " 1  lan.home (192.168.6.1)  0.330 ms"],
			[1.039143, "o", "  0.562 ms  0.739 ms\r\n"],
			[1.040707, "o", " 2  192.0.0.1 (192.0.0.1)  9.771 ms  9.847 ms  9.915 ms\r\n"],
			[1.04143, "o", " 3  195.117.0.225 (195.117.0.225)  9.980 ms  10.047 ms  10.114 ms\r\n"],
			[1.042171, "o", " 4  213.25.12.74 (213.25.12.74)  10.183 ms  10.329 ms  11.883 ms"],
			[1.042524, "o", "\r\n"],
			[1.049679, "o", " 5  213.77.0.194 (213.77.0.194)  12.031 ms  11.928 ms  12.079 ms\r\n"],
			[1.050385, "o", " 6  icm-fw-213-135-52-18.rtr.core.icm.edu.pl (213.135.52.18)  12.143 ms"],
			[1.05069, "o", "  10.030 ms  6.881 ms"],
			[4.047775, "o", "\r\n 7  * * *\r\n 8  * * *"],
			[4.048196, "o", "\r\n 9  * * *\r\n10  *"],
			[4.629688, "o", "^C"],
			[4.630399, "o", "\r\n"],
			[4.630747, "o", eduMovie.prompt()],
			
			["ping_ttl + 0.16293", "o", "ping -c1 -t 7 ciekawi.icm.edu.pl"],
			["ping_ttl + 0.64888", "o", "\r\n"],
			["ping_ttl + 0.71981", "o", "PING www2.icm.edu.pl (213.135.59.55) 56(84) bytes of data.\r\n"],
			["ping_ttl + 0.76565", "o", "64 bytes from www2.icm.edu.pl (213.135.59.55): icmp_seq=1 ttl=60 time=3.58 ms\r\n\r\n--- www2.icm.edu.pl ping statistics ---\r\n1 packets transmitted, 1 received, 0% packet loss, time 0ms\r\nrtt min/avg/max/mdev = 3.578/3.578/3.578/0.000 ms\r\n"],
			["ping_ttl + 0.77318", "o", eduMovie.prompt()],
			
			["traceroute_icmp + 0.072502", "o", "sudo traceroute -I ciekawi.icm.edu.pl"],
			["traceroute_icmp + 0.462566", "o", "\r\n"],
			["traceroute_icmp + 0.476975", "o", "traceroute to ciekawi.icm.edu.pl (213.135.59.55), 30 hops max, 60 byte packets"],
			["traceroute_icmp + 0.477434", "o", "\r\n"],
			["traceroute_icmp + 0.488654", "o", " 1  lan.home (192.168.6.1)  0.391 ms"],
			["traceroute_icmp + 0.488983", "o", "  0.557 ms  0.724 ms\r\n"],
			["traceroute_icmp + 0.489985", "o", " 2  192.0.0.1 (192.0.0.1)  9.056 ms  9.095 ms  9.171 ms\r\n"],
			["traceroute_icmp + 0.490949", "o", " 3  195.117.0.225 (195.117.0.225)  9.248 ms  9.377 ms"],
			["traceroute_icmp + 0.491209", "o", "  9.463 ms\r\n"],
			["traceroute_icmp + 0.491927", "o", " 4  213.25.12.74 (213.25.12.74)  9.621 ms  9.694 ms  9.770 ms\r\n"],
			["traceroute_icmp + 0.493424", "o", " 5  213.77.0.194 (213.77.0.194)  9.526 ms  11.310 ms  11.404 ms\r\n"],
			["traceroute_icmp + 0.49433", "o", " 6  icm-fw-213-135-52-18.rtr.core.icm.edu.pl (213.135.52.18)  11.489 ms"],
			["traceroute_icmp + 0.4946", "o", "  4.190 ms"],
			["traceroute_icmp + 0.503629", "o", "  9.259 ms"],
			["traceroute_icmp + 0.503677", "o", "\r\n"],
			["traceroute_icmp + 0.507783", "o", " 7  www2.icm.edu.pl (213.135.59.55)  9.280 ms"],
			["traceroute_icmp + 0.507937", "o", "  9.357 ms  9.679 ms\r\n"],
			["traceroute_icmp + 0.510512", "o", eduMovie.prompt()],
			
			["mtr + 0.0906", "o", "mtr ciekawi.icm.edu.pl"],
			["mtr + 0.269562", "o", "\r\n"],
			["mtr + 0.385353", "o", "\u001b(B\u001b)0\u001b[?1049h\u001b[1;23r\u001b[m\u000f\u001b[4l\u001b[39;49m\u001b[39;49m\u001b[m\u000f\u001b[H\u001b[J\u001b[1;29H\u001b[0;1m\u000f\u001b[1K My traceroute  [v0.92]\r\n\u001b[m\u000f" + eduMovie.defaultHost + " (192.168.6.3)\u001b[2;56H2021-01-18T16:58:33+0000\r\nKeys:  \u001b[0;1m\u000fH\u001b[m\u000felp   \u001b[0;1m\u000fD\u001b[m\u000fisplay mode   \u001b[0;1m\u000fR\u001b[m\u000festart statistics   \u001b[0;1m\u000fO\u001b[m\u000frder of fields   \u001b[0;1m\u000fq\u001b[m\u000fuit\u001b[4;37H\u001b[0;1m\u000f   Packets               Pings\r\n Host\u001b[5;37H Loss%   Snt   Last   Avg  Best  Wrst StDev\r\u001bM\u001bM\u001b[m\u000f"],
			["mtr + 0.486754", "o", "\n\n\n 1. 192.168.6.1\u001b[6;39H0.0%     1    0.5   0.5   0.5   0.5   0.0\r\n 2. ???\u001b[H\n\n"],
			["mtr + 0.488789", "o", "\n\n\n 1. lan.home   \u001b[H\n\n"],
			["mtr + 0.590055", "o", "\u001b[7;5H192.0.0.1\u001b[7;39H0.0%     1    3.5   3.5   3.5   3.5   0.0\r\n 3. ???\u001b[H\n\n"],
			["mtr + 0.686521", "o", "\u001bM\u001b[74G4\r\n"],
			["mtr + 0.690372", "o", "\u001b[8;5H195.117.0.225\u001b[8;39H0.0%     1    3.4   3.4   3.4   3.4   0.0\r\n 4. ???\u001b[H\n\n"],
			["mtr + 0.790749", "o", "\u001b[9;5H213.25.12.74\u001b[9;39H0.0%     1    3.5   3.5   3.5   3.5   0.0\r\n 5. ???\u001b[H\n\n"],
			["mtr + 0.893817", "o", "\u001b[10;5H213.77.0.194\u001b[10;39H0.0%     1    6.2   6.2   6.2   6.2   0.0\r\n 6. ???\u001b[H\n\n"],
			["mtr + 0.991378", "o", "\u001b[11;5H213.135.52.18\u001b[11;39H0.0%     1    3.3   3.3   3.3   3.3   0.0\r\n 7. ???\u001b[H\n\n"],
			["mtr + 0.993345", "o", "\u001b[11;5Hicm-fw-213-135-52-18.rtr.core.ic\u001b[H\n\n"],
			["mtr + 1.091719", "o", "\u001b[12;5H213.135.59.55\u001b[12;39H0.0%     1    3.3   3.3   3.3   3.3   0.0\u001b[H\n\n"],
			["mtr + 1.093009", "o", "\u001b[12;5Hwww2.icm.edu.pl\u001b[H\n\n"],
			["mtr + 1.315841", "o", "\u001b[6;48H2\u001b[H\n\n"],
			["mtr + 1.441348", "o", "\u001b[7;48H2    1.7   2.6   1.7\u001b[77G1.3\u001b[H\n\n"],
			["mtr + 1.568353", "o", "\u001b[8;48H2\u001b[55G3   3.3   3.3\u001b[79G1\u001b[H\n\n"],
			["mtr + 1.690172", "o", "\u001bM\u001b[74G5\r\n"],
			["mtr + 1.693494", "o", "\u001b[9;48H2    2.9   3.2   2.9\u001b[79G5\u001b[H\n\n"],
			["mtr + 1.819668", "o", "\u001b[10;48H2    3.5   4.9   3.5\u001b[77G1.9\u001b[H\n\n"],
			["mtr + 1.944792", "o", "\u001b[11;48H2\u001b[H\n\n"],
			["mtr + 4.069887", "o", "\u001b[12;48H2\u001b[55G0   3.1   3.0\u001b[79G"],
			["mtr + 4.070154", "o", "2\u001b[H\n\n"],
			["mtr + 4.210804", "o", "\u001b[6;48H3\u001b[55G4\u001b[6;67H4\u001b[79G1\u001b[H\n\n"],
			["mtr + 4.356182", "o", "\u001b[7;48H3    2.6\u001b[77G0.9\u001b[H\n\n"],
			["mtr + 4.500657", "o", "\u001b[8;48H3\u001b[55G8   3.5\u001b[73G8   0.3\u001b[H\n\n"],
			["mtr + 4.644249", "o", "\u001b[9;48H3    4.0   3.5\u001b[9;71H4.0   0.6\u001b[H\n\n"],
			["mtr + 4.783199", "o", "\u001bM\u001b[74G6\r\n"],
			["mtr + 4.786021", "o", "\u001b[10;48H3    2.3   4.0   2.3\u001b[77G2.0\u001b[H\n\n"],
			["mtr + 4.936", "o", "\u001b[11;48H3    9.0   5.2\u001b[11;71H9.0   3.3\u001b[H\n\n"],
			["mtr + 5.073986", "o", "\u001b[12;48H3\u001b[55G7   3.3\u001b[73G7   0.4\u001b[H\n\n"],
			["mtr + 5.149913", "o", "\u001b[23;1H\u001b[?1049l\r\u001b[?1l\u001b>"],
			["mtr + 5.151547", "o", eduMovie.prompt()],
		],
		'text' : [
			'Kolejnymi poleceniami diagnostycznymi używającymi ICMP <m> są polecenia typu tracepath, traceroute i <mtr>[M T R]. <m>'
			'Wszystkie one służą do ustalenia trasy prowadzącej do wskazanego hosta, <m> czyli wypisania listy routerów przez które przechodzi pakiet idący do tego hosta. <m>'
			'Istnieją różne implementacje tych poleceń, <m> różnią się one m.in. przyjmowanymi opcjami. <m>'
			'Większość z nich jednak, podobnie jak ping, <m> przyjmuje opcje <-n>[minus n] wyłączającą odwrotny DNS. <m>'
			'Część z nich także opcje <-4>[minus 4], <-6>[minus 6] wymuszające daną <m> wersję protokołu IP, a niektóre będą miały osobne polecenia dla IPv4 i IPv6, <m> gdzie typowo to drugie ma dodaną cyfrę <6>[sześć] w nazwie polecenia. <m>'
			
			'Polecenie traceroute wysyła pakiety UDP z zwiększaną kolejno <m> wartością TTL, aby zobaczyć od jakich routerów otrzyma komunikat ICMP <m> o przekroczeniu TTL (lub hop limit), <m>'
				'czyli najpierw wysyła z TTL równym jeden, potem dwa i tak dalej. <m>'
			'Brak odpowiedzi sygnalizowany jest gwiazdką. <m>'
			'Jeżeli występuje ona tylko na jednym poziomie, <m> to znaczy że dany router nie wysyła komunikatów ICMP o przekroczeniu TTL. <m>'
			'Natomiast jeżeli od pewnego momentu mamy same gwiazdki, <m> może oznaczać kilka sytuacji. <m>'
			'Być może któryś router po drodze blokuje komunikaty ICMP tego typu <m>'
				'lub dotarliśmy do hosta docelowego, <m> który po cichu zignorował nasz pakiet <m> (nie zwracając żadnego komunikatu ICMP). <mark name="ping_ttl" />'
			
			'Jeżeli host docelowy odpowiada na pingi to możemy ustalić ile routerów <m> mamy do niego, wysyłając do niego pingi z odpowiednim TTL. <m>'
			'Jak widzimy na ekranie ping z TTL o wartosci 7 <m> (pierwszej na której urwał się traceroute) <m> dostał odpowiedź od docelowego hosta, <m>'
				'czyli nasz traceroute pokazał całą ścieżkę, tylko host docelowy <m> ignorował po cichu pakiety których używał traceroute. <mark name="traceroute_icmp" />'
			"Gdybyśmy w traceroute zamiast pakietów UDP używali pakietów ICMP lub TCP, <m> co akurat w wypadku tej wersji tego polecenia wymaga praw <root'a>[ruta], <m>"
				'to w tym wypadku od razu dostalibyśmy poprawną ścieżkę, bez gwiazdek. <mark name="mtr" />'
			'Polecenie <mtr>[M T R] działa podobnie tyle że standardowo korzysta z pakietów ICMP, <m> a wyniki wypisuje na żywo podając także bieżące czasy opóźnień. <m>'
		]
	},
	{  # nc -6 -l -p 4444;   ncat ::1 4444
		'console': [
			[0.495142, "o", "\u001b[H\u001b[2J\u001b]2;screen\u0007" + prompt_txt],
			[0.495142, "o", "\r\u001b[11B\u001b[7m   0 bash                                                                       \r\u001b[12B   1 bash                                                                       \r\u001b[10A"],
			[0.547436, "o", "\u001b[1m\u001b[31m\u001b[0m\u001b[1m\u001b[36m\u001b[0m" + prompt_txt],
			[0.557436, "o", "\u001b[1;" + prompt_len_str + "H"],
			[1.591726, "o", "n"],
			[1.839564, "o", "c"],
			[2.063544, "o", " "],
			[2.383638, "o", "-"],
			[3.17547, "o", "6"],
			[3.391587, "o", " "],
			[3.615535, "o", "-"],
			[3.991445, "o", "l"],
			[4.247508, "o", " "],
			[4.471551, "o", "-"],
			[4.783478, "o", "p"],
			[5.927597, "o", " "],
			[6.271616, "o", "4"],
			[6.463568, "o", "4"],
			[6.903539, "o", "4"],
			[7.031475, "o", "4"],
			[7.855717, "o", "\r\n"],
			[9.639612, "o", "\u001b[13;" + prompt_len_str + "H"],
			[10.19706, "o", "n"],
			[10.343653, "o", "c"],
			[10.631477, "o", "a"],
			[11.015589, "o", "t"],
			[12.199516, "o", " "],
			[13.055877, "o", ":"],
			[13.215882, "o", ":"],
			[13.719756, "o", "1"],
			[14.327824, "o", " "],
			[14.53708, "o", "4"],
			[14.903742, "o", "4"],
			[15.063695, "o", "4"],
			[15.255768, "o", "4"],
			[16.047798, "o", "\r\n"],
			[17.927759, "o", "A"],
			[18.119622, "o", "l"],
			[18.279663, "o", "a"],
			[18.495597, "o", " "],
			[18.687531, "o", "m"],
			[18.815501, "o", "a"],
			[18.943516, "o", " "],
			[19.135589, "o", "b"],
			[19.415552, "o", "o"],
			[19.607614, "o", "t"],
			[19.927568, "o", "a"],
			[20.303815, "o", "\r\n"],
			[20.304191, "o", "\u001b[13AAla ma bota\r\n\u001b[12B"],
			[22.391747, "o", "1"],
			[22.647649, "o", "2"],
			[22.935626, "o", "3"],
			[23.439718, "o", "\r\n"],
			[23.440136, "o", "\u001b[13A123\r\n\u001b[12B"],
			[26.671714, "o", "\u001b[12A"],
			[27.959746, "o", "9"],
			[28.279818, "o", "8"],
			[28.535741, "o", "7"],
			[29.135782, "o", "\r\n"],
			[29.136141, "o", "\u001b[11B987\r\n \u001b[5;1H"],
			[31.015776, "o", "6"],
			[31.303773, "o", "5"],
			[31.58382, "o", "4"],
			[32.167762, "o", " "],
			[32.583822, "o", "."],
			[32.735701, "o", "."],
			[33.879868, "o", "."],
			[34.511833, "o", " "],
			[35.015753, "o", "3"],
			[35.39977, "o", "2"],
			[35.591774, "o", "1"],
			[36.95191, "o", "\r\n"],
			[36.952371, "o", "\u001b[11B654 ... 321\r\n \u001b[6;1H"],
			[38.343834, "o", "\u001b[12B"],
			[38.513507, "o", "\u001b[12A" + prompt_txt + "\r\u001b[12B" + prompt_txt],
		],
		'text' : [
			'Omawiając narzędzia pozwalające na diagnozowanie problemów z siecią <m> trzeba także wspomnieć o narzędziach takich jak netcat i telnet. <m>'
			'Netcat jest programem mogącym pełnić funkcje zarówno <m> klienta TCP, czy UDP jak też serwera. <m>'
			'Czyli może on pełnić zarówno funkcję strony nawiązującej połączenie, <m> jak też oczekującej na nie i je odbierającej, <m> w obu podstawowych protokołach warstwy czwartej. <m>'
			'Możemy z jego pomocą podłączać się <m> do serwerów różnych usług i testować ich działanie. <m>'
			'Możemy też tak jak widać to na ekranie <m> nawiązać połączenie pomiędzy dwoma netcatami. <m>'
			'Występuje on w wielu różnych implementacjach, <m> pod nazwami poleceń takimi jak <nc>[N C], netcat lub <ncat>[en cat]. <m>'
			'W roli klienta TCP często używane jest też polecenie telnet. <m>'
		]
	},
	{  # sudo tcpdump -i any icmp or icmp6 ; ping -4 -c1 google.pl ; ping -6 -c1 google.pl
		'console': [
			[0.495142, "o", "\u001b[H\u001b[2J\u001b]2;screen\u0007" + prompt_txt],
			[0.495142, "o", "\r\u001b[11B\u001b[7m   0 bash                                                                       \r\u001b[12B   1 bash                                                                       \r\u001b[10A"],
			[0.547436, "o", "\u001b[1m\u001b[31m\u001b[0m\u001b[1m\u001b[36m\u001b[0m" + prompt_txt],
			[0.557436, "o", "\u001b[1;" + prompt_len_str + "H"],
			[1.389158, "o", "sudo tcpdump -i any icmp or icmp6"],
			[2.459699, "o", "\r\n"],
			[2.503653, "o", "tcpdump: verbose output suppressed, use -v or -vv for full protocol decode\r\nlistening on any, link-type LINUX_SLL (Linux cooked), capture size 262144 bytes\r\n \b"],
			[3.603582, "o", "\u001b[13;" + prompt_len_str + "H"],
			[5.293443, "o", "ping -4 -c1 google.pl"],
			[6.227771, "o", "\r\n"],
			[6.240199, "o", "PING google.pl (172.217.18.3) 56(84) bytes of data.\r\n \b"],
			[6.246925, "o", "\u001b[H\u001b[K" + prompt_txt + " sudo tcpdump -i any icmp or icmp6\r\n\u001b[Ktcpdump: verbose output suppressed, use -v or -vv for full protocol decode\r\n\u001b[Klistening on any, link-type LINUX_SLL (Linux cooked), capture size 262144 bytes\r\n\u001b[K18:14:37.029133 IP " + eduMovie.defaultHost + " > fra15s28-in-f3.1e100.net: ICMP echo request, id 6119\r\n, seq 1, length 64\r\n\u001b[K\n\u001b[K\n\u001b[K\n\u001b[K\n\u001b[K\n\u001b[K\u001b[4B"],
			[6.264025, "o", "\u001b[H\u001b[K" + prompt_txt + " sudo tcpdump -i any icmp or icmp6\r\n\u001b[Ktcpdump: verbose output suppressed, use -v or -vv for full protocol decode\r\n\u001b[Klistening on any, link-type LINUX_SLL (Linux cooked), capture size 262144 bytes\r\n\u001b[K18:14:37.029133 IP " + eduMovie.defaultHost + " > fra15s28-in-f3.1e100.net: ICMP echo request, id 6119\r\n, seq 1, length 64\r\n\u001b[K18:14:37.052315 IP fra15s28-in-f3.1e100.net > " + eduMovie.defaultHost + ": ICMP echo reply, id 6119, \r\nseq 1, length 64\r\n\u001b[K\n\u001b[K\n\u001b[K\n\u001b[K\u001b[4B"],
			[6.266211, "o", "\u001b[2A\u001b[K" + prompt_txt + " ping -4 -c1 google.pl\r\n\u001b[KPING google.pl (172.217.18.3) 56(84) bytes of data.\r\n\u001b[K64 bytes from fra15s28-in-f3.1e100.net (172.217.18.3): icmp_seq=1 ttl=116 time=2\r\n\u001b[K\u001b[15;80H23.2 ms\r\n\u001b[K\n\u001b[K--- google.pl ping statistics ---\r\n\u001b[K\n\u001b[K\n\u001b[K\n\u001b[K\n\u001b[K\u001b[4A1 packets transmitted, 1 received, 0% packet loss, time 0ms\r\nrtt min/avg/max/mdev = 23.221/23.221/23.221/0.000 ms\r\n \b"],
			[6.267426, "o", prompt_txt],
			[9.560954, "o", "ping -6 -c1 google.pl"],
			[10.347663, "o", "\r\n"],
			[10.361156, "o", "\u001b[9A\u001b[KPING google.pl (172.217.18.3) 56(84) bytes of data.\r\n\u001b[K64 bytes from fra15s28-in-f3.1e100.net (172.217.18.3): icmp_seq=1 ttl=116 time=2\r\n\u001b[K\u001b[14;80H23.2 ms\r\n\u001b[K\n\u001b[K--- google.pl ping statistics ---\r\n\u001b[K1 packets transmitted, 1 received, 0% packet loss, time 0ms\r\n\u001b[Krtt min/avg/max/mdev = 23.221/23.221/23.221/0.000 ms\r\n\u001b[K" + prompt_txt + " ping -6 -c1 google.pl\r\n\u001b[KPING google.pl(fra16s24-in-x03.1e100.net (2a00:1450:4001:824::2003)) 56 data byt\r\n\u001b[K\u001b[21;80Htes\r\n\u001b[K"],
			[10.364009, "o", "\u001b[H\u001b[K" + prompt_txt + " sudo tcpdump -i any icmp or icmp6\r\ntcpdump: verbose output suppressed, use -v or -vv for full protocol decode\r\nlistening on any, link-type LINUX_SLL (Linux cooked), capture size 262144 bytes\r\n18:14:37.029133 IP " + eduMovie.defaultHost + " > fra15s28-in-f3.1e100.net: ICMP echo request, id 6119\r\n, seq 1, length 64\r\n\u001b[K18:14:37.052315 IP fra15s28-in-f3.1e100.net > " + eduMovie.defaultHost + ": ICMP echo reply, id 6119, \r\nseq 1, length 64\r\n18:14:46.149774 IP6 " + eduMovie.defaultHost + " > fra16s24-in-x03.1e100.net: ICMP6, echo request, seq\r\n 1, length 64\r\n\u001b[12B"],
			[10.389204, "o", "\u001b[H\u001b[K" + prompt_txt + " sudo tcpdump -i any icmp or icmp6\r\ntcpdump: verbose output suppressed, use -v or -vv for full protocol decode\r\nlistening on any, link-type LINUX_SLL (Linux cooked), capture size 262144 bytes\r\n18:14:37.029133 IP " + eduMovie.defaultHost + " > fra15s28-in-f3.1e100.net: ICMP echo request, id 6119\r\n, seq 1, length 64\r\n\u001b[K18:14:37.052315 IP fra15s28-in-f3.1e100.net > " + eduMovie.defaultHost + ": ICMP echo reply, id 6119, \r\nseq 1, length 64\r\n18:14:46.149774 IP6 " + eduMovie.defaultHost + " > fra16s24-in-x03.1e100.net: ICMP6, echo request, seq\r\n 1, length 64\r\n18:14:46.177641 IP6 fra16s24-in-x03.1e100.net > " + eduMovie.defaultHost + ": ICMP6, echo reply, seq 1\r\n, length 64\r\n\u001b[12B"],
			[10.390858, "o", "\u001b[10A\u001b[Krtt min/avg/max/mdev = 23.221/23.221/23.221/0.000 ms\r\n\u001b[K" + prompt_txt + " ping -6 -c1 google.pl\r\n\u001b[KPING google.pl(fra16s24-in-x03.1e100.net (2a00:1450:4001:824::2003)) 56 data byt\r\n\u001b[K\u001b[15;80Htes\r\n\u001b[K64 bytes from fra16s24-in-x03.1e100.net (2a00:1450:4001:824::2003): icmp_seq=1 t\r\n\u001b[K\u001b[17;80Httl=113 time=27.9 ms\r\n\u001b[K\n\u001b[K--- google.pl ping statistics ---\r\n\u001b[K1 packets transmitted, 1 received, 0% packet loss, time 0ms\r\n\u001b[Krtt min/avg/max/mdev = 27.893/27.893/27.893/0.000 ms\r\n\u001b[K"],
			[10.391961, "o", prompt_txt],
		],
		'text' : [
			'W diagnozowaniu problemów sieciowych bardzo przydatne jest <m> także podsłuchiwanie komunikacji. <m>'
			'Pozwalają na to programy takie jak <tcpdump>[TCP dump] czy <wireshark>[wire shark]. <m>'
			'Są one wstanie wypisać informację o podsłuchanych pakietach, <m> bądź nawet ich zawartość. <m>'
			'Nasłuch odbywa się na wskazanym interfejsie, <m> istnieje też możliwość filtracji pakietów. <m>'
			
			'W przykładzie pokazanym na ekranie widzimy nasłuch pakietów ICMP <m> związanych z obydwoma wersjami protokołu IP, <m> na wszystkich interfejsach (opcja <-i any>[minus i any]). <m>'
			'Z najważniejszych opcji <tcpdump>[ticipi dump] należy wymienić także <-n>[minus n] <m> wyłączającą zamianę numerów na nazwy, <m> <-v>[minus v] zwiększającą ilość wypisywanych informacji, <m>'
				'czy też <-A>[minus a duże] powodującą wypisanie zawartości pakietu jako tekstu. <m>'
			'Szczegóły znajdują się w stosownej dokumentacji man. <m>'
			
			'Wireshark jest podobnym programem, tyle że korzystającym <m> z graficznego interfejsu użytkownika i wspierającym także <m> dekodowanie dużej ilości protokołów warstw wyższych. <m>'
		]
	},
]
