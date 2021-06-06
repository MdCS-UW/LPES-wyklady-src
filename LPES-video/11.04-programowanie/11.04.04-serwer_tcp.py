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
prompt_len = len( eduMovie.prompt(color=False) ) + 1

code_tcp_server = r"""
import socket, select, signal, sys, os

MAX_CHILD = 3
QUERY_SIZE = 2
TIMEOUT = 63
BUF_SIZE = 4096

if len(sys.argv) != 2:
    print("USAGE: " + sys.argv[0] + " listenPort", file=sys.stderr)
    exit(1);

# obsługa sygnału o zakończeniu potomka
childNum = 0
def onChildEnd(s, f):
    print("odebrano sygnał o śmierci potomka")
    global childNum
    childNum -= 1
    os.waitpid(-1, os.WNOHANG);
signal.signal(signal.SIGCHLD, onChildEnd)

# utworzenie gniazd sieciowych ... SOCK_STREAM oznacza TCP
sfd_v4 = socket.socket(socket.AF_INET,  socket.SOCK_STREAM)
sfd_v6 = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)

# ustawienie opcji gniazda ... IPV6_V6ONLY=1 wyłącza korzystanie
# z tego samego socketu dla IPv4 i IPv6
sfd_v6.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_V6ONLY, 1)

# przypisanie adresów ...
# '0.0.0.0' oznacza dowolny adres IPv4 (czyli to samo co INADDR_ANY)
# '::' oznacza dowolny adres IPv6 (czyli to samo co in6addr_any)
sfd_v4.bind(('0.0.0.0', int(sys.argv[1])))
sfd_v6.bind(('::',      int(sys.argv[1])))

# określenie gniazd jako używanych do odbioru połączeń przychodzących
# (długość kolejki połączeń ustawiona na wartość QUERY_SIZE)
sfd_v4.listen(QUERY_SIZE)
sfd_v6.listen(QUERY_SIZE)

# czekanie na połączenia z użyciem select() w nieskończonej pętli
while True:
    sfd, _, _ = select.select([sfd_v4, sfd_v6], [], [])
    for fd in sfd:
        #  odebranie połączenia
        sfd_c, sAddr = fd.accept()
        
        # weryfikacja ilości potomków
        if childNum >= MAX_CHILD:
            print("za dużo potomków - odrzucam połączenie od:", sAddr);
            sfd_c.send("Internal Server Error\r\n".encode())
            sfd_c.close()
            continue
        
        # aby móc obsługiwać wiele połączeń rozgałęziamy proces
        pid = os.fork()
        if pid > 0:
            # rodzic - zwiększamy licznik potomków
            childNum += 1
        else:
            # potomek - obsługa danego połączenia
            print("połączenie od:", sAddr)
            while True:
                # czekanie na dane z timeout'em
                # aby zabezpieczyć się przed atakiem DoS
                rd, _, _ = select.select([sfd_c], [], [], TIMEOUT)
                if sfd_c in rd:
                    data = sfd_c.recv(BUF_SIZE)
                    if data:
                        print("odebrano od", sAddr, ":", data.decode());
                        sfd_c.send(data)
                    else:
                        print("koniec połączenia od:", sAddr)
                        break
                else:
                    print("timeout połączenia od:", sAddr)
                    break
            # zamykanie połączenia
            sfd_c.shutdown(socket.SHUT_RDWR)
            sfd_c.close()
            sys.exit()
"""

