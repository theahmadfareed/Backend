import React, { useRef, useState } from "react";
import emailjs from "@emailjs/browser";
import { FaGithub, FaLinkedin, FaTwitter, FaReddit } from "react-icons/fa";
import { SiFiverr } from "react-icons/si";
import { toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
import "./style.css"; // Import your CSS file

const Contact = () => {
  const formRef = useRef();
  const [form, setForm] = useState({
    user_name: "",
    user_email: "",
    user_subject: "",
    user_message: "",
  });

  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    const { target } = e;
    const { name, value } = target;

    setForm({
      ...form,
      [name]: value,
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    setLoading(true);

    emailjs
      .send(
        `service_qa6nqeo`,
        `template_f3fbirq`,
        {
          user_name: form.user_name,
          user_email: form.user_email,
          user_subject: form.user_subject,
          user_message: form.user_message,
        },
        `FnE1paE1eAfiokfEA`
      )
      .then(
        () => {
          setLoading(false);
          toast.success("Thank you. I will get back to you as soon as possible.", {
            position: "top-right",
            autoClose: 5000, // 5 seconds
            hideProgressBar: false,
            closeOnClick: true,
            pauseOnHover: true,
            draggable: true,
          });
          setForm({
            user_name: "",
            user_email: "",
            user_subject: "",
            user_message: "",
          });
        },
        (error) => {
          setLoading(false);

          toast.error("Ahh, something went wrong. Please try again.", {
            position: "top-right",
            autoClose: 5000, // 5 seconds
            hideProgressBar: false,
            closeOnClick: true,
            pauseOnHover: true,
            draggable: true,
          });
          console.error(error);
        }
      );
  };

  return (
    <section className="contact-section">
      <div className="contact-container">
        <div className="contact-text">
          <p className="contact-intro">Got a project in mind?</p>
          <h3 className="contact-heading">Let's talk about it!</h3>
        </div>
        <div className="contact-form-container">
          <form ref={formRef} onSubmit={handleSubmit} className="contact-form">
            <label className="form-label">
              <span className="label-text">Your Name</span>
              <input
                type="text"
                name="user_name"
                value={form.user_name}
                onChange={handleChange}
                placeholder="What's your good name?"
                className="form-input"
              />
            </label>
            <label className="form-label">
              <span className="label-text">Your Email</span>
              <input
                type="email"
                name="user_email"
                value={form.user_email}
                onChange={handleChange}
                placeholder="What's your web address?"
                className="form-input"
              />
            </label>
            <label className="form-label">
              <span className="label-text">Your Subject</span>
              <input
                type="text"
                name="user_subject"
                value={form.user_subject}
                onChange={handleChange}
                placeholder="What's the subject of discussion?"
                className="form-input"
              />
            </label>
            <label className="form-label">
              <span className="label-text">Your Message</span>
              <textarea
                rows={7}
                name="user_message"
                value={form.user_message}
                onChange={handleChange}
                placeholder="What do you want to say?"
                className="form-input"
              />
            </label>

            <button
              type="submit"
              className="submit-button"
            >
              {loading ? "Sending..." : "Send"}
            </button>
          </form>
          <div className="contact-info">
            <h3 className="contact-info-heading">You can also find me here</h3>
            <p>
              Email:{" "}
              <a href="mailto:hafizmuhammadahmadfarid@gmail.com">
                hafizmuhammadahmadfarid@gmail.com
              </a>
            </p>
            <p>Phone: +92-307-0612407</p>
            <div className="social-icons">
              <a href="https://www.reddit.com/user/ahmadfareed" target="_blank" rel="noopener noreferrer">
                <FaReddit />
              </a>
              <a href="https://twitter.com/Ali62763942275" target="_blank" rel="noopener noreferrer">
                <FaTwitter />
              </a>
              <a href="https://github.com/theahmadfareed" target="_blank" rel="noopener noreferrer">
                <FaGithub />
              </a>
              <a href="https://linkedin.com/in/theahmadfareed/" target="_blank" rel="noopener noreferrer">
                <FaLinkedin />
              </a>
              <a href="https://www.fiverr.com/ahmadfareed151" target="_blank" rel="noopener noreferrer">
                <SiFiverr />
              </a>
            </div>
          </div>
        </div>
      </div>
      <div id="ava" className="scroll-to-top">
        <a href="#hero">
          <div className="scroll-to-top-button">
            {/* Your scroll-to-top button */}
          </div>
        </a>
      </div>
    </section>
  );
};

export default Contact;
