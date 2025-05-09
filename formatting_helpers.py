from io import BytesIO

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

def study_plan_to_txt(plan_dict):
    txt = "📚 Your Study Plan\n\n"
    for day, tasks in plan_dict.items():
        txt += f"{day}:\n"
        if tasks:
            for task in tasks:
                txt += f"  - {task['task_name']} – {task['hours']} hrs (Priority {task['priority']})\n"
        else:
            txt += "  ✅ No tasks assigned. Free day!\n"
        txt += "\n"
    return txt
