import React, { useState } from 'react';
import { IoSend } from 'react-icons/io5';

const MessageInput = ({ onSend }) => {
  const [text, setText] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (text.trim()) {
      onSend(text);
      setText('');
    }
  };

  const handleKeyDown = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSubmit(e);
    }
  };

  return (
    <form className="p-4 bg-white border-t border-gray-200" onSubmit={handleSubmit}>
      <div className="flex items-center bg-gray-100 rounded-2xl p-3 border border-gray-200 focus-within:border-blue-500">
        <input
          type="text"
          value={text}
          onChange={(e) => setText(e.target.value)}
          onKeyDown={handleKeyDown}
          placeholder="Type a message..."
          className="flex-1 bg-transparent border-none outline-none p-2 text-sm resize-none max-h-[150px]"
        />
        <button 
          type="submit" 
          className="bg-transparent border-none text-blue-500 cursor-pointer p-2 flex items-center justify-center disabled:text-gray-400 disabled:cursor-not-allowed"
          disabled={!text.trim()}
        >
          <IoSend size={20} />
        </button>
      </div>
    </form>
  );
};

export default MessageInput;
