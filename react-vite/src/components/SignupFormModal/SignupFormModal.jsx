import { useState } from "react";
import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import { thunkSignup } from "../../redux/session";
import "./SignupForm.css";

function SignupFormModal() {
  const dispatch = useDispatch();
  const [email, setEmail] = useState("");
  const [username, setUsername] = useState("");
  const [first_name, setFirstName] = useState("");
  const [last_name, setLastName] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [errors, setErrors] = useState({});
  const { closeModal } = useModal();

  const handleSubmit = async (e) => {
    e.preventDefault();
    const newErrors = {};

    if (!/\S+@\S+\.\S+/.test(email)) newErrors.email = "Please enter a valid email address.";
    if (username.length < 4) newErrors.username = "Username must be at least 4 characters.";
    if (password.length < 6) newErrors.password = "Password must be at least 6 characters.";
    if (password !== confirmPassword) {
      return setErrors({
        confirmPassword:
          "Confirm Password field must be the same as the Password field",
      });
    }

    if (Object.keys(newErrors).length > 0) return setErrors(newErrors);

    const serverResponse = await dispatch(
      thunkSignup({
        email,
        first_name,
        last_name,
        username,
        password,
      })
    );

    if (serverResponse) {
      setErrors(serverResponse);
    } else {
      closeModal();
    }
  };

  return (
    <>
      <h1>Create your account</h1>
      <form onSubmit={handleSubmit}>
        <label>
          First Name
          <input
            type="text"
            value={first_name}
            onChange={(e) => setFirstName(e.target.value)}
            required
          />
        </label>

        <label>
        Last Name
        <input
          type="text"
          value={last_name}
          onChange={(e) => setLastName(e.target.value)}
          required
        />
        </label>

        <label>
        Username
          <input
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
          />
        </label>
        {errors.username && <p className="error">{errors.username}</p>}

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


        <label>
        Confirm Password
        <input
          type="password"
          value={confirmPassword}
          onChange={(e) => setConfirmPassword(e.target.value)}
          required
          className={errors.password ? "error" : ""}
        />
        </label>
        {errors.confirmPassword && <p className="error">{errors.confirmPassword}</p>}

        <button type="submit">Register</button>
      </form>

    </>
  );
}

export default SignupFormModal;
