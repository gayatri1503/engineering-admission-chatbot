import React from 'react';
import { Bot, User } from 'lucide-react';

const ChatMessage = ({ message, isUser }) => {
  const formatMessage = (text) => {
    if (!text) return '';
    
    const parts = text.split(/(\*\*.*?\*\*)/g);
    
    return parts.map((part, index) => {
      if (part.startsWith('**') && part.endsWith('**')) {
        return <strong key={index}>{part.slice(2, -2)}</strong>;
      }
      return <span key={index}>{part}</span>;
    });
  };

  return (
    <div className={`message-wrapper ${isUser ? 'user-message-wrapper' : 'bot-message-wrapper'}`}>
      <div className={`message ${isUser ? 'user-message' : 'bot-message'}`}>
        <div className="message-icon">
          {isUser ? <User size={20} /> : <Bot size={20} />}
        </div>
        <div className="message-content">
          <div className="message-text">
            {formatMessage(message)}
          </div>
        </div>
      </div>
    </div>
  );
};

export default ChatMessage;