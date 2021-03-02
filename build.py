#!/usr/bin/python

import os, time, sys

original_license = """
/*
	Finite State Machine Designer (http://madebyevan.com/fsm/)
	License: MIT License (see below)

	Copyright (c) 2010 Evan Wallace

	Permission is hereby granted, free of charge, to any person
	obtaining a copy of this software and associated documentation
	files (the "Software"), to deal in the Software without
	restriction, including without limitation the rights to use,
	copy, modify, merge, publish, distribute, sublicense, and/or sell
	copies of the Software, and to permit persons to whom the
	Software is furnished to do so, subject to the following
	conditions:

	The above copyright notice and this permission notice shall be
	included in all copies or substantial portions of the Software.

	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
	EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
	OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
	NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
	HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
	WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
	FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
	OTHER DEALINGS IN THE SOFTWARE.
*/
"""


def sources():
	path = './src/'
	return [os.path.join(base, f) for base, folders, files in os.walk(path) for f in files if f.endswith('.js')]

def build():
	addedLicense = False
	path = './www/fsm.js'
	data = '\n'.join(open(file, 'r').read() for file in sources())
	with open(path, 'w') as f:
		if (addedLicense == False):
			f.write(original_license + '\n')
			addedLicense = True
		f.write(data)
	print 'built %s (%u bytes)' % (path, len(data))

def stat():
	return [os.stat(file).st_mtime for file in sources()]

def monitor():
	a = stat()
	while True:
		time.sleep(0.5)
		b = stat()
		if a != b:
			a = b
			build()

if __name__ == '__main__':
	build()
	if '--watch' in sys.argv:
		monitor()
