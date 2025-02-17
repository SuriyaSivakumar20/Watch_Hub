import React, { useState, useEffect } from "react";

function Chat({ socket, room }) {
  const [messages, setMessages] = useState([]);
  const [msg, setMsg] = useState("");

  useEffect(() => {
    socket.on("receive_message", (data) => {
      setMessages((prev) => [...prev, data.message]);
    });
  }, [socket]);

  const sendMessage = () => {
    socket.emit("chat_message", { room, message: msg });
    setMsg("");
  };

  return (
    <div>
      <div>{messages.map((m, i) => <p key={i}>{m}</p>)}</div>
      <input value={msg} onChange={(e) => setMsg(e.target.value)} />
      <button onClick={sendMessage}>Send</button>
    </div>
  );
}

export default Chat;
