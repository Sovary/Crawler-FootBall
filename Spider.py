
import Craw
import sys
import gc
from lxml import html
import time
class Spider(Craw.Craw):
	
	
	__loot = []
	service_args = []
	def __init__(self,url):
		super().__init__(self.service_args)#chrome 1 default phantom 0
		time.sleep(2)
		self.doGet(url)
		self.first_page = html.fromstring(self.driver.page_source)
	#do on list page
	def doSpider(self):
		try:
			polbock = self.first_page.xpath(('//*[@id="tbodds"]/tbody[@class]'))
			
			for i_polblock in range(0,len(polbock)):

				ar_match=[]
				ar_against=[]
				#loop row of one pul
				rowpol = polbock[i_polblock].xpath('//*[@id="tbodds"]/tbody[@class]['+str(i_polblock+1)+']/tr')
				
				
				against=""
				match = polbock[i_polblock].xpath('//*[@id="tbodds"]/tbody[@class]['+str(i_polblock+1)+']/tr[1]/td[2]')[0].text_content().strip()
				

				for i_rowpol in range(0,len(rowpol)):
					#first row
					if i_rowpol == 0 :
						
						against = rowpol[i_rowpol].xpath('//*[@id="tbodds"]/tbody[@class]['+str(i_polblock+1)+']/tr[1]/td[3]')[0].text_content().strip()
						
						f1x2 = rowpol[i_rowpol].xpath('//*[@id="tbodds"]/tbody[@class]['+str(i_polblock+1)+']/tr[1]/td[4]')[0].text_content().strip()
						
						fhandi =""
						
						if len(rowpol[i_rowpol].xpath('//*[@id="tbodds"]/tbody[@class]['+str(i_polblock+1)+']/tr[1]/td[5]/span/a'))>0:

							fhandi = rowpol[i_rowpol].xpath('//*[@id="tbodds"]/tbody[@class]['+str(i_polblock+1)+']/tr[1]/td[5]/span/a')[0].text_content().strip()
						
						fover = rowpol[i_rowpol].xpath('//*[@id="tbodds"]/tbody[@class]['+str(i_polblock+1)+']/tr[1]/td[6]/span/a')[0].text_content().strip()
						
						h1x2 = rowpol[i_rowpol].xpath('//*[@id="tbodds"]/tbody[@class]['+str(i_polblock+1)+']/tr[1]/td[7]')[0].text_content().strip()
						
						hhandi = ""
						
						if(len(rowpol[i_rowpol].xpath('//*[@id="tbodds"]/tbody[@class]['+str(i_polblock+1)+']/tr[1]/td[8]/span/a')) >0):
						
							hhandi = rowpol[i_rowpol].xpath('//*[@id="tbodds"]/tbody[@class]['+str(i_polblock+1)+']/tr[1]/td[8]/span/a')[0].text_content().strip()
						
						hover = ""
						
						if len(rowpol[i_rowpol].xpath('//*[@id="tbodds"]/tbody[@class]['+str(i_polblock+1)+']/tr[1]/td[9]'))>0:

							hover = rowpol[i_rowpol].xpath('//*[@id="tbodds"]/tbody[@class]['+str(i_polblock+1)+']/tr[1]/td[9]')[0].text_content().strip()
						
						ar_against.append({"F1x2":f1x2,"FHandicap":fhandi,"FOverUnder":fover,"H1x2":h1x2,"HHandicap":hhandi,"HOverUnder":hover})

					elif i_rowpol ==1 :
						f1x2 = rowpol[i_rowpol].xpath('//*[@id="tbodds"]/tbody[@class]['+str(i_polblock+1)+']/tr[2]/td[1]')[0].text_content().strip()
						
						fhandi = ""

						if len(rowpol[i_rowpol].xpath('//*[@id="tbodds"]/tbody[@class]['+str(i_polblock+1)+']/tr[2]/td[2]/span/a'))>0:

							fhandi = rowpol[i_rowpol].xpath('//*[@id="tbodds"]/tbody[@class]['+str(i_polblock+1)+']/tr[2]/td[2]/span/a')[0].text_content().strip()
						
						fover = rowpol[i_rowpol].xpath('//*[@id="tbodds"]/tbody[@class]['+str(i_polblock+1)+']/tr[2]/td[3]/span/a')[0].text_content().strip()
						
						h1x2 = rowpol[i_rowpol].xpath('//*[@id="tbodds"]/tbody[@class]['+str(i_polblock+1)+']/tr[2]/td[4]')[0].text_content().strip()
						
						hhandi =""

						if len(rowpol[i_rowpol].xpath('//*[@id="tbodds"]/tbody[@class]['+str(i_polblock+1)+']/tr[2]/td[5]/span/a'))>0:
						
							hhandi = rowpol[i_rowpol].xpath('//*[@id="tbodds"]/tbody[@class]['+str(i_polblock+1)+']/tr[2]/td[5]/span/a')[0].text_content().strip()
						
						hover = ""

						if len(rowpol[i_rowpol].xpath('//*[@id="tbodds"]/tbody[@class]['+str(i_polblock+1)+']/tr[2]/td[6]/span/a'))>0:

							hover = rowpol[i_rowpol].xpath('//*[@id="tbodds"]/tbody[@class]['+str(i_polblock+1)+']/tr[2]/td[6]/span/a')[0].text_content().strip()
					
						ar_against.append({"F1x2":f1x2,"FHandicap":fhandi,"FOverUnder":fover,"H1x2":h1x2,"HHandicap":hhandi,"HOverUnder":hover})

						ar_match.append({"AGAINST":against,"DATA":ar_against})
					else:
						against = rowpol[i_rowpol].xpath('//*[@id="tbodds"]/tbody[@class]['+str(i_polblock+1)+']/tr[3]/td[1]')[0].text_content().strip()
						
						f1x2 = rowpol[i_rowpol].xpath('//*[@id="tbodds"]/tbody[@class]['+str(i_polblock+1)+']/tr[3]/td[2]')[0].text_content().strip()
						
						h1x2 = rowpol[i_rowpol].xpath('//*[@id="tbodds"]/tbody[@class]['+str(i_polblock+1)+']/tr[3]/td[4]')[0].text_content().strip()

						hover = rowpol[i_rowpol].xpath('//*[@id="tbodds"]/tbody[@class]['+str(i_polblock+1)+']/tr[3]/td[6]/a')[0].text_content().strip()
						ar_against=[]
						ar_against.append({"F1x2":f1x2,"FHandicap":"","FOverUnder":"","H1x2":h1x2,"HHandicap":"","HOverUnder":hover})

						ar_match.append({"AGAINST":against,"DATA":ar_against})
				#added each block pul
				self.__loot.append({"MATCH":match,"DATA":ar_match})
				#gc.collect()

				if(i_polblock ==5):
					break
				
			print (self.__loot)

		except Exception as e:
			print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
		finally:
			self.close()
	


spi = Spider("http://s2.7m.hk/default_en.shtml")
spi.doSpider()
spi.close()



# template =[
#   {
#     "MATCH": "NOR D1",
#     "DATA": [
#       {
#         "AGAINST": "Aalesund FKSogndal",
#         "DATA": [
#           {
#             "F1x2": "1001",
#             "FHandicap": "Regular",
#             "FOverUnder": "",
#             "H1x2": "1001",
#             "HHandicap": "Regular",
#             "HOverUnder": ""
#           },
#           {
#             "F1x2": "1001",
#             "FHandicap": "Regular",
#             "FOverUnder": "",
#             "H1x2": "1001",
#             "HHandicap": "Regular",
#             "HOverUnder": ""
#           }
#         ]
#       },
#       {
#         "AGAINST": "Draw",
#         "DATA": [
#           {
#             "F1x2": "1001",
#             "FHandicap": "Regular",
#             "FOverUnder": "",
#             "H1x2": "1001",
#             "HHandicap": "Regular",
#             "HOverUnder": ""
#           }
#         ]
#       }
#     ]
#   }
# ]