def convert_df_to_text(df):
    '''
    Takes dataframe and turns it into neat formatted string for llm
    '''
    lines = []
    for _, row in df.iterrows():
        lines.append(
            f"Task: {row['Work']}\nPriority: {row['Priority']}\nHours Required: {row['Number of Hours Required']}\n"
        )
    return "\n---\n".join(lines)