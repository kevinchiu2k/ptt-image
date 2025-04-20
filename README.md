# ppt-image
## 本程式主要是將KoreaDrama和KoreaStart透過程式把它下載過來

1. 利用下列命令取得uv.exe工具
> python -m pip install uv

2. 利用下面命令建立工作目錄
> projectuv init project

3. 下載python的第三方套件
> uv add requests bs4 time

4. 使用下面命令編譯程式，這支程式為抓取對象是"KoreaDrama" 和 "KoreaStart" 的所有圖片
> uv run ../koreadrama.py

