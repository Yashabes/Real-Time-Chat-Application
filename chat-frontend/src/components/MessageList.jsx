import React, { useEffect, useRef } from 'react';
import { format } from 'date-fns';

const MessageList = ({ messages, currentUser }) => {
  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const isCurrentUser = (username) => {
    return username === currentUser;
  };

  const formatTime = (timestamp) => {
    return format(new Date(timestamp), 'HH:mm');
  };

  return (
    <div className="flex-1 p-6 overflow-y-auto bg-gray-100 bg-opacity-50 bg-blend-overlay" style={{ backgroundImage: "url(\"data:image/svg+xml,%3Csvg width='100' height='100' viewBox='0 0 100 100' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M11 18c3.866 0 7-3.134 7-7s-3.134-7-7-7-7 3.134-7 7 3.134 7 7 7zm48 25c3.866 0 7-3.134 7-7s-3.134-7-7-7-7 3.134-7 7 3.134 7 7 7zm-43-7c1.657 0 3-1.343 3-3s-1.343-3-3-3-3 1.343-3 3 1.343 3 3 3z' fill='%23d1d8e0' fill-opacity='0.1' fill-rule='evenodd'/%3E%3C/svg%3E\")" }}>
      {messages.map((message, index) => (
        <div
          key={index}
          className={`mb-4 flex ${isCurrentUser(message.username) ? 'justify-end' : 'justify-start'}`}
        >
          <div className={`max-w-[70%] p-4 rounded-2xl shadow-sm bg-white ${isCurrentUser(message.username) ? 'bg-blue-500 text-white' : ''}`}>
            <div className="flex justify-between text-xs mb-1">
              <span className={`font-semibold ${isCurrentUser(message.username) ? 'text-white' : 'text-gray-700'}`}>{message.username}</span>
              <span className={`ml-2 ${isCurrentUser(message.username) ? 'text-blue-100' : 'text-gray-500'}`}>{formatTime(message.timestamp)}</span>
            </div>
            <div className="text-sm">{message.text}</div>
          </div>
        </div>
      ))}
      <div ref={messagesEndRef} />
    </div>
  );
};

export default MessageList;
