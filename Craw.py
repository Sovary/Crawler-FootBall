from selenium import webdriver
from os import path,makedirs,environ
import time
import datetime
import re
import random
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb

class Craw:
	
	

	def __init__(self,service=[],flag=0):
		cap = webdriver.DesiredCapabilities.PHANTOMJS
		environ['TZ'] = 'Asia/Bangkok' # change accordingly
		#time.tzset()#unix only
		userA = [
		'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0',
		"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
		"Mozilla/5.0 (Macintosh; U; PPC Mac OS X; fi-fi) AppleWebKit/420+ (KHTML, like Gecko) Safari/419.3",
		"Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-us) AppleWebKit/312.8 (KHTML, like Gecko) Safari/312.6"]
		cap["phantomjs.page.settings.userAgent"] = random.choice(userA)
		cap["phantomjs.page.settings.loadImages"] = False
		#service_args=service_args
		self.driver = webdriver.PhantomJS(desired_capabilities=cap,service_args=service) if flag==0 else webdriver.Chrome(desired_capabilities=cap)
		
	def doGet(self,url):
		self.driver.get(url)

	def cleanTxt(self,txt):
		return ' '.join(txt.split())
		# regex = re.compile(r'[\n\r\t]')
		# return regex.sub(' ', txt)
	def printHtml(self,dom):
		print (html.tostring(dom, encoding='unicode'))

	def screenshot(self,name=str(datetime.datetime.now())+"_webpage.png"):
		directory = "snip"
		if not os.path.exists(directory):
			os.makedirs(directory)
		self.driver.save_screenshot(directory+"/"+name)

	def close(self):
		self.driver.quit()

	

	def open_con(self):
		db = MySQLdb.connect("127.0.0.1","root","pass","db",charset = 'utf8',use_unicode=True )
		return db


	def insert(self,items):
		db = self.open_con()
		cursor = db.cursor()
		sql = """
			INSERT IGNORE INTO jobs(`job_title`,`job_description`,`job_address`,`job_phone_call`,`job_phone_multi`,`job_dead_line`,`job_company_name`,`job_company_logo`,`job_hire_number`,`job_language`,`job_gender`,`job_salary_from`,`job_salary_to`,`job_type`,`job_res`,`job_latitude`,`job_longitude`,`job_contact_name`,`job_email`,`job_site`,`job_url`,`category_id`,`source_id`,`location_id`,`status`,`created_at`,`updated_at`)
			VALUES (%(job_title)s,%(job_description)s,%(job_address)s,%(job_phone_call)s,%(job_phone_multi)s,%(job_dead_line)s,%(job_company_name)s,%(job_company_logo)s,%(job_hire_number)s,%(job_language)s,%(job_gender)s,%(job_salary_from)s,%(job_salary_to)s,%(job_type)s,%(job_res)s,%(job_latitude)s,%(job_longitude)s,%(job_contact_name)s,%(job_email)s,%(job_site)s,%(job_url)s,%(category_id)s,%(source_id)s,%(location_id)s,%(status)s,"""+time.strftime('%Y-%m-%d %H:%M:%S')+""","""+time.strftime('%Y-%m-%d %H:%M:%S')+""")
		"""
		try:
			# cursor.executemany(sql,(data['job_title'],data['job_description'],data['job_address'],data['job_phone_call'],data['job_phone_multi'],data['job_dead_line'],data['job_company_name'],data['job_company_logo'],data['job_hire_number'],data['job_language'],data['job_gender'],data['job_salary'][0],data['job_salary'][1],data['job_type'],data['job_res'],data['job_latitude'],data['job_longitude'],data['job_contact_name'],data['job_email'],data['job_site'],data['job_url'],data['category_id'],data['source_id'],data['location_id'],data['status'],"NOW()","NOW()"))
			cursor.executemany(sql,items)
			db.commit()
		except Exception as e :
			print(e)
			db.rollback()
		db.close()
