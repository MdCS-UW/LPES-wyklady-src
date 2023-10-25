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

code_exec_A = r"""
import os

os.execv("/bin/ls", ["ls", "-l"])

print("to się nigdy nie wypisze")
"""

code_exec_B = r"""
exec("a=231")
print(a)
"""

code_os_system_A = r"""
import os

os.system("ls -l")
"""

code_os_system_B = r"""
import os

xx="Ala \n ma kota"
os.system("echo '" + xx + "' | grep -v A")
"""

code_subprocess_A = r"""
import subprocess

xx = "Ala \n ma kota"

res = subprocess.run(["grep", "-v", "A"], input=xx.encode(), stdout=subprocess.PIPE)

print("Kod powrotu to: " + str(res.returncode))
print("Standardowe wyjście z komendy to: " + res.stdout.decode())
"""

try: clipData
except NameError: clipData = []

clipData += [
	{ 'comment': 'exec' },
	{ #  
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_exec_A, "py")],
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(code_exec_A, [], cmd="python3")],
		],
		'text' : [
			'Nie zawsze chcemy po rozgałęzieniu procesu kontynuować <m> w dwóch procesach wykonywanie tego samego programu. <m>'
			'Dlatego też należy powiedzieć o kolejnej funkcji czyli exec, <m> która pozwala na zastąpienie kodu bieżącego procesu jakimś innym, <m>'
			'czyli wykonanie w nim jakiegoś podanego przekazanego do tej funkcji kodu. <m>'
			
			'Funkcja ta posiada kilka wariantów dostępnych w module <os>[O S] <m> i pozwala na uruchomienie wskazanego programu. <m>'
			'Jeden z wariantów jej działania widzimy na ekranie, w tym przykładzie <m> powoduje on wykonanie w miejsce interpretera Pythona komendy <ls>[L S]. <m>'
			'Funkcja exec nie powoduje zmiany identyfikatora procesu. <m>'
			'Jeżeli funkcja exec uruchomiła się bez błędu to nigdy nie wraca, <m> czyli kod występujący po niej nie będzie wykonywany. <m>'
			'W Pythonie w przypadku błędów generuje wyjątek, <m> więc po prostu nigdy nie wraca. <m>'
		]
	},
	{ #  
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_exec_B, "py")],
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(code_exec_B, [], cmd="python3")],
		],
		'text' : [
			'Należy rozróżniać funkcje z rodziny exec dostępne w module <os>[O S] <m> od pythonowej funkcji exec, która pozwala na wykonanie w bieżącym <m> interpreterze Pythona kodu pythonowego zawartego w napisie. <m>'
		]
	},
	{ #  
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_os_system_A, "py")],
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(code_os_system_A, [], cmd="python3")],
		],
		'text' : [
			"Moduł <os>[O S] dostarcza także inną metodę wykonania <m> zewnętrznego polecenia, która w odróżnieniu od funkcji z rodziny exec <m> nie powoduje zakończenia pracy pythona (gdyż wewnętrznie używa także fork'a) <m> jest nią funkcja system. <m>"
			'Pozwala ona wykonać dowolny ciąg znakowy (napis) <m> tak jakby był uruchomiony w powłoce zgodnej ze składnią <sh>[S H]. <m>'
			
			'Funkcja system nie zapewnia jednak wygodnych mechanizmów komunikacji <m> z uruchamianym programem poprzez przekazywanie danych <m> przez standardowe wejście, wyjście tego polecenia. <m>'
		]
	},
	{ #  
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_os_system_B, "py")],
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(code_os_system_B, [], cmd="python3")],
		],
		'text' : [
			'Jeżeli uruchamiana komenda miałaby przyjąć coś na standardowe wejście <m> to możemy użyć w ramach wykonywanego napisu polecenia echo, <m>'
			'któremu w argumencie przekażemy dane wejściowe <m> i wynik tego polecenia przekażemy na standardowe wejście tej komendy. <m>'
			
			'Możemy też korzystać z tymczasowych plików do wymiany takich danych, <m> jednak też nie jest to najwygodniejsza metoda. <m>'
			'Na szczęście Python dostarcza wygodniejsze <m> mechanizmy do uruchamiania zewnętrznych poleceń. <m>'
		]
	},
	{ #  
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_subprocess_A, "py")],
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(code_subprocess_A, [], cmd="python3")],
		],
		'text' : [
			'Takim mechanizmem jest funkcja <run>[ran] z modułu subprocess. <m>'
			'W opcjonalnych argumentach tej funkcji możemy wskazać co ma zostać <m> przekazane na standardowe wejście polecenia i co ma się stać z jego <m> standardowym wyjściem i lub wyjściem błędu. <m>'
			
			'W widocznym przykładzie na standardowe wejście przekazujemy <m> ciąg bajtowy utworzony z napisu zawartego w zmiennej <xx>[X X], <m>'
			'a standardowe wyjście zostanie przechwycone i będzie dostępne <m> w polu <stdout>[S T D out] obiektu zwróconego przez tą funkcję. <m>'
			
			'Z obiektu zwróconego przez funkcję <run>[ran] możemy także uzyskać <m> kod powrotu uruchamianego polecenia. <m>'
		]
	},
]
