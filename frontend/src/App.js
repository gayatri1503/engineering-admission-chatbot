import React, { useState } from 'react';
import Header from './components/Header';
import Sidebar from './components/Sidebar';
import ChatBot from './components/ChatBot';
import './App.css';

function App() {
  const [isSidebarOpen, setIsSidebarOpen] = useState(false);

  const handleMenuClick = () => {
    setIsSidebarOpen(true);
  };

  const handleCloseSidebar = () => {
    setIsSidebarOpen(false);
  };

  const handleQuickAction = (action) => {
    console.log('Quick action:', action);
  };

  return (
    <div className="App">
      <Header onMenuClick={handleMenuClick} />
      <Sidebar 
        isOpen={isSidebarOpen} 
        onClose={handleCloseSidebar}
        onQuickAction={handleQuickAction}
      />
      <ChatBot />
    </div>
  );
}

export default App;