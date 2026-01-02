import React, { useState, useEffect, useRef } from 'react';
import ChatMessage from './ChatMessage';
import ChatInput from './ChatInput';
import { sendMessage } from '../services/api';
import '../styles/ChatBot.css';

const ChatBot = () => {
  const [messages, setMessages] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [sessionId] = useState(() => `session_${Date.now()}`);
  const [suggestions, setSuggestions] = useState([]);
  const [formData, setFormData] = useState(null);
  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  useEffect(() => {
    const welcomeMessage = "Hello! 👋 I'm your Engineering Admission Assistant. I can help you with:\n\n• Finding colleges based on your MHT CET percentile\n• CAP round information\n• Document requirements for different categories\n• College cutoffs and details\n• Admission deadlines and fees\n\nHow can I assist you today?";
    
    setMessages([{ text: welcomeMessage, isUser: false }]);
    setSuggestions(['Find colleges', 'Document checklist', 'CAP rounds info', 'Check cutoffs']);
  }, []);

  const handleSendMessage = async (userMessage, additionalData = {}) => {
    const newUserMessage = { text: userMessage, isUser: true };
    setMessages(prev => [...prev, newUserMessage]);
    setIsLoading(true);
    setSuggestions([]);
    setFormData(null);

    try {
      const response = await sendMessage(userMessage, sessionId, additionalData);
      
      const botMessage = { text: response.reply, isUser: false };
      setMessages(prev => [...prev, botMessage]);
      
      if (response.suggestions) {
        setSuggestions(response.suggestions);
      }
      
      if (response.form) {
        setFormData(response.form);
      }
    } catch (error) {
      const errorMessage = { 
        text: "Sorry, I'm having trouble connecting. Please try again.", 
        isUser: false 
      };
      setMessages(prev => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };

  const handleSuggestionClick = (suggestion) => {
    const suggestionMap = {
      'Find colleges': 'I want to find colleges based on my percentile',
      'Document checklist': 'What documents do I need?',
      'CAP rounds info': 'Tell me about CAP rounds',
      'Check cutoffs': 'Show me college cutoffs',
      'Fees info': 'What are the fees?',
      'More details': 'Tell me more details',
      'TFWS details': 'What is TFWS?',
      'Scholarships': 'Tell me about scholarships'
    };

    const message = suggestionMap[suggestion] || suggestion;
    handleSendMessage(message);
  };

  const handleFormSubmit = (e) => {
    e.preventDefault();
    const formDataObj = new FormData(e.target);
    const data = Object.fromEntries(formDataObj.entries());
    
    const message = `I have percentile ${data.percentile}, category ${data.category}, interested in ${data.branch}`;
    handleSendMessage(message, data);
  };

  return (
    <div className="chatbot-container">
      <div className="messages-container">
        {messages.map((msg, index) => (
          <ChatMessage key={index} message={msg.text} isUser={msg.isUser} />
        ))}
        
        {isLoading && (
          <div className="loading-indicator">
            <div className="typing-dots">
              <span></span>
              <span></span>
              <span></span>
            </div>
          </div>
        )}

        {formData && (
          <div className="form-container">
            <form onSubmit={handleFormSubmit} className="bot-form">
              {formData.fields.map((field, index) => (
                <div key={index} className="form-field">
                  <label>{field.label}</label>
                  {field.type === 'select' ? (
                    <select name={field.name} required={field.required}>
                      <option value="">Select {field.label}</option>
                      {field.options.map((opt, i) => (
                        <option key={i} value={opt}>{opt}</option>
                      ))}
                    </select>
                  ) : (
                    <input
                      type={field.type}
                      name={field.name}
                      required={field.required}
                      placeholder={field.label}
                      step={field.type === 'number' ? '0.01' : undefined}
                    />
                  )}
                </div>
              ))}
              <button type="submit" className="form-submit-button">Submit</button>
            </form>
          </div>
        )}

        {suggestions.length > 0 && (
          <div className="suggestions-container">
            {suggestions.map((suggestion, index) => (
              <button
                key={index}
                className="suggestion-button"
                onClick={() => handleSuggestionClick(suggestion)}
              >
                {suggestion}
              </button>
            ))}
          </div>
        )}
        
        <div ref={messagesEndRef} />
      </div>
      
      <ChatInput onSend={handleSendMessage} disabled={isLoading} />
    </div>
  );
};

export default ChatBot;