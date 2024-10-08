import { useState } from "react";
import { useDispatch } from "react-redux";
import { useNavigate } from "react-router-dom";
import { thunkLogin } from "../../redux/session";
import { useModal } from "../../context/Modal";
import SignupFormModal from "../SignupFormModal/SignupFormModal";
import OpenModalMenuItem from "../Navigation/OpenModalMenuItem";
import "./LoginForm.css";

function LoginFormModal({ text, closeMenu }) {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [errors, setErrors] = useState({});
  const { closeModal } = useModal();

  const handleSubmit = async (e) => {
    e.preventDefault();

    const serverResponse = await dispatch(
      thunkLogin({
        email,
        password,
      })
    );

    if (serverResponse) {
      setErrors(serverResponse);
    } else {
      closeModal();
      if (closeMenu) closeMenu();
      navigate("/");
    }
  };

  const handleDemo = async () => {
    const demoUser = {
      email: "sarah.jiang@example.com",
      password: "password",
    };
    const serverResponse = await dispatch(thunkLogin(demoUser));

    if (serverResponse) {
      setErrors(serverResponse);
    } else {
      closeModal();
      if (closeMenu) closeMenu();
      navigate("/");
    }
  };

  return (
    <>
      {text && <div className="signed-out-popoff">{text}</div>}
      <h1>Log In</h1>
      <form onSubmit={handleSubmit}>
        <label>
          Email
          <input
            type="text"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        </label>
        {errors.email && <p className="error">{errors.email}</p>}
        <label>
          Password
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </label>
        {errors.password && <p className="error">{errors.password}</p>}
        <button type="submit">Log In</button>
        <button type="button" onClick={handleDemo}>
          Demo User
        </button>
      </form>
      <div className="register">
        <p>—————— New to HelloWorld? ——————</p>
        <button className="cursor">
          <OpenModalMenuItem
            itemText="Register"
            modalComponent={<SignupFormModal closeMenu={closeMenu} />}
          />
        </button>
      </div>
    </>
  );
}

export default LoginFormModal;
