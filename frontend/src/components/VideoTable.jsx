export default function VideoTable({ videos }) {
  return (
    <div>
      {videos.map(v => (
        <div key={v.video_id}>
          <img src={v.thumbnail} width="200" />
          <h3>{v.title}</h3>
          <p>{v.channel}</p>
        </div>
      ))}
    </div>
  );
}