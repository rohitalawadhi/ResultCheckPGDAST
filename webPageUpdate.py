import time
from mechanize import Browser
from win10toast import ToastNotifier
br = Browser()
while True:
	url = "https://gradecard.ignou.ac.in/gradecardR/Result.asp"
	br.open(url)
	br.select_form(name="FRMResult")
	br['Program'] = ["PGDAST              "]
	br["eno"] = 'xxxxxxxxx'
	response1 = br.submit()
	bytecode = response1.read()
	htmlstr = bytecode.decode()
	if str(htmlstr).find('MST005') == -1 or str(htmlstr).find("MSTE001") == -1 or str(htmlstr).find("MSTE002") == -1  :
		time.sleep(60)
		continue
	else:
		toaster = ToastNotifier()
		toaster.show_toast("notification",
                   "Result out",
                   duration=100000)
		break
