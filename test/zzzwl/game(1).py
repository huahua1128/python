#Werewolves of Miller's Hollow
# 3坏人  5平民  2警察
# 10个人分别 编号为： N0 -- N9



# 警察类
class Police:
	def __init__(self, code, name, age):
		self.code = code		# 代号
		self.name = name		# 姓名
		self.age  = age			# 年龄
		self.type = 'police'	# 类别

	def shoot(self, person, list):	
		if person in list :
			print("%s是平民！！！ ----> %s不能开枪" %(person, self.name))
		else :
			print("警察 " + self.name + "----> 对 %s 开枪了" %person)
		
	def identify(self):
		print("---------------------------------------------------------------\n"+
				self.name + " 请指认你要杀的人：")
		res = input()
		self.kill = res
	
# 坏人类
class BadEgg:
	def __init__(self, code, name, age):
		self.code = code		# 代号
		self.name = name		# 姓名
		self.age  = age			# 年龄
		self.type = 'badegg'	# 类别
		self.kill = '0'
	
	def rob_bank(self) :
		print(self.name + "----> 抢银行去了\n")
	
	def steal(self) :
		print(self.name + "----> 偷东西去了\n")
	
	def shoot(self, person) :	
		print("坏人 " + self.name + "----> 对 %s 开枪了" %person)
		
	def identify(self, obj) :
		print("坏人 " + self.name + "----> 指认了： " + obj + "\n")
	
	def choose(self):
		print("---------------------------------------------------------------\n"+
				self.name + " 请选择你要做的事：")
		res = input()
		if res == 'M0' :
			self.rob_bank()
		elif res == 'M1' :
			self.steal()
		else :
			self.kill = res
			self.identify(self.kill)

	
# 平民类
class People:
	def __init__(self, code, name, age):
		self.code = code		# 代号
		self.name = name		# 姓名
		self.age  = age			# 年龄
		self.type = 'people'	# 类别
		self.kill = '0'

	def shoot(self, person):	
		print("平民 " + self.name + "----> 对 %s 开枪了" %person)
		
	def identify(self):
		print("---------------------------------------------------------------\n"+
				self.name + " 请指认你要杀的人：")
		res = input()
		self.kill = res
		
#检查各角色情况，判断游戏是否结束		
def game_over(badegg, people, police) :
	#确认剩余人员：
	if (len(badegg) == 0) :
		print("恭喜： 警察、平民 胜利啦！！！！")
		return 0
	if (len(people) == 0 or len(police) == 0) :
		print("很遗憾： 警察、平民 输啦！！！！")			
		return 0
		
		
##1 创建游戏角色：
N0 = BadEgg("N0", "pitt", 30)
N1 = BadEgg("N1", "河畔", 31)
N2 = BadEgg("N2", "海绵", 31)

N3 = People("N3", "花花", 22)
N4 = People("N4", "七月", 24)
N5 = People("N5", "晴天", 26)
N6 = People("N6", "简爱", 28)
N7 = People("N7", "阿牛", 20)

N8 = Police("N8", "挖矿", 40)
N9 = Police("N9", "月亮", 35)

##2 创建不同类游戏角色列表	
badegg = ['N0', 'N1', 'N2']
people = ['N3', 'N4', 'N5', 'N6', 'N7']
police = ['N8', 'N9']

