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

code_getaddrinfo_A = r"""
import socket

x = socket.getaddrinfo("vip.opcode.eu.org", 80)
print(x)
"""

code_getaddrinfo_B = r"""
import socket

x = socket.getaddrinfo("vip.opcode.eu.org", 80, proto=6)
print(x)

x = socket.getaddrinfo("vip.opcode.eu.org", 80, type=socket.SOCK_STREAM)
print(x)
"""

code_getaddrinfo_C = r"""
import socket

x = socket.getaddrinfo("vip.opcode.eu.org", "www")
print(x)
"""

code_getaddrinfo_D = r"""
import socket

adresyInfo = socket.getaddrinfo("vip.opcode.eu.org", "www", type=socket.SOCK_STREAM)
for adres in adresyInfo:
  print(adres[0], "->", adres[4])
"""

clipData += [
	{ 'title': [ "#11.4", "Programowanie", "usług", "sieciowych" ] },
	
	{ 'comment': 'getaddrinfo' },
	{
		'consoleTop': [
			[0.0, ""],
			["getaddrinfo_A", eduMovie.clear + eduMovie.code2console(code_getaddrinfo_A, "py")],
			["getaddrinfo_B", eduMovie.clear + eduMovie.code2console(code_getaddrinfo_B, "py")],
			["getaddrinfo_C", eduMovie.clear + eduMovie.code2console(code_getaddrinfo_C, "py")],
			["getaddrinfo_D", eduMovie.clear + eduMovie.code2console(code_getaddrinfo_D, "py")],
		],
		'consoleDown': [
			[0.0, ""],
			["getaddrinfo_A", eduMovie.runCode(code_getaddrinfo_A, [], cmd="python3")],
			["getaddrinfo_B", eduMovie.runCode(code_getaddrinfo_B, [], cmd="python3")],
			["getaddrinfo_C", eduMovie.runCode(code_getaddrinfo_C, [], cmd="python3")],
			["getaddrinfo_D", eduMovie.runCode(code_getaddrinfo_D, [], cmd="python3")],
		],
		'text' : [
			'Aby całe korzystanie z sieci komputerowych, konfigurowanie adresacji, <m> routingu, filtracji pakietów i tak dalej czemuś służyło, <m>'
			'konieczna jest możliwość skorzystania z komunikacji sieciowej <m> na poziomie jakiegoś działającego programu. <m>'
			'Programowanie aplikacji korzystających z komunikacji sieciowej, <m> czy też fragmentów aplikacji to robiących określa się niekiedy <m> jako programowanie usług sieciowych. <m>'
			
			'W ramach kursu poznaliśmy już kilka języków programowania <m> i większości z nich moglibyśmy użyć do tego celu. <m>'
			'Można napisać serwer pocztowy w postaci skryptu powłoki, <m> używającego netcata i AWK, można też użyć C, C++ lub nawet asemblera. <m>'
			'Natomiast w ramach tych zajęć będziemy to robić w Pythonie, <m> głównie ze względu na to, iż korzystanie z sieci jest w nim <m> bardzo podobne to tego realizowanego w C, <m>'
			'jednak nie musimy się zajmować obsługą błędów, diagnostyką <m> na kolejnych etapach bo robi to za nas Python generując odpowiedni wyjątek. <m>'
			'W tym celu będziemy korzystać z modułu socket, obudowującego <m> stosowne wywołania biblioteki standardowej C. <mark name="getaddrinfo_A" />'
			
			"Pierwszą rzeczą którą warto nauczyć się robić jest korzystanie <m> z zamiany nazw <domenowych>[domen'owych] na adresy IP, <m> opartej o poznane wcześniej mechanizmy (DNS, <resolver>[resolwer], plik hosts, itd.). <m>"
			'Pozwala na to funkcja <getaddrinfo>[get addr info], która także potrafi zamieniać <m> nazwy usług na związane z nimi numery portów. <m>'
			'Przykład użycia widoczny jest na ekranie. <m>'
			
			"Pierwszym argumentem funkcji <getaddrinfo>[get addr info] jest nazwa <domenowa>[domen'owa], <m> drugim argumentem jest nazwa usługi, której chcemy użyć. <m>"
			'Funkcja jest dość uniwersalna i pozwala na podanie zamiast nazw również <m> wartości numerycznych portu, czy też adresu IP w którejś ze standardowych notacji. <m>'
			
			'Funkcja ta zwraca nam listę krotek, czyli listę stałych list. <m>'
			'Każda z tych składowych list reprezentuje możliwy wariant połączenia <m> z wskazanym adresem. <m>'
			'Ma określony protokół warstwy trzeciej (inet dla IPv4, <inet6>[inet 6] dla IPv6), <m> określony typ gniazda i związany z nim protokół warstwy czwartej <m> (<SOCK_DGRAM>[sock de gram] dla UDP, <SOCK_STREAM>[sock stream] dla TCP). <m>'
			'Widoczne w wyniku wartości 17 i 6 to numeryczne identyfikatory protokołów, <m> które zostaną wstawione w polu nagłówka pakietu IP określającym typ kolejnego nagłówka. <mark name="getaddrinfo_B" />'
			
			'Jeżeli interesują nas tylko konkretne protokoły, <m> a na ogół wiemy czy będziemy używać UDP czy TCP, <m> to możemy wyniki tej funkcji zawęzić używając dodatkowych argumentów. <m>'
			'W przykładzie widocznym na ekranie zawęziliśmy je do komunikacji TCP <m> na dwa (w praktyce) równoważne sposoby <m>'
			'– przez określenie typu gniazda, które chcemy użyć <m> lub przez określenie identyfikatora protokołu warstwy transportowej. <mark name="getaddrinfo_C" />'
			
			'Zawężenie takie będzie miało też miejsce w oparciu o dane <m> z pliku </etc/services>[E T C services] jeżeli zamiast numeru portu podamy nazwę usługi. <m>'
			'W przypadku WWW ta usługa standardowo jest świadczona <m> tylko z użyciem TCP, zatem dostaliśmy tylko tego typu gniazda. <mark name="getaddrinfo_D" />'
			
			'W polu numer <4>[cztery] każdej z krotek mamy informację o adresie IP <m> i numerze portu, które możemy wykorzystać do nawiązania połączenia. <m>'
		]
	},
]
