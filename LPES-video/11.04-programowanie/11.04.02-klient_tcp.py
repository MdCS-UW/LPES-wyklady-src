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


code_tcp_client = r"""
import socket, select, sys

# struktura zawierająca adres na który wysyłamy
dstAI = socket.getaddrinfo("ciekawi.icm.edu.pl", "www")

# mogliśmy uzyskać kilka adresów, więc próbujemy używać kolejnych do skutku
for aiIter in dstAI:
	try:
		print("try connect to:", aiIter[4])
		# utworzenie gniazda sieciowego ... SOCK_STREAM oznacza TCP
		sfd = socket.socket(aiIter[0], socket.SOCK_STREAM)
		# połączenie ze wskazanym adresem
		sfd.connect(aiIter[4])
	except:
		# jeżeli się nie udało ... zamykamy gniazdo
		if sfd:
			sfd.close()
		sfd = None
		# i próbujemy następny adres
		continue
	break;

if sfd == None:
	print("Can't connect", file=sys.stderr)
	exit(1);

# wysyłanie
sfd.sendall("HEAD / HTTP/1.1\r\nHost: ciekawi.icm.edu.pl\r\n\r\n".encode())

# czekanie na odbiór i odbiór
while True:
	rdfd, _, _ = select.select([sfd], [], [], 2.0)
	if sfd in rdfd:
		d = sfd.recv(4096)
		d = d.decode()
		print(d, end="")
		
		# odbiór pustego pakietu kończy działanie
		if d == "":
			break
	else:
		# timeout kończy działanie
		break

# zamykanie połączenia
sfd.shutdown(socket.SHUT_RDWR)
sfd.close()
"""

clipData += [
	{ 'comment': 'klient TCP' },
	{
		'console': [
			[0.0, eduMovie.code2console(code_tcp_client, "py", first=1,  last=24, limit=24)],
			*[  ["connect2 + " + str(i),      eduMovie.clear + eduMovie.code2console(code_tcp_client, "py", first=1+i,  last=24+i, limit=24)] for i in range(1,3)  ],
			*[  ["sendrecv + " + str(i*.7-4), eduMovie.clear + eduMovie.code2console(code_tcp_client, "py", first=1+i,  last=24+i, limit=24)] for i in range(3,27)  ],
		],
		'text' : [
			'Po uzyskaniu informacji o adresach z użyciem funkcji <getaddrinfo>[get addr info], <m> możemy użyć tych informacji do nawiązania połączenia z <m> usługą, bądź hostem, określonym w argumentach tej funkcji. <m>'
			'W tym celu najpierw należy utworzyć gniazdo sieciowe odpowiedniego typu, <m> czyli <DGRAM>[de gram] dla UDP lub STREAM dla TCP i odpowiedniej wersji IP. <m>'
			'Po jego utworzeniu możemy użyć go do nawiązania połączenia <m> z adresem uzyskanym z funkcji <getaddrinfo>[get addr info]. <m>'
			
			'Możemy zrobić to tak jak pokazano w widocznym przykładzie, <m> czyli w pętli po wynikach zwróconych przez tą funkcję. <m>'
			'Zaletą takiego rozwiązania jest możliwość skorzystania z stosowanej <m> niekiedy metody zapewnienia wysokiej dostępności usług sieciowych <m>'
			'''polegającej na podaniu kilku różnych adresów IP dla danej nazwy <domenowej>[domen'owej]. <mark name="connect2" />'''
			
			'Wykorzystujemy tutaj przechwytywanie wyjątków <m> które mogą być rzucone przez te funkcje <m>'
			'i w przypadku niepowodzenia danej próby przechodzimy do kolejnej, <m> używającej kolejnego elementu z listy zwróconej przez <getaddrinfo>[get addr info]. <m>'
			'W przypadku powodzenia pętla zostanie przerwana instrukcją break. <m>'
			
			'Po pętli musimy sprawdzić, czy udało nam się nawiązać <m> połączenie z wskazanym adresem. <mark name="sendrecv" />'
			'Jeżeli nie to kończymy działanie naszego programu. <m>'
			
			'Jeżeli tak to wysyłamy do niego żądanie HTTP i oczekujemy na odpowiedź. <m>'
			'Do oczekiwania używamy poznanej już funkcji select, <m> której tym razem zamiast pliku, czy standardowego wejścia, <m> przekazujemy nasze gniazdo sieciowe, <m> które także jest obiektem typu plikowego. <m>'
			
			'Jeżeli select zakończył się z powodu odebrania danych <m> to je wypisujemy i oczekujemy na kolejne, <m>'
			'jeżeli zakończył się z innych powodów to kończymy pracę <m> uprzednio zamykając połączenie sieciowe. <m>'
			
			'Oczywiście napisy wysyłane muszą zostać skonwertowane <m> na ciąg bajtowy metodą encode, a odbierane ciągi bajtowe <m> zdekodowane do postaci napisu metodą decode, <m>'
			'co omawialiśmy przy przetwarzaniu napisów w pythonie. <m>'
		]
	},
	{
		'console': [
			[0.0, eduMovie.runCode(code_tcp_client, [], cmd="python3")],
		],
		'text' : [
			'Po uruchomieniu naszego przykładu widzimy że serwer odpowiedział <m> na nasze żądanie przesłania nagłówka kodem 200 OK i żądanym nagłówkiem. <m>'
			
			'Stworzyliśmy w ten sposób szkielet programu będącego klientem HTTP <m> i umożliwiającego pobranie jakiś danych z serwera HTTP. <m>'
			'Oczywiście jeżeli chcielibyśmy realnie używać takiego kodu, <m> to nie powinniśmy opierać zakończenia działania na tym, <m> że przez jakiś czas nie otrzymujemy danych od serwera, <m> tak jak w pokazanym przykładzie. <m>'
			'Zamiast tego powinniśmy analizować otrzymane dane <m> i kończyć połączenie, czekać dalej lub wysyłać kolejne żądanie, <m> w zależności od tego czy dostaliśmy to co chcemy, czy nie. <m>'
			
			'Oczywiście jeżeli w Pythonie potrzebujemy użyć HTTP do pobierania <m> jakiś danych, możemy to zrobić prościej z wykorzystaniem odpowiedniej <m> biblioteki niż samemu zaimplementować cały protokół. <m>'
			'Natomiast jeżeli chcemy stworzyć jakiś własny protokół, <m> to na ogół gotowej biblioteki nie będzie i warto umieć <m> napisać klienta i serwer, tak aby mogły się ze sobą komunikować. <m>'
		]
	},
]
