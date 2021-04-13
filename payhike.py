import pywebio
from pywebio.input import input, FLOAT
from pywebio.output import put_text, put_html, put_markdown, put_table

def hike():
    current_salary = input("Enter your current salary ($)：", type=FLOAT)
    new_salary = input("Enter your new salary ($)：", type=FLOAT)
    total_hike = (new_salary -current_salary) 
    hike_per = (((new_salary -current_salary) / current_salary ) * 100)
    put_markdown('# **Results**')
    put_html('<br><br>')
    put_markdown('Your Hike: %.1f. Hike percentage: %s' % (total_hike, hike_per))
    put_html('<hr>')
    put_table([
        ['Hike($)', 'Hike (%)'],
        [total_hike, hike_per],
    ])

if __name__ == '__main__':
    pywebio.start_server(hike, port=55)