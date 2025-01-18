import cv2
import os

def extract_frames(video_path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    cap = cv2.VideoCapture(video_path)
    frame_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame_filename = os.path.join(output_folder, f"frame_{frame_count:04d}.jpg")
        cv2.imwrite(frame_filename, frame)
        frame_count += 1

    cap.release()

def process_video_folder(input_folder, output_base_folder):
    if not os.path.exists(input_folder):
        print(f"Klaida: įvesties aplankas '{input_folder}' neegzistuoja!")
        return

    if not os.path.exists(output_base_folder):
        os.makedirs(output_base_folder)

    video_files = [f for f in os.listdir(input_folder) if f.endswith(('.mp4', '.avi', '.mov', '.mkv'))]
    
    if not video_files:
        print(f"Įspėjimas: aplanke '{input_folder}' nerasta jokių vaizdo įrašų!")
        return

    print(f"Rasti {len(video_files)} vaizdo įrašai.")
    
    for video_file in video_files:
        video_path = os.path.join(input_folder, video_file)
        video_name = os.path.splitext(video_file)[0]
        output_folder = os.path.join(output_base_folder, video_name)
        
        print(f"Apdorojamas vaizdo įrašas: {video_file}")
        extract_frames(video_path, output_folder)
        print(f"Baigtas apdoroti: {video_file}")

# Pavyzdys kaip naudoti
if __name__ == "__main__":
    input_folder = 'input_videos'  # Aplankas su vaizdo įrašais
    output_base_folder = 'extracted_frames'  # Pagrindinis išvesties aplankas
    
    print(f"Pradedamas apdorojimas...")
    print(f"Ieškoma vaizdo įrašų aplanke: {input_folder}")
    process_video_folder(input_folder, output_base_folder)
    print("Apdorojimas baigtas!")
