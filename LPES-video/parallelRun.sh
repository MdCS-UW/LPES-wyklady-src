#!/bin/bash

# Copyright (c) 2021 Matematyka dla Ciekawych Świata (http://ciekawi.icm.edu.pl/)
# Copyright (c) 2021 Robert Ryszard Paciorek <rrp@opcode.eu.org>
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


if [ $# -lt 1 ]; then
	echo "USAGE: $0 screenplaydir screenplaydir [...]]"
fi

LOCKFILE="../tmp-build/prepareRender.lock"

waitForMemomry() {
	echo -n "  wait for memory: "
	while true; do
		if [ `free -g | awk '/^Mem:/ {print $7}'` -gt 40 ]; then
			echo "OK";
			return
		fi
		sleep 30
		echo -n "."
		sleep 30
	done
}

waitForUnlock() {
	echo -n "  wait for render unlock: "
	while true; do
		flock -w 30 "$LOCKFILE" -c "echo OK" && return
		echo -n "."
		sleep 30
	done
}

mkdir  -p ../output/logs

for d in "$@"; do
	echo "Rendering $d"
	waitForMemomry
	waitForUnlock
	(
		flock -n 9 || exit 100;
		echo "  start!"
		python3 eduMovie.py $d/*.py >& "../output/logs/$d.log"
	) 9>"$LOCKFILE" &
	sleep 2
done
