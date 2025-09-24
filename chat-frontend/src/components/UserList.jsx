import React from 'react';
import { IoPerson } from 'react-icons/io5';

const UserList = ({ users }) => {
  return (
    <div className="w-60 bg-gray-50 border-r border-gray-200 p-4 overflow-y-auto">
      <div className="flex justify-between items-center mb-4 pb-2 border-b border-gray-200">
        <h3 className="text-lg font-semibold text-gray-700">Online Users</h3>
        <span className="bg-blue-500 text-white rounded-full px-2 py-1 text-xs">{users.length}</span>
      </div>
      <div>
        {users.map((user, index) => (
          <div key={index} className="flex items-center p-2 mb-2 rounded hover:bg-gray-100 transition-colors">
            <IoPerson className="text-blue-500 mr-3" />
            <span className="text-sm text-gray-700">{user.username}</span>
          </div>
        ))}
      </div>
    </div>
  );
};

export default UserList;
