import React, { useEffect, useRef } from "react";
import ReactPlayer from "react-player";

function VideoPlayer({ socket, room }) {
  const playerRef = useRef(null);

  useEffect(() => {
    socket.on("update_video", (data) => {
      playerRef.current.seekTo(data.time);
    });
  }, [socket]);

  const handlePlay = () => {
    socket.emit("sync_video", { room, time: playerRef.current.getCurrentTime() });
  };

  return (
    <ReactPlayer
      ref={playerRef}
      url="https://www.example.com/movie.mp4"
      controls
      onPlay={handlePlay}
    />
  );
}

export default VideoPlayer;
