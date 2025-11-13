import pandas as pd
import sqlite3
import os

# File and table setup
CSV_FILE="data.csv"
DB_FILE="students.db"
TABLE_NAME="marks"

# Load data from CSV file
def load_data(csv_path):
    if not os.path.exists(csv_path):
        raise FileNotFoundError(csv_path,"not found")
    return pd.read_csv(csv_path)

# Save DataFrame to SQLite database
def save_to_db(df,db_file,table_name):
    import sqlite3
    conn=sqlite3.connect(db_file)
    df.to_sql(table_name,conn,if_exists='replace',index=False)
    conn.close()

# Load data from database
def load_from_db(db_file,table_name):
    import sqlite3
    conn=sqlite3.connect(db_file)
    df=pd.read_sql_query(f"select * from {table_name}",conn)
    conn.close()
    return df

# Analyze marks data
def analyze_data(df):
    print("\n-----  Data Analysis  -----")
    avg_sub=df.groupby('subject')['marks'].mean()
    print("\nAverage marks per subject:\n", avg_sub)
    print("\nHighest marks:", df['marks'].max())
    print("Lowest marks:", df['marks'].min())
    print("Overall class average:", df['marks'].mean())

    # Find topper in each subject
    top_students=df.loc[df.groupby('subject')['marks'].idxmax()]
    print("\n Top students per subject: ")
    print(top_students[['name','subject','marks']].to_string(index=False))
    
    return avg_sub,top_students

# Export final report as CSV
def export_report(avg_by_subject,top_students):
    report_df = avg_by_subject.reset_index()
    report_df.columns = ['Subject', 'Average Marks']
    
    topper_df=top_students[['subject','name','marks']].rename(columns={'subject':'Subject','name':'Top Student','marks':'Top marks'})
    
    final_report = pd.merge(report_df, topper_df, on='Subject')
    final_report['Average Marks']=final_report['Average Marks'].round(2)
    final_report.to_csv('report.csv', index=False)

    print("\n📁 Report saved as 'report.csv'")
    print(final_report)
    
# Main program execution
def main():
    df_csv=load_data(CSV_FILE)
    print("✅ csv data loaded successfully:")
    print(df_csv.head())
    
    save_to_db(df_csv,DB_FILE,TABLE_NAME)
    print("\n💾 data saved into database name",DB_FILE,"under table",TABLE_NAME)
    
    df_db=load_from_db(DB_FILE,TABLE_NAME)
    print("\n data loaded from database:")
    print(df_db.head())
    
    avg_by_subject,top_students= analyze_data(df_db)
    export_report(avg_by_subject,top_students)

# Run program
if __name__=="__main__":
    main()





