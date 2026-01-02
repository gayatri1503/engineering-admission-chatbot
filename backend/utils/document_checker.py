import json
import os

def load_documents_data():
    file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'documents.json')
    with open(file_path, 'r') as f:
        return json.load(f)

def get_documents_by_category(category):
    documents = load_documents_data()
    
    category_upper = category.upper()
    
    if category_upper in documents:
        return documents[category_upper]
    
    return None

def get_all_categories():
    documents = load_documents_data()
    return list(documents.keys())

def format_document_list(category):
    doc_info = get_documents_by_category(category)
    
    if not doc_info:
        return "Category not found. Please choose from: OPEN, OBC, SC, ST, EWS, TFWS"
    
    response = f"📋 **Documents Required for {doc_info['category_name']}**\n\n"
    
    for i, doc in enumerate(doc_info['required_documents'], 1):
        response += f"{i}. {doc}\n"
    
    response += f"\n⚠️ **Important Note:**\n{doc_info['verification_notes']}"
    
    return response