import { useState, useEffect } from "react";

function Dashboard({ dataLoaded }) {
  const [summary, setSummary] = useState(null);
  const [categories, setCategories] = useState(null);
  const [monthly, setMonthly] = useState(null);

  useEffect(() => {
    if (!dataLoaded) return;

    fetch("http://localhost:8000/api/insights/summary")
      .then((r) => r.json())
      .then(setSummary)
      .catch(console.error);

    fetch("http://localhost:8000/api/insights/categories")
      .then((r) => r.json())
      .then(setCategories)
      .catch(console.error);

    fetch("http://localhost:8000/api/insights/monthly")
      .then((r) => r.json())
      .then(setMonthly)
      .catch(console.error);
  }, [dataLoaded]);

  if (!dataLoaded) {
    return (
      <div className="card">
        <p className="empty">Upload a CSV file above to see your dashboard.</p>
      </div>
    );
  }

  return (
    <>
      {/* Summary Stats */}
      <div className="card">
        <h2>Summary</h2>
        {summary ? (
          <div className="stats-grid">
            <div className="stat-box">
              <div className="label">Total Spent</div>
              <div className="value">${summary.total_spent?.toFixed(2) ?? "—"}</div>
            </div>
            <div className="stat-box">
              <div className="label">Transactions</div>
              <div className="value">{summary.transaction_count ?? "—"}</div>
            </div>
            <div className="stat-box">
              <div className="label">Average</div>
              <div className="value">${summary.average_transaction?.toFixed(2) ?? "—"}</div>
            </div>
            <div className="stat-box">
              <div className="label">Largest</div>
              <div className="value">${summary.largest_transaction?.toFixed(2) ?? "—"}</div>
            </div>
          </div>
        ) : (
          <p className="empty">Loading summary...</p>
        )}
      </div>

      {/* Spending by Category */}
      <div className="card">
        <h2>Spending by Category</h2>
        {categories ? (
          <table>
            <thead>
              <tr>
                <th>Category</th>
                <th>Total</th>
              </tr>
            </thead>
            <tbody>
              {Object.entries(categories).map(([cat, amt]) => (
                <tr key={cat}>
                  <td>{cat}</td>
                  <td>${Number(amt).toFixed(2)}</td>
                </tr>
              ))}
            </tbody>
          </table>
        ) : (
          <p className="empty">Loading categories...</p>
        )}
      </div>

      {/* Spending by Month */}
      <div className="card">
        <h2>Spending by Month</h2>
        {monthly ? (
          <table>
            <thead>
              <tr>
                <th>Month</th>
                <th>Total</th>
              </tr>
            </thead>
            <tbody>
              {Object.entries(monthly).map(([month, amt]) => (
                <tr key={month}>
                  <td>{month}</td>
                  <td>${Number(amt).toFixed(2)}</td>
                </tr>
              ))}
            </tbody>
          </table>
        ) : (
          <p className="empty">Loading monthly data...</p>
        )}
      </div>
    </>
  );
}

export default Dashboard;
