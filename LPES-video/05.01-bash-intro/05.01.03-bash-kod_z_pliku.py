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
	{ 'section': 'uruchamianie \n kodu z pliku' },
	{
		'console': [
			[0.0, eduMovie.clear + eduMovie.runCommandString(r"""echo 'a="ABC DEF !"' > /tmp/abc.sh""")],
			[0.6, eduMovie.runCommandString(r"""echo 'echo Hello $a' >> /tmp/abc.sh""")],
			["1.7", eduMovie.runCommandString(r"bash /tmp/abc.sh")],
			
			["exec",       eduMovie.runCommandString(r"""echo '#!/bin/bash' > /tmp/abc.sh""")],
			["exec + 0.6", eduMovie.runCommandString(r"""echo 'a="ABC DEF !"' >> /tmp/abc.sh""")],
			["exec + 1.3", eduMovie.runCommandString(r"""echo 'echo Hello $a' >> /tmp/abc.sh""")],
			["exec + 1.9", eduMovie.runCommandString(r"""chmod +x /tmp/abc.sh""")],
			["exec + 2.7", eduMovie.runCommandString(r"""/tmp/abc.sh""")],
			
			["echoa", eduMovie.runCommandString(r"echo $a")],
			["kropka", eduMovie.runCommandString(r". /tmp/abc.sh; echo $a")],
			["kropka2", eduMovie.runCommandString(r"a=15; . /tmp/abc.sh; echo $a")],
		],
		'text' : [
			'Podobnie jak w przypadku Pythona, czy wielu innych języków skryptowych <m> (na przykład poznanego już AWK), kod możemy pisać w pliku. <m>'
			'Pliki klasycznie mają rozszerzenie <.sh>[SH], ale nie jest ono wymagane. <m>'
			'Plik możemy uruchamiać wywołując polecenie bash do którego <m> przekazujemy jako argument ścieżkę do pliku. <mark name="exec" />'
			
			'Możemy też dopisać komentarz sterujący określający interpreter, <m> nadać plikowi prawo wykonywalności i uruchamiać jak inne programy. <mark name="echoa" />'
			
			'Jak widzimy żadna z tych metod uruchomienia kodu z pliku nie zapewnia <m> nam dostępu do definiowanych w nim zmiennych po zakończeniu wykonania. <m>'
			'Dzieje się tak dlatego iż są one uruchamiane <m> w nowej instancji basha a nie w bieżącej. <mark name="kropka" />'
			
			'Jeżeli chcemy wykonać kod z pliku w ramach bieżącej instancji <m> basha możemy to zrobić pisząc kropka spacja ścieżka do pliku. <m>'
			'Plik w tym wypadku może, ale nie musi mieć prawa wykonywalności. <mark name="kropka2" />'
			
			'Kropka jest poleceniem wbudowanym powodującym <m> wykonanie komend z wskazanego pliku w aktualnej powłoce. <m>'
			'W szczególności jeżeli plik ustawia jakieś zmienne <m> to będą one dostępne po jego przeczytaniu. <m>'
			
			'Kropka działa podobnie jak pythonowy exec od przeczytanego pliku, <m> o którym mówiliśmy jakiś czas temu. <m>'
			'I używając tej komendy należy zachować podobną ostrożność <m> – nie należy wykonywać w ten sposób danych otrzymanych z zewnątrz <m> lub od innego użytkownika, <m>'
				'gdyż ustawiane są nie tylko wartości zmiennych, <m> a wykonywany jest cały kod z takiego pliku wliczając np. <rm -fr *>[RM minus FR gwiazdka]. <m>'
			'Ponadto kropka ignoruje komentarz sterujący w wczytywanym pliku, <m> traktując go zawsze jak plik bashowy. <m>'
		]
	},
	{
		'console': [
			[0.0, eduMovie.runCommandString(r"echo 'echo XX: $1 $2 $# $@' >> /tmp/abc.sh")],
			[1.0, eduMovie.runCommandString(r"bash /tmp/abc.sh argument")],
			[2.0, eduMovie.runCommandString(r"/tmp/abc.sh argument")],
			[3.0, eduMovie.runCommandString(r"cd /tmp; ./abc.sh aa bb cc")],
		],
		'text' : [
			'Skrypt bashowy uruchamiany z pliku może przyjmować argumenty. <m>'
			'Dostępne są one jako dolar jeden, dolar dwa i tak dalej. <m>'
			'Jeżeli numer jest liczbą kilku cyfrową należy podać go w klamerkach. <m>'
			'Nazwa lub ścieżka do wykonywanego pliku dostępna jest jako dolar zero. <m>'
			'Dolar hash zwraca ilość argumentów, <m> a dolar małpa udostępnia listę wszystkich argumentów. <m>'
			
			'Pisząc kod w pliku możemy rozdzielać polecenia przy pomocy <m> znaku nowej linii, który działa tak jak średnik. <m>'
			'Średnik jest raczej używany w poleceniach jedno linijkowych wpisywanych <m> bezpośrednio w interpreterze, ale oczywiście może też być użyty w pliku. <m>'
			'Pisząc kod w pliku staramy się go formatować tak aby był czytelny, <m> czyli stosować odpowiednio przejścia do nowych linii, wcięcia itd. <m>'
		]
	},

]
