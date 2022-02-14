from django.db import models


class AmtcModel(models.Model):
	PORT1 = (
		(1, 1),
		(2, 2),
		(3, 3),
		(4, 4),
		(5, 5),
		(6, 6),
		(7, 7),
		(8, 8),
		(9, 9),
		(10, 10),
		(11, 11),
		(12, 12),
		(13, 13),
		(14, 14),
		(15, 15),
		(16, 16),
		(17, 17),
		(18, 18),
		(19, 19),
		)

	PORT2 = (
		(0, 0),
		(1, 1),
		(2, 2),
		(3, 3),
		(4, 4),
		(5, 5),
		(6, 6),
		(7, 7),
		(8, 8),
		(9, 9),
		(10, 10),
		(11, 11),
		(12, 12),
		(13, 13),
		(14, 14),
		(15, 15),
		
		)

	PORT3 = (
		(0, 0),
		(1, 1),
		(2, 2),
		(3, 3),
		(4, 4),
		(5, 5),
		(6, 6),
		(7, 7),
		(8, 8),
		(9, 9),
		(10, 10),
		(11, 11),
		(12, 12),
		(13, 13),
		(14, 14),
		(15, 15),
		(16, 16),
		(17, 17),
		(18, 18),
		(19, 19),
		(20, 20),
		(21, 21),
		(22, 22),
		(23, 23),
		(24, 24),
		(25, 25),
		(26, 26),
		(27, 27),
		(28, 28),
		(29, 29),
		(30, 30),
		(31, 31),
		)

	VLAN = (
		(700, 700),
		(701, 701),
		(702, 702),
		(703, 703),
		(704, 704),
		(705, 705),
		(706, 706),
		(707, 707),
		(708, 708),
		(709, 709),
		(710, 710),
		)


	fio = models.CharField('FIO',max_length=100, null=True)
	sn = models.CharField('SN',max_length=100, null=True)
	p1 = models.PositiveSmallIntegerField('PLATA', choices=PORT1, null=True)
	p2 = models.PositiveSmallIntegerField('PORT', choices=PORT2, null=True)
	p3 = models.PositiveSmallIntegerField('ONT', choices=PORT3, null=True)
	vlan = models.PositiveSmallIntegerField('VLAN',default=700 ,choices=VLAN, null=True)
	vaqt = models.DateTimeField(auto_now=True, null=True, blank=True)

	@property
	def serPort(self):
		if self.p1 == 1:
			ser_p  = 0 + self.p2 * 192 + (self.p3*3)
		elif self.p1 == 2:
			ser_p  = 3072 + self.p2 * 192 + (self.p3*3)
		elif self.p1 == 3:
			ser_p  = 6144 + self.p2 * 192 + (self.p3*3)
		elif self.p1 == 4:
			ser_p  = 9216 + self.p2 * 192 + (self.p3*3)
		elif self.p1 == 5:
			ser_p  = 12288 + self.p2 * 192 + (self.p3*3)
		elif self.p1 == 6:
			ser_p  = 15360 + self.p2 * 192 + (self.p3*3)
		elif self.p1 == 7:
	    	 ser_p  = 18432 + self.p2 * 192 + (self.p3*3)  
		elif self.p1 == 8:
			ser_p  = 21504 + self.p2 * 192 + (self.p3*3)
		elif self.p1 == 11:
			ser_p  = 24576 + self.p2 * 96 + (self.p3*3)
		elif self.p1 == 12:
			ser_p  = 26112 + self.p2 * 96 + (self.p3*3)
		elif self.p1 == 13:
			ser_p  = 27648 + self.p2 * 96 + (self.p3*3)
		elif self.p1 == 14:
			ser_p  = 29184 + self.p2 * 96 + (self.p3*3)
		elif self.p1 == 15:
			ser_p  = 30720 + self.p2 * 96 + (self.p3*3)
		elif self.p1 == 16:
			ser_p  = 32256 + self.p2 * 96 + (self.p3*3)
		elif self.p1 == 17:
			ser_p  = 33792 + self.p2 * 96 + (self.p3*3)
		elif self.p1 == 18:
			ser_p  = 35328 + self.p2 * 96 + (self.p3*3)
		elif self.p1 == 19:
			ser_p  = 36864 + self.p2 * 96 + (self.p3*3)
		else:
			ser_p = 0
		

		return ser_p


	def __str__(self):
		return self.fio
