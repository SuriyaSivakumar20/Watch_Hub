# 🎬 Watch Party Hub - Movie Nights with Friends!

**A seamless, login-free watch party experience! Create a link, share it, and enjoy movies with friends via live video, audio, and chat.**

---

## 🚀 Features

✅ **Instant Access** - No login required, just a link!  
✅ **Movie Synchronization** - The host controls playback.  
✅ **Live Video & Audio Chat** - WebRTC-based real-time interaction.  
✅ **Text Chat & Voice Messages** - Chat while watching.  
✅ **Screen Sharing** - Stream your own movies.  
✅ **Auto-Expiring Links** - Ensures privacy after the session ends.  
✅ **Reactions Feature** - Express yourself while watching!  
✅ **Minimal UI & Dark Mode** - Simple and user-friendly.  
✅ **YouTube/Twitch Streaming** - Watch videos together.  

---

## 🎥 Animated Demo

![Watch Party Hub Demo](https://your-demo-gif-url.com)

---

## 🏗️ Project Structure
```
watch-party-hub/
│── backend/                 # Node.js (Express + WebRTC + Socket.io backend)
│   ├── server.js           # Main backend server
│   ├── package.json        # Backend dependencies
│   ├── config/             # Server configurations
│   ├── routes/             # API routes
│   ├── public/             # Static files
│   └── utils/              # Utility functions
│
│── frontend/                # React.js frontend (TailwindCSS + Plyr.js)
│   ├── src/
│   │   ├── components/     # UI components (Chat, Video, Controls)
│   │   ├── App.js          # Main React component
│   │   ├── index.js        # React entry point
│   │   ├── styles.css      # Custom styling
│   │   ├── utils/          # Helper functions
│   ├── public/             # Frontend static assets
│   ├── package.json        # Frontend dependencies
│   └── .env                # Environment variables
│
└── README.md                # Project documentation
```

---

## 🛠️ Tech Stack

### **Frontend**  
[![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)](https://react.dev/)  
[![TailwindCSS](https://img.shields.io/badge/TailwindCSS-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white)](https://tailwindcss.com/)  
[![Plyr.js](https://img.shields.io/badge/Plyr.js-FF5733?style=for-the-badge&logo=javascript&logoColor=white)](https://github.com/sampotts/plyr)  

### **Backend**  
[![Node.js](https://img.shields.io/badge/Node.js-43853D?style=for-the-badge&logo=node.js&logoColor=white)](https://nodejs.org/)  
[![Express.js](https://img.shields.io/badge/Express.js-000000?style=for-the-badge&logo=express&logoColor=white)](https://expressjs.com/)  
[![Socket.io](https://img.shields.io/badge/Socket.io-010101?style=for-the-badge&logo=socket.io&logoColor=white)](https://socket.io/)  
[![WebRTC](https://img.shields.io/badge/WebRTC-008000?style=for-the-badge&logo=webrtc&logoColor=white)](https://webrtc.org/)  

---

## ⚙️ How It Works

1. **User creates a watch party link.**  
2. **Friends join the party via the link.**  
3. **Host starts the movie (either uploaded or streamed).**  
4. **Everyone watches together with synchronized playback.**  
5. **Users can chat, send voice messages, and react!**  
6. **Once the session ends, the link expires.**  

---

## 🚀 Quick Start

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/SuriyaSivakumar20/watch-party-hub.git
cd watch-party-hub
```

### **2️⃣ Backend Setup**
```sh
cd backend
npm install
node server.js
```

### **3️⃣ Frontend Setup**
```sh
cd ../frontend
npm install
npm start
```

### **4️⃣ Open in Browser**
```
http://localhost:3000
```

---

## 📜 License

This project is licensed under the **MIT License**. Feel free to modify and use it!

---

### 📧 **Need Help?**
**Developer:** [Suriya Sivakumar](https://www.linkedin.com/in/suriya-sivakumar-483735258)  
**GitHub:** [SuriyaSivakumar20](https://github.com/SuriyaSivakumar20)  
**Email:** [suriyasivakumar08@gmail.com](mailto:suriyasivakumar08@gmail.com)  

Happy Streaming! 🎥🍿

