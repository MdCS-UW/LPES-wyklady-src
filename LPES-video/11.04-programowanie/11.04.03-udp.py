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

code_udp_client = r"""
import socket, select, sys
if len(sys.argv) != 3:
  print("USAGE: " + sys.argv[0] + " dstHost dstPort", file=sys.stderr)
  exit(1)

dstAddrInfo = socket.getaddrinfo(sys.argv[1], sys.argv[2], type=socket.SOCK_DGRAM)
for x in dstAddrInfo:
    try:
        sfd = socket.socket(x[0], socket.SOCK_DGRAM)
        sfd.sendto("Ala ma kota".encode(), x[4])
    except:
        if sfd:
            sfd.close()
        continue
    break

while True:
    rdfd, _, _ = select.select([sfd], [], [], 33.0)
    if sfd in rdfd:
        data, sAddr, = sfd.recvfrom(4096)
        print("odebrano od", sAddr, ":", data.decode());
    else:
        print("Timeout!")
        break
"""

code_udp_server = r"""
import socket, select, sys

if len(sys.argv) != 2:
  print("USAGE: " + sys.argv[0] + " listenPort", file=sys.stderr)
  exit(1)

sfd = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
sfd.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_V6ONLY, 0)

sfd.bind(('::', int(sys.argv[1])))

while True:
    rdfd, _, _ = select.select([sfd], [], [], 33.0)
    if sfd in rdfd:
        data, sAddr, = sfd.recvfrom(4096)
        print("odebrano od", sAddr, ":", data.decode());
    else:
        print("Timeout!")
        break
"""

code_udp_server_fmt = eduMovie.code2console(code_udp_server, "py", limit=24)

