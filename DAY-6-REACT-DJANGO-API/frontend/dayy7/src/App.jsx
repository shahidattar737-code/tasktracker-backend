import { useEffect, useState } from "react";
import "./App.css";

function App() {
  const [tasks, setTasks] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8001/api/tasks/")
      .then((response) => response.json())
      .then((data) => {
        setTasks(data.tasks);
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  }, []);

  return (
    <div className="app">
      <h1>Task Tracker</h1>
      <p>React + Django API Integration</p>

      {tasks.map((task) => (
        <div className="task-card" key={task.id}>
          <h3>{task.task_name}</h3>
          <p>Status: {task.status}</p>
        </div>
      ))}
    </div>
  );
}

export default App;