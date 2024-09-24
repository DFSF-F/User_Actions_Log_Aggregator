import os
import sys
import pandas as pd
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

INPUT_DIR = os.getenv('INPUT_DIR')
OUTPUT_DIR = os.getenv('OUTPUT_DIR')


def calculate_aggregates(end_date):
    end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
    start_date = end_date - timedelta(days=6)

    data_frames = []
    for i in range(7):
        current_date = start_date + timedelta(days=i)
        file_path = os.path.join(INPUT_DIR, current_date.strftime("%Y-%m-%d") + ".csv")

        if os.path.exists(file_path):
            df = pd.read_csv(file_path, header=None, names=['email', 'action', 'dt'])
            data_frames.append(df)
        else:
            print(f"Файл не найден: {file_path}")

    if not data_frames:
        print("Нет данных для обработки.")
        return

    all_data = pd.concat(data_frames)

    aggregated_data = all_data.groupby(['email', 'action']).size().unstack(fill_value=0).reset_index()

    aggregated_data.columns = ['email', 'create_count', 'read_count', 'update_count', 'delete_count']

    output_file = os.path.join(OUTPUT_DIR, str(end_date) + ".csv")
    aggregated_data.to_csv(output_file, index=False)
    print(f"Агрегированный файл записан: {output_file}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Использование: python script.py <YYYY-mm-dd>")
        sys.exit(1)

    target_date_str = sys.argv[1]

    try:
        datetime.strptime(target_date_str, "%Y-%m-%d")
    except ValueError:
        print("Некорректный формат даты. Используйте YYYY-mm-dd.")
        sys.exit(1)

    calculate_aggregates(target_date_str)
