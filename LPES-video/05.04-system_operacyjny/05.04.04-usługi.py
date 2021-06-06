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
	{ 'section': 'standardowe usługi' },
	{
		'console': [
			[0.074497, "o", eduMovie.prompt()],
			["crontab + 0.597377", "o", "crontab -l"],
			["crontab + 1.452345", "o", "\r\n"],
			["crontab + 1.457663", "o", "# Each task to run has to be defined through a single line\r\n# indicating with different fields when the task will be run\r\n# and what command to run for the task\r\n# \r\n# To define the time you can provide concrete values for\r\n# minute (m), hour (h), day of month (dom), month (mon),\r\n# and day of week (dow) or use '*' in these fields (for 'any').\r\n# \r\n# Notice that tasks will be started based on the cron's system\r\n# daemon's notion of time and timezones.\r\n# \r\n# Output of the crontab jobs (including errors) is sent through\r\n"],
			["crontab + 1.458071", "o", "# email to the user the crontab file belongs to (unless redirected).\r\n# \r\n# For example, you can run a backup of all your user accounts\r\n# at 5 a.m every week with:\r\n# 0 5 * * 1 tar -zcf /var/backups/home.tgz /home/\r\n# \r\n# m h  dom mon dow   command\r\n"],
			["crontab + 1.458919", "o", eduMovie.prompt()],
		],
		'text' : [
			'Warto wspomnieć jeszcze o dwóch usługach systemowych <m> – jest to usługa mail związana z wysyłaniem poczty <m> oraz usługa cron związana z planowaniem zadań. <mark name="crontab" />'
			
			"Usługę związaną z planowaniem zadań możemy obsługiwać przy pomocy polecenia crontab, <m> które pozwala nam na definiowanie zadań, które będą uruchamiane cyklicznie w podanym czasie. <m>"
			"Crontab bazuje na plikach złożonych z linii o postaci: <m> minuty, godzina, dzień miesiąca, miesiąc, dzień tygodnia, komenda. <m>"
			"W dowolnym z pól określających czas możemy podać gwiazdkę <m> co oznacza nie testowanie wartości tego pola <m> (czyli np. o każdej godzinie, jeżeli gwiazdka będzie w polu godzin). <m>"
			"Jeżeli napiszemy gwiazdka ukośnik liczba to będzie oznaczało, że polecenie <m> ma być wykonywane, gdy wartość tego pola jest podzielna przez podaną liczbę. <m>"
			"Linie zaczynające się od hasha są komentarzami. <m>"
			
			"Wyjście komendy uruchamianej przez cron'a standardowo wysyłane jest mailem <m> do użytkownika z crontaba którego została ona uruchomiona. <m>"
			"W związku z tym na ogół chcemy żeby takie komendy wypisywały coś tylko w momencie <m> kiedy jest to jakaś krytyczna sytuacja i komenda musi nas o tym poinformować. <m>"
		]
	},
	{
		'console': [
			[2.168224, "o", "echo \"/tmp/alarm.sh\" | at 22:57"],
			[2.820119, "o", "\r\n"],
			[2.82515, "o", "warning: commands will be executed using /bin/sh\r\n"],
			[2.825708, "o", "job 1 at Fri Jan  8 22:57:00 2021\r\n"],
			[2.827106, "o", eduMovie.prompt()],
			
			["mail + 0.643494", "o", "m"],
			["mail + 0.835821", "o", "a"],
			["mail + 0.986779", "o", "i"],
			["mail + 1.211339", "o", "l"],
			["mail + 1.468095", "o", " "],
			["mail + 1.684363", "o", "r"],
			["mail + 1.842649", "o", "r"],
			["mail + 2.003703", "o", "p"],
			["mail + 3.01306", "o", "\r\n"],
			["mail + 3.026869", "o", "Subject: "],
			["mail + 4.091656", "o", "t"],
			["mail + 4.338309", "o", "e"],
			["mail + 4.530665", "o", "s"],
			["mail + 4.850903", "o", "t"],
			["mail + 5.099396", "o", "o"],
			["mail + 5.323003", "o", "w"],
			["mail + 5.61202", "o", "y"],
			["mail + 5.907779", "o", "\r\n"],
			["mail + 6.922823", "o", "t"],
			["mail + 7.267078", "o", "r"],
			["mail + 7.459423", "o", "e"],
			["mail + 7.651762", "o", "s"],
			["mail + 8.09166", "o", "c"],
			["mail + 8.346523", "o", " "],
			["mail + 8.628197", "o", "m"],
			["mail + 8.851826", "o", "a"],
			["mail + 8.979703", "o", "i"],
			["mail + 9.202479", "o", "l"],
			["mail + 9.323934", "o", "a"],
			["mail + 9.739", "o", "\r\n"],
			["mail + 10.003487", "o", " kończymy Control-D"],
			["mail + 10.39889", "o", "\r\n"],
			["mail + 10.731461", "o", "Cc: "],
			["mail + 11.884758", "o", "\r\n"],
			["mail + 11.90682", "o", eduMovie.prompt()],
		],
		'text' : [
			'Drugą komendą oprócz crona umożliwiającą planowanie zadań jest komenda at, <m> która umożliwia jednorazowe zaplanowanie zadania, <m> które zostanie odpalone o określonej w wywołaniu tej komendy porze. <mark name="mail" />'
			
			"Współcześnie na niektórych systemach domyślnie nie będzie aktywna usługa mail, <m> natomiast jeżeli mówimy o serwerach, a nie desktopach <m> to na ogół komenda mail będzie działała i pozwala nam na wysłanie poczty. <m>",
		]
	},
	{ 'section': 'podsumowanie' },
	{
		'console': [
			[0.0, ""]
		],
		'text' : [
			"To tyle w ramach bardzo krótkiego wprowadzenia do systemów operacyjnych. <m> Na studiach na ogół jest to co najmniej semestralny przedmiot. <m>"
			'W związku z tym było dość ogólne i ograniczało się tylko do <m> najważniejszych informacji pomocnych w zrozumieniu "jak to działa". <m>'
			"Osobom zainteresowanym tą tematyką polecam zapoznanie się <m> ze szczegółami, na przykład algorytmami kolejkowania, tematyce blokad w innych źródłach. <m>",
			
			"To chyba też dobry moment aby wspomnieć że Linux nie jest jedynym, <m> ani najstarszym unixowym systemem operacyjnym. <m>"
			"Historia unixów sięga końca lat sześćdziesiątych ubiegłego wieku, <m> a Linuxa jedynie początków lat dziewięćdziesiątych. <m>"
			"Linux nie jest też jedynym tego typu systemem dostępnym na wolnej licencji. <m>"
			"Wśród innych takich systemów na pewno należy wspomnieć o rodzinie systemów BSD, <m> z której pochodzi też część oprogramowania dostarczanego <m> wraz z dystrybucjami Linuxa. <m>"
			"Są to systemy wywodzące się właśnie z tych pierwszych unixów <m> z końca lat sześćdziesiątych. <m>"
			"Cały czas aktywnie rozwijane <m> i dostępne na bardziej liberalnej licencji niż Linux, <m> gdyż nie narzucającej zachowania tych samych warunków licencyjnych. <m>"
			"Wiele rzeczy (w szczególności podstawowe komendy) będzie w nich działać <m> podobnie lub nawet tak samo, jednak też duża część zagadnień związanych z <m> konfiguracją systemu będzie wyglądać odmiennie. <m>"
		]
	},
]
