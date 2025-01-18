import os
import pandas as pd

def create_labels_csv(frames_folder, output_csv):
    data = []
    for root, dirs, files in os.walk(frames_folder):
        for file in files:
            if file.endswith('.jpg'):
                frame_path = os.path.join(root, file)
                label = 0  # Default label, you can modify this as needed
                data.append([frame_path, label])

    df = pd.DataFrame(data, columns=['frame_path', 'label'])
    df.to_csv(output_csv, index=False)
    print(f"CSV failas '{output_csv}' sėkmingai sukurtas!")

# Pavyzdys kaip naudoti
if __name__ == "__main__":
    frames_folder = 'extracted_frames'  # Aplankas su išgautais kadrais
    output_csv = 'labels.csv'  # Išvesties CSV failas

    print(f"Pradedamas CSV failo kūrimas...")
    create_labels_csv(frames_folder, output_csv)
    print("CSV failo kūrimas baigtas!")
