import { useState } from "react";

function UploadForm({ onUploadSuccess }) {
  const [file, setFile] = useState(null);
  const [status, setStatus] = useState("");

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
    setStatus("");
  };

  const handleSubmit = async (event) => {
    event.preventDefault();

    if (!file) {
      alert("Please select a CSV file first!");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      setStatus("Uploading...");
      const res = await fetch("http://localhost:8000/api/upload/", {
        method: "POST",
        body: formData,
      });

      const data = await res.json();
      setStatus(`Loaded ${data.message}`);
      onUploadSuccess();
    } catch (error) {
      console.error("Upload error:", error);
      setStatus("Upload failed. Is the backend running?");
    }
  };

  return (
    <div className="card">
      <h2>Upload CSV</h2>
      <form onSubmit={handleSubmit} className="upload-area">
        <input type="file" accept=".csv" onChange={handleFileChange} />
        <button type="submit" className="btn btn-primary">Upload</button>
      </form>
      {status && <p className="status-msg">{status}</p>}
    </div>
  );
}

export default UploadForm;
