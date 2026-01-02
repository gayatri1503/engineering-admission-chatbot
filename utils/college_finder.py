import json
import os

def load_json_data(filename):
    file_path = os.path.join(os.path.dirname(__file__), '..', 'data', filename)
    with open(file_path, 'r') as f:
        return json.load(f)

def find_colleges_by_percentile(percentile, category="OPEN", branch="Computer Engineering"):
    cutoffs = load_json_data('cutoffs.json')
    colleges_data = load_json_data('colleges.json')
    
    eligible_colleges = []
    
    for cutoff in cutoffs:
        if cutoff['category'] == category and cutoff['branch'] == branch:
            if percentile >= cutoff['round3_percentile']:
                college_info = next((c for c in colleges_data if c['id'] == cutoff['college_id']), None)
                if college_info:
                    eligible_colleges.append({
                        'college_name': cutoff['college_name'],
                        'branch': cutoff['branch'],
                        'category': cutoff['category'],
                        'cutoff_percentile': cutoff['round3_percentile'],
                        'location': college_info['location'],
                        'type': college_info['type'],
                        'website': college_info['website']
                    })
    
    eligible_colleges.sort(key=lambda x: x['cutoff_percentile'], reverse=True)
    
    return eligible_colleges

def get_college_details(college_name):
    colleges = load_json_data('colleges.json')
    
    for college in colleges:
        if college_name.lower() in college['name'].lower():
            return college
    
    return None

def get_cutoff_details(college_name, branch="Computer Engineering", category="OPEN"):
    cutoffs = load_json_data('cutoffs.json')
    
    results = []
    for cutoff in cutoffs:
        if college_name.lower() in cutoff['college_name'].lower():
            if branch.lower() in cutoff['branch'].lower() and cutoff['category'] == category:
                results.append(cutoff)
    
    return results

def get_all_branches():
    colleges = load_json_data('colleges.json')
    branches = set()
    
    for college in colleges:
        branches.update(college['branches'])
    
    return sorted(list(branches))

def get_categories():
    return ["OPEN", "OBC", "SC", "ST", "EWS", "TFWS"]