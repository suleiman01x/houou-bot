import chromedriver_binary
import re
import json
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--headless')

driver = webdriver.Chrome(options=options)
driver.get('https://naga.dmv.nico/htmls/2a42a9763cc316d8b39a9a3f37d6afaaa233b3ac050bb44099cc68913d31284fv2_0_0.html?tw=3')

pred_raw = driver.execute_script('return pred')
pred_str = json.dumps(pred_raw)

pred_str1 = pred_str.replace('"actor":', '\n"actor":')
pred_str2 = pred_str1.replace('"real_dahai":', '\n"read_dahai":')

pred_pattern = re.compile(r'"real_dahai": "(.*?)", "pred_dahai": "(.*?)"')
pred_str3 = pred_pattern.sub(r'\n"real_dahai": "\1", "pred_dahai": "\2"\n', pred_str2)

pred_str4 = pred_str3.replace('"', '')

print(pred_str4, file=open('pred5.txt', mode='w'))

driver.quit()