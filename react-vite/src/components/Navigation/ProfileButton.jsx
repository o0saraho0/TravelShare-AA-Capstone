import { useState, useEffect, useRef } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useNavigate } from "react-router-dom";
import { thunkLogout } from "../../redux/session";
import OpenModalMenuItem from "./OpenModalMenuItem";
import LoginFormModal from "../LoginFormModal";

function ProfileButton() {
  const dispatch = useDispatch();
  const navigate = useNavigate();

  const [showMenu, setShowMenu] = useState(false);
  const user = useSelector((store) => store.session.user);
  const ulRef = useRef();

  const toggleMenu = (e) => {
    e.stopPropagation(); // Keep from bubbling up to document and triggering closeMenu
    setShowMenu(!showMenu);
  };

  useEffect(() => {
    if (!showMenu) return;

    const closeMenu = (e) => {
      if (ulRef.current && !ulRef.current.contains(e.target)) {
        setShowMenu(false);
      }
    };

    document.addEventListener("click", closeMenu);

    return () => document.removeEventListener("click", closeMenu);
  }, [showMenu]);

  const closeMenu = () => setShowMenu(false);

  const logout = async (e) => {
    e.preventDefault();
    await dispatch(thunkLogout());
    closeMenu();
    navigate("/");
  };

  return (
    <div className="profile-wrapper">
      <div className="parent-container">
        <div onClick={toggleMenu}>
          {user ? (
            <>
              <img
                src={user.profile_url}
                alt="Profile_URL"
                className="profile-image"
              />
            </>
          ) : (
            <OpenModalMenuItem
              itemText="Sign in"
              onItemClick={closeMenu}
              modalComponent={<LoginFormModal />}
            />
          )}
        </div>
        {showMenu && (
          <div>
            {user ? (
              <div ref={ulRef} className="profile-dropdown">
                <div className="unclickable">
                  <p>{user.username}</p>
                  <p>{user.email}</p>
                </div>
                <div className="clickable">
                  <p
                    onClick={() => {
                      navigate("/itineraries/current");
                      closeMenu;
                    }}
                  >
                    Manage Itineraries
                  </p>
                  <p
                    onClick={() => {
                      navigate("/collections/current");
                      closeMenu;
                    }}
                  >
                    Your Collections
                  </p>
                  <p onClick={logout}>Log Out</p>
                </div>
              </div>
            ) : null}
          </div>
        )}
      </div>
    </div>
  );
}

export default ProfileButton;
