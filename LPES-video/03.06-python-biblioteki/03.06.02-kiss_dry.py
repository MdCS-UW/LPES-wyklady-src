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
	{ 'comment': 'kiss dry' },
	{
		'image': [
			[0.0, ""] # TODO jakiś obrazek ?
		],
		'text' : [
			"Mówiąc o tak ogólno-programistycznych tematach, <m> trzeba wspomnieć także o regułach dry i kiss. <m>"
			"Można powiedzieć że są to wręcz główne reguły programistyczne, <m> mają także liczne zastosowania w innych dziedzinach techniki. <m>",
			
			
			"Pierwsza z nich - „Don't Repeat Yourself”, czyli „nie powtarzaj się” <m> zaleca unikanie powtarzania tych samych czynności, <m>"
				"czy też tworzenia takich samych, <m> a nawet analogicznych, podobnych fragmentów kodu. <m>"
			
			"To właśnie ta zasada nakazuje stosowanie pętli, funkcji, bibliotek, <m> zamiast wielokrotnego powtarzania tego samego kodu. <m>"
			"Innymi przejawami jej stosowania są różnego rodzaju systemy i skrypty <m> służące automatyzacji czynności <m> (takich jak np. kompilacja, instalacja, aktualizacja, monitoring, itp.), <m>"
				"czy nawet dziedziczenie w programowaniu obiektowym <m> i mechanizmy pozwalające na wywoływanie <m> innych programów i komunikację z nimi. <m>"
			
			"Unikanie powtórzeń takiego samego lub (co często nawet gorsze) <m> tylko nieznacznie zmienionego kodu <m> jest też szczególnie istotne ze względu na łatwość utrzymania kodu. <m>"
			"Na przykład jakąś poprawkę wprowadza się tylko w odpowiednio <m> sparametryzowanej funkcji, a nie kilkunastu podobnych <m> (ale nie identycznych, ze względu na brak parametryzacji) <m> fragmentach kodu. <m>"
			
			"W zastosowaniach nie programistycznych reguła ta przejawia się często <m> jako wydzielanie modułów i dążenie do ich powtarzalności oraz <m> redukcji liczby ich typów (np. dzięki parametryzacji, czy konfigurowalności). <m>",

			"Drugą, nawet chyba ważniejszą, z tych dwóch reguł jest <m> „Keep It Simple, Stupid!” (niekiedy Keep It Small and Simple), <m> którą można streścić jako „proste jest lepsze”. <m>"
			"Reguła KISS jest bardziej ogólna <m> (można nawet powiedzieć że reguła DRY wynika z reguły KISS), <m> posiada dużo szersze pole zastosowań (także nie technicznych). <m>"
			"Może być uważana za implementację Brzytwy Ockhama w inżynierii. <m>"
			
			"Reguła ta zaleca tworzenie przejrzystych, czytelnych i prostych rozwiązań <m> – zarówno pod względem samego projektu, koncepcji, <m> jak też ich implementacji, wykonania. <m>"
			"W myśl tej reguły jeżeli mamy kilka (równie) skutecznych rozwiązań <m> jakiegoś problemu, to powinniśmy wybrać rozwiązanie najprostsze. <m>"
			"Nakazuje ona także myślenie o łatwości późniejszego utrzymania i serwisu <m> tworzonego rozwiązania – nie ważne czy to programu, urządzenia elektronicznego, <m> czy nawet jakiegoś budynku lub fabryki. <m>"
			
			"W duchu prostoty nakazywanej regułą KISS należy także starać się trzymać <m> powszechnie stosowanych standardów (zawsze gdy tylko jest to możliwe <m> i nie powoduje zbyt wielkiej komplikacji naszego projektu), <m>"
				"zamiast każdorazowo tworzyć nowe, własne standardy, protokoły czy interfejsy. <m>"
		]
	},
]
