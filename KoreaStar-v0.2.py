import os
from time import sleep
import requests
from bs4 import BeautifulSoup

headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
        }

start_num = 13479   # 目前文章的起始編號
n=20	# 每次取20筆文章

while True:
	start_num = input('從文章第幾號開始 (13479)？')
	type = input('是否確定？(y/N)')
	if type == 'y':
		start_num=int(start_num)  
		break
	elif type == 'n':
		continue

while True:
	i = input('以n=1等於20筆文章，請輸入n？')
	type = input('是否確定？(y/N)')
	if type == 'y':
		i=int(i)
		break
	elif type == 'n':
		continue


url1 = []
for count in range(1,i+1):
	url0 = 'https://disp.cc/b/KoreaStar?pn=' + str(start_num -count*n)    # 一次取n筆
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
		# url1.append('https://disp.cc' + img)        # 加上前面網址，形成一筆資料
		url1.append(url_set)
		start_num = start_num - 1
			
	print(url1, end='\n')   # 全部記錄在一個list中	
# exit()

#-----------------------

no=1
for url, title, num in url1:   # 注意 set 的排序
	print()
	print(f'-> ({no}) {title} [{num}]')
	path = '../photo/KoreaStar/' + title
	try:
		os.makedirs(path, exist_ok=True)  # 建立資料夾
		print("😊 目錄 [%s] 建立!" % path)
	except Exception as e:
		print(f'(X)⏱️ Error: {e}')
    
	web = requests.get(url, headers = headers)  
	soup = BeautifulSoup(web.text, 'html.parser')

	div_tags = soup.find_all('div', class_='img')
	for img_tag in div_tags:
		# print(img_tag)
		file = img_tag.img.get('data-src')      # 取得每一張照片網址
		print(file)             # 打印出來
		# continue
		try:
			r = requests.get(file, headers= headers, timeout= 3)
			rcode = r.status_code          # 取得每一張照片的狀態碼
	
			if rcode == 200:
				# print(f' <Status Code = 200 & OK>')
				fx = file.split('/')[-1]
				# print(fx)

				fn = path + '/' + fx        # 檔名
				with open(fn , 'wb') as f:        # 存檔工作
						f.write(requests.get(file, headers=headers).content)    # 寫入照片
			else:
				print(f' [Error status code = {rcode}]')
					
		except Exception as e:
			print(f'(X)⏱️ Error: {e}')

no=no+1         
sleep(3)
    
    
