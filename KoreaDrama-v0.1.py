import os
from time import sleep
import requests
from bs4 import BeautifulSoup

headers = {
			'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
		}

start_num = 6685
n=20

try:
	start_num = int(input('從第幾號開始 (6685)？'))
# n = int(input('n = (20) '))
except Exception as e:
	print(f'Error: {e}')

url1 = []
for count in range(1,3):
	url0 = 'https://disp.cc/b/KoreaDrama?pn=' + str(start_num -count*n)    # 一次取n筆
	web = requests.get(url0, headers = headers)
	soup = BeautifulSoup(web.text, 'html.parser')
	# print(web.text)
	span_tags = soup.find_all('span', class_="L34 nowrap listTitle")
	for a_tag in span_tags:
		img = a_tag.find('a')['href']       # 文章的網址
		title = a_tag.a.span.text           # 文章的標題
		print(title)
		print('https://disp.cc' + img)

		url_set = ('https://disp.cc' + img, title, start_num)
		url1.append(url_set)
		start_num = start_num - 1
		
print(url1,end='\n')   # 全部記錄在一個list中
# exit()

#-----------------------

no=1
for url, title, num in url1:   # 注意set的排序
	print()
	print(f'--> ({no}) {title} [{num}]')

	path = '../image/KoreaDrama/' + title
	os.makedirs(path, exist_ok=True)  # 建立資料夾
	print("😊 Folder %s created!" % path)
		
	web = requests.get(url, headers = headers) 
	soup = BeautifulSoup(web.text, 'html.parser')

	div_tags = soup.find_all('div', class_='img')
	for img_tag in div_tags:
		# print(img_tag)
		file = img_tag.img.get('data-src')      # 取得每一張照片網址
		print(file)             # 打印出來
		
		try:
			r = requests.get(file, headers= headers, timeout= 3)
			rcode = r.status_code          # 取得每一張照片的狀態碼
		
			if rcode == 200:
				print(f' <Status Code = 200 & OK>')
				fx = file.split('/')[-1]
				# print(fx)
	
				fn = path + '/' + fx        # 檔名
				with open(fn , 'wb') as f:        # 存檔工作
					f.write(requests.get(file, headers=headers).content)    # 寫入照片
			else:
				print(f' [error status code = {rcode}]')
				
		except Exception as e:
			print(f'(X)⏱️ Error: {e}')

no=no+1         
sleep(3)



