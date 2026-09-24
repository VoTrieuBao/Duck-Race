import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="TRƯỜNG ĐUA VỊT MAY MẮN",
    page_icon="🦆",
    layout="wide"
)

html_code = """
<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<title>TRƯỜNG ĐUA VỊT MAY MẮN</title>
<style>
    * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
    body { background-color: #f4f7fb; color: #333; padding: 20px; display: flex; flex-direction: column; align-items: center; }
    .container { max-width: 900px; width: 100%; }
    h1 { text-align: center; color: #ff8c00; text-shadow: 2px 2px 0px #333, -1px -1px 0 #fff; font-size: 2.2rem; margin-bottom: 20px; text-transform: uppercase; }
    .card { background: white; border-radius: 12px; padding: 20px; box-shadow: 0 4px 15px rgba(0,0,0,0.08); margin-bottom: 20px; border: 1px solid #e1e8ed; }
    label { font-weight: bold; display: block; margin-bottom: 8px; font-size: 1.1rem; color: #2c3e50; }
    textarea { width: 100%; height: 110px; padding: 10px; border: 2px solid #cbd5e1; border-radius: 8px; font-size: 1rem; resize: vertical; outline: none; transition: 0.2s; }
    textarea:focus { border-color: #3b82f6; }
    .btn-group { display: flex; gap: 10px; margin-top: 12px; flex-wrap: wrap; }
    button { padding: 10px 18px; border: none; border-radius: 8px; font-weight: bold; cursor: pointer; font-size: 0.95rem; transition: 0.2s; display: inline-flex; align-items: center; gap: 6px; }
    button:hover { opacity: 0.9; transform: translateY(-1px); }
    .btn-primary { background: #2563eb; color: white; }
    .btn-secondary { background: #e2e8f0; color: #334155; }
    .btn-success { background: #16a34a; color: white; font-size: 1.05rem; }
    .btn-warning { background: #f59e0b; color: white; }
    .track-title { text-align: center; font-size: 1.4rem; font-weight: bold; margin-bottom: 12px; color: #1e293b; }
    .track-container { position: relative; background: linear-gradient(180deg, #38bdf8 0%, #0284c7 100%); border-radius: 12px; border: 4px solid #0284c7; overflow: hidden; padding: 15px 80px 15px 10px; min-height: 220px; box-shadow: inset 0 0 20px rgba(0,0,0,0.15); }
    .lane { position: relative; height: 48px; border-bottom: 2px dashed rgba(255,255,255,0.4); display: flex; align-items: center; }
    .lane:last-child { border-bottom: none; }
    .finish-line { position: absolute; right: 25px; top: 0; bottom: 0; width: 24px; background: repeating-linear-gradient(0deg, #000, #000 12px, #fff 12px, #fff 24px); border-left: 2px solid #fff; border-right: 2px solid #fff; z-index: 2; }
    .finish-banner { position: absolute; right: 5px; top: 5px; background: #dc2626; color: white; font-weight: bold; font-size: 0.75rem; padding: 2px 6px; border-radius: 4px; z-index: 3; text-transform: uppercase; letter-spacing: 1px; }
    .duck { position: absolute; left: 0; width: 42px; height: 42px; transition: left 0.1s linear; z-index: 4; display: flex; flex-direction: column; align-items: center; }
    .duck-nametag { background: rgba(255, 255, 255, 0.95); color: #0f172a; font-weight: bold; font-size: 0.75rem; padding: 1px 6px; border-radius: 10px; white-space: nowrap; box-shadow: 0 2px 4px rgba(0,0,0,0.2); border: 1px solid #94a3b8; margin-bottom: -2px; }
    .duck-svg { width: 32px; height: 32px; filter: drop-shadow(0 2px 3px rgba(0,0,0,0.3)); }
    .controls { display: flex; align-items: center; justify-content: space-between; margin-top: 15px; background: #f8fafc; padding: 12px 20px; border-radius: 8px; border: 1px solid #e2e8f0; flex-wrap: wrap; gap: 10px; }
    .time-input { display: flex; align-items: center; gap: 8px; font-weight: bold; }
    .time-input input { width: 60px; padding: 6px; border: 1px solid #cbd5e1; border-radius: 6px; text-align: center; font-size: 1rem; }
    .modal { display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); z-index: 100; justify-content: center; align-items: center; }
    .modal-content { background: white; padding: 25px; border-radius: 12px; max-width: 450px; width: 90%; text-align: center; box-shadow: 0 10px 25px rgba(0,0,0,0.2); }
    .modal h2 { color: #d97706; margin-bottom: 15px; }
    .winner-list { text-align: left; margin: 15px 0; background: #fef3c7; padding: 12px; border-radius: 8px; border: 1px solid #fde68a; }
    .winner-item { font-size: 1.1rem; padding: 4px 0; font-weight: bold; color: #78350f; }
</style>
</head>
<body>

<div class="container">
    <h1>🦆 TRƯỜNG ĐUA VỊT MAY MẮN 🦆</h1>

    <div class="card">
        <label for="names">NHẬP TÊN ĐUA (Mỗi dòng 1 tên)</label>
        <textarea id="names" placeholder="Nhập danh sách tên ở đây...">Khải&#10;Tùng&#10;Lan&#10;Cường&#10;Minh&#10;Anh</textarea>
        <div class="btn-group">
            <button class="btn-primary" onclick="setupRace()">Xác nhận danh sách</button>
            <button class="btn-secondary" onclick="shuffleNames()">Trộn tên</button>
            <button class="btn-secondary" onclick="useSample()">Sử dụng mẫu</button>
        </div>
    </div>

    <div class="card">
        <div class="track-title">Đường Đua</div>
        <div class="track-container" id="track">
            <div class="finish-banner">FINISH</div>
            <div class="finish-line"></div>
            <!-- Lanes & Ducks injected by JS -->
        </div>

        <div class="controls">
            <div class="time-input">
                <span>⏱ Thời gian (giây):</span>
                <input type="number" id="raceTime" value="10" min="3" max="60">
            </div>
            <div class="btn-group">
                <button class="btn-success" id="startBtn" onclick="startRace()">🚀 BẮT ĐẦU CUỘC ĐUA</button>
                <button class="btn-secondary" onclick="resetRace()">🔄 CHƠI LẠI</button>
            </div>
        </div>
    </div>
</div>

<div class="modal" id="resultModal">
    <div class="modal-content">
        <h2>🏆 KẾT QUẢ CUỘC ĐUA 🏆</h2>
        <div class="winner-list" id="winnerList"></div>
        <button class="btn-warning" onclick="closeModal()">Đóng & Tiếp tục</button>
    </div>
</div>

<script>
    const colors = ['#ef4444', '#3b82f6', '#10b981', '#f59e0b', '#8b5cf6', '#ec4899', '#14b8a6', '#f97316'];
    let ducks = [];
    let isRacing = false;
    let raceInterval = null;

    function getSvgDuck(color) {
        return `<svg class="duck-svg" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M12 36C12 28 20 26 28 26C32 26 36 24 38 20C40 16 44 14 50 16C54 17.5 56 22 52 26C48 30 46 36 46 42C46 50 38 54 28 54C16 54 12 46 12 36Z" fill="${color}"/>
            <circle cx="46" cy="20" r="3" fill="white"/>
            <circle cx="47" cy="20" r="1.5" fill="black"/>
            <path d="M52 22C56 22 60 25 58 28C55 30 51 27 51 25" fill="#f97316"/>
            <path d="M18 38C22 36 28 38 26 44C24 48 18 46 18 38Z" fill="rgba(0,0,0,0.15)"/>
        </svg>`;
    }

    function setupRace() {
        if (isRacing) return;
        const rawNames = document.getElementById('names').value.split('\n');
        const names = rawNames.map(n => n.trim()).filter(n => n.length > 0);
        
        const track = document.getElementById('track');
        track.querySelectorAll('.lane').forEach(e => e.remove());
        ducks = [];

        if (names.length === 0) return;

        names.forEach((name, index) => {
            const lane = document.createElement('div');
            lane.className = 'lane';
            
            const color = colors[index % colors.length];
            const duckEl = document.createElement('div');
            duckEl.className = 'duck';
            duckEl.id = `duck-${index}`;
            duckEl.innerHTML = `
                <div class="duck-nametag">${name}</div>
                ${getSvgDuck(color)}
            `;
            
            lane.appendChild(duckEl);
            track.appendChild(lane);

            ducks.push({
                id: index,
                name: name,
                pos: 0,
                el: duckEl,
                finished: false,
                finishTime: 0
            });
        });
    }

    function shuffleNames() {
        const area = document.getElementById('names');
        const names = area.value.split('\n').map(n => n.trim()).filter(n => n.length > 0);
        for (let i = names.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [names[i], names[j]] = [names[j], names[i]];
        }
        area.value = names.join('\n');
        setupRace();
    }

    function useSample() {
        document.getElementById('names').value = "Khải\nTùng\nLan\nCường\nMinh\nAnh";
        setupRace();
    }

    function startRace() {
        if (isRacing || ducks.length === 0) return;
        
        isRacing = true;
        document.getElementById('startBtn').disabled = true;
        
        const duration = parseFloat(document.getElementById('raceTime').value) * 1000;
        const startTime = Date.now();
        const trackWidth = document.getElementById('track').clientWidth - 130; 
        
        ducks.forEach(d => {
            d.pos = 0;
            d.finished = false;
            d.el.style.left = '0px';
        });

        const finishedDucks = [];

        raceInterval = setInterval(() => {
            const elapsed = Date.now() - startTime;
            let allFinished = true;

            ducks.forEach(d => {
                if (!d.finished) {
                    const speedVariation = Math.random() * 1.8 + 0.2;
                    const progress = Math.min((elapsed / duration) * speedVariation, 1);
                    
                    d.pos += (trackWidth - d.pos) * (0.03 * Math.random() + 0.01);
                    
                    if (d.pos >= trackWidth || elapsed >= duration) {
                        d.pos = trackWidth;
                        d.finished = true;
                        d.finishTime = Date.now() - startTime;
                        finishedDucks.push(d);
                    } else {
                        allFinished = false;
                    }
                    d.el.style.left = `${d.pos}px`;
                }
            });

            if (allFinished || elapsed >= duration + 2000) {
                clearInterval(raceInterval);
                isRacing = false;
                document.getElementById('startBtn').disabled = false;
                
                ducks.forEach(d => {
                    if (!d.finished) {
                        d.pos = trackWidth;
                        d.el.style.left = `${trackWidth}px`;
                        finishedDucks.push(d);
                    }
                });

                showResults(finishedDucks);
            }
        }, 50);
    }

    function resetRace() {
        if (isRacing) clearInterval(raceInterval);
        isRacing = false;
        document.getElementById('startBtn').disabled = false;
        setupRace();
    }

    function showResults(results) {
        const winnerList = document.getElementById('winnerList');
        winnerList.innerHTML = '';
        
        const medals = ['🥇 Hạng 1', '🥈 Hạng 2', '🥉 Hạng 3'];
        results.slice(0, 3).forEach((d, i) => {
            const item = document.createElement('div');
            item.className = 'winner-item';
            item.innerHTML = `${medals[i]}: <strong>${d.name}</strong>`;
            winnerList.appendChild(item);
        });

        document.getElementById('resultModal').style.display = 'flex';
    }

    function closeModal() {
        document.getElementById('resultModal').style.display = 'none';
    }

    // Khởi tạo ban đầu
    window.onload = setupRace;
</script>
</body>
</html>
"""

components.html(html_code, height=850, scrolling=True)
