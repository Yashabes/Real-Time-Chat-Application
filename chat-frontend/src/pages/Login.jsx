import React from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../contexts/AuthContext';
import LoginForm from '../components/LoginForm';

function Login() {
  const navigate = useNavigate();
  const { login } = useAuth();

  const handleLogin = async (username, room) => {
    try {
      // For now, we'll create a mock user object since we don't have a real API
      // In a real application, you would make an API call here
      const userData = {
        username: username,
        room: room,
        // Add other user data as needed
      };
      
      login(userData);
      navigate('/chat');
    } catch (err) {
      throw new Error('Failed to login. Please try again.');
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-50">
      <div className="max-w-md w-full">
        <LoginForm onLogin={handleLogin} />
      </div>
    </div>
  );
}

export default Login;
