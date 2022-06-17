import os
import shutil

root = os.path.join(os.getcwd(), "my_project")

root_templates = os.path.join(root, 'templates')
if not os.path.exists(root_templates):
    os.mkdir(root_templates)

for app in os.listdir(root):
    app_path = os.path.join(root, app)
    if not os.path.isdir(app_path):
        continue
    templates_path = os.path.join(root, app, "templates", app)
    if os.path.exists(templates_path):
        inner_app_path = os.path.join(root_templates, app)
        if not os.path.exists(inner_app_path):
            os.mkdir(inner_app_path)
        for file in os.listdir(templates_path):
            file_path = os.path.join(templates_path, file)
            shutil.copy(file_path, inner_app_path)