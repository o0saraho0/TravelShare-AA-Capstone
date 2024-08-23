import { NavLink } from "react-router-dom";
import ProfileButton from "./ProfileButton";
import "./Navigation.css";

function Navigation() {
  // const navigate = useNavigate();
  return (
    <nav className="inline">
      <div className="home-link">
        <NavLink to="/">
        <img src="/images/hello.png" alt="logo" />
        </NavLink>
      </div>
      
      <div className="inline nav-categories">
        <div>City Exploration</div>
        <div>Nature Escapes</div>
        <div>Road Trips</div>
      </div>
      
      <ul>
        <li>
          <ProfileButton />
        </li>
      </ul>
    </nav>
  );
}

export default Navigation;
