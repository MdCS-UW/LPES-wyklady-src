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
	{ 'comment': 'multiprocessing' },
	{
		'consoleTop': [
			[0.0, eduMovie.clear],
		],
		'consoleDown': [
			[0.0, ""],
		],
		'text' : [
			'To co tutaj zostało pokazane jest podejściem bardziej <m> w stylu biblioteki standardowej C niż Pythona. <m>'
			'Python oferuje na przykład moduł multiprocessing pozwalający na <m> tworzenie grupy procesów, które będą wykonywały równolegle jakąś operację. <m>'
			'Jednak zagadnienia te wykraczają trochę poza program tego kursu i osoby <m> zainteresowane nimi zapraszam do zapoznania się z innymi materiałami. <m>'
		] # TODO może jednak omówić multiprocessing + lock (?)
	},
]

