# 老媽機器人 - LSA 第五組期末專題
老媽機器人是一款創新的應用程式，旨在提醒使用者保持良好的坐姿和定期喝水，即使身處遠離家鄉的南投。這款應用透過Webcam偵測使用者的行為，並在必要時播放錄製的母親聲音來提醒使用者。

# 功能
坐姿檢測: 利用Webcam偵測使用者的坐姿，並透過媽媽的聲音提醒糾正坐姿。
喝水提醒: 每隔10分鐘或偵測到使用者一段時間內沒有喝水動作時，播放媽媽的聲音提醒喝水。
坐姿監控網頁: 透過Flask建立的網頁，展示Webcam捕捉的影像，並即時展示坐姿狀態和播放聲音的條件。

# 技術和方法
MediaPipe: 用於人體關節辨識，並利用OpenCV畫出關節之間的連線。
NumPy: 計算關節的角度，判斷坐姿是否正確。
Time Module: 設定定時提醒。
TensorFlow (選擇性): 如果時間允許，將用於訓練一個識別喝水動作的模型。
Flask: 建立網頁以顯示坐姿狀態。
Python 音訊播放庫: 用於播放錄製的媽媽聲音。

# 安裝和使用
![image](https://github.com/yuzher33/LSA/assets/151426386/5f071930-e238-4f0c-9990-4df45e9b1770)
## 安裝指南

在樹莓派上安裝 `opencv-python`, `mediapipe`, `numpy`, 和 `pygame` 需要執行以下步驟。這些庫將使你能夠執行包括圖像處理和人體姿態識別在內的多種功能。

### 前提條件

確保你的樹莓派的系統是最新的並且已經安裝了 Python。本指南假設你使用的是 Python 3。

### 安裝步驟

請按照以下步驟在您的樹莓派上安裝 Python 3 和 pip：

1. **開啟樹莓派終端**。
   
   打開您的樹莓派終端，準備輸入安裝命令。

2. **更新系統包列表**：

   在終端中輸入以下命令來更新您的系統包列表和現有的軟件包。
   
   ```bash
   sudo apt-get update
   sudo apt-get upgrade  

3.**安裝 Python 3**：
   
    sudo apt-get install python3    
   
4.**安裝 PIP**：
   
    sudo apt-get install python3-pip    

5.**安裝 opencv-python**：
   
    pip3 install opencv-python    

6.**安裝 mediapipe**：
   
    pip3 install mediapipe    

7.**安裝 numpy**：
   
    pip3 install numpy    

8.**安裝 pygame**：
   
    pip3 install pygame    

### 傳輸程式碼到樹莓派

為了運行 MediaPipe 應用，你需要將 你寫好的mediapipe程式碼（我的文件是叫app.py)`app.py` 文件傳輸到樹莓派。以下是通過 SSH 傳輸文件的步驟：

1. **準備你的 `app.py` 文件**。

   確保你的 `app.py` 包含所有必要的 MediaPipe 程式碼並且在你的電腦上是可訪問的。

2. **開啟終端或命令提示字元**。

   在你的本地機器上開啟終端（Linux 或 macOS）或命令提示字元/PowerShell（Windows）。

3. **使用 SCP 傳輸文件**。

   使用 SCP 命令將 `app.py` 傳輸到樹莓派。你將需要替換 `<USERNAME>` 為你的樹莓派的用戶名，`<RASPBERRY_PI_IP>` 為樹莓派的 IP 地址，並且指定正確的文件路徑：

   ```bash
   scp /path/to/app.py <USERNAME>@<RASPBERRY_PI_IP>:/path/to/destination

### 通過 SSH 連接到樹莓派

要運行樹莓派上的 `app.py` 文件，請先通過 SSH 連接到你的樹莓派：

   ssh <USERNAME>@<RASPBERRY_PI_IP>  
   
# 團隊成員  
廖宇哲  
定世荷  
蔡秉霖  
張傑然
