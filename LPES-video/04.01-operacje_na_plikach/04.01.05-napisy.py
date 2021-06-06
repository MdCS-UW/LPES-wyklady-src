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
	{ 'comment': 'napisy' },
	{
		'console': [
			[0.0, eduMovie.runCommandString(r"echo 'Ala ma kota' | sed -e 's#kota#psa#g'")],
			["grep", eduMovie.runCommandString(r"echo 'Ala ma bota' | grep bot >/dev/null && echo 'pasuje'")],
			["wc", eduMovie.runCommandString(r"echo 'aąbc ćd' | wc -m")],
			["wc + 0.5", eduMovie.runCommandString(r"echo 'aąbc ćd' | wc -c")],
			["wc + 1.0", eduMovie.runCommandString(r"echo 'aąbc ćd' | wc -w")],
			["wc + 1.0", eduMovie.runCommandString(r"wc -l /etc/passwd")],
		],
		'text' : [
			'Manipulując różnymi komendami takimi jak grep, cut, sed <m> możemy operować nie tylko na zawartości plików, <m> ale też na napisach, gdyż możemy na przykład <m>'
			"wypisać jakiś napis przy pomocy echo, <m> przekazać go strumieniem do sed'a i uzyskać napis zmodyfikowany." + '<mark name="grep" />'
			
			'Podobnie wysyłając ciąg do polecenia grep i sprawdzając kod <m> powrotu można sprawdzić czy napis ten pasuje do wyrażenia regularnego. <m>'
			'Mamy zatem podstawowe narzędzia do modyfikacji <m> i wykonywania innych operacji na napisach. <mark name="wc" />'
			
			'W przypadku zarówno plików jak i napisów przydatna może być także <m> komenda <wc>[Wu Ce], która umożliwia nam liczenie liter (za pomocą opcji <-m>[minus M]), bajtów (opcja <-c>[minus C])'
			', słów (opcja <-w>[minus W]) oraz linii (<-l>[minus L]). <m>'
			'Warto zauważyć różnicę pomiędzy liczeniem bajtów a znaków, <m> która objawia się dla znaków z poza podstawowego zakresu ASCII. <m>'
			'W tym wypadku bajtów mamy o 2 więcej, <m> bo użyliśmy dwóch polskich znaków które w utf-8 są kodowane dwubajtowo. <m>'
		]
	},
	{
		'console': [
			[0.0, eduMovie.runCommandString(r"basename /etc/network/firewall.sh")],
			[2.0, eduMovie.runCommandString(r"basename /etc/network/firewall.sh .sh")],
			["dirname", eduMovie.runCommandString(r"dirname /etc/network/firewall.sh")],
		],
		'text' : [
			'Mamy również polecenia związane z przetwarzaniem ścieżek. <m>'
			'basename wypisuje nazwę pliku czyli ostatni element ścieżki, <m> może być także użyty do usunięcia wskazanego rozszerzenia. <mark name="dirname" />'
			'dirname wypisuje nazwę katalogu, <m> czyli wszystko co nie jest ostatnim elementem ścieżki. <m>'
			
			'Należy pamiętać że komendy te działają w oparciu o przetwarzanie napisów, <m> czyli ich nie interesuje czy dana ścieżka istnieje <m> i czy w rzeczywistości wskazuje katalog czy zwykły plik. <m>'
			'Polecenia te przetwarzają napisy, a nie ścieżki jako obiekty w systemie plików. <m>'
		]
	},
]
