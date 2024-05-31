import requests

def fetch_top_models():
    url = "https://huggingface.co/api/models"
    response = requests.get(url)
    models = response.json()

    # Sort models by downloads
    sorted_models = sorted(models, key=lambda x: x.get('downloads', 0), reverse=True)
    top_models = sorted_models[:10]

    # Create a report
    report = "Top 10 Hugging Face Models by Downloads:\n"
    for model in top_models:
        report += f"Model: {model['modelId']}, Downloads: {model.get('downloads', 'N/A')}\n"

    with open('report.txt', 'w') as file:
        file.write(report)

    print("Report generated and saved to report.txt")

if __name__ == "__main__":
    fetch_top_models()
