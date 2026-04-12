import { useState } from "react";
import UploadForm from "./components/UploadForm";
import Dashboard from "./components/Dashboard";
import Transactions from "./components/Transactions";
import ManualEntry from "./components/ManualEntry";

const TABS = ["Dashboard", "Transactions", "Add Transaction"];

function App() {
  const [activeTab, setActiveTab] = useState("Dashboard");
  const [dataLoaded, setDataLoaded] = useState(false);

  return (
    <div className="app-layout">
      <nav className="sidebar">
        <h2>Finance Analyzer</h2>
        {TABS.map((tab) => (
          <button
            key={tab}
            className={activeTab === tab ? "active" : ""}
            onClick={() => setActiveTab(tab)}
          >
            {tab}
          </button>
        ))}
      </nav>

      <main className="main-content">
        <UploadForm onUploadSuccess={() => setDataLoaded(true)} />

        {activeTab === "Dashboard" && <Dashboard dataLoaded={dataLoaded} />}
        {activeTab === "Transactions" && <Transactions dataLoaded={dataLoaded} />}
        {activeTab === "Add Transaction" && <ManualEntry onAdded={() => setDataLoaded(true)} />}
      </main>
    </div>
  );
}

export default App;
