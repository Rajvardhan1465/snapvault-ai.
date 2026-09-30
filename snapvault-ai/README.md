\# SnapVault AI: On-Device Knowledge Assistant for HP Snapdragon PCs



SnapVault AI is a privacy-first, zero-cloud-latency document Q\&A and knowledge retrieval assistant designed for \*\*Snapdragon-powered HP PCs\*\*.



\## 🚀 Key Features

\- \*\*100% On-Device \& Offline:\*\* Local vector processing ensures zero cloud data transmission.

\- \*\*NPU Acceleration via Qualcomm AI Hub:\*\* Offloads generative AI tasks to the Hexagon NPU using the Qualcomm QNN Execution Provider via ONNX Runtime.

\- \*\*Power Efficient:\*\* Low battery draw optimized for HP Copilot+ laptops.



\## 🛠 Tech Stack

\- \*\*Framework:\*\* Python, ONNX Runtime (`QNNExecutionProvider`), Streamlit

\- \*\*AI Models:\*\* Sourced from Qualcomm AI Hub

\- \*\*Target OS:\*\* Windows 11 on ARM (Snapdragon Copilot+ HP PCs)



\## 📦 Setup \& Run

```bash

pip install -r requirements.txt

streamlit run app.py

