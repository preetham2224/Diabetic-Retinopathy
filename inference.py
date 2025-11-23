import torch
import torch.nn as nn
import timm
from torchvision import transforms
from PIL import Image
import io

# --- Class Labels ---
CLASS_LABELS = {
    0: "No_DR",
    1: "Mild",
    2: "Moderate",
    3: "Severe",
    4: "Proliferative_DR"
}

# --- CoAtNet Model Definition ---
class CoAtNetModel(nn.Module):
    def __init__(self, num_classes=5):
        super().__init__()
        self.model = timm.create_model('coatnet_bn_0_rw_224', pretrained=False, num_classes=num_classes)
    def forward(self, x):
        return self.model(x)

# --- Load Model Function ---
def load_model(weights_path):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"🧠 Using device: {device}")

    model = CoAtNetModel(num_classes=5)
    model.load_state_dict(torch.load(weights_path, map_location=device))
    model.eval()
    model.to(device)
    print("✅ Model loaded successfully!")

    return model, device

# --- Preprocessing & Prediction ---
def predict_image(model, device, image_bytes):
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406],
                             std=[0.229, 0.224, 0.225])
    ])

    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    input_tensor = transform(image).unsqueeze(0).to(device)

    with torch.no_grad():
        outputs = model(input_tensor)
        probs = torch.softmax(outputs, dim=1)
        pred_class = torch.argmax(probs, dim=1).item()

    pred_label = CLASS_LABELS.get(pred_class, "Unknown")
    return pred_class, pred_label, probs.squeeze().tolist()
