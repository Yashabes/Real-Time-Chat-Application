import React, { useState, useEffect, useRef } from 'react';
import { io } from 'socket.io-client';
import MessageList from './MessageList';
import MessageInput from './MessageInput';
import UserList from './UserList';

const ChatContainer = ({ username, room, onLogout }) => {
  const [messages, setMessages] = useState([]);
  const [users, setUsers] = useState([]);
  const socketRef = useRef(null);

  useEffect(() => {
    // Initialize socket connection
    socketRef.current = io('http://localhost:3000'); // Default backend port, will be updated when you provide the actual APIs

    // Join room
    socketRef.current.emit('joinRoom', { username, room });

    // Listen for messages
    socketRef.current.on('message', (message) => {
      setMessages((prevMessages) => [...prevMessages, message]);
    });

    // Listen for user list updates
    socketRef.current.on('roomUsers', ({ users }) => {
      setUsers(users);
    });

    // Clean up on component unmount
    return () => {
      socketRef.current.disconnect();
    };
  }, [username, room]);

  const sendMessage = (text) => {
    if (text.trim()) {
      socketRef.current.emit('chatMessage', text);
    }
  };

  return (
    <div className="flex flex-col h-screen bg-white">
      <div className="flex justify-between items-center p-4 bg-gradient-to-r from-blue-500 to-purple-600 text-white shadow-md z-10">
        <h2 className="text-xl font-semibold">#{room}</h2>
        <button 
          onClick={onLogout} 
          className="bg-white bg-opacity-20 border border-white border-opacity-30 rounded px-4 py-2 hover:bg-opacity-30 transition-all"
        >
          Logout
        </button>
      </div>
      <div className="flex flex-1 overflow-hidden">
        <UserList users={users} />
        <div className="flex flex-col flex-1">
          <MessageList messages={messages} currentUser={username} />
          <MessageInput onSend={sendMessage} />
        </div>
      </div>
    </div>
  );
};

export default ChatContainer;
