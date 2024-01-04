# 老媽機器人 - LSA 第五組期末專題
# 動機發想 Motivation
老媽機器人是一款創新的應用程式，旨在提醒使用者保持良好的坐姿和定期喝水，即使身處遠離家鄉的南投。這款應用透過Webcam偵測使用者的行為，並在必要時播放錄製的母親聲音來提醒使用者。  
![1704275895419](https://github.com/yuzher33/LSA/assets/151426386/c14fb4d7-cb85-4ac4-9b22-6377ea2bc006)

# 功能 Function
坐姿檢測: 利用Webcam偵測使用者的坐姿，並透過媽媽的聲音提醒糾正坐姿。
坐姿監控網頁: 透過Flask建立的網頁，展示Webcam捕捉的影像，並即時展示坐姿狀態和播放聲音的條件。

# 使用設備
* Respberry pi 3 (From TA NT$ 0)
* WebCam*1(from 張晏誠學長 NT$ 0)
  
# 技術和方法
* MediaPipe: 用於人體關節辨識，並利用OpenCV畫出關節之間的連線。
* Opencv:用於處理圖像相關程式
* Time Module: 設定定時提醒。
* Flask: 建立網頁以顯示坐姿狀態。
* subprocess Popen:用於播放音樂。

# Mediapipe的關節點標示
![image](https://github.com/yuzher33/LSA/assets/148021569/0121f494-3c08-4e64-a0f9-3bd8a14be182)
# 安裝和使用
![image](https://github.com/yuzher33/LSA/assets/151426386/367c9d21-7dd0-4316-ac56-d99c16facbe9)

# Usage 
## 使用gitclone(Ubuntu用戶)
### 將git下載下來之後解壓縮，接著指到解壓縮後檔案的路徑
```bash
cd path/to/ur_file
```
### 下載requirements.txt
```bash
pip install -r requirements.txt
```
### 執行主程式
```bash
python3 app.py
```
## 樹梅派用戶

### 前提條件
因爲我們其他方法裝不了，系統環境限制了在外部管理的環境中進行安裝，所以我們在樹莓派裏面創建了
一個虛擬環境
### 安裝步驟

請按照以下步驟在您的樹莓派上安裝 Python 3 和 pip：

1. **開啟樹莓派終端**。
   
   打開您的樹莓派終端，準備輸入安裝命令。

2. **更新系統包列表**：

   在終端中輸入以下命令來更新您的系統包列表和現有的軟件包。
   
   ```bash
   sudo apt-get update
   sudo apt-get upgrade
   ```
   
3.**開啓樹莓派的終端機，輸入以下指令創建一個虛擬環境**：
   ```bash
   python3 -m venv myenv   
   ```   
4.**啓動虛擬環境**：
   啟動:
   ```bash
   source myenv/bin/activate
   ```
5.**檔案下載在別台主機**:
在別台主機使用gitclone下載壓縮檔後解壓縮到想要的路徑

6.**將所需文件scp到自己想要的路徑**:
在樹梅派上用scp將檔案載到自己想要的路徑(要在虛擬環境中scp)
```bash
scp  目標用戶名@目標ip:/目標檔案的路徑/檔名  /path/you/want/to/download
```

7.**進入檔案所在位置**
```bash
cd /path/to/your_file
```
   
8.**下載requirements.txt**
```bash
pip install -r requirements.txt
```
9.**執行主程式**
```bash
python3 app.py
```

* 若您想要退出虛擬環境，則輸入以下指令:
```bash
deactivate（退出)    
```

# UI
無論是樹梅派用戶或是Ubuntu用戶，在執行 `app.py`後，會顯示網頁在哪個`ipdress:埠口`上，接著去瀏覽器輸入網址後即可連到我們的網頁


# 遇到的困難  
**安裝問題，無法如期在樹莓派上安裝套件(必須在樹莓派上架設虛擬環境)**  
*樹莓派記憶體不足，導致無法正確偵測(延遲超過10秒)*（我們寫的程式跑起來會佔670mb)

# 簡報連結
https://www.canva.com/design/DAF40kCBqEE/DS0blEr1bFYMjQuJBbWNww/edit

# 團隊分工
* 110213015蔡秉霖
  * 撰寫mediapipe程式碼
  * 樹梅派測試環境
* 110213055定世荷
  * 撰寫mediapipe程式碼
  * 網頁程式碼編寫
* 110213034廖宇哲
  * 製作簡報
  * 設定樹莓派
  * 撰寫github  
* 110213065張傑然
  * 設定樹莓派
  * 下載套件  
  * 製作簡報

# Refrences
* https://www.youtube.com/watch?v=06TE_U21FK4 *
* Chatgpt

# 特別感謝
感謝 **吳梓睿** 助教熬兩天夜跟我們一起debug
感謝 **陳柏瑋** 助教願意借我們Ubuntu作業系統的筆電以及提供我們各種套件的建議
感謝 **張晏誠** 借我們Webcam <3
感謝 **王詠平** 助教幫助我們網頁上的問題
