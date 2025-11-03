<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Object Detection & Counting — Demo</title>
  <meta name="description" content="Streamlit + YOLOv8: Image & Webcam object detection and counting" />

  <style>
    :root{
      --bg:#0f1724;
      --card:#0b1220;
      --accent:#06b6d4;
      --muted:#94a3b8;
      --white:#e6eef6;
      --glass: rgba(255,255,255,0.03);
      --radius:12px;
      font-family: Inter, ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial;
    }
    html,body{height:100%; margin:0; background:linear-gradient(180deg,#07122a 0%, #041222 100%); color:var(--white); -webkit-font-smoothing:antialiased;}
    .container{max-width:1100px;margin:36px auto;padding:28px;}
    .hero{
      display:flex;gap:24px;align-items:center;
      background:linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01));
      border-radius:var(--radius);padding:28px;box-shadow:0 6px 30px rgba(2,6,23,0.6);
    }
    .logo{
      width:92px;height:92px;border-radius:14px;background:linear-gradient(135deg,var(--accent),#7c3aed);
      display:flex;align-items:center;justify-content:center;font-weight:700;font-size:28px;color:#031024;
      box-shadow:0 6px 18px rgba(3,10,25,0.5);
    }
    h1{margin:0;font-size:28px}
    p.lead{margin:6px 0 0;color:var(--muted);max-width:68%}
    .badges{display:flex;gap:10px;margin-top:12px;flex-wrap:wrap}
    .badge{background:var(--glass);padding:8px 12px;border-radius:999px;color:var(--muted);font-size:13px}

    .grid{display:grid;grid-template-columns:1fr 340px;gap:20px;margin-top:24px}
    .card{background:var(--card);padding:18px;border-radius:12px;box-shadow:0 8px 24px rgba(2,6,23,0.6)}
    .features{display:grid;grid-template-columns:repeat(2,1fr);gap:12px}
    .feature{display:flex;gap:12px;align-items:flex-start}
    .dot{width:42px;height:42px;border-radius:10px;background:linear-gradient(180deg,#0b1220 0,#071226 100%);display:flex;align-items:center;justify-content:center;border:1px solid rgba(255,255,255,0.03)}
    .dot svg{opacity:0.9}
    ul.check{margin:8px 0 0;padding-left:18px;color:var(--muted)}

    .screenshot-grid{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:12px}
    .screenshot{border-radius:8px;overflow:hidden;border:1px solid rgba(255,255,255,0.03);background:#000;height:220px;display:flex;align-items:center;justify-content:center;color:var(--muted)}
    pre.code{background:#031124;padding:16px;border-radius:8px;overflow:auto;color:#cbd5e1;font-size:13px;border:1px solid rgba(255,255,255,0.03)}
    .file-structure{background:linear-gradient(180deg,#071727, #05121a);padding:12px;border-radius:8px;color:var(--muted);font-family:monospace}

    footer{margin-top:22px;color:var(--muted);font-size:13px;display:flex;justify-content:space-between;align-items:center}
    a.btn{
      display:inline-block;padding:10px 14px;border-radius:10px;background:linear-gradient(90deg,var(--accent),#7c3aed);color:#021120;text-decoration:none;font-weight:600;margin-top:8px;
      box-shadow:0 10px 28px rgba(6,182,212,0.08);
    }
    @media (max-width:900px){
      .grid{grid-template-columns:1fr}
      .hero p.lead{max-width:100%}
      .screenshot{height:160px}
    }
  </style>
</head>
<body>
  <div class="container">
    <div class="hero">
      <div class="logo">OD</div>
      <div style="flex:1">
        <h1>Object Detection & Counting</h1>
        <div class="badges">
          <div class="badge">Streamlit</div>
          <div class="badge">YOLOv8</div>
          <div class="badge">OpenCV</div>
          <div class="badge">Python</div>
        </div>
        <p class="lead">Simple, local app to detect and count objects from an image or live webcam feed. Highlights detected objects while blacking out the rest for focused visualization.</p>
        <div style="margin-top:12px">
          <a class="btn" href="#usage">Quick Start</a>
          <a class="btn" href="#features" style="background:transparent;border:1px solid rgba(255,255,255,0.06);color:var(--white);margin-left:10px">Features</a>
        </div>
      </div>
    </div>

    <div class="grid">
      <div class="card">
        <h3 id="features">Features</h3>
        <div class="features" style="margin-top:12px">
          <div>
            <div class="feature"><div class="dot">📷</div><div><strong>Image Upload</strong><div style="color:var(--muted)">Upload and detect objects, side-by-side original + highlighted view</div></div></div>
            <div class="feature" style="margin-top:8px"><div class="dot">🎥</div><div><strong>Live Webcam</strong><div style="color:var(--muted)">Real-time detection and counting with easy start/stop controls</div></div></div>
            <div class="feature" style="margin-top:8px"><div class="dot">🎯</div><div><strong>Select Class</strong><div style="color:var(--muted)">Count specific classes (e.g., person, car)</div></div></div>
          </div>
          <div>
            <div class="feature"><div class="dot">✨</div><div><strong>Highlight Mode</strong><div style="color:var(--muted)">Detected objects remain in color; rest of image blacked out for clarity</div></div></div>
            <div class="feature" style="margin-top:8px"><div class="dot">⚡</div><div><strong>Fast</strong><div style="color:var(--muted)">Use yolov8n for CPU speed; yolov8m/x for accuracy</div></div></div>
            <div class="feature" style="margin-top:8px"><div class="dot">🗂️</div><div><strong>Clean Structure</strong><div style="color:var(--muted)">Modular code for easy upgrades and model swapping</div></div></div>
          </div>
        </div>

        <h3 style="margin-top:18px">Demo Screenshots</h3>
        <div class="screenshot-grid">
          <div class="screenshot">Original image with bounding boxes<br><small style="color:var(--muted)">add screenshot at assets/original_sample.jpg</small></div>
          <div class="screenshot">Highlighted detected objects<br><small style="color:var(--muted)">add screenshot at assets/highlighted_sample.jpg</small></div>
        </div>

        <h3 style="margin-top:18px" id="usage">Quick start</h3>
        <p style="color:var(--muted);margin-top:6px">Run locally after installing dependencies.</p>
        <pre class="code"># clone
git clone https://github.com/yourusername/Object-Detection-and-Object-Counting
cd Object-Detection-and-Object-Counting

# create venv (recommended)
python -m venv venv
source venv/bin/activate   # mac / linux
venv\Scripts\activate      # windows

# install
pip install -r requirements.txt

# run
streamlit run app.py
</pre>

        <h3 style="margin-top:12px">File structure</h3>
        <div class="file-structure">
<pre>
Object-Detection-and-Object-Counting/
├─ app.py
├─ detect_image.py
├─ utils/
│  └─ draw_utils.py
├─ models/
│  └─ yolov8m.pt
├─ requirements.txt
└─ README.md
</pre>
        </div>
      </div>

      <div>
        <div class="card" style="margin-bottom:16px">
          <h3>Installation (requirements)</h3>
          <ul style="color:var(--muted);margin-top:8px">
            <li>Python 3.9+</li>
            <li>Ultralytics (YOLOv8)</li>
            <li>OpenCV</li>
            <li>Streamlit</li>
          </ul>
          <pre class="code">streamlit
ultralytics
opencv-python
numpy
torch</pre>
        </div>

        <div class="card" style="margin-bottom:16px">
          <h3>How it works</h3>
          <p style="color:var(--muted);margin-top:8px">App reads an image or webcam frame → runs it through YOLOv8 → draws boxes and builds a mask for detected regions → displays original and highlighted outputs side-by-side.</p>
        </div>

        <div class="card">
          <h3>Author & Contact</h3>
          <p style="color:var(--muted)">Bibek — AI / Computer Vision</p>
          <p style="color:var(--muted)">GitHub: <a href="https://github.com/yourusername" style="color:var(--accent)">yourusername</a></p>
          <p style="color:var(--muted)">Email: <a href="mailto:your-email@example.com" style="color:var(--accent)">your-email@example.com</a></p>
        </div>
      </div>
    </div>

    <footer>
      <div>© <strong>Object Detection & Counting</strong> • Built with Streamlit + YOLOv8</div>
      <div style="color:var(--muted)">Made by Bibek</div>
    </footer>
  </div>
</body>
</html>
