from io import BytesIO
from weasyprint import HTML

def convert_df_to_text(df):
    '''
    Takes dataframe and turns it into neat formatted string for llm
    '''
    lines = []
    for _, row in df.iterrows():
        task_line = (
            f"Task: {row['Work']}\n"
            f"Hours: {row['Number of Hours Required']}\n"
            f"Priority: {row['Priority']}\n"
        )
        lines.append(task_line)
    return str("\n---\n".join(lines))

def study_plan_to_html(plan_dict):
    html = """
    <html>
    <head>
        <style>
            body { font-family: Arial, sans-serif; padding: 20px; }
            h1 { text-align: center; }
            h2 { color: #2c3e50; margin-top: 30px; }
            p { line-height: 1.5; }
            .task { margin-bottom: 10px; }
        </style>
    </head>
    <body>
        <h1>📚 Your Study Plan</h1>
    """
    for day, tasks in plan_dict.items():
        html += f"<h2>{day}</h2>"
        if tasks:
            for task in tasks:
                html += (
                    f"<div class='task'><b>{task['task_name']}</b> – "
                    f"{task['hours']} hrs (Priority {task['priority']})</div>"
                )
        else:
            html += "<p><i>No tasks assigned. ✅ Free day!</i></p>"

    html += "</body></html>"
    return html

def html_to_pdf_bytes(html_string):
    pdf_buffer = BytesIO()
    HTML(string=html_string).write_pdf(pdf_buffer)
    pdf_buffer.seek(0)
    return pdf_buffer
