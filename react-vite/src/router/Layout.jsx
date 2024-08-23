import { useEffect, useState } from "react";
import { Outlet, useLocation, useParams, useNavigate } from "react-router-dom";
import { useDispatch } from "react-redux";
import { ModalProvider, Modal } from "../context/Modal";
import { thunkAuthenticate } from "../redux/session"
import Navigation from "../components/Navigation/Navigation";

export default function Layout() {
  const dispatch = useDispatch();
  const location = useLocation();
  const navigate = useNavigate();
  const [isLoaded, setIsLoaded] = useState(false);

  const {itineraryId} = useParams();
  
  useEffect(() => {
    dispatch(thunkAuthenticate()).then(() => setIsLoaded(true));
  }, [dispatch]);

  const pathsWithoutNavigation = [`/itineraries/${itineraryId}`, `/itineraries/${itineraryId}/activities`];

  const showNavigation = !pathsWithoutNavigation.some(path => location.pathname.includes(path));

  return (
    <>
      <ModalProvider>
        {showNavigation? <Navigation />: 
        <div className="home-link" style={{ position: "absolute", zIndex: 1, margin: "20px 50px"}} onClick={() => navigate("/")}>
        <img src="/images/hello.png" alt="logo" />
        </div>}
        {isLoaded && <Outlet />}
        <Modal />
      </ModalProvider>
    </>
  );
}
