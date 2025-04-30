import json

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
    return "\n---\n".join(lines)

def convert_json_to_output(json_output):
    content = json.loads(json_output)