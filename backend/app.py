from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from datetime import datetime
from backend.utils.college_finder import find_colleges_by_percentile, get_college_details, get_cutoff_details, get_all_branches, get_categories
from backend.utils.document_checker import get_documents_by_category, format_document_list

app = Flask(__name__)
CORS(app)

conversation_history = {}

@app.route('/')
def home():
    return jsonify({
        'message': 'Engineering Admission Chatbot API',
        'version': '1.0',
        'status': 'active'
    })

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_message = data.get('message', '').lower()
        session_id = data.get('session_id', 'default')
        
        if session_id not in conversation_history:
            conversation_history[session_id] = []
        
        conversation_history[session_id].append({
            'user': user_message,
            'timestamp': datetime.now().isoformat()
        })
        
        response = process_message(user_message, data)
        
        conversation_history[session_id].append({
            'bot': response['reply'],
            'timestamp': datetime.now().isoformat()
        })
        
        return jsonify(response)
    
    except Exception as e:
        return jsonify({
            'reply': f'Sorry, I encountered an error: {str(e)}',
            'type': 'error'
        }), 500

def process_message(message, data):
    message = message.lower().strip()
    
    if any(word in message for word in ['hello', 'hi', 'hey', 'start']):
        return {
            'reply': "Hello! 👋 I'm your Engineering Admission Assistant. I can help you with:\n\n• Finding colleges based on your MHT CET percentile\n• CAP round information\n• Document requirements for different categories\n• College cutoffs and details\n• Admission deadlines and fees\n\nHow can I assist you today?",
            'type': 'greeting',
            'suggestions': ['Find colleges', 'Document checklist', 'CAP rounds info', 'Check cutoffs']
        }
    
    elif any(word in message for word in ['college', 'find', 'suggest', 'recommend', 'percentile']):
        percentile = data.get('percentile')
        category = data.get('category', 'OPEN').upper()
        branch = data.get('branch', 'Computer Engineering')
        
        if not percentile:
            return {
                'reply': "To find suitable colleges, I need your MHT CET percentile. Please provide:\n\n• Your percentile score (e.g., 95.5)\n• Your category (OPEN/OBC/SC/ST/EWS)\n• Preferred branch (optional)",
                'type': 'info_request',
                'form': {
                    'fields': [
                        {'name': 'percentile', 'type': 'number', 'label': 'MHT CET Percentile', 'required': True},
                        {'name': 'category', 'type': 'select', 'label': 'Category', 'options': get_categories()},
                        {'name': 'branch', 'type': 'select', 'label': 'Branch', 'options': get_all_branches()}
                    ]
                }
            }
        
        try:
            percentile_float = float(percentile)
            colleges = find_colleges_by_percentile(percentile_float, category, branch)
            
            if colleges:
                reply = f"Based on your percentile of {percentile_float}% in {category} category for {branch}, here are your options:\n\n"
                
                for i, college in enumerate(colleges[:5], 1):
                    reply += f"{i}. **{college['college_name']}** ({college['type']})\n"
                    reply += f"   📍 {college['location']}\n"
                    reply += f"   📊 Cutoff: {college['cutoff_percentile']}%\n"
                    reply += f"   🔗 {college['website']}\n\n"
                
                return {
                    'reply': reply,
                    'type': 'college_list',
                    'colleges': colleges[:5],
                    'suggestions': ['Document checklist', 'CAP rounds', 'More details']
                }
            else:
                return {
                    'reply': f"I couldn't find colleges matching {percentile_float}% in {category} category for {branch}. You might want to:\n\n• Try a different branch\n• Check other category options\n• Look at previous year cutoffs",
                    'type': 'no_results'
                }
        
        except ValueError:
            return {
                'reply': 'Please provide a valid percentile number (e.g., 95.5)',
                'type': 'error'
            }
    
    elif any(word in message for word in ['document', 'documents', 'papers', 'certificates', 'checklist']):
        category = data.get('category', 'OPEN').upper()
        
        if 'category' not in data:
            return {
                'reply': "Which category documents do you need? Please select:",
                'type': 'category_select',
                'options': get_categories()
            }
        
        doc_list = format_document_list(category)
        
        return {
            'reply': doc_list,
            'type': 'documents',
            'suggestions': ['Find colleges', 'CAP rounds', 'Fees info']
        }
    
    elif any(word in message for word in ['cap', 'round', 'rounds', 'admission process']):
        return {
            'reply': """📅 **CAP (Centralized Admission Process) Rounds**

**Round 1:**
• Option form filling opens
• College preferences submission
• Seat allotment
• Document verification & fee payment
• Reporting to allotted college

**Round 2:**
• For vacant seats after Round 1
• Fresh option form filling
• New allotments based on availability
• Document verification & admission

**Round 3:**
• Final round for remaining seats
• Limited options available
• Last chance for admission

**Important Points:**
• You can participate in all rounds
• Freezing seat means you accept that college
• Sliding allows you to keep allocated seat but try for better options
• Floating lets you participate in next round while keeping current seat

**Timeline:** Usually conducted in July-August (after MHT CET results)""",
            'type': 'cap_info',
            'suggestions': ['Document checklist', 'Find colleges', 'Fees structure']
        }
    
    elif any(word in message for word in ['fee', 'fees', 'cost', 'tuition', 'expense']):
        return {
            'reply': """💰 **Fee Structure (Approximate)**

**Government Colleges:**
• Tuition Fee: ₹70,000 - ₹1,00,000 per year
• Development Fee: ₹5,000 - ₹10,000
• Other Charges: ₹5,000 - ₹10,000
• **Total:** ₹80,000 - ₹1,20,000 per year

**Private Colleges:**
• Tuition Fee: ₹1,00,000 - ₹3,50,000 per year
• Development Fee: ₹10,000 - ₹25,000
• Other Charges: ₹10,000 - ₹25,000
• **Total:** ₹1,20,000 - ₹4,00,000 per year

**Additional Costs:**
• Hostel: ₹50,000 - ₹1,00,000 per year
• Mess: ₹30,000 - ₹50,000 per year
• Books & Study Material: ₹10,000 - ₹20,000 per year

**TFWS (Tuition Fee Waiver Scheme):**
• Available for students with family income < ₹8 lakhs
• Covers tuition fees in private colleges
• Must maintain academic standards

💡 Fees vary by college and branch. Check specific college websites for exact amounts.""",
            'type': 'fees_info',
            'suggestions': ['TFWS details', 'Find colleges', 'Scholarships']
        }
    
    elif any(word in message for word in ['cutoff', 'cut off', 'cut-off']):
        return {
            'reply': "I can show you cutoff details. Please provide:\n\n• College name\n• Branch (e.g., Computer Engineering)\n• Category (OPEN/OBC/SC/ST)",
            'type': 'cutoff_request',
            'form': {
                'fields': [
                    {'name': 'college', 'type': 'text', 'label': 'College Name'},
                    {'name': 'branch', 'type': 'select', 'label': 'Branch', 'options': get_all_branches()},
                    {'name': 'category', 'type': 'select', 'label': 'Category', 'options': get_categories()}
                ]
            }
        }
    
    elif any(word in message for word in ['deadline', 'date', 'schedule', 'when']):
        return {
            'reply': """📅 **Important Admission Dates (Tentative)**

**MHT CET Exam:** May (Usually)

**Result Declaration:** June

**CAP Process:**

**Round 1:**
• Registration: Mid-July
• Option Form: Late July
• Seat Allotment: Early August
• Document Verification: Within 3-4 days of allotment
• Reporting: Within 1 week

**Round 2:**
• Option Form: Mid-August
• Seat Allotment: Late August
• Admission: Within 3-4 days

**Round 3:**
• Usually in September

⚠️ **Important:** Check official DTE Maharashtra website (dtemaharashtra.gov.in) for exact dates as they may vary each year.""",
            'type': 'deadline_info',
            'suggestions': ['CAP rounds', 'Document checklist', 'Find colleges']
        }
    
    elif any(word in message for word in ['thank', 'thanks']):
        return {
            'reply': "You're welcome! 😊 If you have any more questions about engineering admissions, feel free to ask. Good luck with your admission process!",
            'type': 'closing'
        }
    
    else:
        return {
            'reply': "I'm here to help with engineering admissions! I can assist you with:\n\n• Finding colleges based on percentile\n• Document requirements\n• CAP round information\n• Cutoffs and fees\n• Important deadlines\n\nWhat would you like to know?",
            'type': 'help',
            'suggestions': ['Find colleges', 'Document checklist', 'CAP rounds', 'Fees info']
        }

@app.route('/api/colleges', methods=['GET'])
def get_colleges():
    percentile = request.args.get('percentile', type=float)
    category = request.args.get('category', 'OPEN')
    branch = request.args.get('branch', 'Computer Engineering')
    
    if not percentile:
        return jsonify({'error': 'Percentile is required'}), 400
    
    colleges = find_colleges_by_percentile(percentile, category, branch)
    return jsonify({'colleges': colleges})

@app.route('/api/documents/<category>', methods=['GET'])
def get_documents(category):
    docs = get_documents_by_category(category)
    
    if docs:
        return jsonify(docs)
    else:
        return jsonify({'error': 'Category not found'}), 404

@app.route('/api/branches', methods=['GET'])
def get_branches():
    branches = get_all_branches()
    return jsonify({'branches': branches})

@app.route('/api/categories', methods=['GET'])
def get_category_list():
    categories = get_categories()
    return jsonify({'categories': categories})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)