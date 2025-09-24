import React from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../contexts/AuthContext';
import ChatContainer from '../components/ChatContainer';

function Chat() {
  const { user, logout } = useAuth();
  const navigate = useNavigate();

  const handleLogout = () => {
    logout();
    navigate('/login');
  };

  if (!user) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-gradient-to-r from-blue-500 to-purple-600 p-4">
        <div className="max-w-md w-full text-center bg-white p-8 rounded-lg shadow-xl">
          <h2 className="text-2xl font-bold mb-4 text-gray-800">Not logged in</h2>
          <button 
            onClick={() => navigate('/login')}
            className="w-full bg-gradient-to-r from-blue-500 to-purple-600 text-white font-semibold py-3 rounded-lg hover:from-blue-600 hover:to-purple-700 transition-all duration-200 transform hover:-translate-y-0.5 hover:shadow-lg"
          >
            Go to Login
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-50">
      <ChatContainer username={user.email || user.username} room="general" onLogout={handleLogout} />
    </div>
  );
}

export default Chat;
