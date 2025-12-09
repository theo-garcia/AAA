def html_page_builder(template_path,var_list):
    with open(template_path, 'r') as template:
        content = template.read()
        for var in var_list:
            content = content.replace(var['label'],var['value'])
    with open('index.html', 'w') as file:
        file.write(content)
    
var_list = [
                {'label': '{{ cpu_load }}', 'value' : '50%'},
                {'label': '{{ ram_size }}', 'value' : '6G'},
                {'label': '{{ ram_load }}', 'value' : '30%'},
                {'label': '{{ storage_size }}', 'value' : '70G'},
                {'label': '{{ storage_load }}', 'value' : '70%'}
            ]

html_page_builder('template.html',var_list)