clipData += [
	{ 'comment': 'TCP serwer' },
	{
		'console': [
			[0.0, eduMovie.clear],
			["tcp",        eduMovie.code2console(code_tcp_server, "py", first=1,  last=23+1,  limit=24)],
			["tcp_socket", eduMovie.code2console(code_tcp_server, "py", first=21, last=23+21, limit=24)],
			["tcp_loop",   eduMovie.code2console(code_tcp_server, "py", first=40, last=23+40, limit=24)],
			["tcp_child",  eduMovie.code2console(code_tcp_server, "py", first=59, last=23+59, limit=24)],
		],
		'text' : [
			'Serwer TCP przypominać będzie trochę serwer UDP, ale jako że TCP <m> jest protokołem połączeniowym, to każdy z klientów po nawiązaniu połączenia <m>'
			'jest obsługiwany na swoim dedykowanym porcie <m> (innym niż port używany do nasłuchiwania nowych połączeń). <m>'
			'Zapewnia to łatwe rozdzielenie ruchu od różnych klientów. <m>'
			'Porządny serwer TCP będzie używał wątków, bądź procesów, <m> do obsługi wielu takich połączeń. <m>'
			'Często w układzie jeden wątek na klienta, w czym pomocna jest też <m> taka obsługa połączeń różnych klientów na różnych portach. <mark name="tcp" />'
			
			'Na ekranie widzimy kod przykładowego serwera TCP. <m>',
			
			'Aby kończące się procesy związane z obsługą poszczególnych klientów <m> nie stawały się procesami zombie, <m> definiujemy na początku obsługę sygnału o śmierci naszego potomka. <m>'
			'Obsługę tę będzie realizować funkcja <onChildEnd>[on czild end], <m> która zostanie wywołana asynchronicznie <m> w stosunku co do normalnego kodu gdy odbierzemy sygnał <SIGCHLD>[sig cze el de]. <m>'
			'Za ustawienie tej funkcji do obsługi tego sygnału odpowiada <m> stosowne wywołanie funkcji signal. <m>'
			'Zasadniczo to nas nie interesuje z jakim kodem powrotu ten potomek umarł, <m> ale odbieramy go żeby zapobiec apokalipsie zombie. <mark name="tcp_socket" />'
			
			'Następnie tworzymy dwa osobne gniazda sieciowe <m> – jedno dla wersji czwartej IP, drugie dla wersji szóstej <m>'
			'i tą samą opcję socketu, którą ostatnio ustawialiśmy na zero <m> (aby gniazdo wersji szóstej obsługiwało także wersję czwartą) <m> ustawiamy na jeden. <m>'
			'Pozwala to na obsługę różnych wersji IP na różnych gniazdach <m> i jedynym powodem dla którego w tym programie robimy to inaczej niż w poprzednim <m> jest chęć pokazania obu możliwości. <m>'
			
			'Oba gniazda bindujemy na adresy zerowe z podanym numerem portu, <m> czyli będziemy słuchać na wskazanym porcie <m> na wszystkich adresach IP naszego hosta. <m>',
			
			'Następnie na obu tych gniazdach uruchamiamy słuchanie z określoną długością <m> kolejki połączeń przychodzących poprzez wywołanie metody listen. <mark name="tcp_loop" />'
			
			'W pętli głównej czekamy na odbiór jakieś danych <m> na utworzonych wcześniej gniazdach z użyciem funkcji select. <m>'
			'Dla każdego gniazda zwróconego przez tą funkcję dokonujemy <m> odebrania takiego połączenia funkcją accept, <m>'
			'która zwraca gniazdo związane z tym połączeniem <m> oraz informację o adresie klienta (w tym numer portu). <m>'
			
			'Następnie sprawdzamy czy nie przekroczyliśmy <m> limitu połączeń związanego z liczbą potomków. <m>'
			'Jeżeli przekroczyliśmy wypisujemy komunikat po stronie serwera <m> przy pomocy print oraz odsyłamy komunikat o błędzie <m> do klienta metodą send i zamykamy to połączenie. <m>'
			'Należy zwrócić uwagę że operujemy na gnieździe zwróconym <m> przez funkcję accept, a nie naszych gniazdach nasłuchowych. <m>',
			
			'Jeśli nie przekraczamy limitu połączeń to tworzymy nowego potomka <m> z użyciem znanej nam już funkcji fork, <m>'
			'po której w procesie rodzica zwiększamy tylko i wyłącznie liczbę potomków, <m> a cała obsługa połączenia będzie odbywała się w procesie potomka. <mark name="tcp_child" />'
			
			'Na początek wypiszemy informacje od kogo jest to połączenie, <m> którą uzyskaliśmy w wyniku funkcji accept. <m>'
			'Następnie w nieskończonej pętli oczekujemy na kolejne porcje danych <m> z użyciem funkcji select, która ma też określoną wartość timeoutu połączenia. <m>'
			
			'Jeżeli są dane do odebrania to odbieramy je metodą <recv>[rec v], <m> która zwraca tylko dane. <m>'
			'W odróżnieniu od odbioru po UDP mamy tutaj już nawiązane połączenie <m> z konkretnym klientem i nasz proces zajmuje się tylko tym połączeniem. <m>'
			'Adres z którego zostały odebrane dane w ramach połączenia TCP nie zmienia się, <m> jest to cały czas adres tego klienta, który zwróciła nam funkcja accept. <m>'
			
			'Jeżeli dostaliśmy niepusty zbiór danych to wypisujemy go <m> i odsyłamy do klienta (wykonując usługę echo). <m>'
			'Jeżeli zbiór danych był pusty to przerywamy pętlę <m> celem zakończenia połączenia, podobnie jeżeli nastąpił timeout. <m>'
			
			'Po wyjściu z pętli dokonujemy prawidłowego zamknięcia połączenia TCP. <m>'
			'Jeżeli tego nie zrobimy to połączenie będzie wisiało <m> do momentu systemowego timeoutu połączenia TCP. <m>'
		]
	},
	{
		'console': [
			[0.0, "o", "\u001b[?25l\u001b[32m\u001b[8;1H────────────────────────────────────────┬───────────────────────────────────────\u001b[39m\u001b[9;41H│\u001b[10;41H│\u001b[11;41H│\u001b[12;41H│\u001b[13;41H│\u001b[14;41H│\u001b[15;41H│\r\n────────────────────────────────────────┼───────────────────────────────────────\u001b[17;41H│\u001b[18;41H│\u001b[19;41H│\u001b[20;41H│\u001b[21;41H│\u001b[22;41H│\u001b[23;41H│\u001b[24;41H│\u001b[H\u001b(B\u001b[m" + prompt_txt + "\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\u001b[9;40H\u001b[1K\r" + prompt_txt + "\u001b[10;40H\u001b[1K\n\u001b[1K\n\u001b[1K\n\u001b[1K\n\u001b[1K\n\u001b[1K\u001b[9;42H" + prompt_txt + "\u001b[K\u001b[10;42H\u001b[K\n\u001b[K\n\u001b[K\n\u001b[K\n\u001b[K\n\u001b[K\u001b[17;40H\u001b[1K\r" + prompt_txt + "\u001b[18;40H\u001b[1K\n\u001b[1K\n\u001b[1K\n\u001b[1K\n\u001b[1K\n\u001b[1K\n\u001b[1K\u001b[17;42H" + prompt_txt + "\u001b[K\u001b[18;42H\u001b[K\n\u001b[K\n\u001b[K\n\u001b[K\n\u001b[K\n\u001b[K\n\u001b[K\u001b[1;" + str( prompt_len ) + "H\u001b[?12l\u001b[?25h\u001b[?69h\u001b[1;24r\u001b[s\u001b[1;" + str( prompt_len ) + "H"],
			[0.416734, "o", "python3 przykład.py 4444"],
			[0.88311, "o", "\r\n"],
			[1.579879, "o", "\u001b[?25l\u001b[32m\u001b[6B────────────────────────────────────────┬\u001b[39m───────────────────────────────────────\u001b[32m\u001b[9;41H│\u001b[10;41H│\u001b[11;41H│\u001b[12;41H│\u001b[13;41H│\u001b[14;41H│\u001b[15;41H│\r\n────────────────────────────────────────┼\u001b[39m───────────────────────────────────────\u001b[17;41H│\u001b[18;41H│\u001b[19;41H│\u001b[20;41H│\u001b[21;41H│\u001b[22;41H│\u001b[23;41H│\u001b[24;41H│\u001b(B\u001b[m\u001b[9;" + str( prompt_len ) + "H\u001b[?12l\u001b[?25h"],
			[2.041724, "o", "nc localhost 4444"],
			[3.491026, "o", "\r\n"],
			[3.498236, "o", "\u001b[2dpołączenie od: ('::1', 46882, 0, 0)\u001b[10;1H"],
			[4.531193, "o", "test 1"],
			[5.082702, "o", "\r\n"],
			[5.083578, "o", "\u001b[3dodebrano od ('::1', 46882, 0, 0) : test 1\u001b[11;1Htest 1\r\n"],
			[6.155915, "o", "\u001b[?25l\u001b[4A────────────────────────────────────────┬───────────────────────────────────────\u001b[9;41H│\u001b[10;41H│\u001b[11;41H│\u001b[12;41H│\u001b[13;41H│\u001b[14;41H│\u001b[15;41H│\u001b[32m\r\n────────────────────────────────────────┼\u001b[39m───────────────────────────────────────\u001b[32m\u001b[17;41H│\u001b[18;41H│\u001b[19;41H│\u001b[20;41H│\u001b[21;41H│\u001b[22;41H│\u001b[23;41H│\u001b[24;41H│\u001b(B\u001b[m\u001b[17;" + str( prompt_len ) + "H\u001b[?12l\u001b[?25h"],
			[6.258314, "o", "nc ::1 4444"],
			[6.739326, "o", "\r\n"],
			[6.747023, "o", "\u001b[5dpołączenie od: ('::1', 46888, 0, 0)\u001b[18;1H"],
			[7.619108, "o", "test 2"],
			[8.490831, "o", "\r\n"],
			[8.491758, "o", "test 2\u001b[1;7r\u001b[7;80H\n\u001b[5;1Hodebrano od ('::1', 46888, 0, 0) : test 2\u001b[1;24r\u001b[20;1H"],
			[9.155864, "o", "\u001b[?25l\u001b[32m\u001b[8d────────────────────────────────────────┬\u001b[39m───────────────────────────────────────\u001b[32m\u001b[9;41H│\u001b[10;41H│\u001b[11;41H│\u001b[12;41H│\u001b[13;41H│\u001b[14;41H│\u001b[15;41H│\r\n────────────────────────────────────────┼\u001b[39m───────────────────────────────────────\u001b[17;41H│\u001b[18;41H│\u001b[19;41H│\u001b[20;41H│\u001b[21;41H│\u001b[22;41H│\u001b[23;41H│\u001b[24;41H│\u001b(B\u001b[m\u001b[12;1H\u001b[?12l\u001b[?25h"],
			[9.827123, "o", "test 3"],
			[10.251314, "o", "\r\n\u001b[1;7r\u001b[2S\u001b[5dodebrano od ('::1', 46882, 0, 0) : test 3\u001b[1;24r\u001b[13;1H"],
			[10.251776, "o", "test 3\r\n"],
			[11.23563, "o", "\u001b[?25l\u001b[6A────────────────────────────────────────\u001b[32m┬───────────────────────────────────────\u001b[9;41H│\u001b[10;41H│\u001b[11;41H│\u001b[12;41H│\u001b[13;41H│\u001b[14;41H│\u001b[15;41H│\u001b[39m\r\n────────────────────────────────────────\u001b[32m┼───────────────────────────────────────\u001b[39m\u001b[17;41H│\u001b[18;41H│\u001b[19;41H│\u001b[20;41H│\u001b[21;41H│\u001b[22;41H│\u001b[23;41H│\u001b[24;41H│\u001b(B\u001b[m\u001b[9;" + str(41 + prompt_len) + "H\u001b[?12l\u001b[?25h"],
			[11.562096, "o", "nc 127.0.0.1 4444"],
			[11.92738, "o", "\u001b[10;42H"],
			[12.934754, "o", "\u001b[7;1Hpołączenie od: ('127.0.0.1', 57552)\u001b[1;24r\u001b[10;42H"],
			[13.427261, "o", "test 4"],
			[13.938877, "o", "\u001b[11;42H"],
			[13.939436, "o", "\u001b[1;7r\u001b[2S\u001b[5dodebrano od ('127.0.0.1', 57552) : test 4\u001b[1;24r\u001b[11;42Htest 4\u001b[12;42H"],
			[14.019905, "o", "\u001b[?25l\u001b[8;1H────────────────────────────────────────┬───────────────────────────────────────\u001b[9;41H│\u001b[10;41H│\u001b[11;41H│\u001b[12;41H│\u001b[13;41H│\u001b[14;41H│\u001b[15;41H│\r\n────────────────────────────────────────\u001b[32m┼───────────────────────────────────────\u001b[17;41H│\u001b[18;41H│\u001b[19;41H│\u001b[20;41H│\u001b[21;41H│\u001b[22;41H│\u001b[23;41H│\u001b[24;41H│\u001b(B\u001b[m\u001b[17;" + str(41 + prompt_len) + "H\u001b[?12l\u001b[?25h"],
			[15.828993, "o", "nc ::1 4444"],
			[16.403424, "o", "\u001b[18;42H"],
			[16.40928, "o", "\u001b[7;1Hza dużo potomków - odrzucam połą\u001b[1;7r\u001b[7;80H\n\u001b[6;33Hczenie od: ('::1', 46892, 0, 0)\u001b[1;24r\u001b[18;42HInternal Server Error\u001b[19;42H"],
			[17.535773, "o", "^C"],
			[17.536109, "o", "\u001b[20;42H"],
			[17.536951, "o", prompt_txt],
			[19.260097, "o", "\u001b[?25l\u001b[8;1H────────────────────────────────────────\u001b[32m┬───────────────────────────────────────\u001b[9;41H│\u001b[10;41H│\u001b[11;41H│\u001b[12;41H│\u001b[13;41H│\u001b[14;41H│\u001b[15;41H│\u001b[39m\r\n────────────────────────────────────────\u001b[32m┼───────────────────────────────────────\u001b[39m\u001b[17;41H│\u001b[18;41H│\u001b[19;41H│\u001b[20;41H│\u001b[21;41H│\u001b[22;41H│\u001b[23;41H│\u001b[24;41H│\u001b(B\u001b[m\u001b[12d\u001b[?12l\u001b[?25h"],
			[20.56343, "o", "^C"],
			[20.564119, "o", "\u001b[7;1Hkoniec połą\u001b[1;7r\u001b[7;80H\n\u001b[6;12Hczenia od: ('127.0.0.1', 57552)\u001b[1;24r\u001b[13;42H"],
			[20.564518, "o", prompt_txt],
			[20.578606, "o", "\u001b[7;1Hodebrano sygnał o ś\u001b[1;7r\u001b[7;80H\n\u001b[6;20Hmierci potomka\u001b[1;24r\u001b[13;" + str(41 + prompt_len) + "H"],
			[21.672878, "o", "nc ::1 4444"],
			[22.171222, "o", "\u001b[14;42H"],
			[22.177877, "o", "\u001b[7;1Hpołą\u001b[1;7r\u001b[7;80H\n\u001b[6;5Hczenie od: ('::1', 46894, 0, 0)\u001b[?25l\u001b[1;24r\u001b[14;42H\u001b[?12l\u001b[?25h"],
			[23.14715, "o", "test 5"],
			[24.12312, "o", "\u001b[15;42H"],
			[24.123724, "o", "\u001b[1;7r\u001b[2S\u001b[5dodebrano od ('::1', 46894, 0, 0) : test 5\u001b[1;24r\u001b[15;42H\u001b[9;15r\u001b[9;15r\u001b[42;80s\u001b[15;80H\n\u001b[14;42Htest 5"],
			[24.124006, "o", "\u001b[1;24r\u001b[1;24r\u001b[s\u001b[15;42H"],
			[25.244087, "o", "\u001b[?25l\u001b[8;1H────────────────────────────────────────┬───────────────────────────────────────\u001b[9;41H│\u001b[10;41H│\u001b[11;41H│\u001b[12;41H│\u001b[13;41H│\u001b[14;41H│\u001b[15;41H│\r\n────────────────────────────────────────\u001b[32m┼───────────────────────────────────────\u001b[17;41H│\u001b[18;41H│\u001b[19;41H│\u001b[20;41H│\u001b[21;41H│\u001b[22;41H│\u001b[23;41H│\u001b[24;41H│\u001b(B\u001b[m\u001b[20;" + str(41 + prompt_len) + "H\u001b[?12l\u001b[?25h"],
			[26.199709, "o", "nc ::1 4444"],
			[26.507221, "o", "\u001b[21;42H"],
			[26.51315, "o", "\u001b[7;1Hza dużo potomków - odrzucam połą\u001b[1;7r\u001b[7;80H\n\u001b[6;33Hczenie od: ('::1', 46896, 0, 0)\u001b[1;24r\u001b[21;42HInternal Server Error\u001b[22;42H"],
			[28.283856, "o", "^C"],
			[28.284452, "o", "\u001b[23;42H"],
			[28.284884, "o", prompt_txt],
		],
		'text' : [
			'Możemy spróbować uruchomić nasz serwer i sprawdzić jego działanie. <m>'
			'Jak widzimy połączenia nawiązywane zarówno w <m> czwartej jak i szóstej wersji IP obsługiwane są prawidłowo. <m>'
			'Każdy z klientów dostaje tylko odpowiedzi które powinny do niego trafić. <m>'
			'Również ograniczenie na ilość potomków działa zgodnie z założeniami <m> - do serwera może być podłączonych maksymalnie <3>[trzech] klientów. <m>'
			'Podłączenie się kolejnego możliwe jest dopiero po zakończeniu któregoś <m> z istniejących połączeń i związanej z tym śmierci danego potomka. <m>'
		]
	},
]
