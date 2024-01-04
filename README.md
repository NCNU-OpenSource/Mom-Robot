# 老媽機器人 - LSA 第五組期末專題
老媽機器人是一款創新的應用程式，旨在提醒使用者保持良好的坐姿和定期喝水，即使身處遠離家鄉的南投。這款應用透過Webcam偵測使用者的行為，並在必要時播放錄製的母親聲音來提醒使用者。  
![1704275895419](https://github.com/yuzher33/LSA/assets/151426386/c14fb4d7-cb85-4ac4-9b22-6377ea2bc006)

# 功能
坐姿檢測: 利用Webcam偵測使用者的坐姿，並透過媽媽的聲音提醒糾正坐姿。
坐姿監控網頁: 透過Flask建立的網頁，展示Webcam捕捉的影像，並即時展示坐姿狀態和播放聲音的條件。

# 技術和方法
* MediaPipe: 用於人體關節辨識，並利用OpenCV畫出關節之間的連線。*
* Time Module: 設定定時提醒。*
* Flask: 建立網頁以顯示坐姿狀態。*
* subprocess Popen:用於播放音樂*

# Mediapipe的關節點標示
![image](https://github.com/yuzher33/LSA/assets/148021569/0121f494-3c08-4e64-a0f9-3bd8a14be182)
# 安裝和使用
![image](https://github.com/yuzher33/LSA/assets/151426386/367c9d21-7dd0-4316-ac56-d99c16facbe9)

## 安裝指南

在樹莓派上安裝 `opencv-python`, `mediapipe`,`flask`需要執行以下步驟。這些庫將使你能夠執行包括圖像處理和人體姿態識別在內的多種功能。

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
   
3.**開啓樹莓派的終端機，輸入以下指令創建一個虛擬環境**：
   
      python3 -m venv myenv   
   
4.**啓動及推出虛擬環境**：
   
    source myenv/bin/activate
   
      deactivate（退出)    
   
4.**創建requirements.txt檔，並將所需的工具(套件)寫在requirements.txt檔裏面**：
   
absl-py==2.0.0  
attrs==23.2.0  
blinker==1.7.0  
cffi==1.16.0  
click==8.1.7  
contourpy==1.2.0  
cycler==0.12.1  
Flask==3.0.0  
flatbuffers==20181003210633  
fonttools==4.47.0  
itsdangerous==2.1.2  
Jinja2==3.1.2  
kiwisolver==1.4.5  
MarkupSafe==2.1.3  
matplotlib==3.8.2  
mediapipe==0.10.9  
numpy==1.26.3  
opencv-contrib-python==4.9.0.80  
opencv-python==4.9.0.80  
packaging==23.2  
pillow==10.2.0  
pip==23.0.1  
protobuf==3.20.3  
pycparser==2.21  
pygame==2.5.2  
pyparsing==3.1.1  
python-dateutil==2.8.2  
setuptools==66.1.1  
six==1.16.0  
sounddevice==0.4.6  
Werkzeug==3.0.1        

5.**執行以下指令，安裝所需套件**：
   
    pip install -r requirements.txt    
   
### 傳輸程式碼到樹莓派

為了運行 MediaPipe 應用，你需要將 你寫好的mediapipe程式碼（我的文件是叫app.py)`app.py` 文件傳輸到樹莓派。以下是通過 SSH 傳輸文件的步驟：
**記得要在樹莓派的虛擬環境下**
1. **準備你的 `app.py` 文件**。

   確保你的 `app.py` 包含所有必要的 MediaPipe 程式碼並且在你的電腦上是可訪問的，把app.py文件放到隨便一個目錄(請記得你的目錄,謝謝)

2. **開啟終端或命令提示字元**。

   在你的本地機器上開啟終端（Linux 或 macOS）或命令提示字元/PowerShell（Windows）。

3. **使用 SCP 傳輸文件**。

   使用 SCP 命令將 `app.py` 傳輸到樹莓派。你將需要替換 `<USERNAME>` 為你的樹莓派的用戶名，`<RASPBERRY_PI_IP>` 為樹莓派的 IP 地址，並且指定正確的文件路徑：

   ```bash
   scp /path/to/app.py <USERNAME>@<RASPBERRY_PI_IP>:/path/to/destination

### 通過 SSH 連接到樹莓派

   **樹莓派連的網路和你電腦連的網路要一樣，這樣ssh才連得上！！！！！！！**
   
   1.要運行樹莓派上的 `app.py` 文件，請先通過 SSH 連接到你的樹莓派：

  
      ssh <USERNAME>@<RASPBERRY_PI_IP>


   2.導航到文件存放的目錄,連接到樹莓派之後，使用 cd 命令轉到存放 app.py 的目錄：

  
      cd /path/to/destination


   3.運行 app.py,在樹莓派的終端中，運行以下命令來啟動你的應用：

  
      python3 app.py

# 遇到的困難  
**安裝問題，無法如期在樹莓派上安裝套件(必須在樹莓派上架設虛擬環境)**  
*樹莓派記憶體不足，導致無法正確偵測(延遲超過10秒)*（我們寫的程式跑起來會佔670mb)

# 簡報連結
https://www.canva.com/design/DAF40kCBqEE/DS0blEr1bFYMjQuJBbWNww/edit

# 團隊分工
蔡秉霖:撰寫mediapipe程式碼與測試環境  
定世荷:撰寫mediapipe程式碼與測試環境  
廖宇哲:製作簡報，設定樹莓派，撰寫github  
張傑然:製作簡報，設定樹莓派，下載套件  
