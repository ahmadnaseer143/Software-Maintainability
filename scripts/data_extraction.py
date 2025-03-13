import os
import subprocess
import pandas as pd

def get_loc_and_complexity(project_path):
    """Extracts Lines of Code (LOC) and Cyclomatic Complexity (CC) using Radon."""
    try:
        loc_output = subprocess.check_output(f"radon raw {project_path}", shell=True).decode()
        cc_output = subprocess.check_output(f"radon cc {project_path} -s", shell=True).decode()

        loc_lines = [line for line in loc_output.split('\n') if "loc" in line]
        cc_lines = [line for line in cc_output.split('\n') if line]

        data = []
        for cc_line in cc_lines:
            parts = cc_line.split()
            if len(parts) >= 3:
                filename = parts[0]
                cc_score = int(parts[-1])
                loc = int(loc_lines[0].split(":")[-1]) if loc_lines else 0
                data.append((filename, loc, cc_score))

        df = pd.DataFrame(data, columns=["File_Name", "LOC", "Cyclomatic_Complexity"])
        return df

    except Exception as e:
        print(f"Error extracting data: {e}")
        return pd.DataFrame()

if __name__ == "__main__":
    project_dir = input("Enter project directory path: ")
    results = get_loc_and_complexity(project_dir)
    results.to_csv("raw_data.csv", index=False)
    print("Data extraction completed. Saved to raw_data.csv.")
