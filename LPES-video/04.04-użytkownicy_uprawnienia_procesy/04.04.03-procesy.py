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

prompt_txt = eduMovie.prompt(user="rrp")
prompt_len = len(eduMovie.prompt(user="rrp", color=False))

try: clipData
except NameError: clipData = []

clipData += [
	{ 'section': "Procesy" },
	{
		'console': [
			[0.060906, "o", prompt_txt],
			[1.359762, "o", "p"],
			[1.959739, "o", "s"],
			[3.959704, "o", "\r\n"],
			[3.973287, "o", "  PID TTY          TIME CMD\r\n 5163 pts/3    00:00:00 sh\r\n 5164 pts/3    00:00:00 bash\r\n 5236 pts/3    00:00:00 ps\r\n"],
			[3.974983, "o", prompt_txt],
			
			["psf + 0.407686", "o", "p"],
			["psf + 1.127662", "o", "s"],
			["psf + 2.015678", "o", " "],
			["psf + 3.295582", "o", "-"],
			["psf + 3.551659", "o", "f"],
			["psf + 3.863602", "o", "\r\n"],
			["psf + 3.87849", "o", "UID        PID  PPID  C STIME TTY          TIME CMD\r\n"],
			["psf + 3.878868", "o", "rrp       5163  5154  0 18:43 pts/3    00:00:00 sh -c /bin/bash\r\nrrp       5164  5163  0 18:43 pts/3    00:00:00 /bin/bash\r\nrrp       5317  5164  0 18:43 pts/3    00:00:00 ps -f\r\n"],
			["psf + 3.880474", "o", prompt_txt],
			
			["psfuser", "o", eduMovie.editBegin(2) + "" + eduMovie.markBegin + "rrp" + eduMovie.markEnd + "       5164  5163  0 18:43 pts/3    00:00:00 /bin/bash" + eduMovie.editEnd(2, prompt_len)],
			["psfpid",  "o", eduMovie.editBegin(2) + "rrp       " + eduMovie.markBegin + "5164" + eduMovie.markEnd + "  5163  0 18:43 pts/3    00:00:00 /bin/bash" + eduMovie.editEnd(2, prompt_len)],
			["psfppid", "o", eduMovie.editBegin(2) + "rrp       5164  " + eduMovie.markBegin + "5163" + eduMovie.markEnd + "  0 18:43 pts/3    00:00:00 /bin/bash" + eduMovie.editEnd(2, prompt_len)],
			["psftty",  "o", eduMovie.editBegin(2) + "rrp       5164  5163  0 18:43 " + eduMovie.markBegin + "pts/3" + eduMovie.markEnd + "    00:00:00 /bin/bash" + eduMovie.editEnd(2, prompt_len)],
			["psfcmd",  "o", eduMovie.editBegin(2) + "rrp       5164  5163  0 18:43 pts/3    00:00:00 " + eduMovie.markBegin + "/bin/bash" + eduMovie.markEnd + "" + eduMovie.editEnd(2, prompt_len)],
		],
		'text' : [
			'Przy programowaniu w Pythonie mówiliśmy trochę o procesach, <m> tworzeniu potomków i tym podobnych. <m>'
			'Do wyświetlania działających w systemie procesów służy komenda <ps>[PS], <m> która tak naprawdę jest tylko i wyłącznie parserem plików tekstowych <m> i struktury katalogowej z katalogu </proc>[ukośnik proc]. <m>'
			
			'Domyślnie <ps>[PS] wypisuje procesy bieżącego użytkownika <m> działające na bieżącym terminalu, natomiast <ps>[PS] z opcją <m> x wypisze nam wszystkie procesy bieżącego użytkownika. <m>'
			'Użycie opcji <-A>[minus A duże] spowoduje wypisanie <m> wszystkich procesów wszystkich użytkowników. <mark name="psf" />'
			
			'Natomiast dodanie opcji <-f>[minus f] zwiększy <m> szczegółowość wypisywanych informacji. <m>'
			'W wyniku polecenia otrzymujemy informacje takie jak:'
			'<mark name="psfuser" /> nazwę użytkownika,'
			'<mark name="psfpid" /> PID czyli identyfikator procesu,'
			'<mark name="psfppid" /> identyfikator rodzica,'
			'<mark name="psftty" /> terminal na którym działa dany proces oraz'
			'<mark name="psfcmd" /> komendę wraz z opcjami.'
		]
	},
	{
		'console': [
			[0.0, "o", eduMovie.editBegin(2) + "rrp       5164  5163  0 18:43 pts/3    00:00:00 /bin/bash" + eduMovie.editEnd(2, prompt_len)],
			[0.065886, "o", eduMovie.prompt()],
			[1.358073, "o", "t"],
			[1.58198, "o", "o"],
			[1.773859, "o", "p"],
			[2.181966, "o", "\r\n"],
			[2.218269, "o", "\u001b[?1h\u001b=\u001b[?25l"],
			[2.390159, "o", "\u001b[H\u001b[J\u001b[m\u000ftop - 19:06:30 up  4:24,  6 users,  load average: 0.12, 0.10, 0.16\u001b[m\u000f\u001b[39;49m\u001b[m\u000f\u001b[39;49m\u001b[K\r\nTasks:\u001b[m\u000f\u001b[39;49m\u001b[1m 223 \u001b[m\u000f\u001b[39;49mtotal,\u001b[m\u000f\u001b[39;49m\u001b[1m   1 \u001b[m\u000f\u001b[39;49mrunning,\u001b[m\u000f\u001b[39;49m\u001b[1m 222 \u001b[m\u000f\u001b[39;49msleeping,\u001b[m\u000f\u001b[39;49m\u001b[1m   0 \u001b[m\u000f\u001b[39;49mstopped,\u001b[m\u000f\u001b[39;49m\u001b[1m   0 \u001b[m\u000f\u001b[39;49mzombie\u001b[m\u000f\u001b[39;49m\u001b[m\u000f\u001b[39;49m\u001b[K\r\n%Cpu(s):\u001b[m\u000f\u001b[39;49m\u001b[1m  0.0 \u001b[m\u000f\u001b[39;49mus,\u001b[m\u000f\u001b[39;49m\u001b[1m  2.0 \u001b[m\u000f\u001b[39;49msy,\u001b[m\u000f\u001b[39;49m\u001b[1m  0.0 \u001b[m\u000f\u001b[39;49mni,\u001b[m\u000f\u001b[39;49m\u001b[1m 98.0 \u001b[m\u000f\u001b[39;49mid,\u001b[m\u000f\u001b[39;49m\u001b[1m  0.0 \u001b[m\u000f\u001b[39;49mwa,\u001b[m\u000f\u001b[39;49m\u001b[1m  0.0 \u001b[m\u000f\u001b[39;49mhi,\u001b[m\u000f\u001b[39;49m\u001b[1m  0.0 \u001b[m\u000f\u001b[39;49msi,\u001b[m\u000f\u001b[39;49m\u001b[1m  0.0 \u001b[m\u000f\u001b[39;49mst\u001b[m\u000f\u001b[39;49m\u001b[m\u000f\u001b[39;49m\u001b[K\r\nMiB Mem :\u001b[m\u000f\u001b[39;49m\u001b[1m   7977.1 \u001b[m\u000f\u001b[39;49mtotal,\u001b[m\u000f\u001b[39;49m\u001b[1m    825.0 \u001b[m\u000f\u001b[39;49mfree,\u001b[m\u000f\u001b[39;49m\u001b[1m   1952.0 \u001b[m\u000f\u001b[39;49mused,\u001b[m\u000f\u001b[39;49m\u001b[1m   5200.2 \u001b[m\u000f\u001b[39;49mbuff/cache\u001b[m\u000f\u001b[39;49m\u001b[m\u000f\u001b[39;49m\u001b[K\r\nMiB Swap:\u001b[m\u000f\u001b[39;49m\u001b[1m      0.0 \u001b[m\u000f\u001b[39;49mtotal,\u001b[m\u000f\u001b[39;49m\u001b[1m      0.0 \u001b[m\u000f\u001b[39;49mfree,\u001b[m\u000f\u001b[39;49m\u001b[1m      0.0 \u001b[m\u000f\u001b[39;49m"],
			[2.390553, "o", "used.\u001b[m\u000f\u001b[39;49m\u001b[1m   5640.0 \u001b[m\u000f\u001b[39;49mavail Mem \u001b[m\u000f\u001b[39;49m\u001b[m\u000f\u001b[39;49m\u001b[K\r\n\u001b[K\r\n\u001b[7m  PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND    \u001b[m\u000f\u001b[39;49m\u001b[K\r\n\u001b[m\u000f\u001b[1m26948 rrp       20   0   13032   3784   3096 R   6.2   0.0   0:00.02 top        \u001b[m\u000f\u001b[39;49m\u001b[K\r\n\u001b[m\u000f    1 root      20   0  169644  10220   7752 S   0.0   0.1   0:02.74 systemd    \u001b[m\u000f\u001b[39;49m\u001b[K\r\n\u001b[m\u000f    2 root      20   0       0      0      0 S   0.0   0.0   0:00.01 kthreadd   \u001b[m\u000f\u001b[39;49m\u001b[K\r\n\u001b[m\u000f    3 root       0 -20       0      0      0 I   0.0   0.0   0:00.00 rcu_gp     \u001b[m\u000f\u001b[39;49m\u001b[K\r\n\u001b[m\u000f    4 root       0 -20       0      0      0 I   0.0   0.0   0:00.00 rcu_par_gp \u001b[m\u000f\u001b[39;49m\u001b[K\r\n\u001b[m\u000f    6 root       0 -20       0      0      0 I   0.0   0.0   0:00.00 kworker/0+ \u001b[m\u000f\u001b[39;49m\u001b[K\r\n\u001b[m\u000f    8 root       0 -20       0      0      0 I   0.0   0.0   0:00.00 mm_percpu+ \u001b[m\u000f\u001b[39;49m\u001b[K\r\n\u001b[m\u000f    9 root      20   0       0      0      0 S   0.0   0.0   0:00.48 ksoftirqd+ \u001b[m\u000f\u001b[39;49m\u001b[K\r\n\u001b[m\u000f   10 root      20  "],
			[2.390779, "o", " 0       0      0      0 I   0.0   0.0   0:22.66 rcu_sched  \u001b[m\u000f\u001b[39;49m\u001b[K\r\n\u001b[m\u000f   11 root      20   0       0      0      0 I   0.0   0.0   0:00.00 rcu_bh     \u001b[m\u000f\u001b[39;49m\u001b[K\r\n\u001b[m\u000f   12 root      rt   0       0      0      0 S   0.0   0.0   0:00.06 migration+ \u001b[m\u000f\u001b[39;49m\u001b[K\r\n\u001b[m\u000f   14 root      20   0       0      0      0 S   0.0   0.0   0:00.00 cpuhp/0    \u001b[m\u000f\u001b[39;49m\u001b[K\r\n\u001b[m\u000f   15 root      20   0       0      0      0 S   0.0   0.0   0:00.00 cpuhp/1    \u001b[m\u000f\u001b[39;49m\u001b[K\r\n\u001b[m\u000f   16 root      rt   0       0      0      0 S   0.0   0.0   0:00.41 migration+ \u001b[m\u000f\u001b[39;49m\u001b[K\r\n\u001b[m\u000f   17 root      20   0       0      0      0 S   0.0   0.0   0:00.23 ksoftirqd+ \u001b[m\u000f\u001b[39;49m\u001b[K\r\n\u001b[m\u000f   19 root       0 -20       0      0      0 I   0.0   0.0   0:00.00 kworker/1+ \u001b[m\u000f\u001b[39;49m\u001b[K"],
			[4.922268, "o", "\u001b[?25l\u001b[H\u001b[m\u000ftop - 19:06:32 up  4:24,  6 users,  load average: 0.12, 0.10, 0.16\u001b[m\u000f\u001b[39;49m\u001b[m\u000f\u001b[39;49m\u001b[K\r\n\r\n%Cpu(s):\u001b[m\u000f\u001b[39;49m\u001b[1m  1.1 \u001b[m\u000f\u001b[39;49mus,\u001b[m\u000f\u001b[39;49m\u001b[1m  0.8 \u001b[m\u000f\u001b[39;49msy,\u001b[m\u000f\u001b[39;49m\u001b[1m  0.0 \u001b[m\u000f\u001b[39;49mni,\u001b[m\u000f\u001b[39;49m\u001b[1m 98.1 \u001b[m\u000f\u001b[39;49mid,\u001b[m\u000f\u001b[39;49m\u001b[1m  0.0 \u001b[m\u000f\u001b[39;49mwa,\u001b[m\u000f\u001b[39;49m\u001b[1m  0.0 \u001b[m\u000f\u001b[39;49mhi,\u001b[m\u000f\u001b[39;49m\u001b[1m  0.1 \u001b[m\u000f\u001b[39;49msi,\u001b[m\u000f\u001b[39;49m\u001b[1m  0.0 \u001b[m\u000f\u001b[39;49mst\u001b[m\u000f\u001b[39;49m\u001b[m\u000f\u001b[39;49m\u001b[K\r\nMiB Mem :\u001b[m\u000f\u001b[39;49m\u001b[1m   7977.1 \u001b[m\u000f\u001b[39;49mtotal,\u001b[m\u000f\u001b[39;49m\u001b[1m    825.1 \u001b[m\u000f\u001b[39;49mfree,\u001b[m\u000f\u001b[39;49m\u001b[1m   1951.9 \u001b[m\u000f\u001b[39;49mused,\u001b[m\u000f\u001b[39;49m\u001b[1m   5200.2 \u001b[m\u000f\u001b[39;49mbuff/cache\u001b[m\u000f\u001b[39;49m\u001b[m\u000f\u001b[39;49m\u001b[K\r\nMiB Swap:\u001b[m\u000f\u001b[39;49m\u001b[1m      0.0 \u001b[m\u000f\u001b[39;49mtotal,\u001b[m\u000f\u001b[39;49m\u001b[1m      0.0 \u001b[m\u000f\u001b[39;49mfree,\u001b[m\u000f\u001b[39;49m\u001b[1m      0.0 \u001b[m\u000f\u001b[39;49mused.\u001b[m\u000f\u001b[39;49m\u001b[1m   5640.1 \u001b[m\u000f\u001b[39;49mavail Mem \u001b[m\u000f\u001b[39;49m\u001b[m\u000f\u001b[39;49m\u001b[K\r\n\u001b[K\r\n\r\n\u001b[m\u000f  807 root      20   0 1029612 150000  94364 S   1.6   1.8  11:59.25 Xorg       \u001b[m\u000f\u001b[39;49m\u001b[K\r\n\u001b[m\u000f 1167 rrp       20   0  109112  40604 "],
			[4.922698, "o", " 25396 S   1.2   0.5   2:04.64 fbpanel    \u001b[m\u000f\u001b[39;49m\u001b[K\r\n\u001b[m\u000f 1606 rrp       20   0 3593616 560404 193832 S   1.2   6.9  33:17.21 firefox-e+ \u001b[m\u000f\u001b[39;49m\u001b[K\r\n\u001b[m\u000f 7563 rrp       20   0 2548984 245320  96588 S   1.2   3.0  12:24.70 vlc        \u001b[m\u000f\u001b[39;49m\u001b[K\r\n\u001b[m\u000f 1770 rrp       20   0 2607156 212624  82148 S   0.8   2.6   3:57.31 WebExtens+ \u001b[m\u000f\u001b[39;49m\u001b[K\r\n\u001b[m\u000f25651 rrp       20   0   11740   3712   2684 S   0.8   0.0   0:21.63 tmux: ser+ \u001b[m\u000f\u001b[39;49m\u001b[K\r\n\u001b[m\u000f   10 root      20   0       0      0      0 I   0.4   0.0   0:22.67 rcu_sched  \u001b[m\u000f\u001b[39;49m\u001b[K\r\n\u001b[m\u000f 1165 rrp       20   0   22480   7696   3256 S   0.4   0.1   0:49.29 xcompmgr   \u001b[m\u000f\u001b[39;49m\u001b[K\r\n\u001b[m\u000f 1826 rrp       20   0 2954360 266204 153736 S   0.4   3.3   2:23.35 Web Conte+ \u001b[m\u000f\u001b[39;49m\u001b[K\r\n\u001b[m\u000f 1878 rrp       20   0 3225700 445228 204832 S   0.4   5.5   2:05.93 Web Conte+ \u001b[m\u000f\u001b[39;49m\u001b[K\r\n\u001b[m\u000f 3530 root      20   0       0      0      0 I   0.4   0.0   0:14.19 kworker/0+ \u001b[m\u000f\u001b[39;49m\u001b[K\r\n\u001b[m\u000f 5000 rrp       20   0   43740  13916   8364 S   0.4"],
			[4.92292, "o", "   0.2   0:00.77 xterm      \u001b[m\u000f\u001b[39;49m\u001b[K\r\n\u001b[m\u000f 6705 rrp       20   0 2045028 162276 105272 S   0.4   2.0   5:05.91 kate       \u001b[m\u000f\u001b[39;49m\u001b[K\r\n\u001b[m\u000f18020 root      20   0       0      0      0 I   0.4   0.0   0:00.47 kworker/5+ \u001b[m\u000f\u001b[39;49m\u001b[K\r\n\u001b[m\u000f\u001b[1m26948 rrp       20   0   13000   3792   3096 R   0.4   0.0   0:00.03 top        \u001b[m\u000f\u001b[39;49m\u001b[K\r\n\u001b[m\u000f    1 root      20   0  169644  10220   7752 S   0.0   0.1   0:02.74 systemd    \u001b[m\u000f\u001b[39;49m\u001b[K"],
			[6.550056, "o", "\u001b[?1l\u001b>\u001b[24;1H\r\n\u001b[34h\u001b[?25h\u001b[K"],
			[6.551862, "o", eduMovie.prompt()],
		],
		'text' : [
			'Listę działających procesów możemy też oglądać przy pomocy polecenia top, <m> który wyświetla procesy sortowane według na przykład <m> zużycia procesora, zużycia pamięci, itd. <m>'
			'Kolumnę sortowania można zmieniać przy pomocy znaków większe / mniejsze. <m>'
		]
	},
	{ 'section': "Sygnały" },
	{
		'console': [
			[0.0, ""],
			["kill + 0.687682", "o", "p"],
			["kill + 0.943624", "o", "s"],
			["kill + 1.199558", "o", "\r\n"],
			["kill + 1.213453", "o", "  PID TTY          TIME CMD\r\n30638 pts/6    00:00:00 sh\r\n30639 pts/6    00:00:00 bash\r\n30668 pts/6    00:00:00 ps\r\n"],
			["kill + 1.214639", "o", eduMovie.prompt()],
			["kill + 2.143694", "o", "k"],
			["kill + 2.367572", "o", "i"],
			["kill + 2.655704", "o", "l"],
			["kill + 2.785185", "o", "l"],
			["kill + 3.095617", "o", " "],
			["kill + 3.287558", "o", "-"],
			["kill + 3.695619", "o", "9"],
			["kill + 4.015649", "o", " "],
			["kill + 5.632542", "o", "30639"],
			["kill + 6.231666", "o", "\r\n"],
			["kill + 6.232846", "o", "Killed\r\n"],
		],
		'text' : [
			'Sygnały są jednym ze sposobów komunikacji między procesowej. <m>'
			'Mogą służyć do przekazywania różnych prostych informacji <m> z jednego procesu do innego. <m>'
			'Sygnał jest krótką informacją, <m> w podstawowej wersji tylko i wyłącznie numeryczną. <m>'
			'Czyli proces otrzymuje sygnał o danym numerze <m> i musi na niego jakoś zareagować. <m>'
			
			'Do wysyłania sygnału do wskazanego procesu <m> możemy użyć polecenia kill. <mark name="kill" />'
			'Polecenie to wbrew nazwie nie służy tylko do zabijania procesów, <m> ani nawet domyślnie nie wysyła sygnału kill. <m>'
			'Polecenie kill domyślnie wysyła łagodną prośbę o zakończenie się procesu <m> w postaci sygnału <SIGTERM>[sig term], którą proces może obsłużyć i np. zignorować. <m>'
			
			'Jeżeli uruchomimy kill z opcją <-9>[minus 9] to zostanie wysłany <m> sygnał <SIGKILL>[sig kill], który tak naprawdę nawet nie dotrze do procesu. <m>'
			'Zamiast tego zostanie on obsłużony (w jego imieniu) przez jądro, <m> które odbierze procesowi dostęp do procesora (czyli prawo wykonywania się), <m>'
				'zajmowane przez niego obszary pamięci uzna za wolne, <m> zamknie i zwolni wszystkie zasoby używane przez proces, <m> a stan procesu zostanie zmieniony na zombie. <m>'
			
			'Po odebraniu kodu powrotu przez rodzica (w tym wypadku będzie to typowo 137, <m> informujące że proces został zakończony na skutek sygnału <SIGKILL>[sig kill]), <m>'
				'informacja na temat procesu (będącego w stanie zombie) <m> zostanie usunięta z listy procesów. <m>'
			
			'Każdy proces kończący swoje działanie staje się na chwilę procesem zombie, <m> czyli nie posiadającym swoich zasobów i prawa wykonywania się <m> wpisem na liście procesów, zawierającym między innymi kod powrotu. <m>'
			'Proces zostanie usunięty z tej listy gdy jego rodzic odbierze ten kod powrotu. <m>'
			'Typowo dzieje się to na tyle szybko że procesy zombie nie są widoczne w systemie. <m>'
			'Natomiast jeżeli rodzic jest czymś zajęty i nie interesuje go śmierć <m> jego dzieci, to zakończony potomek pozostanie w tym stanie na dłużej. <m>'
			'Możemy wtedy zabić rodzica, co powinno doprowadzić <m> do usunięcia procesów zombi będących jego potomkami. <m>'
		]
	},
]
