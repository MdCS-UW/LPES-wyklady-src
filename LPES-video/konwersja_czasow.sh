AdobeAudition2json() {
IN_OLD="audio-google/$1.text.info"
IN_NEW="audio-jutuberpl/$1.text*.csv"
OUT="$1.text.info"

tr ',}' '\n\n' < $IN_OLD | tr -d '"{ ' | cut -f1 -d: > /tmp/nazwy

awk '{print $2}' $IN_NEW | awk -F: '{x=$1*60+$2; if (x>0) print(x)}' > /tmp/czasy

paste /tmp/nazwy /tmp/czasy | python3 -c '
import json, sys;
t={}
for x in sys.stdin:
   x = x.split()
   t[x[0]] = float(x[1])
json.dump(t, open("'$OUT'", "wt"))
'
}

for f in audio-jutuberpl/*text.audio; do
	cp $f .
	AdobeAudition2json `basename "$f" ".text.audio"`
done
