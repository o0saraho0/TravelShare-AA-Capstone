import { FaGithub } from "react-icons/fa";
import { FaLinkedin } from "react-icons/fa";
import "./Footer.css";

function Footer() {
  return (
    <footer>
      <div className="footer-max">
        <h3>Meet the developer</h3>

        <div className="footer-content">
          <div className="sarah-content inline">
            <div className="sarah-pic">
              <a href="https://portfolio-sarah-jiang.netlify.app/">
                <img src="/images/profile_Sarah.JPG" alt="Sarah" />
              </a>
            </div>
            <div className="sarah-info">
              <p>Sarah Jiang</p>
              <div className="sarah-contact">
                <a href="https://github.com/o0saraho0">
                  <FaGithub />
                </a>
                <a href="https://www.linkedin.com/in/sarah-yue-jiang">
                  <FaLinkedin />
                </a>
              </div>
            </div>
          </div>
          <div className="app-intro">
            <p>
              HelloWorld is a travel planning application inspired by{" "}
              <a href="https://wanderlog.com/home">Wanderlog</a>
            </p>
            <p>
              Developed by Sarah as her App Academy coding bootcamp capstone
              project
            </p>
          </div>
        </div>
      </div>
    </footer>
  );
}

export default Footer;
