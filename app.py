from mimetypes import init
from turtle import back
from flask import Flask, render_template, Response,Request, jsonify
import cv2
import mediapipe as mp
import subprocess
#from playsound import playsound
from threading import Thread
app = Flask(__name__)
#def play_music():
    #playsound('/home/lab103/Downloads/rpi2/chung.mp3')
#pygame.init()
#class AudioPlayer:
    #def __init__(self):
        #self.current_process = None

    #def play(self, sound_file):
        # 检查是否有其他音频正在播放
        #if self.current_process is not None and self.current_process.poll() is None:
            #raise PlaybackInProgressError("音频正在播放中")
def play_music(file_path):
    player = 'mpg321'
    process = subprocess.Popen([player, file_path])
    return process
def generate_frames():
    cap = cv2.VideoCapture(0)
    mp_drawing = mp.solutions.drawing_utils
    mp_pose = mp.solutions.pose
    in_back =0
    in_head =0
    T_F = None
    frame_count = 0
    global frame_count_back
    global frame_count_head
    global frame_count_both
    frame_count_back = 0
    frame_count_head = 0
    frame_count_both = 0
    music_playing = False
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            ret, frame = cap.read()
            #print(f"Read frame successful: {ret}")
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False
            results = pose.process(image)
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            frame_count += 1
            time = 450 - frame_count
            if(time) == 0:
                in_back = -100*(shoulder_y-hip_y)
                in_head = -100*(nose_y-shoulder_y)
            
            try:
                landmarks = results.pose_landmarks.landmark
                shoulder_y=landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y
                hip_y=landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y
                backyyy=-100*(shoulder_y-hip_y)
                nose_y = landmarks[mp_pose.PoseLandmark.NOSE.value].y
                headyyy = -100*(nose_y-shoulder_y)
                #print(backyyy)
                if backyyy < ((in_back)*0.98) and headyyy > ((in_head)*0.9):
                    T_F = 'backnono'
                    if(frame_count_back%150 ==0):
                        music_process = play_music("/home/lab103/Downloads/rpi2/chung.mp3")
                    frame_count_back += 1
                    #player = AudioPlayer()
                    #player.play("home/lab103/Downloads/rpi2/chung.mp3")
                    #should_play_music = True
                    #if should_play_music and not music_playing:
                       # music_file = '/home/lab103/Downloads/rpi2/chung.mp3'
                       # command = ['mpg321',music_file]
                       # subprocess.Popen(command)
                    #music.playing = True
                    #music_thread = Thread(target = play_music)
                    #music_thread.start()
                    #pygame.mixer.music.load('/home/lab103/Downloads/rpi2/chung.mp3')
                    #pygmae.mixer.music.play()
                    #if pygame.mixer.music.get_busy():
                        #pygame.time.Clock().tick(10)
                elif headyyy < ((in_head)*0.9) and backyyy > ((in_back)*0.98):
                    T_F = 'necknono'
                    if(frame_count_head%150 ==0):
                        music_process = play_music("/home/lab103/Downloads/rpi2/turtle.mp3")
                    frame_count_head += 1
                    #player.play_song("/home/lab103/Downloads/rpi2/turtle.mp3")
                    #sound1 = pygame.mixer.Sound("turtle.mp3")
                    #sound1.play()

                elif backyyy < ((in_back)*0.98) and headyyy < ((in_head)*0.9):
                    T_F = 'both nono'
                    if(frame_count_both%150 ==0):
                        music_process = play_music("/home/lab103/Downloads/rpi2/both.mp3")
                    frame_count_both += 1
                    #player.play_song("/home/lab103/Downloads/rpi2/both.mp3")
                    #sound2 = pygame.mixer.Sound("both.mp3")
                    #sound2.play()

                else:   
                    T_F = 'good'
                
                """
                if (backyyy<=50 or headyyy<=55):
                    
                    if backyyy>=45 and headyyy<30:
                        pygame.mixer.music.play(if(frame_count_back%150 ==0):
                        music_process = play_music("/home/lab103/Downloads/rpi2/turtle.mp3")
                    frame_count_head += 1)
                        if pygame.mixer.music.get_busy():
                            pygame.time.Clock().tick(10)
                        T_F = "necknono"
                    
                    if backyyy<50 and headyyy>=45:
                        T_F = "backnono"
                    elif backyyy<50 and headyyy<=55:
                        T_F="bothnono"
                    else:
                        T_F ="good"
                """   
            
            except:
                pass
        
            cv2.rectangle(image, (0, 0), (1000, 73), (1, 180, 104), -1)
            cv2.putText(image, 'REPS', (15, 12), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)

            cv2.putText(image, 'T/F', (550, 12), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
            cv2.putText(image, T_F, (485, 60), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 2, cv2.LINE_AA)
            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                    mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2), 
                                    mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2))               
            
            ret, buffer = cv2.imencode('.jpg', image)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
