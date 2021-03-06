
from time import *
import sys

class ONPyTimer(object):
	'''	
		ONPyTimer allows to monitor time difference between the lines of a
		Python script in a stopwatch-like manner.

		=== Usage: =====================

		from ONPyTimer import *

		ONPyTimer.check(flag='A')   # will show current time and flag name
		...
		ONPyTimer.check(flags=['A']) # will show time diff from flag 'A'
		...
		ONPyTimer.check(flag='B', flags=['A']) # will show new flag name and time diff
		... 								   # from flag 'A'
		...
		ONPyTimer.check(flags=['A', 'B']) # will show time diff from flags 'A' and 'B'
		...
		ONPyTimer.check(flags=['A'], output=f) # will write time diff from flag 'A' to file 'f'

		================================

		Author: Nicolas Alliaume - ON Lab
		GitHub: http://github.com/nicolasalliaume/ONPyTimer
		@ 2014
	'''

	__measures = {}

	@staticmethod
	def check(flags=[], flag=None, output=sys.stdout):
		'''
			Time is measured.
			
			If a string is passed to the flag param,
			this measure is added as a flagged mesure and
			can be used later to compare.

			Time differences are displayed from current time
			to each of the flagged times indicated in the
			flags parameter. Flags parameter must be a list
			of valid flag names.

			If no flags are passed, current time is displayed.

			To print the timer info into a file, pass an opened
			file as output.
		'''
		_time = time()
		if flags:
			ONPyTimer.__pretty_print(ONPyTimer.__diff(filter(lambda m: m[0] in flags, ONPyTimer.__measures.items()), _time), output)
		else:
			output.write('[-> Current time: %f]\n' % _time)
		if flag:
			ONPyTimer.__measures[flag] = _time
			output.write('[-> FLAG: %s]\n' % flag)

	@staticmethod
	def __pretty_print(measures, output):
		'''
			Prints in the console the given list
			of measures.

			Each measure is a dictionary containing:
				- diff: time difference
				- from: from flag name
		'''
		output.write('[-> ' + '\n[-> '.join(('%f sec. from %s]' % (m['diff'], m['from']) for m in measures)) + '\n')

	@staticmethod
	def __diff(_from_measures, _to_time):
		'''
			Returns a list of measures.

			- _from_measures: a list of tuples containing
						measures in the format:	(flag_name, time)
			- _to_time: a time measure

			Each measure is a dictionary with two
			items:
				- flag: a flag name (flag)
				- diff: the difference between _to_time
						and the flag time (time)
		'''
		return map(lambda m: {'diff': _to_time - m[1], 'from': m[0]}, _from_measures)
