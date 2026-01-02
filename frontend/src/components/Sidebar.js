import React from 'react';
import { X, FileText, School, Calendar, DollarSign, HelpCircle } from 'lucide-react';
import '../styles/Sidebar.css';

const Sidebar = ({ isOpen, onClose, onQuickAction }) => {
  const quickActions = [
    { icon: School, label: 'Find Colleges', action: 'find_colleges' },
    { icon: FileText, label: 'Document Checklist', action: 'documents' },
    { icon: Calendar, label: 'CAP Rounds Info', action: 'cap_rounds' },
    { icon: DollarSign, label: 'Fees Structure', action: 'fees' },
    { icon: HelpCircle, label: 'Help', action: 'help' }
  ];

  const handleAction = (action) => {
    onQuickAction(action);
    onClose();
  };

  return (
    <>
      <div className={`sidebar-overlay ${isOpen ? 'active' : ''}`} onClick={onClose}></div>
      <div className={`sidebar ${isOpen ? 'open' : ''}`}>
        <div className="sidebar-header">
          <h2>Quick Actions</h2>
          <button className="close-button" onClick={onClose}>
            <X size={24} />
          </button>
        </div>
        <div className="sidebar-content">
          <div className="quick-actions">
            {quickActions.map((item, index) => {
              const Icon = item.icon;
              return (
                <button
                  key={index}
                  className="quick-action-button"
                  onClick={() => handleAction(item.action)}
                >
                  <Icon size={20} />
                  <span>{item.label}</span>
                </button>
              );
            })}
          </div>
          <div className="sidebar-info">
            <h3>About</h3>
            <p>This chatbot helps you with engineering admission guidance in Maharashtra.</p>
            <p className="version">Version 1.0</p>
          </div>
        </div>
      </div>
    </>
  );
};

export default Sidebar;