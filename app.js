import React, { useState, useEffect } from "react";
import io from "socket.io-client";
import VideoPlayer from "./VideoPlayer";
import Chat from "./Chat";
import WebRTC from "./WebRTC";

const socket = io("http://localhost:5000");

function App() {
  const [room, setRoom] = useState("");
  const [joined, setJoined] = useState(false);

  const joinRoom = async () => {
    const res = await fetch("http://localhost:5000/create-room");
    const data = await res.json();
    setRoom(data.room_id);
    setJoined(true);
    socket.emit("join", { room: data.room_id });
  };

  return (
    <div>
      {!joined ? (
        <button onClick={joinRoom}>Create Room</button>
      ) : (
        <>
          <h2>Room ID: {room}</h2>
          <VideoPlayer socket={socket} room={room} />
          <Chat socket={socket} room={room} />
          <WebRTC room={room} />
        </>
      )}
    </div>
  );
}

export default App;
