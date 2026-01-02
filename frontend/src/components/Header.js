import React from 'react';
import { Menu, GraduationCap } from 'lucide-react';
import '../styles/Header.css';

const Header = ({ onMenuClick }) => {
  return (
    <header className="header">
      <div className="header-content">
        <button className="menu-button" onClick={onMenuClick}>
          <Menu size={24} />
        </button>
        <div className="header-title">
          <GraduationCap size={28} />
          <h1>Engineering Admission Assistant</h1>
        </div>
      </div>
    </header>
  );
};

export default Header;