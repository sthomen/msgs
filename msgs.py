# vim:ts=4:sw=4:

import os

from ..applet import Applet
from .message import Messages
from datetime import datetime

class Msgs(Applet):
	def __init__(self):
		Applet.__init__(self)
		self.updated = None
		self.cachetime = 60

		self.base_path=os.path.dirname(__file__)
		self.base_url='apps/msgs'

		self.add_template_dir(os.path.join(self.base_path, 'templates'))

	def dispatch(self, method, *args, **kwargs):
		output=None

		self.load_messages()

		self.metadata={}

		if len(args) == 3 and args[1] == 'message':
			output=self.message(int(args[2]))
		else:
			output=self.list()

		return output

	def list(self):
		self.metadata['title']='Messages'

		return self.render('list', { 'messages': self.messages })

	def message(self, id):
		if id in self.messages:
			message=self.messages.get(id)

			self.metadata['title']=message.title

			return self.render('message', { 'message': message })

		self.metadata['code']=404

		return self.render('notfound', { 'id': id })

	def load_messages(self):
		path=None

		try:
			if Config.has_section('messages'):
				path=Config.get('messages', 'path')
		except:
			pass
			
		if self.updated == None or (datetime.now() - self.updated).total_seconds() > self.cachetime:
			self.messages=Messages(path)
			self.updated=datetime.now()
