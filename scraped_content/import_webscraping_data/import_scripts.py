import json
import xmlrpc.client
from datetime import datetime


url = "http://hgagy-latitude-e5570:8016"
db = "odoo_test"
username = "a"
password = "a"

common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")
uid = common.authenticate(db, username, password, {})
models = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object")



# Import Jobs Data
with open('linkedin_jobs.json', 'r', encoding='utf-8') as f:
    jobs = json.load(f)
for job in jobs:
        models.execute_kw(db, uid, password,
                          'scraped.job', 'create', [{
                          'name': job.get('Job Title', ''),
                          'company_name': job.get('Company', ''),
                          'location': job.get('Location', ''),
                          'company_logo_url': job.get('Logo', '') or '',
                          'date_posted': job.get('Date Job', ''),
                          'source_url': job.get('url', ''),
                          'status': 'new',
                      }])

 # Import  Blog Data
with open('blogs.json', 'r') as f:
    blogs = json.load(f)

for blog in blogs:
        raw_date = blog.get('Publish Date', '')
        date_parsed = datetime.now().strftime('%Y-%m-%d')
        if 'hour' not in raw_date.lower():
            try:
                date_parsed = datetime.strptime(raw_date, '%B %d, %Y').strftime('%Y-%m-%d')
            except:
                pass

        models.execute_kw(db, uid, password,
            'scraped.blog', 'create', [{
                'title': blog.get('Title', ''),
                'summary': blog.get('Summary', ''),
                'content': blog.get('Full Content', ''),
                'source_url': blog.get('Source Url', ''),
                'date_published': date_parsed,
                'status': 'new',
            }])
 # Import  Static Page Data
with open('static_page.json', 'r') as f:
    pages = json.load(f)
for page in pages :
    models.execute_kw(db, uid, password,
                      'scraped.page', 'create', [{
            'title': page.get('title', ''),
            'content': page.get('content', ''),
            'source_url': page.get('source_url', ''),
            'status': 'new',
        }])
