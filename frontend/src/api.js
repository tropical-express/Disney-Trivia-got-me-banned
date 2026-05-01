export async function fetchVideos() {
  const res = await fetch("http://localhost:8000/videos");
  return res.json();
}