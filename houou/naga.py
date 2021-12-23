import chromedriver_binary
import re
import json
from selenium import webdriver

class Naga:
	def __init__(self, url):
		# scrape "pred" variable from javascript
		options = webdriver.ChromeOptions()
		options.add_argument('--headless')
		driver = webdriver.Chrome(options=options)
		driver.get(url)
		self.pred_raw = driver.execute_script('return pred')
		driver.quit()
		self.url = url

	def organize(self):
		pred_str = json.dumps(self.pred_raw)

		pred_str1 = pred_str.replace('"actor":', '\n"actor":')
		pred_str2 = pred_str1.replace('"real_dahai":', '\n"read_dahai":')
		pred_pattern = re.compile(r'"real_dahai": "(.*?)", "pred_dahai": "(.*?)"')
		pred_str3 = pred_pattern.sub(r'\n"real_dahai": "\1", "pred_dahai": "\2"\n', pred_str2)
		pred_str4 = pred_str3.replace('"', '')
		return pred_str4

if __name__ == "__main__":
	#testurl = 'https://naga.dmv.nico/htmls/2a42a9763cc316d8b39a9a3f37d6afaaa233b3ac050bb44099cc68913d31284fv2_0_0.html?tw=3'
	testurl = 'https://www.google.com'
	#testurl = '999'

	test = Naga(testurl)

	print(test.organize(), file=open('pred7.txt', mode='w'))