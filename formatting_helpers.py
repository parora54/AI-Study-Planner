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
    study_text = ""
    
    for day, tasks in plan_dict.items():
        study_text += f"{day}:\n"
        if tasks:
            for task in tasks:
                study_text += f"  - {task['task_name']} – {task['hours']} hours (Priority {task['priority']})\n"
        else:
            study_text += "  ✅ No tasks assigned. Free day!\n"
        study_text += "\n"
