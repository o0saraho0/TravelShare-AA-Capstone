import { FaGithub } from "react-icons/fa";
import { FaLinkedin } from "react-icons/fa";
import "./Footer.css";

function Footer() {
  return (
    <footer>
      <h3>Meet the developer</h3>

      <div className="footer-content">
        <div className="sarah-content inline">
          <div className="sarah-pic">
            <img src="/images/Sarah.JPG" alt="Sarah" />
          </div>
          <div className="sarah-info">
            <p>Sarah Jiang</p>
            <div className="sarah-contact">
              <a href="https://github.com/o0saraho0">
                <FaGithub />
              </a>
              <a href="https://www.linkedin.com/in/yue-jiang-ab016278">
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
    </footer>
  );
}

export default Footer;
