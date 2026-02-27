const express = require('express');
const bodyParser = require('body-parser');

const app = express();
const PORT = 3000;

// Middleware
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// ===== Home Page =====
app.get('/', (req, res) => {
  res.send(`
    <!DOCTYPE html>
    <html>
    <head>
      <title>Node Server</title>
      <style>
        body {
          font-family: Arial, sans-serif;
          background: #111;
          color: #eee;
          text-align: center;
          padding-top: 50px;
        }
        input, button {
          padding: 10px;
          font-size: 16px;
        }
        button {
          cursor: pointer;
          background: #00c853;
          border: none;
          color: white;
        }
        .box {
          margin-top: 20px;
          padding: 20px;
          background: #222;
          display: inline-block;
          border-radius: 8px;
        }
      </style>
    </head>
    <body>
      <h1>🚀 Server Running</h1>
      <p>Time: ${new Date().toLocaleString()}</p>

      <div class="box">
        <h3>Send Message to API</h3>
        <input id="msg" placeholder="Type something..." />
        <button onclick="sendMsg()">Send</button>
        <p id="response"></p>
      </div>

      <script>
        async function sendMsg() {
          const msg = document.getElementById('msg').value;
          const res = await fetch('/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ msg })
          });
          const data = await res.json();
          document.getElementById('response').innerText = data.response;
        }
      </script>
    </body>
    </html>
  `);
});

// ===== Health Check =====
app.get('/health', (req, res) => {
  res.json({
    status: 'ok',
    uptime: process.uptime(),
    timestamp: Date.now()
  });
});

// ===== Chat API =====
app.post('/chat', (req, res) => {
  const msg = req.body.msg || '';
  res.json({
    response: `AI received: ${msg}`
  });
});

// ===== 404 Handler =====
app.use((req, res) => {
  res.status(404).json({ error: 'Not Found' });
});

// ===== Start Server =====
app.listen(PORT, '0.0.0.0', () => {
  console.log('LISTEN_OK', process.pid, 'NODE_ENV=', process.env.NODE_ENV);
});
