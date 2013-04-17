import writer

class XMLWriter(object):
	def __init__(self, stateDiagram):
		self.stateDiagram = stateDiagram

	def execute(self, fd):
		writer.attach()
		retval = self.stateDiagram.to_xml()
		writer.detach()

		fd.write(retval)

		return fd