clipData += [
	{ 'comment': 'UDP' },
	{
		'console': [
			[0.0, eduMovie.code2console(code_udp_client, "py", limit=24)],
		],
		'text' : [
			'Pisanie serwera zaczniemy jednak od prostszego przypadku jakim jest UDP. <m>'
			'Na ekranie widzimy przykład kodu wysyłającego coś po UDP, <m> można powiedzieć że klienta jakiejś usługi UDP. <m>'
			
			'Jest on dość podobny do klienta TCP, <m> tyle że zamiast tworzenia połączenia wysyłamy od razu dane. <m>'
			'Wysyłanie zrealizowane jest wewnątrz bloku try, tak jak connect w TCP. <m>'
			'Wynika to z tego, iż w przypadku braku dostępu do danego hosta w TCP <m> zawiedzie funkcja connect, a w UDP zawiedzie dopiero wysyłanie <m> – bo nie mamy nawiązywania połączenia i funkcji connect. <m>'
			
			'Później również oczekujemy na jakąś odpowiedź. <m>'
			'Warto jednak zauważyć że funkcja użyta do odebrania odpowiedzi zwraca <m> nie tylko jej treść, jak było to w TCP, ale także adres nadawcy. <m>'
			'Nie mamy tutaj połączenia i odpowiedź może przyjść od kogokolwiek. <m>' # zatem często dobrym zwyczajem byłoby sprawdzenie <m> czy taka odpowiedź przyszła od hosta do którego wysłaliśmy zapytanie. <m>'
			
			'Dodatkowo (w odróżnieniu od poprzedniego programu) tym razem <m> adres i port z którym mamy się połączyć przyjmujemy w linii poleceń, <m>'
			'a gdy nie został podany to wpisujemy odpowiednią, <m> krótką informację na temat użycia tego programu. <m>'
			'Ogólnie polecam w tworzonych programach, które przyjmują jakieś argumenty <m> w linii poleceń umieszczać taki warunek, <m>'
			'ponieważ przydaje się on do łatwego przypomnienia sobie po kilku latach <m> jakie to argumenty miał dostać nasz program, <m> bez czytania całego kodu tego programu. <m>'
		]
	},
	{
		'console': [
			[0.0, "o", "\u001b[?25l\u001b[32m\u001b[8;1H────────────────────────────────────────────────────────────────────────────────\u001b[39m\u001b[16;1H────────────────────────────────────────────────────────────────────────────────\u001b[1;1H\u001b(B\u001b[m" + prompt_txt + "\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\u001b[2B" + prompt_txt + "\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\u001b[2B" + prompt_txt + "\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\u001b[1;" + prompt_len_str + "H\u001b[?12l\u001b[?25h"],
			[0.424809, "o", "nc -lup 4444"],
			[1.180725, "o", "\r\n"],
			[2.069185, "o", "\u001b[?25l\u001b[32m\u001b[6B────────────────────────────────────────────────────────────────────────────────\u001b[16;1H────────────────────────────────────────────────────────────────────────────────\u001b(B\u001b[m\u001b[9;" + prompt_len_str + "H\u001b[?12l\u001b[?25h"],
			[3.552154, "o", "python3 przykład.py 127.0.0.1 4444"],
			[3.956795, "o", "\r\n"],
			[3.989271, "o", "\u001b[2dAla ma kota\u001b[10;1H"],
			[4.973274, "o", "\u001b[?25l\u001b[32m\u001b[2A────────────────────────────────────────────────────────────────────────────────\u001b[39m\u001b[16;1H────────────────────────────────────────────────────────────────────────────────\u001b(B\u001b[m\u001b[2;12H\u001b[?12l\u001b[?25h"],
			[5.727499, "o", "k"],
			[5.897499, "o", "o"],
			[5.97499, "o", "t"],
			[6.072499, "o", "a"],
			[6.2499, "o", " "],
			[6.40299, "o", "a"],
			[6.527499, "o", " "],
			[6.707499, "o", "n"],
			[6.927499, "o", "i"],
			[7.127499, "o", "e"],
			[7.27499, "o", " "],
			[7.427499, "o", "b"],
			[7.567499, "o", "o"],
			[7.727499, "o", "t"],
			[7.847499, "o", "a"],
			[7.97499, "o", "?"],
			[8.160792, "o", "\r\n"],
			[8.161203, "o", "\u001b[7Bodebrano od ('127.0.0.1', 4444) : kota a nie bota?\u001b[3;1H"],
			[9.40528, "o", "\u001b[?25l\u001b[32m\u001b[5B────────────────────────────────────────────────────────────────────────────────\u001b[16;1H────────────────────────────────────────────────────────────────────────────────\u001b(B\u001b[m\u001b[12;1H\u001b[?12l\u001b[?25h"],
			[9.87706, "o", "\u001b[?25l\u001b[4A────────────────────────────────────────────────────────────────────────────────\u001b[32m\u001b[16;1H────────────────────────────────────────────────────────────────────────────────\u001b(B\u001b[m\u001b[17;" + prompt_len_str + "H\u001b[?12l\u001b[?25h"],
			
			["findPort + 0.098743", "o", "netstat -a | grep udp"],
			["findPort + 0.636533", "o", "\r\n"],
			["findPort + 0.666986", "o", "\u001b[31m\u001b[1mudp\u001b(B\u001b[m\u001b[K        0      0 0.0.0.0:bootpc          0.0.0.0:*                          \r\n\u001b[31m\u001b[1mudp\u001b(B\u001b[m\u001b[K        0      0 localhost:4444          localhost:39106         ESTABLISHED\r\n\u001b[31m\u001b[1mudp\u001b(B\u001b[m\u001b[K        0      0 0.0.0.0:39106           0.0.0.0:*                          \r\n"],
			["findPort + 0.670475", "o", prompt_txt],
			
			["send2client + 2.7", "o", "nc -u 127.0.0.1 "],
			["send2client + 2.9", "o", "39106"],
			["send2client + 4.080881", "o", "\r\n"],
			["send2client + 4.17289", "o", "Ala nic nie ma"],
			["send2client + 4.716984", "o", "\r\n"],
			["send2client + 4.717369", "o", "\u001b[11Aodebrano od ('127.0.0.1', 60294) : Ala nic nie ma\u001b[23;1H"],
		],
		'text' : [
			'Widzimy że dane wysłane przez naszego klienta UDP zostały odebrane <m> przez netcata, jak również odpowiedzi od netcata dotarły do naszego programu. <m>'
			'Wspomnieliśmy że w związku z bezpołączeniowością UDP nasz klient może <m> otrzymać odpowiedź z innych adresów niż ten z którym się łączył. <m>'
			'Spróbujmy to sprawdzić. <m>'
			
			'Adres na którym słucha nasz klient można ustalić na kilka sposobów <m> - na przykład podsłuchując wysyłany przez niego pakiet (jest tam adres i port źródłowy) <mark name="findPort" />'
			'lub korzystając z polecenia <netstat>[net stat] potrafiącego wypisać <m> wszystkie otwarte połączenia na danym hoście, procesy je obsługujące i tak dalej. <m>'
			
			'Widzimy że najprawdopodobniej jest to 39106, <mark name="send2client" /> zatem spróbujmy coś wysłać na ten numer portu. <m>'
			'Jak widzimy nasz klient odebrał te dane, zna też adres ich nadawcy, <m> czyli mógłby wysłać odpowiedź. <m>'
			
			'Zasadniczo gdybyśmy nie musieli "na około" ustalać adresu na którym słucha <m> nasz klient to mógłby on pełnić funkcję serwera usługi UDP. <m>'
		]
	},
	{
		'console': [
			[0.0, eduMovie.clear + code_udp_server_fmt],
			["gniazdo", eduMovie.clear + eduMovie.markLines(code_udp_server_fmt, [6], False, "")],
			["gniazdo2", eduMovie.clear + eduMovie.markLines(code_udp_server_fmt, [7], False, "")],
			["gniazdo3", eduMovie.clear + eduMovie.markLines(code_udp_server_fmt, [], False, "")],
			["bind", eduMovie.clear + eduMovie.markLines(code_udp_server_fmt, [9], False, "")],
			["bind2", eduMovie.clear + eduMovie.markLines(code_udp_server_fmt, [], False, "")],
		],
		'text' : [
			'Serwer UDP, którego przykładowy kod widzimy na ekranie, <m> w istocie nie różni się znacząco od klienta. <m>'
			'Tym razem nie mamy adresu z którym się łączymy, zatem sami musimy zdecydować <m> czy używamy IPv4 czy IPv6 do słuchania, tworząc odpowiednie gniazdo. <mark name="gniazdo" />'
			'W widocznym przykładzie tworzymy gniazdo IPv6 <mark name="gniazdo2" /> i wyłączamy na nim opcje ipv6 only, <m> w efekcie czego będzie odbierało również połączenia IPv4.  <mark name="gniazdo3" />'
			
			'Jako że chcemy po prostu słuchać, <m> a nie słuchać w oczekiwaniu na odpowiedź na coś co wysłaliśmy to musimy <m> samodzielnie wskazać adres ip i numer portu na którym słuchamy. <mark name="bind" />'
			'W tym celu wywołujemy funkcję bind, której przekazujemy te dane <m> i rozpoczyna ona odbiór danych na wskazanym adresie i porcie. <m>'
			'Oczywiście pod warunkiem że wskazany port na wskazanym adresie <m> nie jest zajęty przez inny słuchający na nim program <m> oraz że mamy prawo słuchać na danym porcie. <m>'
			'(typowo portów o numerach niższych niż 1024 może używać tylko root). <m>'
			
			'W widocznym przykładzie podajemy adres IP złożony z samych zer, <m> co oznacza że słuchamy na wszystkich adresach hosta, <m> na którym został uruchomiony ten program. <m>'
			'Jawnie wskazujemy też numer portu używanego do odbioru połączeń, <m> gdyż w przypadku serwera chcemy żeby była to dobrze określona wartość, <m> a nie coś co musimy jakoś ustalić po jego uruchomieniu. <mark name="bind2" />'
			
			'Pętla odbierająca wygląda tak samo jak wcześniej w kliencie. <m>'
		]
	},
	{
		'console': [
			[0.0, "o", "\u001b[?25l\u001b[32m\u001b[8;1H────────────────────────────────────────────────────────────────────────────────\u001b[39m\u001b[16;1H────────────────────────────────────────────────────────────────────────────────\u001b[1;1H\u001b(B\u001b[m" + prompt_txt + "\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\u001b[2B" + prompt_txt + "\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\u001b[2B" + prompt_txt + "\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\r\n\u001b[K\u001b[1;" + prompt_len_str + "H\u001b[?12l\u001b[?25h"],
			[0.569514, "o", "python3 przykład.py 4444"],
			[1.586711, "o", "\r\n"],
			[1.990973, "o", "\u001b[?25l\u001b[32m\u001b[6B────────────────────────────────────────────────────────────────────────────────\u001b[16;1H────────────────────────────────────────────────────────────────────────────────\u001b(B\u001b[m\u001b[9;" + prompt_len_str + "H\u001b[?12l\u001b[?25h"],
			[2.355447, "o", "nc -u ::1 4444"],
			[3.138404, "o", "\r\n"],
			[4.522273, "o", "test 1"],
			[5.202252, "o", "\r\n"],
			[5.202648, "o", "\u001b[2dodebrano od ('::1', 34195, 0, 0) : test 1\u001b[11;1H"],
			[6.595093, "o", "\u001b[?25l\u001b[3A────────────────────────────────────────────────────────────────────────────────\u001b[32m\u001b[16;1H────────────────────────────────────────────────────────────────────────────────\u001b(B\u001b[m\u001b[17;" + prompt_len_str + "H\u001b[?12l\u001b[?25h"],
			[7.156072, "o", "nc -u 127.0.0.1 4444"],
			[7.8546406, "o", "\r\n"],
			[9.766638, "o", "test 2"],
			[10.938556, "o", "\r\n"],
			[10.938924, "o", "\u001b[4dodebrano od ('::ffff:127.0.0.1', 56277, 0, 0) : test 2\u001b[19;1H"],
			[11.547179, "o", "\u001b[?25l\u001b[32m\u001b[8d────────────────────────────────────────────────────────────────────────────────\u001b[16;1H────────────────────────────────────────────────────────────────────────────────\u001b(B\u001b[m\u001b[11;1H\u001b[?12l\u001b[?25h"],
			[12.434616, "o", "test 3"],
			[13.490627, "o", "\r\n"],
			[13.490945, "o", "\u001b[1;7r\u001b[7;80H\n\u001b[5;1Hodebrano od ('::1', 34195, 0, 0) : test 3\u001b[1;24r\u001b[12;1H"],
		],
		'text' : [
			'Możemy uruchomić nasz serwer UDP i zobaczyć go w działaniu. <m>'
			'Widzimy że odbiera zarówno połączenia po IPv6, jak i po IPv4. <m>'
			'Poprawnie identyfikuje też klienta od którego otrzymał daną informację, <m> więc mógłby odesłać do niego jakąś odpowiedź. <m>'
			'Warto zwrócić uwagę na zapis adresu IPv4 w mapowaniu do postaci IPv6. <m>'
			'Jest to standardowa notacja, <m> a jej wystąpienie tutaj jest efektem obsługi IPv4 na gnieździe IPv6. <m>'
		]
	},
]
