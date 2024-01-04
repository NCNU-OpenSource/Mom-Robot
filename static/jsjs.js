let mainTimer;
let extraTimer;

let mainTimeLeft = 5; // 10分钟转换为秒
let extraTimeLeft = 15; // 15秒

function startTimers() {
    // 主计时器，每秒减一
    mainTimer = setInterval(function() {
        mainTimeLeft--;
        const mainMinutes = Math.floor(mainTimeLeft / 60);
        const mainSeconds = mainTimeLeft % 60;
        document.getElementById('main-timer-display').innerText = `${mainMinutes}:${mainSeconds.toString().padStart(2, '0')}`;

        if (mainTimeLeft <= 0) {
            clearInterval(mainTimer);
            document.getElementById('main-timer-display').innerText = '去喝水啦';
            document.getElementById('reset-timer-button').style.display = 'block';
            playSound(); // 播放声音

        }
    }, 1000);

    // 额外计时器，每秒减一
    extraTimer = setInterval(function() {
        extraTimeLeft--;
        const extraMinutes = Math.floor(extraTimeLeft / 60);
        const extraSeconds = extraTimeLeft % 60;
        document.getElementById('extra-timer-display').innerText = `${extraMinutes}:${extraSeconds.toString().padStart(2, '0')}`;

        if (extraTimeLeft <= 0) {
            clearInterval(extraTimer);
            document.getElementById('extra-timer-display').innerText = '偵測已開始！';
            playSound(); // 播放声音
        }
    }, 1000);
}

function playSound() {
    let ting = new Audio('/Users/tingshiho/Desktop/python/rpi/ting.mp3');
    ting.play();
    console.log("playSound function called");
    document.getElementById('play-sound-button').addEventListener('click', playSound);
}

// 其他代码保持不变...

function resetTimers() {
    mainTimeLeft = 5; // 重置主计时器为10分钟
    extraTimeLeft = 15; // 重置额外计时器为15秒
    document.getElementById('reset-timer-button').style.display = 'none';
    startTimers();

    // 播放音频文件（请替换为你的音频文件路径）
    
}

// 页面加载时启动计时器
document.addEventListener('DOMContentLoaded', function() {
    startTimers();
});

// 为重置按钮添加事件监听器
document.getElementById('reset-timer-button').addEventListener('click', resetTimers);