##3 游戏开始
round = 0
while 1:
	round += 1
	print("@@@@@@@@@@@@@@>> 第 %d 轮 <<@@@@@@@@@@@@@@" %(round))
	
	#0.1 -------------------------------------------------------------------------坏人
	print(">>>>>>>>>>>>>>>>>>>坏人可选择以下事项，输入对应编号即可：\n"
			"\tM0 : 抢银行\n"
			"\tM1 : 偷东西\n"
			"\t"+ str(people) + str(police) +": 指认，杀人\n"
			"===============================================================")
	tmp_list = []
	for item in badegg:
		tmp_obj = eval(item)
		tmp_obj.choose()
		if tmp_obj.kill != '0' :
			tmp_list.append(tmp_obj.kill)
	
	person_out = "" #存最终应该杀的人
	if len(tmp_list) == 3 :
		for item in tmp_list:
			if tmp_list.count(item) >= 2 : 
				person_out = item
				break
	elif len(tmp_list) == 2 :
		if (tmp_list[0] == tmp_list[1]) :
			person_out = tmp_list[0]
	elif len(tmp_list) == 1 :	
		person_out = tmp_list[0]
		
	if person_out != "" : #平局 person_out为空
		for item in badegg:
			tmp_obj = eval(item)
			if tmp_obj.kill == person_out :
				tmp_obj.shoot(person_out)
				
		if person_out in police : 	#是警察
			police.remove(person_out)
			print("警察 " + person_out + " 这轮被坏人杀掉了！！！")
			if 0 == game_over(badegg, people, police) :
				break
		else :						#其余的是平民
			people.remove(person_out)
			print("平民 " + person_out + " 这轮被坏人杀掉了！！！")
			if 0 == game_over(badegg, people, police) :
				break
	else :
		print("哈哈，平局！ 无人牺牲！！！！！")
			
	print() #打印一个空行

	#0.2 -------------------------------------------------------------------------平民
	print(">>>>>>>>>>>>>>>>>>>平民可选择以下事项，输入对应编号即可：\n"
			"\t"+ str(badegg) + str(police) +": 指认，杀人\n"
			"===============================================================")
	tmp_list = []
	for item in people:
		tmp_obj = eval(item)
		tmp_obj.identify()
		if tmp_obj.kill != '0' :
			tmp_list.append(tmp_obj.kill)
	
	print(tmp_list)
	
	person_out = "" #存最终应该杀的人
	if len(tmp_list) == 5 :
		tmp_count = 0
		tmp_buf = ""
		for item in tmp_list:
			if tmp_list.count(item) > 2 : 
				person_out = item
				break
			if tmp_list.count(item) == 2 :
				tmp_buf = item
			if tmp_list.count(item) == 1 :
				tmp_count += 1
		if tmp_count == 3 :
			person_out = tmp_buf
	elif len(tmp_list) == 4 :
		for item in tmp_list:
			if tmp_list.count(item) == 3 : 
				person_out = item
				break
	elif len(tmp_list) == 3 :
		for item in tmp_list:
			if tmp_list.count(item) >= 2 : 
				person_out = item
				break	
	elif len(tmp_list) == 2 :
		if tmp_list[0] == tmp_list[1] :
			person_out = tmp_list[0]
	elif len(tmp_list) == 1	:	
		person_out = tmp_list[0]	
		
	if person_out != "" : #平局 person_out为空
		for item in people:
			tmp_obj = eval(item)
			if tmp_obj.kill == person_out :
				tmp_obj.shoot(person_out)
				
		if person_out in police : 	#是警察
			police.remove(person_out)
			print("警察 " + person_out + " 这轮被平民杀掉了！！！")
			if 0 == game_over(badegg, people, police) :
				break
		else :						#其余的是坏人
			badegg.remove(person_out)
			print("坏人 " + person_out + " 这轮被平民杀掉了！！！")
			if 0 == game_over(badegg, people, police) :
				break
	else :
		print("哈哈，平局！ 无人牺牲！！！！！")
		
	print() #打印一个空行
	
	#0.3 -------------------------------------------------------------------------警察
	print(">>>>>>>>>>>>>>>>>>>警察可选择以下事项，输入对应编号即可：\n"
			"\t"+ str(badegg) + str(people) +": 指认，杀人\n"
			"===============================================================")
	tmp_list = []
	for item in police:
		tmp_obj = eval(item)
		tmp_obj.identify()
		if (tmp_obj.kill != '0') :
			tmp_list.append(tmp_obj.kill)
	
	person_out = "" #存最终应该杀的人
	if len(tmp_list) == 2 :
		if tmp_list[0] == tmp_list[1] :
			person_out = tmp_list[0]
	elif len(tmp_list) == 1 :	
		person_out = tmp_list[0]
		
	if person_out != "" : #平局 person_out为空
		for item in police:
			tmp_obj = eval(item)
			if tmp_obj.kill == person_out :
				tmp_obj.shoot(person_out, people)
				
		if person_out in people :	#不能杀平民
			print("！！！ 警察不能杀平民， 无效！！！")
		else :						#其余的是坏人
			badegg.remove(person_out)
			print("坏人 " + person_out + " 这轮被警察杀掉了！！！")
			if 0 == game_over(badegg, people, police) :
				break
	else :
		print("哈哈，平局！ 无人牺牲！！！！！")
		
	print() #打印一个空行
	

		
		
		
		
		
		