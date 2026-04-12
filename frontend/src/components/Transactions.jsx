import { useState, useEffect } from "react";

function Transactions({ dataLoaded }) {
  const [transactions, setTransactions] = useState([]);

  useEffect(() => {
    if (!dataLoaded) return;

    fetch("http://localhost:8000/api/transaction/")
      .then((r) => r.json())
      .then((data) => setTransactions(data.transactions ?? []))
      .catch(console.error);
  }, [dataLoaded]);

  if (!dataLoaded) {
    return (
      <div className="card">
        <p className="empty">Upload a CSV file above to see your transactions.</p>
      </div>
    );
  }

  return (
    <div className="card">
      <h2>All Transactions ({transactions.length})</h2>
      {transactions.length === 0 ? (
        <p className="empty">No transactions found.</p>
      ) : (
        <table>
          <thead>
            <tr>
              <th>Date</th>
              <th>Description</th>
              <th>Category</th>
              <th>Amount</th>
            </tr>
          </thead>
          <tbody>
            {transactions.map((t, i) => (
              <tr key={i}>
                <td>{t.date}</td>
                <td>{t.description}</td>
                <td>{t.category}</td>
                <td>${Number(t.amount).toFixed(2)}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}

export default Transactions;
