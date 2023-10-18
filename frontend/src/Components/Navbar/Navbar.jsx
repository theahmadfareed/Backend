import React from 'react';
import { Link } from 'react-router-dom';

export default function Navbar() {
  const styles = {
    navBar: {
      backgroundColor: "rgb(249, 231, 159)",
      padding: "10px 0",
      boxShadow: "0 2px 4px rgba(0, 0, 0, 0.1)",
      display: "flex",
      justifyContent: "center",
      alignItems: "center",
    },
    navList: {
      display: "flex",
      justifyContent: "space-evenly",
      listStyle: "none",
      padding: 0,
    },
    navItem: {
      margin: 0,
      padding: "10px 20px",
      fontSize: "16px",
      textDecoration: "none",
      color: "black",
      border: "1px solid transparent",
      borderRadius: "5px",
      transition: "background-color 0.3s",
    },
    navItemHover: {
      backgroundColor: "rgba(0, 0, 0, 0.1)",
    }
  };

  return (
    <div style={styles.navBar}>
      <ul style={styles.navList}>
        <Link to='/'>
          <li style={styles.navItem}>
            Landing Page
          </li>
        </Link>
        <Link to='/sign-up'>
          <li style={styles.navItem}>
            Sign Up
          </li>
        </Link>
        <Link to='/sign-in'>
          <li style={styles.navItem}>
            Sign In
          </li>
        </Link>
        <Link to='/dashboard'>
          <li style={styles.navItem}>
            Dashboard
          </li>
        </Link>
        <Link to='/create-project'>
          <li style={styles.navItem}>
            Create Project
          </li>
        </Link>
        <Link to='/comparison'>
          <li style={styles.navItem}>
            Comparison
          </li>
        </Link>
        <Link to='/reports'>
          <li style={styles.navItem}>
            Reports
          </li>
        </Link>
        <Link to='/contact-us'>
          <li style={styles.navItem}>
            Contact Us
          </li>
        </Link>
      </ul>
    </div>
  );
}
