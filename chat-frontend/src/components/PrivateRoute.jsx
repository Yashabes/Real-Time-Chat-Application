import React from 'react';
import { Navigate } from 'react-router-dom';
import { useAuth } from '../contexts/AuthContext';

function PrivateRoute({ children }) {
  const { user, loading } = useAuth();

  console.log('Loading:', loading);
  console.log('Current User:', user);

  if (loading) {
    return (
      <div className="flex items-center justify-center min-h-screen bg-gradient-to-r from-blue-500 to-purple-600">
        <div className="text-center">
          <div className="inline-block animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-white"></div>
          <div className="text-lg font-semibold text-white mt-4">Loading...</div>
        </div>
      </div>
    );
  }

  return user ? children : <Navigate to="/login" />;
}

export default PrivateRoute;
