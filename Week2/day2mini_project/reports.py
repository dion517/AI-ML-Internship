def top_students(df):
    print("\nTop 5 Students")
    print(df.sort_values(by="Average", ascending=False).head(5))

def bottom_students(df):
    print("\nBottom 5 Students")
    print(df.sort_values(by="Average").head(5))

def department_average(df):
    print("\nDepartment-wise Average")
    print(df.groupby("Department")["Average"].mean())

def pass_percentage(df):
    passed = len(df[df["Average"] >= 50])
    total = len(df)

    print(f"Pass Percentage = {(passed/total)*100:.2f}%")

def fail_percentage(df):
    failed = len(df[df["Average"] < 50])
    total = len(df)

    print(f"Fail Percentage = {(failed/total)*100:.2f}%")

def export_report(df):
    df.to_csv("final_report.csv", index=False)
    print("Report Exported Successfully.")