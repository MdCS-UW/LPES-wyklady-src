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
	{ 'section': 'konfiguracja DNS' },
	{
		'console': [
			[0.0, eduMovie.clear + eduMovie.prompt()],
			[0.5, "cat /etc/resolv.conf"],
			[1.3, "\n\rsearch ciekawi.icm.edu.pl icm.edu.pl\n\rnameserver 2001:6a0:0:2000::18\n\rnameserver 193.219.28.52\n\r" + eduMovie.prompt()],
		],
		'text' : [
			'Konfiguracja DNS nie odbywa się przy pomocy komend, <m> a przy pomocy pliku konfiguracyjnego. <m>'
			"Wynika to po części z faktu, że za zamianę nazw <domenowych>[domen'owych] na numery IP <m> odpowiadają funkcje biblioteki standardowej C, a nie jądra systemu operacyjnego. <m>"
			'Biblioteka ta wykorzystuje do tego plik resolv.conf z katalogu <etc>[E Te Ce]. <m>'
			
			'Jak widzimy może on zawierać kilka wpisów nameserver <m> po których następuje numer IP serwera rozwiązującego nazwy. <m>'
			'Obecnie używane są maksymalnie trzy pierwsze wpisy tego typu. <m>'
			'Jeżeli serwer z pierwszego wpisu jest z jakiegoś powodu niedostępny, <m> to biblioteka odpytuje kolejny z podanych serwerów. <m>'
		]
	},
	{
		'image': [
			[0.0, eduMovie.convertFile('dns_search.svg', negate=True)],
			#["domainsearch2", ""],
		],
		'text' : [
			'W pliku tym możemy też mieć wpisy domain i search <m>'
			'Określają one domyślnie używane domeny wyższych poziomów. <m>'
			'Pozwalając nam na łatwe posługiwanie się skróconymi <m> nazwami hostów należących do naszych domen. <m>'
			'Czyli mając we wpisie search podaną domenę <icm.edu.pl>[ICM edu PL] <m> i pisząc ping ciekawi, zostanie wygenerowane zapytanie o <ciekawi.icm.edu.pl.>[ciekawi kropka ICM kropka edu kropka PL kropka], <m>'
				'a dopiero gdyby się okazało że takiej domeny nie ma <m> to o ciekawi kropka do root serwera DNS. <m>'
			
			'Kolejność generacji zapytań zależy od liczby kropek w krótkiej postaci, <m> domyślnie jeżeli wystąpi tam nawet jedna kropka <m>'
			'to resolver najpierw odpytywany jest o pełną nazwę w postaci jaką podaliśmy, <m> a dopiero gdy takiej nie było to o nazwę z dodaną domeną lokalną. <m>'
			'Zachowanie to można zmienić opcją <ndots>[en dots]. <mark name="domainsearch2" />'
			
			'Wpis search określa listę maksymalnie <6>[sześciu] domen, <m> które będą użyte kolejno do takiego doklejania i zasłania wpis domain. <m>'
			
			'Wpis domain określa domyślną domenę lokalną, <m> która jest użyta w tym celu gdy nie ma wpisu search. <m>'
			'W przypadku braku wpisu domain, domena lokalna będzie ustawiona <m> w oparciu o nazwę hosta lokalnego (jeżeli ta zawiera domenę). <m>'
			'Jeżeli chcemy wyłączyć używanie domeny lokalnej <m> i zawsze odpytywać od razu o podaną nazwę <m> to można to zrobić wpisując domain kropka do resolv.conf. <m>'
			
			'W ramach tego pliku mogą wystąpić również inne wpisy konfiguracyjne <m> – szczegóły w odpowiedniej stronie manuala systemowego. <m>'
		]
	},
	{
		'console': [
			[0.0, eduMovie.prompt()],
			[0.5, "cat /etc/hosts"],
			[1.3, "\n\r 127.0.0.1       localhost\n\r ::1             localhost ip6-localhost ip6-loopback\n\r ff02::1         ip6-allnodes\n\r ff02::2         ip6-allrouters\n\r" + eduMovie.prompt()],
		],
		'text' : [
			'Innym plikiem związanym z zamianą nazw na numery IP <m> oraz numerów IP na nazwy jest plik </etc/hosts>[E Te Ce hosts]. <m>'
			'Jest on prostą mapą adres IP i związana z nim nazwa, <m> bądź związane z nim nazwy i stanowi używanego do dziś poprzednika systemu DNS. <m>'
			
			'Wpisy zawarte w tym pliku mają wyższy priorytet od wpisów w DNS, <m> czyli biblioteka najpierw próbuje ustalić adres IP (lub nazwę) <m> w oparciu o zawartość tego pliku, <m>'
			'a dopiero później dokonuje odpytywania DNS <m> w oparciu o konfigurację w resolv conf. <m>'
			'Pozwala to na nadpisywanie globalnego DNS swoimi lokalnymi zmianami, <m> co jest użyteczne na przykład jeżeli testujemy jakąś stronę WWW, <m>'
			'która jest ustawiona pod docelowym adresem, ale nie został jeszcze <m> zmieniony DNS ponieważ nadal to jest wersja testowa. <m>'
		]
	},
]
