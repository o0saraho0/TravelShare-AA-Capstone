import { NavLink } from "react-router-dom";
import ProfileButton from "./ProfileButton";
import "./Navigation.css";

function Navigation() {
  return (
    <nav>
      <div className="nav-max inline">
        <div className="home-link">
          <NavLink to="/">
            <img src="/images/hello.png" alt="logo" />
          </NavLink>
        </div>

        <div className="inline nav-categories">
          <NavLink to="/itineraries/category/1">City Exploration</NavLink>
          <NavLink to="/itineraries/category/2">Nature Escapes</NavLink>
          <NavLink to="/itineraries/category/3">Road Trips</NavLink>
        </div>

        <ul>
          <li>
            <ProfileButton />
          </li>
        </ul>
      </div>
    </nav>
  );
}

export default Navigation;
