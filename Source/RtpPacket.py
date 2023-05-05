import sys
from time import time
HEADER_SIZE = 12

class RtpPacket:	
	header = bytearray(HEADER_SIZE)
	
	def __init__(self):
		pass
		
	def encode(self, version, padding, extension, cc, seqnum, marker, pt, ssrc, payload):
		#print('RtpPacket: def encode')
		"""Encode the RTP packet with header fields and payload."""
		timestamp = int(time())
		header = bytearray(HEADER_SIZE)
		#--------------
		# TO COMPLETE
		#--------------
		# Fill the header bytearray with RTP header fields
		# the first byte
		self.header[0] = version << 6						#version bit  ( 6 first bits)
		self.header[0] = self.header[0] | padding << 5		# padding bit ()
		self.header[0] = self.header[0] | extension << 4	# extension bit
		self.header[0] = self.header[0] | cc				# 4 bits left for cc
		# the 2nd byte
		self.header[1] = marker << 7						
		self.header[1] = self.header[1] | pt
		# the 3rd byte
		self.header[2] = seqnum >> 8
		self.header[3] = seqnum
		# byte 4 5 6 7 contain timestamp
		self.header[4] = (timestamp >> 24) & 0xFF
		self.header[5] = (timestamp >> 16) & 0xFF
		self.header[6] = (timestamp >> 8) & 0xFF
		self.header[7] = timestamp & 0xFF

		self.header[8] = (ssrc >> 24) & 0xFF
		self.header[9] = (ssrc >> 16) & 0xFF
		self.header[10] = (ssrc >> 8) & 0xFF
		self.header[11] = ssrc & 0xFF
		# Get the payload from the argument
		# self.payload = ...
		self.payload = payload

	def decode(self, byteStream):
		#print('RtpPacket: def decode')
		"""Decode the RTP packet."""
		self.header = bytearray(byteStream[:HEADER_SIZE])
		self.payload = byteStream[HEADER_SIZE:]
	
	def version(self):
		#print('RtpPacket: def version')
		"""Return RTP version."""
		return int(self.header[0] >> 6)
	
	def seqNum(self):
		#print('RtpPacket: def seqNum')
		"""Return sequence (frame) number."""
		seqNum = self.header[2] << 8 | self.header[3]
		return int(seqNum)
	
	def timestamp(self):
		#print('RtpPacket: def timestamp')
		"""Return timestamp."""
		timestamp = self.header[4] << 24 | self.header[5] << 16 | self.header[6] << 8 | self.header[7]
		return int(timestamp)
	
	def payloadType(self):
		#print('RtpPacket: def payloadType')
		"""Return payload type."""
		pt = self.header[1] & 127
		return int(pt)
	
	def getPayload(self):
		#print('RtpPacket: def getPayload')
		"""Return payload."""
		return self.payload
		
	def getPacket(self):
		#print('RtpPacket: def getPacket')
		"""Return RTP packet."""
		return self.header + self.payload