# Batch prediction
# Training Pipelie
from Travel_Package_prediction.pipeline.batch_prediction import start_batch_prediction

file_path = r"C:\Users\Nplite\Desktop\Travel-Package-Prediction-New\TourismData.csv"


if __name__ == "__main__":
    try:
        output = start_batch_prediction(input_file_path=file_path)
    except Exception as e:
        print(e)


