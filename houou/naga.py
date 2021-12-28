import re
import requests

class Naga:
	def __init__(self, url):
		# scrape "pred" variable from javascript
		self.url = url
		self.response = requests.get(url)

	def organize(self):
		pred_str = self.response.text

		pred_str1 = pred_str.replace('"actor":', '\n"actor":')
		pred_str2 = pred_str1.replace('"real_dahai":', '\n"read_dahai":')

		pred_pattern1 = re.compile(r'"real_dahai": "(.*?)", "pred_dahai": "(.*?)"')
		pred_str3 = pred_pattern1.sub(r'\n"real_dahai": "\1", "pred_dahai": "\2"\n', pred_str2)

		pred_pattern2 = re.compile(r'^.*DOCTYPE html.*\n')
		pred_str4 = pred_pattern2.sub(r'', pred_str3)

		pred_str4 = pred_str4.replace('"', '')
		return pred_str4

if __name__ == "__main__":
	testurl = 'https://naga.dmv.nico/htmls/2a42a9763cc316d8b39a9a3f37d6afaaa233b3ac050bb44099cc68913d31284fv2_0_0.html?tw=3'
	#testurl = 'https://www.google.com'
	#testurl = '999'

	test = Naga(testurl)

	print(test.organize(), file=open('pred7.txt', mode='w'))