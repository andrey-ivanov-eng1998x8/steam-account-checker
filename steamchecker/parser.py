from bs4 import BeautifulSoup
import json

def parse_profile_page(html):
    """Extract basic public stats from steam profile html."""
    soup = BeautifulSoup(html, 'html.parser')
    name_elem = soup.find('span', class_='actual_persona_name')
    name = name_elem.text.strip() if name_elem else 'Unknown'
    
    hours = 0.0
    for block in soup.find_all('div', class_='recent_game_row'):
        hours_elem = block.find('div', class_='hours_played')
        if hours_elem:
            text = hours_elem.text.strip().replace(' hrs', '').replace(',', '')
            try:
                hours += float(text)
            except ValueError:
                pass
                
    return {
        'name': name,
        'total_hours': hours,
    }

def parse_inventory(json_str):
    try:
        data = json.loads(json_str)
        return len(data.get('assets', []))
    except Exception:
        return 0
