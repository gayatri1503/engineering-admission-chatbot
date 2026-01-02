# 🎓 Engineering Admission Assistant Chatbot

An AI-powered chatbot that helps students navigate the engineering admission process in Maharashtra. Get college recommendations, document checklists, CAP round information, and much more.

## ✨ Features

- **Smart College Finder**: Get personalized college recommendations based on your MHT CET percentile
- **Document Checklist**: Category-wise document requirements (OPEN, OBC, SC, ST, EWS, TFWS)
- **CAP Round Guidance**: Complete information about all admission rounds
- **Cutoff Information**: Previous year cutoffs for top engineering colleges
- **Fees Structure**: Detailed breakdown of tuition and other expenses
- **Real-time Chat**: Interactive conversation with intelligent suggestions
- **Responsive Design**: Works seamlessly on desktop and mobile devices

## 🛠️ Tech Stack

### Backend
- **Flask** - Python web framework
- **Flask-CORS** - Cross-origin resource sharing
- **Python 3.8+**

### Frontend
- **React.js** - UI library
- **Axios** - HTTP client
- **Lucide React** - Icon library
- **CSS3** - Styling

## 📁 Project Structure

```
engineering-admission-chatbot/
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   ├── .env
│   ├── data/
│   │   ├── colleges.json
│   │   ├── cutoffs.json
│   │   └── documents.json
│   └── utils/
│       ├── college_finder.py
│       └── document_checker.py
│
├── frontend/
│   ├── package.json
│   ├── public/
│   │   ├── index.html
│   │   └── manifest.json
│   └── src/
│       ├── App.js
│       ├── index.js
│       ├── components/
│       ├── services/
│       └── styles/
│
└── README.md
```

## 🚀 Installation & Setup

### Prerequisites
- Node.js (v16 or higher)
- Python (v3.8 or higher)
- npm or yarn

### Backend Setup

1. Navigate to backend directory:
```bash
cd backend
```

2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the Flask server:
```bash
python app.py
```

Backend will run on `http://localhost:5000`

### Frontend Setup

1. Navigate to frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm start
```

Frontend will run on `http://localhost:3000`

## 💻 Usage

1. Open your browser and go to `http://localhost:3000`
2. Start chatting with the bot
3. Use quick action buttons or type your questions
4. Get personalized recommendations and information

### Sample Queries:
- "Find colleges for 95 percentile"
- "What documents do I need for OBC category?"
- "Tell me about CAP rounds"
- "What are the fees for government colleges?"

## 📱 Mobile Support

The application is fully responsive and works perfectly on:
- Desktop browsers
- Tablets
- Mobile phones (iOS and Android)

### Progressive Web App (PWA)
The app can be installed on mobile devices:
1. Open the app in Chrome/Safari
2. Tap "Add to Home Screen"
3. Use like a native app

## 🎨 Features in Detail

### College Finder
- Enter your MHT CET percentile
- Select your category (OPEN/OBC/SC/ST/EWS/TFWS)
- Choose preferred branch
- Get instant college recommendations with cutoffs

### Document Checklist
- Category-specific document lists
- Verification notes and important information
- Original vs photocopy requirements

### CAP Rounds
- Detailed explanation of Round 1, 2, and 3
- Timeline and important dates
- Freeze, Float, and Slide options explained

### Fees Information
- Government vs Private college fees
- Additional costs (hostel, mess, books)
- TFWS and scholarship information

## 🔧 Configuration

### Backend (.env)
```
FLASK_APP=app.py
FLASK_ENV=development
PORT=5000
```

### Frontend (.env)
```
REACT_APP_API_URL=http://localhost:5000
```

## 📊 Data Management

### Adding New Colleges
Edit `backend/data/colleges.json` and add:
```json
{
  "id": 11,
  "name": "College Name",
  "location": "City",
  "type": "Government/Private",
  "branches": ["CS", "IT", "Mechanical"],
  "facilities": ["Hostel", "Library"],
  "website": "https://example.com"
}
```

### Updating Cutoffs
Edit `backend/data/cutoffs.json` annually with new data.

## 🚀 Deployment

### Backend (Render/Railway/Heroku)

1. Create `Procfile`:
```
web: python app.py
```

2. Push to GitHub
3. Connect to Render/Railway
4. Deploy

### Frontend (Vercel/Netlify)

1. Build the project:
```bash
npm run build
```

2. Deploy to Vercel:
```bash
vercel --prod
```

Or connect GitHub repo to Netlify for automatic deployment.

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📝 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

Your Name

## 📧 Contact

For queries or suggestions, reach out at: your.email@example.com

## 🙏 Acknowledgments

- DTE Maharashtra for admission guidelines
- All contributing colleges for data
- Open source community

---

**Note**: This chatbot provides guidance based on previous year data. Always verify information from official DTE Maharashtra website before making final decisions.