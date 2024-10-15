import "./SubComponents.css";
import { PacmanLoader } from "react-spinners";

function Loading() {

  return (
    <main>
      <div className="center-in-main">
        <PacmanLoader
          color="#95d2b3"
          loading
          margin={0}
          size={45}
          speedMultiplier={1}
        />
      </div>
    </main>
  );
}

export default Loading;
