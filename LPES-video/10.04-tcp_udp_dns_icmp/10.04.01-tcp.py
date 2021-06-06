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
	{ 'title': [ "#10.4", "TCP, UDP,", "ICMP i DNS", "" ] },
	
	{ 'comment': 'TCP UDP' },
	{
		'image': [
			[0.0, eduMovie.convertFile("udp_tcp.tex", dpi=165, margins=8)],
		],
		'text' : [
			'Przy omawianiu warstwowej struktury protokołów sieciowych <m> wspomnieliśmy o dwóch protokołach warstwy transportowej – TCP i UDP. <m>'
			'Na ekranie zobaczyć można strukturę nagłówka tych protokołów. <m>'
			'Tak jak pokazano są one umieszczane w polu danych pakietu IP, <m> a informacja o tym że taki nagłówek został tam umieszczony <m> znajduje się w polu Protocol / Next header pakietu IP. <m>'
			
			'W nagłówkach obu tych protokołów znajdują się <m> <16>[szesnasto] bitowe numery portów - źródłowego i docelowego. <m>'
			'Numer portu docelowego pozwala systemowi operacyjnemu zidentyfikować <m> proces do którego ma zostać dostarczony ten pakiet. <m>'
			'Numer portu źródłowego służy do przesłania ewentualnej odpowiedzi <m> i pozwala na taką identyfikację procesu <m> systemowi operacyjnemu "po drugiej stronie łącza". <m>'
			'Opiera się to na tym, iż program chcąc przyjmować połączenia sieciowe <m> prosi o przydzielenie na ogół jakiegoś konkretnego numeru portu, <m>'
				'a chcąc nawiązać takie połączenie też otrzymuje numer portu <m> na który zostanie przesłana odpowiedź i w oparciu o to <m> system operacyjny wie do kogo ma dostarczać odbierane dane. <m>'
			
			'Oba nagłówki posiadają też sumę kontrolną obejmującą zarówno dane, <m> nagłówek tego protokołu, jak też wybrane pola z nagłówka pakietu IP. <m>'
			'Dla przypomnienia nagłówek IPv4 zawierał sumę kontrolną obejmującą <m> tylko ten nagłówek bez danych, a IPv6 nie zawierał jej wcale. <m>'
			
			'Nagłówek UDP zawiera jeszcze informację o długości, jednak jako że <m> jest zawarta także w nagłówku samego IP to jest ona raczej nadmiarowa. <m>'
			
			'Nagłówek TCP zawiera znacznie więcej dodatkowych pól związanych głównie <m> z tworzeniem połączenia i kontrolą poprawności odbioru informacji. <m>'
			'Jednak nie będziemy ich tutaj omawiać. <m>'
			'Należy natomiast wspomnieć, że celem zapewnienia kontroli przesyłu danych <m> protokół TCP nawiązuje połączenie, <m>'
				'czyli występują w nim fazy nawiązywania połączenia, jego trwania, <m> podczas którego oczekiwane jest potwierdzanie odbioru kolejnych <m> porcji danych (inaczej będą wysyłane ponownie) oraz zamykania połączenia. <m>'
			
			'Innym protokołem warstwy czwartej jest SCTP dedykowany dla strumieni <m> medialnych czasu rzeczywistego, jednak jest on dość rzadko spotykany. <m>'
		]
	},
	{
		'image': [
			[0.0, ""],
		],
		'text' : [
			'W oparciu o stos TCP/IP działa wiele protokołów warstw wyższych, <m> odpowiedzialnych za realizację usług z których na co dzień korzystamy. <m>'
			'Zanim jednak pomówimy o nich należy poświęcić trochę uwagi protokołom <m> działającym trochę z boku w stosunku co do tych protokołów użytkowych, <m>'
				'jednak bardzo istotnym z punktu widzenia działania sieci <m> oraz związanymi z nimi narzędziami diagnostycznymi. <m>'
        ]
    },
]
