import { useEffect, useState } from "react";
import { fetchVideos } from "./api";
import VideoTable from "./components/VideoTable";

export default function App() {
  const [videos, setVideos] = useState([]);

  useEffect(() => {
    fetchVideos().then(setVideos);
  }, []);

  return (
    <div>
      <h1>Video Dashboard</h1>
      <VideoTable videos={videos} />
    </div>
  );
}