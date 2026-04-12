import { useState } from "react";

const EMPTY_FORM = { date: "", description: "", amount: "", category: "" };

function ManualEntry({ onAdded }) {
  const [form, setForm] = useState(EMPTY_FORM);
  const [status, setStatus] = useState("");

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!form.date || !form.description || !form.amount || !form.category) {
      setStatus("Please fill in all fields.");
      return;
    }

    try {
      const res = await fetch("http://localhost:8000/api/transaction/manual", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ ...form, amount: parseFloat(form.amount) }),
      });

      const data = await res.json();
      setStatus(`Added: ${data.transaction?.description}`);
      setForm(EMPTY_FORM);
      onAdded();
    } catch (error) {
      console.error("Error:", error);
      setStatus("Failed to add transaction.");
    }
  };

  return (
    <div className="card">
      <h2>Add Transaction Manually</h2>
      <form onSubmit={handleSubmit} className="manual-form">
        <input
          name="date"
          type="date"
          value={form.date}
          onChange={handleChange}
          placeholder="Date"
        />
        <input
          name="description"
          type="text"
          value={form.description}
          onChange={handleChange}
          placeholder="Description"
        />
        <input
          name="amount"
          type="number"
          step="0.01"
          value={form.amount}
          onChange={handleChange}
          placeholder="Amount"
        />
        <input
          name="category"
          type="text"
          value={form.category}
          onChange={handleChange}
          placeholder="Category (e.g. Food)"
        />
        <div className="form-actions">
          <button type="submit" className="btn btn-primary">Add Transaction</button>
          <button type="button" className="btn btn-secondary" onClick={() => { setForm(EMPTY_FORM); setStatus(""); }}>
            Clear
          </button>
        </div>
      </form>
      {status && <p className="status-msg">{status}</p>}
    </div>
  );
}

export default ManualEntry;
