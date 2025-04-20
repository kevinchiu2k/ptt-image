# ppt-image
## 本程式主要是將KoreaDrama和KoreaStart透過程式把它下載過來

1. 利用下列命令取得uv.exe工具
> python -m pip install uv

2. 利用下面命令建立工作目錄project
> uv init project

3. 用下面命令進入project工作目錄
> cd project

4. 下載python的第三方套件，同時建立虛擬環境(.venv)
> uv add requests bs4

5. 使用下面命令編譯程式，這支程式是為抓取"KoreaDrama" 和 "KoreaStart" 所有圖片
> uv run ../koreadrama.py



