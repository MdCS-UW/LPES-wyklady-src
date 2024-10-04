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


import urllib.request
import json, codecs, re

try:
	from GoogleCloudTextToSpeach import token
except:
	token = '' # <<< put your Google Cloud TTS (https://cloud.google.com/text-to-speech) token here
	
	# 2022-12-18:  in some cases "cloud Text to Speach" return wrong timepoints for markers, this can be observed as non monotonically values of m_[0-9]* in .text.info files (eg. "m_3" before "m_2").

def text2audioFile(txt, fileName):
	if not token:
		raise BaseException("Empty Google cloud Text to Speach token")
	
	txt = txt.replace('. <', '.<break time="300ms"/> <')
	txt = re.sub('<mark name="([^"]*)"/>([ \t\n]*)– ', ' –<break time="200ms"/> <mark name="\\1"/> ', txt) # <break> just after mark cause ignoring <mark> by Google TTS ...
	txt = txt.replace(', ',  ',<break time="100ms"/> ')
	# prepare and send request
	r = '''{
		"audioConfig": {
			"audioEncoding": "LINEAR16",
			"pitch": -1.6,
			"speakingRate": 0.93
		},
		"enable_time_pointing" : [
			"SSML_MARK"
		],
		"voice": {
			"languageCode": "pl-PL",
			"name": "pl-PL-Wavenet-B"
		},
		"input": {
			"ssml": "<speak>''' + txt.replace('"', '\\"') + '''</speak>"
		}
	}'''
	r = urllib.request.Request(
		'https://cxl-services.appspot.com/proxy?url=https://texttospeech.googleapis.com/v1beta1/text:synthesize&token=' + token,
		data=r.encode(),
		headers={
			'Accept' : '*/*',
			'Accept-Language' : 'pl,en-US;q=0.7,en;q=0.3',
			'Content-Type' : 'text/plain;charset=UTF-8',
		},
		method='POST'
	)
	
	# read response
	i = json.load( urllib.request.urlopen(r) )
	
	# write binary audio (.wav file)
	d = codecs.decode(i['audioContent'].encode(), 'base64')
	o = open(fileName + ".audio", "wb")
	o.write(d)
	o.close()
	
	# write timepoints info (.json file)
	points = {}
	for tp in i['timepoints']:
		points[ tp['markName'] ] = tp['timeSeconds']
	o = open(fileName + ".info", "w")
	json.dump(points, o)
	o.close()
