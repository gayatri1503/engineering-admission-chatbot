import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const sendMessage = async (message, sessionId, additionalData = {}) => {
  try {
    const response = await api.post('/api/chat', {
      message,
      session_id: sessionId,
      ...additionalData
    });
    return response.data;
  } catch (error) {
    console.error('Error sending message:', error);
    throw error;
  }
};

export const getColleges = async (percentile, category, branch) => {
  try {
    const response = await api.get('/api/colleges', {
      params: { percentile, category, branch }
    });
    return response.data;
  } catch (error) {
    console.error('Error fetching colleges:', error);
    throw error;
  }
};

export const getDocuments = async (category) => {
  try {
    const response = await api.get(`/api/documents/${category}`);
    return response.data;
  } catch (error) {
    console.error('Error fetching documents:', error);
    throw error;
  }
};

export const getBranches = async () => {
  try {
    const response = await api.get('/api/branches');
    return response.data;
  } catch (error) {
    console.error('Error fetching branches:', error);
    throw error;
  }
};

export const getCategories = async () => {
  try {
    const response = await api.get('/api/categories');
    return response.data;
  } catch (error) {
    console.error('Error fetching categories:', error);
    throw error;
  }
};

export default api;