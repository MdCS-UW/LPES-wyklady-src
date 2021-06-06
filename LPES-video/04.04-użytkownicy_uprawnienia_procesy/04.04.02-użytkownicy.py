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
	{ 'comment': 'uzytkownicy' },
	{
		'console': [
			[0.0, eduMovie.runCommandString(r"id root")],
			[3.0, eduMovie.runCommandString(r"id")],
			["who", eduMovie.runCommandString(r"w")],
			["who + 2.0", eduMovie.runCommandString(r"who")],
		],
		'text' : [
			'Informacje o użytkowniku możemy sprawdzić przy pomocy komendy <id>[ID]. <m>'
			'Możemy podać nazwę użytkownika, wtedy polecenie to wypiszę informację <m> o podanym użytkowniku, wywołane bez argumentów wypisze <m> informację o naszym aktualnym użytkowniku. <m>'
			'Polecenie wypisze nazwę i identyfikator numeryczny użytkownika, <m> nazwę i identyfikator grupy podstawowej oraz wszystkie grupy dodatkowe. <m>'
			'Z grupami dodatkowymi wiążą się na ogół jakieś <m> uprawnienia przydzielane w systemach linuksowych. <mark name="who" />'
			'Możemy też zobaczyć zalogowanych użytkowników przy pomocy polecenia <w>[wu] lub who. <m>'
			'Natomiast listę ostatnich logowań możemy sprawdzić przy pomocy polecenia last. <m>'
		]
	},
	{
		'console': [
			[0.058184, "o", eduMovie.prompt()],
			[0.535376, "o", "p"],
			[0.69524, "o", "a"],
			[0.911296, "o", "s"],
			[2.07119, "o", "s"],
			[2.263267, "o", "w"],
			[2.489234, "o", "d "],
			[2.991311, "o", "\r\n"],
			[2.999701, "o", "Changing password for rrp.\r\nCurrent password: "],
			[4.399348, "o", "\r\n"],
			[4.414777, "o", "New password: "],
			[6.303244, "o", "\r\n"],
			[6.303655, "o", "Retype new password: "],
			[7.791372, "o", "\r\n"],
			[7.830829, "o", "passwd: password updated successfully\r\n"],
			[7.832251, "o", eduMovie.prompt()],
		],
		'text' : [
			'Zmianę hasła możemy przeprowadzić przy pomocy komendy <passwd>[pass wu de]. <m>'
			'Chyba że korzystamy z jakiś sieciowych baz danych autoryzacyjnych, <m> takich jak na przykład <LDAP>[el-dap], wtedy do tego służą odpowiednie komendy <m> związane z danym systemem takich baz. <m>'
			'Administrator może zmienić hasło dowolnego <m> użytkownika bez podawania jego aktualnego hasła. <m>'
		]
	},
	{
		'console': [
			[0.065742, "o", eduMovie.prompt()],
			[0.887857, "o", "s"],
			[1.11174, "o", "u"],
			[1.391696, "o", " "],
			[1.647783, "o", "t"],
			[1.871727, "o", "e"],
			[2.087693, "o", "s"],
			[2.343601, "o", "t"],
			[2.847775, "o", "\r\n"],
			[2.85712, "o", "Password: "],
			[4.431595, "o", "\r\n"],
			[4.518468, "o", eduMovie.prompt(user="test")],
			[5.983777, "o", "exit\r\n"],
			[5.987159, "o", eduMovie.prompt()],
			
			["sudo + 0.059053", "o", eduMovie.prompt()],
			["sudo + 0.972403", "o", "s"],
			["sudo + 1.164369", "o", "u"],
			["sudo + 1.388349", "o", "d"],
			["sudo + 1.516271", "o", "o"],
			["sudo + 1.828273", "o", " "],
			["sudo + 2.02032", "o", "b"],
			["sudo + 2.116482", "o", "a"],
			["sudo + 2.308275", "o", "s"],
			["sudo + 2.524285", "o", "h"],
			["sudo + 3.604424", "o", "\r\n"],
			["sudo + 3.617265", "o", "[sudo] password for rrp: "],
			["sudo + 6.556349", "o", "\r\n"],
			["sudo + 6.577201", "o", eduMovie.prompt(user="root", prompt="# ")],
			["sudo + 9.012532", "o", "exit\r\n"],
			["sudo + 9.015519", "o", eduMovie.prompt()],
		],
		'text' : [
			'Do przełączenia na innego użytkownika służy polecenie <su>[S U] <m> i wbrew szerokiej opinii nie jest to tylko i wyłącznie przełączanie na <m> administratora, ale przełączanie na dowolnego użytkownika, <m>'
			'którego możemy wskazać w tym poleceniu. <mark name="sudo" />'
			
			'Inną metodą uzyskiwania uprawnień innych użytkowników <m> (w tym administratora) jest komenda <sudo>[su do]. <m>'
			'W odróżnieniu od <su>[S U], które przełącza nas na innego użytkownika <m> w oparciu o znajomość jego hasła, <sudo>[su do] pozwala nam <m> uzyskać uprawnienia, które są nam przydzielone w konfiguracji tego programu, <m>'
			'a do potwierdzenia naszej tożsamości używa naszego hasła. <m>'
			'Sudo może być też skonfigurowane do działania bez pytania o hasło. <m>'
			"Domyślnie zarówno <su>[S U] jaki <sudo>[su do], <m> jeżeli nie powiemy mu o jakiego użytkownika nam chodzi, <m> będzie chciał nas przełączyć na uprawnienia administratora czyli <root'a>[ruta]. <m>"
		]
	},
]
